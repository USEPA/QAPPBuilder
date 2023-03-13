# context_processors.py (QAPP_Builder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=W0613

"""
List of dotted Python paths to callables.

Used to populate the context when a template is rendered with a request.
Callables take request object as argument return dict of items merged into
context. Defaults to an empty list.

Available functions:
- TBD
"""

from django.conf import settings


def software_info(_request):
    """
    Return dictionary containing the app's version, name, and disclaimer.

    :param:
    :request:
    :request:
    """
    return {
        'APP_VERSION': settings.APP_VERSION,
        'APP_NAME': settings.APP_NAME,
        'APP_DISCLAIMER': settings.APP_DISCLAIMER
    }
