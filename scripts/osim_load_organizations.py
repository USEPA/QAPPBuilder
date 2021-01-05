#
# Manage.py command to load the OSIM organization data (currently only includes ORD)
#
# assumes that you have run retrieved the latest json from
#
# http://sciencehub.epa.gov/curator/organizations.json
# X-API-EMAIL: sciencehub@epa.gov
# X-API-TOKEN: 5ef9d961aa295b718c48f9107ece3a97
#
#
#
import sys
import re
import json
from django.core.management.base import BaseCommand
from operator import itemgetter
from django.db.models import Q
import datetime

from organization.models import *


class Command(BaseCommand):
    args = '<filename ...>'
    help = 'Load the ORD organization data from the JSON file (exported from Science Hub)'

    def _load_data(self, json_file):

        # open the exported json data from the QAIMs lotus notes database
        document_list = []
        try:
            json_data=open(json_file).read()
            document_list = json.loads(json_data)
        except Exception as e:
            print("Failed to load JSON file: " + str(e))
            return

        # this data is only from ORD, so create an office object
        office = Office.objects.filter(abbreviation = "ORD").first()
        if office is None:
            office = Office()
            office.office = "Office and Research and Development"
            office.abbreviation = "ORD"
            office.save()

        # build a lookup table of Labs
        lab_lookup = {}
        for document in document_list:
            id = document["id"]
            if id not in lab_lookup:
                ancestors = document["ancestor_relationships"]
                depth = len(ancestors) - 1
                if depth == 0:
                    # save if lab does not exist
                    lab = Lab.objects.filter(Q(office = office) & Q(lab = document["name"]) &
                                             Q(abbreviation = document["abbrev"])).first()
                    if lab is None:
                        lab = Lab()
                        lab.lab = document["name"]
                        lab.abbreviation = document["abbrev"]
                        lab.office = office
                        lab.save()
                    lab_lookup[id] = lab

        # build a lookup table of divisions
        division_lookup = {}
        for document in document_list:
            id = document["id"]
            if id not in division_lookup:
                ancestors = document["ancestor_relationships"]
                depth = len(ancestors) - 1
                if depth == 1:
                    lab = lab_lookup[ancestors[depth]["ancestor"]["id"]]
                    division = Division.objects.filter(Q(office = office) & Q(lab = lab) &
                                                       Q(division = document["name"]) &
                                                       Q(abbreviation = document["abbrev"])).first()
                    if division is None:
                        division = Division()
                        division.division = document["name"]
                        division.abbreviation = document["abbrev"]
                        division.office = office
                        division.lab = lab
                        division.save()
                    division_lookup[id] = division


        # build a lookup table of branches
        for document in document_list:
            id = document["id"]
            ancestors = document["ancestor_relationships"]
            depth = len(ancestors) - 1
            if depth == 2:
                lab = lab_lookup[ancestors[depth]["ancestor"]["id"]]
                division = division_lookup[ancestors[depth-1]["ancestor"]["id"]]
                branch = Branch.objects.filter(Q(office = office) & Q(lab = lab) & Q(division = division) &
                                               Q(branch = document["name"]) &
                                               Q(abbreviation = document["abbrev"])).first()
                if branch is None:
                    branch = Branch()
                    branch.branch = document["name"]
                    branch.abbreviation = document["abbrev"]
                    branch.office = office
                    branch.lab = lab
                    branch.division = division
                    branch.save()

    def _convert_foreign_keys(self):
        """
        Update the old foreign keys to point at the new organization models
        :return:
        """


    def handle(self, *args, **options):
        if len(args) != 1:
            print("usage: python manage.py qaims_load_json <filename>")
        else:
            self._load_data(args[0])
            self._convert_foreign_keys()