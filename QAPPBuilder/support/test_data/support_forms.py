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
SUPPORT_PASS_ONE.weblink = "main/support.html"



