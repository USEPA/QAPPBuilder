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

from rms.models import *


class Command(BaseCommand):
    args = '<filename ...>'
    help = 'Load the RMS data from the JSON files (exported from the RMS SOAP service)'

    def _load_programs(self, json_file):

        # open the exported json data from the QAIMs lotus notes database
        document_list = []
        try:
            json_data=open(json_file).read()
            document_list = json.loads(json_data)
        except Exception as e:
            print("Failed to load JSON file: " + str(e))
            return

        for prog in document_list['RMSPrograms']['RMSprogram']:
            program = Program()
            program.rms_id = prog['_id']
            program.title = prog['title']
            program.acronym = prog['acronym']
            program.url = prog['url']
            program.save()

    def _load_projects(self, json_file):

        # open the exported json data from the QAIMs lotus notes database
        document_list = []
        try:
            json_data = open(json_file).read()
            document_list = json.loads(json_data)
        except Exception as e:
            print("Failed to load JSON file: " + str(e))
            return

        for proj in document_list['RMSProjects']['RMSproject']:
            fk = proj['RMSprogram_id']
            end = int(re.sub('Q.+FY', '', proj['end_date']))
            if fk != '' and end >= 2016:
                program = Program.objects.filter(rms_id=fk).first()
                project = Project()
                project.program = program
                project.title = proj['title']
                project.epa_id = proj['epa_id']
                project.IRMS_project_id = proj['IRMS_project_id']
                project.RMSprogram_id = fk
                project.url = proj['url']
                project.rms_id = proj['_id']
                project.start_date = proj['start_date']
                project.end_date = proj['end_date']
                project.save()


    def _load_tasks(self, json_file):

        # open the exported json data from the QAIMs lotus notes database
        document_list = []
        try:
            json_data = open(json_file).read()
            document_list = json.loads(json_data)
        except Exception as e:
            print("Failed to load JSON file: " + str(e))
            return

        for tsk in document_list['RMSTasks']['RMStask']:
            fk = tsk['RMSproject_id']
            # there is at leas one test task with no foreign key
            if fk != '':
                project = Project.objects.filter(rms_id=fk).first()
                # A task may have multiple entries
                # because it can belong to multiple projects
                task = Task.objects.filter(epa_id=tsk['epa_id']).first()
                # if we did not find the task the create it
                if task is None:
                    task = Task()
                    task.title = tsk['title']
                    task.epa_id = tsk['epa_id']
                    task.RMSproject_id = fk
                    task.url = tsk['url']
                    task.rms_id = tsk['_id']
                    task.start_date = tsk['start_date']
                    task.end_date = tsk['end_date']
                    task.save()
                task.projects.add(project)


    def _convert_foreign_keys(self):
        """
        Update the old foreign keys to point at the new organization models
        :return:
        """


    def handle(self, *args, **options):
        # if len(args) != 1:
        #     print("usage: python manage.py qaims_load_json <filename>")
        # else:
        #     self._load_data(args[0])
        #     self._convert_foreign_keys()

        program_file = "rms/data/RMSPrograms.json"
        self._load_programs(program_file)

        project_file = "rms/data/RMSProjects.json"
        self._load_projects(project_file)

        task_file = "rms/data/RMSTasks2014.json"
        self._load_tasks(task_file)
