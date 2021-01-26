# utils.py (constants)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=C0301,R0913

"""
Utility methods for the entire project.

Available functions:
- split_email_list
- is_epa_email
- non_epa_email_message
- create_qt_email_message
- get_rap_fields
- sort_rap_numbers
- xstr
"""

from io import BytesIO
from operator import itemgetter
from os import path
from zipfile import ZipFile
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse


upload_storage = FileSystemStorage(location=settings.UPLOAD_ROOT,
                                   base_url='/uploads')


# NOTE: This path requires a leading 'uploads'
def get_attachment_storage_path(instance, filename):
    """Build the attachment storage path using username and filename."""
    return '%s/attachments/%s' % (
        instance.uploaded_by.username, filename)


# Email Utility functions.
def split_email_list(email_list):
    """Replace all defined delimiter characters with spaces."""
    delimiters = [';', ',', '\t', '|']
    for delim in delimiters:
        email_list = email_list.replace(delim, ' ')
        # replace delims with a space.

    return email_list.split()


def is_epa_email(email):
    """Check if an email is of the EPA domain 'epa.gov'."""
    email = email.strip().lower()
    epa = '@epa.gov'
    if epa not in email:  # initial, does it contain @epa.gov
        return False

    ending = email[email.index(epa) + len(epa):]  # email contains @epa.gov
    # Preventing alphanumeric and '.' to prevent @epa.gov_bad_domain.com...
    # who would do this anyway? Users.
    illegal_end_chars = r"[a-z][A-Z][0-9]\."

    # checks if string has any of the illgal chars
    if any(elem in illegal_end_chars for elem in ending):
        return False
    # print(ending)
    # print(illegal_end_chars)
    return True  # if we pass, it must be epa right?


def non_epa_email_message(emails):
    """
    Lets the user know which emails are not EPA.

    And that they must be sent manually.
    """
    return "Email list may only contain @epa.gov addresses. " + \
        "Please sendnon-EPA emails directly from Outlook. " + \
        "Offending email(s): " + ', '.join(emails)


def create_qt_email_message(email_subject, text_content, from_email, to_emails,
                            carbon_copy=None, blind_carbon_copy=None):
    """
    Modify email content.

    To have a disclaimer at top and adds blind_carbon_copy
    for monitoring that email functionality is working. Returns
    EmailMultiAlternatives object.
    """
    if settings.BCC_EMAIL:
        if blind_carbon_copy:
            blind_carbon_copy.append(settings.BCC_EMAIL)
        else:
            blind_carbon_copy = [settings.BCC_EMAIL]

    html_content = settings.EMAIL_DISCLAIMER + text_content.replace(
        "\r\n", "<br>").replace("\n", "<br>")
    text_content_modified = settings.EMAIL_DISCLAIMER_PLAIN + \
        "\r\n\r\n" + text_content

    the_email = EmailMultiAlternatives(
        email_subject, text_content_modified, from_email,
        to_emails, cc=carbon_copy, bcc=blind_carbon_copy)
    the_email.attach_alternative(html_content, "text/html")

    return the_email


# RAP Utility Functions
def get_rap_fields(fields='default'):
    """Return a list of rap fields."""
    if fields == 'form':
        return [
            ['ace', 'ace_rap_numbers'], ['css', 'css_rap_numbers'],
            ['sswr', 'sswr_rap_numbers'], ['hhra', 'hhra_rap_numbers'],
            ['hsrp', 'hsrp_rap_numbers'], ['hsre', 'hsrp_rap_extensions'],
            ['shc', 'shc_rap_numbers']]

    return ['ace_rap_numbers', 'css_rap_numbers', 'sswr_rap_numbers',
            'hhra_rap_numbers', 'hsrp_rap_numbers',
            'hsrp_rap_extensions', 'shc_rap_numbers']


def sort_rap_numbers(rap_list):
    """
    Sort RAP Numbers.

    Sorts the rap numbers first by it's first digit then alphanumerically.
    """
    def _get_numeric(the_str):
        try:
            val = float(the_str.split('.')[0])  # e.g. the 16 in 16.2.2
            return val
        except ValueError:
            # woah if not numeric assign infinity e.g. like CIVA-2.5
            return float("inf")

    arr = [(row, _get_numeric(row)) for row in rap_list]
    return [row[0] for row in sorted(arr, key=itemgetter(1, 0))]


def xstr(p_str):
    """Check for and replaces None objects with empty strings."""
    if p_str is None:
        return ''
    return str(p_str)


def is_float(val_str):
    """
    Take a string and tries to parse it as a float.

    If parse fails, returns false. Otherwise parse succeeds
    and true is returned.
    """
    try:
        float(val_str)
    except ValueError:
        return False
    return True


def download_files(file_list, zip_name):
    """Shared method to zip multiple files and return them to the browser."""
    # Create a zip archive to return multiple files: PDF, n attachments.
    zip_mem = BytesIO()
    archive = ZipFile(zip_mem, 'w')
    for file in file_list:
        try:
            t_file = file.file.file
            temp_path = path.basename(t_file.name)
            archive.write(t_file.name, temp_path)
        except FileNotFoundError:
            print('File not found!')

    archive.close()
    response = HttpResponse(zip_mem.getvalue(),
                            content_type='application/force-download')
    response['Content-Disposition'] = 'attachment; filename=' + \
        '"%s.zip"' % zip_name
    response['Content-length'] = zip_mem.tell()
    return response


def download_file(p_file):
    """Download a single file (Upload object)."""
    # Check file extensions, some (Excel) require special content types
    name_split = p_file.file.name.split('.')
    ext = name_split[len(name_split) - 1]

    with open(p_file.file.file.name, 'rb') as file:
        if 'xls' in ext:
            con_type = 'application/vnd.vnd.openxmlformats-' + \
                'officedocument.spreadsheetml.sheet'
            response = HttpResponse(file, con_type)
        else:
            response = HttpResponse(file)

        con_disp = 'attachment; filename="' + p_file.name + '"'
        response['Content-Disposition'] = con_disp
        return response
