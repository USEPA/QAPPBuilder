import os
import cgi
import sys
from shutil import copyfile
import re
import json
# Added to get latest OMIS data programmatically.
import requests

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from operator import itemgetter
import datetime
from django.db.models import Q
from django.conf import settings
from projects.models import *
from organization.models import *
# from docxtpl import DocxTemplate
# import jinja2
import csv
from django.db import connection
from django.utils import timezone

#
# If a user does not have the correct org info in QA Track, you can check in the log
# to see what divisions or branches are not being found.
#



class Command(BaseCommand):
    args = '<filename ...>'
    help = 'Load the NERL data from the JSON file (exported from Lotus Notes)'



    def _load_org_data(self, json_file, org_lookup):

        org_updates = 0

        document_list = json_file

        for document in document_list:
            # assign omis variables
            omisID = str(document["id"]) if "id" in document else None

            # check for OMIS ID in profile (using code_kept field for this)
            # get profile
            user_profile = UserProfile.objects.filter(Q(code_kept__iexact=omisID)).all()

            if len(user_profile) == 1:
                userprofile = user_profile[0]

                # update the organization information
                organization = document["organization"] if "organization" in document else None

                if organization is not None:
                    org_id = organization["id"] if "id" in organization else None
                    if org_id is not None:
                        # org = org_lookup[org_id]
                        org = org_lookup[org_id] if org_id in org_lookup else None

                        if org is not None:
                            org_office = None
                            org_lab = None
                            org_division = None
                            org_branch = None
                            org_type = None

                            if isinstance(org, Office):
                                org_office = org
                                org_type = 'OFFICE'
                            elif isinstance(org, Lab):
                                org_office = org.office
                                org_lab = org
                                org_type = 'LAB'
                            elif isinstance(org, Division):
                                org_office = org.office
                                org_lab = org.lab
                                org_division = org
                                org_type = 'DIVISION'
                            elif isinstance(org, Branch):
                                org_office = org.office
                                org_lab = org.lab
                                org_division = org.division
                                org_branch = org
                                org_type = 'BRANCH'

                            doUpdate = False
                            if org_office != userprofile.office:
                                print("omisID: " + omisID + "; office (before|after): " + str(userprofile.office) + "|" + str(org_office))
                                userprofile.office = org_office
                                doUpdate = True
                            if org_lab != userprofile.lab:
                                print("omisID: " + omisID + "; lab (before|after): " + str(userprofile.lab) + "|" + str(org_lab))
                                userprofile.lab = org_lab
                                doUpdate = True
                            if org_division != userprofile.division:
                                print("omisID: " + omisID + "; division (before|after): " + str(userprofile.division) + "|" + str(org_division))
                                userprofile.division = org_division
                                doUpdate = True
                            if org_branch != userprofile.branch:
                                print("omisID: " + omisID + "; branch (before|after): " + str(userprofile.branch) +"|" + str(org_branch))
                                userprofile.branch = org_branch
                                doUpdate = True

                            # If the user does not have a usertype, assign one according to the user's org info.
                            if userprofile.user_type is None and org is not None:
                                print("Initializing user_type for omisID: " + omisID + "; user_type (before|after): " + str(userprofile.user_type) + "|" + str(org_type))
                                userprofile.user_type = org_type
                                doUpdate = True

                            if doUpdate:
                                org_updates += 1
                                userprofile.save()
                                # print("Saving updates for " + document["first_name"] + " " + document["last_name"])
                                print(str(userprofile.user.username) + ": Saving updates for " + document["first_name"] + " " + document["last_name"])

        print("Orgs profiles updated: " + str(org_updates))



    """
    Build a lookup table from OSIM ids to QA track database objects
    :param json_file: json file of organizations
    :return:
    """
    def _build_org_lookup(self, json_file):


        # Open the Curator organization file.
        org_file = json_file

        office = Office.objects.first()

        # build a lookup table of organizations
        # we spin over the data 3 times (labs, then, divs, then branches) to make sure the labs are in before divisions, etc.
        org_lookup = {}

        # Loop to add labs.
        for org in org_file:
            id = org["id"]
            if id not in org_lookup:
                # Haven't processed this org yet.
                ancestors = org["ancestor_relationships"]
                depth = len(ancestors) - 1
                if depth == 0:
                    # This is a center/office/lab. Look for it in QA Track by abbreviation.
                    lab = Lab.objects.filter(Q(office = office) & Q(abbreviation = org["abbrev"])).first()
                    org_lookup[id] = lab

                    if lab is None:
                        print("No center/office/lab:", id, org["abbrev"], org["name"])

        # Loop to add divisions.
        for org in org_file:
            id = org["id"]
            if id not in org_lookup:
                ancestors = org["ancestor_relationships"]
                depth = len(ancestors) - 1
                if depth == 1:
                    lab = org_lookup[ancestors[depth]["ancestor"]["id"]]
                    division = Division.objects.filter(Q(office=office) & Q(lab=lab) & Q(abbreviation=org["abbrev"])).first()
                    org_lookup[id] = division
                    if division is None:
                        # Added special case for MCEARD because it is currently in OMIS with the abbreviation MCEAR.
                        if org["abbrev"] == "MCEAR":
                            real_abbrev = "MCEARD"
                            division = Division.objects.filter(Q(office=office) & Q(lab=lab) &
                                                               Q(division=org["name"]) &
                                                               Q(abbreviation=real_abbrev)).first()
                            org_lookup[id] = division
                            if division is None:
                                # For our own knowledge.
                                print("No division: " + str(id) + " --> " + str(lab) + " " + + "MCEAR or MCEARD [" + org["name"] + "]")
                        else:
                            print("No division: " + str(id) + " --> " + str(lab) + " " + org[ "abbrev"] + " [" + org["name"] + "]")

        # Loop to add branches.
        for org in org_file:
            id = org["id"]
            if id not in org_lookup:
                ancestors = org["ancestor_relationships"]
                depth = len(ancestors) - 1
                if depth == 2:
                    lab = org_lookup[ancestors[depth]["ancestor"]["id"]]
                    division = org_lookup[ancestors[depth-1]["ancestor"]["id"]]
                    branch_abbrev = org["abbrev"]
                    if branch_abbrev == "CPPB":
                        branch_abbrev = "CPB"
                    branch = Branch.objects.filter(Q(office=office) & Q(lab=lab) & Q(division=division) &
                                                   Q(abbreviation=branch_abbrev)).first()
                    org_lookup[id] = branch

                    if branch is None:
                        print("No branch: " + str(id) + " --> Lab: " + str(lab) + " Div: " +str(division) + " Branch: " + org["abbrev"] + " [" + org["name"] + "]")

        return org_lookup


    def _load_data(self, json_file):

        document_list = json_file

        # -----------------------------------------
        # Duplicate checking
        print("Checking for OMIS duplicates ...")

        generic_emails = []
        generic_emails.append("INVALID@EPA.GOV")
        generic_emails.append("YBOSTROM@NYT1.NET")
        generic_emails.append("N/A@EPA.GOV")
        generic_emails.append("KEITH@TANDTJANITORIALSERVICES.COM")

        email_list_all = []
        list_generic_all = []

        for document in document_list:
            email = str(document["email"]).upper()
            if email in generic_emails:
                list_generic_all.append(email + "|" + document["first_name"] + "|" + document["last_name"])
            else:
                email_list_all.append(email)

        dup_emails = []
        for email in email_list_all:
            if email is not None:
                if email_list_all.count(email) > 1:
                    if email not in dup_emails:
                        dup_emails.append(email)

        dup_emails_generic = []
        for list_item in list_generic_all:
            if list_item is not None:
                if list_generic_all.count(list_item) > 1:
                    if list_item not in dup_emails_generic:
                        dup_emails_generic.append(list_item)

        print("non-generic omis dups found: " + str(len(dup_emails)))
        print("generic omis dups found: " + str(len(dup_emails_generic)))
        for gen_dup in dup_emails_generic:
            print(gen_dup)
        print()

        keep_dups = []
        for dup_email in dup_emails:
            max_omis_id = 0
            max_separation_date = "1901-01-01"
            none_separation_date_id = 0
            max_separation_date_id = 0
            separation_date_list = []

            for document in document_list:
                if dup_email == str(document["email"]).upper():
                    # keep track of max id to use as default
                    if document["id"] > max_omis_id:
                        max_omis_id = document["id"]

                    # hold the date to check later
                    separation_date = document["epa_separation_date"]
                    separation_date_list.append(separation_date)

                    if separation_date is None:
                        none_separation_date_id = document["id"]

                    # keep track of max date (that is not none)
                    if document["epa_separation_date"] and document["epa_separation_date"] > max_separation_date:
                        max_separation_date = document["epa_separation_date"]
                        max_separation_date_id = document["id"]

            # if there's only one with none for separation date, use it
            if separation_date_list.count(None) == 1:
                match_id = none_separation_date_id
            elif separation_date_list.count(max_separation_date) == 1:
                match_id = max_separation_date_id
            else:
                match_id = max_omis_id

            keep_dups.append(match_id)

        keep_dups_generic = []
        for dup_item in dup_emails_generic:
            max_omis_id = 0
            max_separation_date = "1901-01-01"
            none_separation_date_id = 0
            max_separation_date_id = 0
            separation_date_list = []

            for document in document_list:
                if dup_item == str(document["email"]).upper() + "|" + document["first_name"] + "|" + document["last_name"]:
                    # keep track of max id to use as default
                    if document["id"] > max_omis_id:
                        max_omis_id = document["id"]

                    # hold the date to check later
                    separation_date = document["epa_separation_date"]
                    separation_date_list.append(separation_date)

                    if separation_date is None:
                        none_separation_date_id = document["id"]

                    # keep track of max date (that is not none)
                    if document["epa_separation_date"] and document["epa_separation_date"] > max_separation_date:
                        max_separation_date = document["epa_separation_date"]
                        max_separation_date_id = document["id"]

            # if there's only one with none for separation date, use it
            if separation_date_list.count(None) == 1:
                match_id = none_separation_date_id
            elif separation_date_list.count(max_separation_date) == 1:
                match_id = max_separation_date_id
            else:
                match_id = max_omis_id

            keep_dups_generic.append(match_id)
        # -------------------

        update_user_cnt = 0
        update_profile_cnt = 0
        new_user_cnt = 0

        for document in document_list:
            add_flag = False
            update_flag = False
            update_user = False
            update_profile = False

            omis_id = document["id"]
            omis_email = document["email"]
            omis_fname = document["first_name"]
            omis_lname = document["last_name"]
            omis_sep_date = document["epa_separation_date"]

            if omis_email is not None:
                omis_email_upper = omis_email.upper()
            else:
                continue

            # see if already in QATrack
            omis_id = str(document["id"])
            qa_profile = UserProfile.objects.filter(Q(code_kept__iexact=omis_id)).all()
            if len(qa_profile) == 1:
                update_flag = True

            else:   # add - unless it's a non valid duplicate
                if omis_email_upper in generic_emails:

                    omis_item = omis_email_upper + "|" + omis_fname + "|" + omis_lname
                    if (omis_item not in dup_emails_generic) or (int(omis_id) in keep_dups_generic):
                        # see if match in db
                        qa_user = User.objects.filter(
                            Q(first_name__iexact=omis_fname) & Q(last_name__iexact=omis_lname) & Q(
                                email__iexact=omis_email)).all()
                        if len(qa_user) == 1:
                            update_flag = True
                        elif len(qa_user) == 0:
                            add_flag = True
                else:

                    if (omis_email_upper not in dup_emails) or (int(omis_id) in keep_dups):

                        # see if match in db
                        qa_user = User.objects.filter(Q(email__iexact=omis_email)).all()
                        if len(qa_user) == 1:
                            update_flag = True
                        elif len(qa_user) == 0:
                            add_flag = True

            if update_flag:
                if len(qa_profile) == 1:
                    # get related user
                    qa_profile = qa_profile[0]
                    qa_user = qa_profile.user

                else:
                    # get related profile
                    qa_user = qa_user[0]
                    qa_profile = UserProfile.objects.filter(Q(user_id__exact=qa_user.id)).all()
                    if len(qa_profile) == 1:
                        qa_profile = qa_profile[0]
                    else:
                        print(str(qa_user) + ": no profile")
                        userprofile = UserProfile()
                        current_time = timezone.now()
                        userprofile.user = qa_user
                        userprofile.created = current_time
                        userprofile.modified = current_time
                        userprofile.email_address_epa = qa_user.email
                        userprofile.email_address_other = qa_user.email
                        userprofile.code_kept = omis_id
                        userprofile.date_epa_separation = omis_sep_date
                        userprofile.office = Office.objects.filter(abbreviation="ORD").first()
                        # userprofile.lab = Lab.objects.filter(abbreviation=data_set).first()
                        userprofile.save()
                        qa_profile = userprofile
                        print(str(qa_user) + ": profile created")

                if not qa_user.is_active:  # only update user data for the inactive users
                    # update user if changed
                    update_user = False
                    if qa_user.first_name != omis_fname:
                        qa_user.first_name = omis_fname
                        update_user = True

                    if qa_user.last_name != omis_lname:
                        qa_user.last_name = omis_lname
                        update_user = True

                    if str(qa_user.email).upper() != omis_email_upper and omis_email is not None:
                        qa_user.email = omis_email
                        # print(str(qa_user.email).upper + ":" + omis_email_upper)
                        update_user = True

                    if update_user:
                        qa_user.save()
                        # print(str(qa_user))
                        update_user_cnt += 1
                        print(str(qa_user.username) + ": updated user")

                # update profile
                update_profile = False
                if qa_profile.code_kept != omis_id:
                    qa_profile.code_kept = omis_id
                    update_profile = True

                db_sep_date = str(qa_profile.date_epa_separation).format('YYYY-MM-DD')
                if db_sep_date != str(omis_sep_date):
                    qa_profile.date_epa_separation = omis_sep_date
                    update_profile = True
                    print(str(qa_user.username) + ": db sep date|omis sep date --> " + db_sep_date + "|" + str(omis_sep_date))

                if update_profile:
                    qa_profile.save()
                    update_profile_cnt += 1

            elif add_flag and omis_email is not None:
                # create new profile and user
                user = User()
                new_user_name = omis_fname[0].lower() + omis_lname[0:25].lower()

                # check for a dup username
                # use this code if username is already taken by another person
                dup_inc = 1
                check_user_name = new_user_name
                while (len(User.objects.filter(Q(username__exact=new_user_name)).all())) != 0:
                    dup_inc += 1
                    new_user_name = check_user_name + str(dup_inc)

                print("Add new user: " + omis_fname + " " + omis_lname + " ---> Username: " + str(new_user_name))

                user.username = new_user_name
                user.first_name = omis_fname
                user.last_name = omis_lname
                user.email = omis_email

                user.is_active = False  # don't let created users log into QA track
                user.save()

                userprofile = UserProfile()
                current_time = timezone.now()
                userprofile.user = user
                userprofile.created = current_time
                userprofile.modified = current_time
                userprofile.email_address_epa = user.email
                userprofile.email_address_other = user.email
                userprofile.code_kept = omis_id
                userprofile.date_epa_separation = omis_sep_date
                userprofile.office = Office.objects.filter(abbreviation="ORD").first()
                # userprofile.lab = Lab.objects.filter(abbreviation=data_set).first()
                userprofile.save()
                new_user_cnt += 1

        # don't want to display users in dropdowns if they left more than a year ago
        strSQL = "update accounts_userprofile set display_in_dropdowns = 'Y'"
        connection.cursor().execute(strSQL)
        strSQL = (
            "update accounts_userprofile set display_in_dropdowns = 'N' "
            "where date_epa_separation < (now() - INTERVAL '1 year')"
        )
        connection.cursor().execute(strSQL)

        # deactivate separated users
        strSQL = (
            "update auth_user set is_active = false where is_active = true "
            "and id in (select user_id from accounts_userprofile where date_epa_separation < (now()))"
        )
        connection.cursor().execute(strSQL)

        print("users updated: " + str(update_user_cnt))
        print("profiles updated: " + str(update_profile_cnt))
        print("new users: " + str(new_user_cnt))
        print()

    def handle(self, *args, **options):
        # usage examples:
        # python manage.py omis_load_users
        # python manage.py omis_load_users >> omis_load.log

        #########

        print("------START--------------------------------------")
        print(str(timezone.now().isoformat()).replace(":", "_"))

        print()
        print("*** START RUN ***")

        reqheader = {'X-API-EMAIL': settings.CURATOR_EMAIL, 'X-API-TOKEN': settings.CURATOR_KEY}
        reqsuccess = True
        try:
            response = requests.get('http://sciencehub.epa.gov/curator/people.json', headers=reqheader)
        except requests.ConnectionError as e:
            print('sciencehub people connection error')
            print(e)
            reqsuccess = False
            pass
        except requests.exceptions.Timeout:
            print('sciencehub people timed out')
            print("------END--------------------------------------")
            sys.exit(1)
        except requests.exceptions.TooManyRedirects:
            print('sciencehub people too many redirects')
            print("------END--------------------------------------")
            sys.exit(1)
        except requests.exceptions.RequestException as e:
            print('sciencehub people exception')
            print(e)
            print("------END--------------------------------------")
            sys.exit(1)

        if reqsuccess == True:
            user_json_object = response.json()

            # Try getting organization data next
            try:
                response = requests.get('http://sciencehub.epa.gov/curator/organizations.json', headers=reqheader)
            except requests.ConnectionError as e:
                print('sciencehub organizations connection error')
                print(e)
                reqsuccess = False
                pass
            except requests.exceptions.Timeout:
                print('sciencehub organizations timed out')
                print("------END--------------------------------------")
                sys.exit(1)
            except requests.exceptions.TooManyRedirects:
                print('sciencehub organizations too many redirects')
                print("------END--------------------------------------")
                sys.exit(1)
            except requests.exceptions.RequestException as e:
                print('sciencehub organizations exception')
                print(e)
                print("------END--------------------------------------")
                sys.exit(1)

        if reqsuccess == True:
            org_json_object = response.json()
            user_json_file = org_json_file = "fetched from sciencehub.epa.gov"
        else:
            json_user_data_file = "omis_people.json"
            json_org_data_file = "osim_organizations.json"
            user_json_file = os.path.join(os.getcwd(), "organization/data/" + json_user_data_file)
            org_json_file = os.path.join(os.getcwd(), "organization/data/" + json_org_data_file)
            with open(user_json_file) as json_file:
                user_json_object = json.load(json_file)
            with open(org_json_file) as json_file:
                org_json_object = json.load(json_file)

        print()
        print("the json user file is " + user_json_file)
        print("the json org file is " + org_json_file)
        print()

        # Add new users.
        self._load_data(user_json_object)

        # Create the organization lookup from OMIS org data.
        org_lookup = self._build_org_lookup(org_json_object)

        # Update organization info for each user.
        # If the user has no user_type, assign according to their org info.
        self._load_org_data(user_json_object, org_lookup)

        print("------END--------------------------------------")
