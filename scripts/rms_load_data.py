#
# rms_load_data.py
# Author: Nick Woodward
# Date: 04/2018
#
# This script attempts to query the EPA's RMS SOAP service for RAP programs, projects, and tasks. The RMS service
# is only available on the EPA's VPN so for testing purposes, it tests for failure of the http request and uses
# XML files pulled in 04/2018 instead.
#

# Urls:
# Gets description of SOAP service
#   https://v26265ncay516.aa.ad.epa.gov/RMS/webservice.cfc?wsdl
# Gets RAP Programs, Projects and Tasks respectively:
#   https://v26265ncay516.aa.ad.epa.gov/RMS/webservice.cfc?method=getRMSPrograms
#   https://v26265ncay516.aa.ad.epa.gov/RMS/webservice.cfc?method=getRMSProjects
#   https://v26265ncay516.aa.ad.epa.gov/RMS/webservice.cfc?method=getRMSTasks

from django.core.management.base import BaseCommand
from django.db.models import Q
from rms.models import *
import datetime
import urllib
import ssl
import xml.etree.ElementTree as ET
import xmltodict
import re


class Command(BaseCommand):

    def _log(self, *args):
        print("DEBUG: " + ','.join(args))

    def _clean_wddx(self,wddx_string):
        cleaned = re.sub(r"<[^>]*>","",wddx_string)
        xml = cleaned.replace("&lt;","<").replace("&gt;",">")
        return xml

    def _load_content_from_urls(self):

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        program_url = "https://v26265ncay516.aa.ad.epa.gov/RMS/webservice.cfc?method=getRMSPrograms"
        project_url = "https://v26265ncay516.aa.ad.epa.gov/RMS/webservice.cfc?method=getRMSProjects"
        task_url = "https://v26265ncay516.aa.ad.epa.gov/RMS/webservice.cfc?method=getRMSTasks"

        program_content = self._clean_wddx(urllib.request.urlopen(program_url, context=ctx).read().decode('utf-8'))
        project_content = self._clean_wddx(urllib.request.urlopen(project_url, context=ctx).read().decode('utf-8'))
        task_content = self._clean_wddx(urllib.request.urlopen(task_url, context=ctx).read().decode('utf-8'))

        return program_content, project_content, task_content

    def _load_content_from_files(self):
        program_file = 'rms/data/RMSPrograms2018.xml'
        project_file = 'rms/data/RMSProjects2018.xml'
        task_file = 'rms/data/RMSTasks2018.xml'

        program_content = open(program_file).read()
        project_content = open(project_file).read()
        task_content = open(task_file).read()

        return program_content, project_content, task_content



    def _update_program_table(self, program_list):
        self._log("Loading Programs.")
        for prog in program_list:
            program = Program.objects.filter(rms_id=prog['@id']).first()
            if program is None:
                self._log("  Program not found: " + prog['acronym'])
                program = Program()
            program.rms_id = prog['@id']
            program.title = prog['title']
            program.acronym = prog['acronym']
            program.url = prog['url']
            program.save()


    def _update_project_table(self, project_list):
        self._log("Loading Projects.")
        for proj in project_list:
            fk = proj['RMSprogram_id']
            if fk != '' and fk != None:
                program = Program.objects.filter(rms_id=fk).first()
                if program is not None:
                    project = Project()
                    program_name = program.acronym
                    pattern = re.compile(program_name, re.IGNORECASE)
                    project.epa_id = pattern.sub("", proj['epa_id']).strip()
                    project.program = program
                    project.title = proj['title']
                    project.IRMS_project_id = proj['IRMS_project_id']
                    project.RMSprogram_id = fk
                    project.url = proj['url']
                    project.rms_id = proj['@id']
                    project.start_date = proj['start_date']
                    project.end_date = proj['end_date']
                    project.save()


    def _update_task_table(self,task_list):
        self._log("Loading Tasks.")
        for tsk in task_list:
            fk = tsk['RMSproject_id']
            if fk != '':
                project = Project.objects.filter(rms_id=fk).first()
                if project is not None:
                    task = Task()
                    program_name = project.program.acronym
                    pattern = re.compile(program_name, re.IGNORECASE)
                    task.epa_id = pattern.sub("", tsk['epa_id']).strip()
                    task.project = project
                    task.program = project.program
                    task.title = tsk['title']
                    task.RMSproject_id = fk
                    task.url = tsk['url']
                    task.rms_id = tsk['@id']
                    task.start_date = tsk['start_date']
                    task.end_date = tsk['end_date']
                    task.save()


    def handle(self, *args, **options):

        try:
            #Test to see if RMS service is available.
            program_string, project_string, task_string = self._load_content_from_urls()
        except Exception as e1:
            self._log("Can't get wsdl service, falling back on files. Error:" + str(e1))
            try:
                #if not get it from files
                program_string, project_string, task_string = self._load_content_from_files()
            except Exception as e2:
                self._log("Failed to load RAP content from files: " + str(e2))
                return

        program_list= xmltodict.parse(program_string)['RMSPrograms']['RMSprogram']
        project_list= xmltodict.parse(project_string)['RMSProjects']['RMSproject']
        task_list= xmltodict.parse(task_string)['RMSTasks']['RMStask']

        if len(program_list) and len(project_list) and len(task_list):
            Task.objects.all().delete()
            Project.objects.all().delete()
#            Program.objects.all().delete() # Not deleting programs to preserve show_project column

            self._update_program_table(program_list)
            self._update_project_table(project_list)
            self._update_task_table(task_list)

