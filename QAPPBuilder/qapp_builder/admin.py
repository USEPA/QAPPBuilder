# admin.py (qapp_builder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov


"""
Defines classes used to generate Django Admin portion of website.

Should be an Admin class for each Model that can be modified by an admin user.

Available functions:
- TBD
"""

from django.contrib import admin
from qapp_builder.forms import QappForm
from qapp_builder.models import Qapp, SectionA, SectionB, SectionD, \
    References, Revision, Division


class QappAdmin(admin.ModelAdmin):
    """
    Define options used to display and edit Qapp objects.

    (qapp_builder) on the Django Admin page.
    """

    list_display = ("division_branch", "title", "qa_category",
                    "revision_number", "strap", "tracking_id")
    search_fields = ("division_branch", "title", "qa_category")
    list_per_page = 25
    form = QappForm

    def save_model(self, request, obj, form, change):
        """
        Overwrite the default save_model method.

        So we can automatically set the prepared_by field as current user.
        """
        # Only set prepared_by when it's the first save (create)
        if not obj.pk:
            obj.prepared_by = request.user
        return super().save_model(request, obj, form, change)


admin.site.register(Qapp, QappAdmin)

admin.site.register(Division)

admin.site.register(SectionA)

admin.site.register(SectionB)

admin.site.register(SectionD)

admin.site.register(References)

admin.site.register(Revision)
