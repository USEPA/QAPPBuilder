# admin.py (accounts)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov

"""
Django Admin Accounts.

This file defines classes that are used to generate the 'Accounts' Django Admin
portion of the website. There should be an Admin class for each Model that can
be modified by an admin user.

Available functions:
- None for this module -- TBD (would like added to manage in Django Admin)
"""

from django.contrib import admin
from accounts.models import UserProfile, Country, State, Sector, Role

admin.site.register(Country)
admin.site.register(State)
admin.site.register(Sector)
admin.site.register(Role)


class UserProfileAdmin(admin.ModelAdmin):
    """Assigns 'USER ID' number, once user registers with QAPP_Builder."""

    list_display = ("user_id",)
    search_fields = ("user__username",)
    exclude = ('created_by', 'last_modified_by',)
    list_filter = ("user_id",)
    list_per_page = 25


admin.site.register(UserProfile, UserProfileAdmin)
