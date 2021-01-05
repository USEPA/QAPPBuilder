#
# Manage.py command to load the OSIM person data (currently only includes ORD)
#
# !! assumes that you have run retrieved the latest json from
#
# http://sciencehub.epa.gov/curator/organizations.json
# X-API-EMAIL: sciencehub@epa.gov
# X-API-TOKEN: 5ef9d961aa295b718c48f9107ece3a97
#
# !! also assumes you have run the osim_load_organizations command
#
import sys
import re
import json
from django.core.management.base import BaseCommand
from operator import itemgetter
from django.db.models import Q
import datetime
from django.contrib.auth.models import User

from organization.models import *
from app.models import *

class Command(BaseCommand):
    args = '<people_file organization_file ...>'
    help = 'Load the ORD people data from the JSON file (exported from Science Hub)'

    def _build_org_lookup(self, json_file):
        """
        Build a lookup table from OSIM ids to QA track database objects
        :param json_file: json file of organizations
        :return:
        """
        # open the exported json data from the QAIMs lotus notes database
        document_list = []
        try:
            json_data=open(json_file).read()
            document_list = json.loads(json_data)
        except Exception as e:
            raise IOError("Failed to load organization JSON file: " + str(e))

        office = Office.objects.first()

        # build a lookup table of organizations
        # we spin over the data 3 times to make sure the labs are in before divisions, etc.
        org_lookup = {}
        # add labs
        for document in document_list:
            id = document["id"]
            if id not in org_lookup:
                ancestors = document["ancestor_relationships"]
                depth = len(ancestors) - 1
                if depth == 0:
                    # save if lab does not exist
                    lab = Lab.objects.filter(Q(office = office) & Q(lab = document["name"]) &
                                             Q(abbreviation = document["abbrev"])).first()

                    org_lookup[id] = lab

        # add divisions
        for document in document_list:
            id = document["id"]
            if id not in org_lookup:
                ancestors = document["ancestor_relationships"]
                depth = len(ancestors) - 1
                if depth == 1:
                    lab = org_lookup[ancestors[depth]["ancestor"]["id"]]
                    division = Division.objects.filter(Q(office = office) & Q(lab = lab) &
                                                       Q(division = document["name"]) &
                                                       Q(abbreviation = document["abbrev"])).first()
                    org_lookup[id] = division

        # add branches
        for document in document_list:
            id = document["id"]
            if id not in org_lookup:
                ancestors = document["ancestor_relationships"]
                depth = len(ancestors) - 1
                if depth == 2:
                    lab = org_lookup[ancestors[depth]["ancestor"]["id"]]
                    division = org_lookup[ancestors[depth-1]["ancestor"]["id"]]
                    branch = Branch.objects.filter(Q(office = office) & Q(lab = lab) & Q(division = division) &
                                                   Q(branch = document["name"]) &
                                                   Q(abbreviation = document["abbrev"])).first()
                    org_lookup[id] = branch

        return org_lookup

    def _get_username(self, first_name, last_name):
        """generate a username"""
        username_base = first_name.lower()[0] + last_name.lower()
        username = username_base
        # make sure username is unique.  Sequentially add numbers until
        # we get a unique username
        user_num = 2
        user = User.objects.filter(username = username).first()
        while(user is not None):
            username = username_base + str(user_num)
            user = User.objects.filter(username = username).first()
            user_num += 1

        return username


    def _load_data(self, person_file, org_lookup):
        """
        Load the person data
        :return:
        """
        try:
            json_data=open(person_file).read()
            person_list = json.loads(json_data)
        except Exception as e:
            raise IOError("Failed to load organization JSON file: " + str(e))

        total_added = 0
        total_updated = 0
        for person in person_list:
            # check if the person already exists in the users table
            email = person["email"] if "email" in person else None
            if email is not None:
                email = email.lower()
            first_name = person["first_name"] if "first_name" in person else None
            last_name = person["last_name"] if "last_name" in person else None
            if email is not None:
                user = User.objects.filter(email__iexact = email).first()
            else:
                user = User.objects.filter(Q(first_name__iexact = first_name) &
                                           Q(last_name__iexact = last_name)).first()

            # create a new
            if user is None:
                total_added += 1
                user = User()
                user.username = self._get_username(first_name, last_name)
                user.first_name = first_name
                user.last_name = last_name
                user.email = email if email is not None else last_name.lower() + "." + first_name.lower() + "@epa.gov"
                user.is_active = False # don't let imported users log into QA track
                user.save()
            else:
                total_updated += 1

            current_time = datetime.datetime.now()
            try:
                userprofile = user.userprofile
            except UserProfile.DoesNotExist:
                userprofile = UserProfile()
                userprofile.user = user
                userprofile.created = current_time
                userprofile.modified = current_time
                userprofile.email_address_epa = user.email
                userprofile.email_address_other = user.email
                # update general user profile info
                if "employee_type" in person and person["employee_type"] == "EPA":
                    userprofile.company = "EPA"
                # set privileges to False if we have not previous info in the database
                if userprofile.is_reviewer is None:
                    userprofile.is_reviewer = 'N'
                if userprofile.is_technical_lead is None:
                    userprofile.is_technical_lead = 'N'
                if userprofile.can_edit is None:
                    userprofile.can_edit = 'N'
                if userprofile.can_create_users is None:
                    userprofile.can_create_users = 'N'

            # update the organization information
            organization = person["organization"] if "organization" in person else None
            if organization is not None:
                org_id = organization["id"] if "id" in organization else None
                if org_id is not None:
                    org = org_lookup[org_id]
                    if org is not None:
                        if isinstance(org, Office):
                            userprofile.office = org
                            userprofile.lab = None
                            userprofile.division = None
                            userprofile.branch = None
                            userprofile.user_type = 'OFFICE'
                        elif isinstance(org, Lab):
                            userprofile.office = org.office
                            userprofile.lab = org
                            userprofile.division = None
                            userprofile.branch = None
                            userprofile.user_type = 'LAB'
                        elif isinstance(org, Division):
                            userprofile.office = org.office
                            userprofile.lab = org.lab
                            userprofile.division = org
                            userprofile.branch = None
                            userprofile.user_type = 'DIVISION'
                        elif isinstance(org, Branch):
                            userprofile.office = org.office
                            userprofile.lab = org.lab
                            userprofile.division = org.division
                            userprofile.branch = org
                            userprofile.user_type = 'BRANCH'


            # save the updated user profile and user
            userprofile.save()
            user.save()

        return (total_added, total_updated)


    def _update_empty_organizations(self):
        """
        Try to fill in the foreign keys to Office, Lab, Division, and Branch based on the previous
        abbreviation information
        :return:
        """
        office = Office.objects.filter(abbreviation = "ORD").first()

        users = User.objects.all()
        for user in users:
            userprofile = user.userprofile
            lab_str = userprofile.user_lab_one
            division_str = userprofile.user_division_one
            branch_str = userprofile.user_branch_one

            # set the office if not yet set
            if userprofile.office is None:
                userprofile.office = office

            # find the lab
            if userprofile.lab is None and lab_str is not None:
                lab = Lab.objects.filter(abbreviation__iexact = lab_str).first()
                if lab is not None:
                    userprofile.lab = lab
                    # find the division
                    if userprofile.division is None and division_str is not None:
                        division = Division.objects.filter(Q(lab = lab) &
                                                           Q(abbreviation__iexact = division_str)).first()
                        if division is not None:
                            userprofile.division = division
                            # find the branch
                            if userprofile.branch is None and branch_str is not None:
                                branch = Branch.objects.filter(Q(lab = lab) &
                                                               Q(division = division) &
                                                               Q(abbreviation__iexact = branch_str)).first()
                                if branch is not None:
                                    userprofile.branch = branch
            userprofile.save()

    def _convert_foreign_keys(self):
        """
        Update the old foreign keys to point at the new organization models
        :return:
        """


    def handle(self, *args, **options):
        if len(args) != 2:
            print("usage: python manage.py qaims_load_json <people_file> <organization_file>")
        else:
            try:
                org_lookup = self._build_org_lookup(args[1])
                (total_added, total_updated) = self._load_data(args[0], org_lookup)
                self._update_empty_organizations()
                self._convert_foreign_keys()
                print("Added " + str(total_added) + " new users")
                print("Updated " + str(total_updated) + " existing users")

            except Exception as e:
                print("Failed to load person data: " + str(e))