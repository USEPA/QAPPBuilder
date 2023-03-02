# pylint: skip-file
# test_data/support_forms.py (GSC_ESSENR)
# !/usr/bin/env python3
# coding=utf-8

"""
This file contains static, pre-filled forms for running Hatch Test Cases
"""

from support.forms import SupportForm

SUPPORT_PASS_ONE = SupportForm()
SUPPORT_PASS_ONE.id = 1
SUPPORT_PASS_ONE.subject = "subject"
SUPPORT_PASS_ONE.the_description = "the_description"
SUPPORT_PASS_ONE.weblink = "aweblink@something.com"

SUPPORT_PASS_ONE_EDIT = SupportForm()
SUPPORT_PASS_ONE_EDIT.id = 1
SUPPORT_PASS_ONE_EDIT.subject = "subject_EDIT"
SUPPORT_PASS_ONE_EDIT.the_description = "the_description_EDIT"
SUPPORT_PASS_ONE_EDIT.weblink = "aweblink@something.com"

SUPPORT_PASS_ONE_EDIT_DICT = {}
SUPPORT_PASS_ONE_EDIT_DICT['id'] = 1
SUPPORT_PASS_ONE_EDIT_DICT['subject'] = "subject_EDIT"
SUPPORT_PASS_ONE_EDIT_DICT['the_description'] = "the_description_EDIT"
SUPPORT_PASS_ONE_EDIT_DICT['weblink'] = "aweblink@something.com"
