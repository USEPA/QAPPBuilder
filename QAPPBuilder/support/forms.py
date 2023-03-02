# forms.py (support)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# pylint: skip-file

"""
Form used to manage support issues.

Available functions:
"""

from django.forms import ModelForm, CharField, TextInput, Textarea, DateField
from django.utils.translation import gettext_lazy as _
from support.models import Support, Priority, SupportType


class SupportForm(ModelForm):
    """A Form For Creating a Support Issue."""

    def __init__(self, *args, **kwargs):
        """Support form to send to Django Admin."""
        super(SupportForm, self).__init__(*args, **kwargs)

    required_css_class = 'required'

    id = CharField(
        label=_("Reference Num"),
        widget=TextInput(
            attrs={'class': 'form-control', 'readonly': 'readonly'}),
        required=False)
    subject = CharField(
        label=_("Subject"), widget=TextInput(attrs={'class': 'form-control'}),
        required=True)

    the_description = CharField(
        label=_("Description"),
        widget=Textarea(attrs={'class': 'form-control'}),
        required=True)
    weblink = CharField(
        label=_("Email Address"),
        widget=TextInput(attrs={'class': 'form-control'}),
        required=True)

    class Meta:
        """Support link."""

        model = Support
        fields = ("id", "subject", "the_description", "weblink",)


class SupportAdminForm(ModelForm):
    """A Form For Responding To a Support Issue."""

    def __init__(self, *args, **kwargs):
        """Support Django Admin form."""
        super(SupportAdminForm, self).__init__(*args, **kwargs)

    required_css_class = 'required'

    id = CharField(
        label=_("Reference Num"),
        widget=TextInput(
            attrs={'class': 'form-control', 'readonly': 'readonly'}),
        required=False)
    subject = CharField(
        label=_("Subject"), widget=TextInput(attrs={'class': 'form-control'}),
        required=True)
    date_resolved = DateField(
        label=_("Date Resolved"),
        widget=TextInput(attrs={'class': 'form-control date-control'}),
        required=False)
    the_description = CharField(
        label=_("Description"),
        widget=Textarea(attrs={'class': 'form-control'}),
        required=True)
    weblink = CharField(
        label=_("Email Address"),
        widget=TextInput(attrs={'class': 'form-control'}),
        required=True)
    review_notes = CharField(
        label=_("Review Notes"),
        widget=Textarea(attrs={'class': 'form-control'}),
        help_text="Notes from review of suggestion", required=False)

    class Meta:
        """All fields to complete support form."""

        model = Support
        fields = (
            "id", "subject", "the_description", "weblink",
            "date_resolved", "review_notes",)


class SupportTypeForm(ModelForm):
    """A Form For Creating a Support Issue."""

    def __init__(self, *args, **kwargs):
        """Form type."""
        super(SupportTypeForm, self).__init__(*args, **kwargs)

    required_css_class = 'required'
    the_name = CharField(
        label=_("Support Type"),
        widget=TextInput(attrs={'class': 'form-control'}),
        required=False)

    class Meta:
        """Name form."""

        model = SupportType
        fields = ("the_name",)


class PriorityForm(ModelForm):
    """A Form For Creating a Support Issue."""

    def __init__(self, *args, **kwargs):
        """Form priority."""
        super(PriorityForm, self).__init__(*args, **kwargs)

    the_name = CharField(
        label=_("Priority"),
        widget=TextInput(attrs={'class': 'form-control'}),
        required=False)

    class Meta:
        """Form priority.."""

        model = Priority
        fields = ("the_name",)
