# models.py (constants)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=C0301

"""
Models for the qapp_builder application for constants.

Available functions:
-
"""

SUBJECT_CHOICES = (('General Inquiry', 'General Inquiry'),
                   ('Send Me More Info', 'Send Me More Info'),
                   ('Registration Problem', 'Registration Problem'),
                   ('Log-In Issue', 'Log-In Issue'))
SUBMISSION_CHOICES = (('Submitted', 'Submitted'),
                      ('Under Review', 'Under Review'),
                      ('Accepted', 'Accepted'))
SUPPORT_CHOICES = (('', ''), ('QAPP Builder', 'QAPP Builder Values'),
                   ('Help', 'Help'),
                   ('Feature', 'Feature Request'), ('Other', 'Other'))

TODO_STATUS_CHOICES = (('', ''), ('Emergency', 'Emergency'),
                       ('Important', 'Important'),
                       ('Back Burner', 'Back Burner'),
                       ('Complete', 'Complete'))

WGK_CHOICES = (('', ''), ('0', 'nwg'), ('1', 'WGK 1'), ('2', 'WGK 2'),
               ('3', 'WGK 3'))

YN_CHOICES = (('', ''), ('Y', 'Yes'), ('N', 'No'))
ONLY_YN_CHOICES = (('Y', 'Y'),)
YES_OR_NO = ((True, 'Yes'), (False, 'No'))

# From QATRACK Constants:
YNNA_CHOICES = (('', ''), ('Y', 'Y'), ('N', 'N'), ('NA', 'NA'))
PUBLIC_CHOICES = (('', ''), ('PUBLIC', 'PUBLIC'), ('PRIVATE', 'PRIVATE'))
RAP_CHOICES = (('', ''), ('ACE', 'ACE'), ('CSS', 'CSS'), ('SSWR', 'SSWR'),
               ('HHRA', 'HHRA'), ('HSR', 'HSR'), ('SHC', 'SHC'),
               ('Not Applicable', 'Not Applicable'), )
STATUS_CHOICES = (('', ''), ('Active', 'Active'), ('Inactive', 'Inactive'))
USER_TYPE_CHOICES = (('', ''), ('SUPER', 'SUPER USER'), ('ALL', 'ALL LABS'),
                     ('LAB', 'SINGLE LAB'), ('DIVISION', 'DIVISION USER'),
                     ('BRANCH', 'BRANCH USER'))
PERMISSION_CHOICES = (('READER', 'READER'), ('EDITOR', 'EDITOR'),
                      ('ADMIN', 'ADMIN'))
EDITOR_PERMISSION_CHOICES = (('READER', 'READER'), ('EDITOR', 'EDITOR'))
READER_PERMISSION_CHOICES = (('READER', 'READER'))
# This is used only i the equipment app - do not know yet whether that app is
# used in QA Track or not.
METROLOGY_DOC_CHOICES = (
    ('Other', 'Other'), ('CP', 'Calibration Procedure'),
    ('MD', 'Metrology Document'), ('TM', 'Technical Manual'),
    ('Image', 'Image'), ('Thumbnail', 'Thumbnail'), ('Key', 'Key Image - BIG'))


DIVISION_CHOICES = [
    'Groundwater Characterization & Remediation Division',
    'Homeland Security & Materials Management Division',
    'Immediate Office', 'Land Remediation & Technology Division',
    'Technical Support & Coordination Division',
    'Water Infrastructure Division']

QA_CATEGORY_CHOICES = (('QA Category A', 'QA Category A'),
                       ('QA Category B', 'QA Category B'))

XMURAL_CHOICES = (('Intramural', 'Intramural'), ('Extramural', 'Extramural'))
