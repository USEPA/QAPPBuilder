# admin.py (support)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# pylint: skip-file

"""
Defines classes used to generate the 'Support' Django Admin.

There should be an Admin class for each Model that can
be modified by an admin user.

Available functions:
- None for this module -- TBD (would like added to manage in Django Admin)
"""

from django.contrib import admin
from support.models import Support, SupportType, Priority

admin.site.register(Support)
admin.site.register(SupportType)
admin.site.register(Priority)
