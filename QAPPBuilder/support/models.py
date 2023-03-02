# models.py (support)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# pylint: skip-file

"""
Models related to app support.

Available functions:
"""

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


def get_support_storage_path(instance, filename):
    """Return the physical path to where support files will be stored."""
    return '%s/support/%s' % (instance.user.username, filename)


def get_instruction_storage_path(instance, filename):
    """Return the physical path to where instruction files will be stored."""
    return '%s/instructions/%s' % (instance.user.username, filename)


def get_support_attachment_storage_path(instance, filename):
    """Return the physical path to where support attachments will be stored."""
    return 'support/%s/%s' % (instance.support_id, filename)


class SupportType(models.Model):
    """Class representing the types of support requests available."""

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.CharField(blank=True, null=True, max_length=255)
    last_modified_by = models.CharField(blank=True, null=True, max_length=255)

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    the_name = models.CharField(blank=True, null=True, max_length=255)

    the_description = models.TextField(null=True, blank=True)

    weblink = models.CharField(blank=True, null=True, max_length=255)
    ordering = models.DecimalField(
        null=True, blank=True, max_digits=10, decimal_places=1)

    class Meta:
        """Define special ordering."""

        ordering = ["ordering", ]

    def __str__(self):
        """Overwrite the default stringify by returning the object's name."""
        return self.the_name or ''


class Priority(models.Model):
    """Class representing the priority of a support request."""

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.CharField(blank=True, null=True, max_length=255)
    last_modified_by = models.CharField(blank=True, null=True, max_length=255)

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)

    the_name = models.CharField(blank=True, null=True, max_length=255)

    the_description = models.TextField(null=True, blank=True)

    weblink = models.CharField(blank=True, null=True, max_length=255)
    ordering = models.DecimalField(
        null=True, blank=True, max_digits=10, decimal_places=1)

    class Meta:
        """Define special ordering."""

        ordering = ["ordering", ]

    def __str__(self):
        """Overwrite the default stringify by returning the object's name."""
        return self.the_name or ''


class Support(models.Model):
    """The main support class, allows users to request support for the app."""

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True,
        related_name="support_created_by")
    last_modified_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True,
        related_name="support_last_modified_by")
    make_public = models.BooleanField(blank=False, default=False)
    share_with_user_group = models.BooleanField(blank=False, default=False)

    attachment = models.FileField(
        null=True, blank=True, upload_to=get_support_storage_path)

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    support_type = models.ForeignKey(
        SupportType, on_delete=models.CASCADE, null=True, blank=True)
    priority = models.ForeignKey(
        Priority, on_delete=models.CASCADE, null=True, blank=True)

    the_name = models.CharField(blank=True, null=True, max_length=255)
    subject = models.CharField(blank=True, null=True, max_length=255)
    length_of_reference = models.CharField(
        blank=True, null=True, max_length=255)
    author = models.CharField(blank=True, null=True, max_length=255)

    is_closed = models.BooleanField(blank=False, default=False)

    the_description = models.TextField(null=True, blank=True)
    resolution = models.TextField(null=True, blank=True)

    weblink = models.CharField(blank=True, null=True, max_length=255)
    ordering = models.DecimalField(
        null=True, blank=True, max_digits=10, decimal_places=1)
    date_resolved = models.DateField(blank=True, null=True)

    STATUSES = (
        ('To Do', 'To Do'),
        ('In Progress', 'In Progress'),
        ('Done', 'Done'),
    )

    status = models.CharField(max_length=25, choices=STATUSES, default='To Do')

    review_notes = models.TextField(null=True, blank=True)

    class Meta:
        """Define special ordering."""

        ordering = ["ordering", ]

    def __str__(self):
        """Overwrite the default stringify by returning the object's name."""
        return self.the_name or ''


class SupportAttachment(models.Model):
    """Class representing an attachment for a support request."""

    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True, null=True, blank=True)
    created_by = models.CharField(blank=True, null=True, max_length=255)
    last_modified_by = models.CharField(blank=True, null=True, max_length=255)

    attachment = models.FileField(
        null=True, blank=True, max_length=255,
        upload_to=get_support_attachment_storage_path)

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    support = models.ForeignKey(Support, on_delete=models.CASCADE,
                                null=True, blank=True,
                                related_name="support_attachments")

    the_name = models.CharField(blank=True, null=True, max_length=255)
    the_size = models.CharField(blank=True, null=True, max_length=255)

    class Meta:
        """Define special ordering."""

        ordering = ['the_name', ]

    def icon_to_use(self):
        """Define what icon to use for an attachment based on file format."""
        if str(self.attachment).endswith('pdf'):
            icon_src = settings.STATIC_URL + "img/pdf-icon.jpg"
        elif str(self.attachment).endswith('xls'):
            icon_src = settings.STATIC_URL + "img/xlsx.jpg"
        elif str(self.attachment).endswith('xlsx'):
            icon_src = settings.STATIC_URL + "img/xlsx.jpg"
        elif str(self.attachment).endswith('doc'):
            icon_src = settings.STATIC_URL + "img/word.png"
        elif str(self.attachment).endswith('docx'):
            icon_src = settings.STATIC_URL + "img/docx.png"
        elif str(self.attachment).endswith('doc'):
            icon_src = settings.STATIC_URL + "img/docx.png"
        elif str(self.attachment).endswith('html'):
            icon_src = settings.STATIC_URL + "img/html.png"
        elif str(self.attachment).endswith('txt'):
            icon_src = settings.STATIC_URL + "img/txt.jpg"
        elif str(self.attachment).endswith('csv'):
            icon_src = settings.STATIC_URL + "img/csv.png"
        elif str(self.attachment).endswith('psd'):
            icon_src = settings.STATIC_URL + "img/psd.jpg"
        else:
            icon_src = settings.STATIC_URL + "uploads/" + str(self.attachment)
        return icon_src
