# context_processors.py (qapp_builder)
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
from django.urls import reverse


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


def context(request):
    claims = request.identity_context_data._id_token_claims
    exclude_claims = ['iat', 'exp', 'nbf', 'uti', 'aio', 'rh']
    claims_to_display = {claim: value for claim, value in claims.items()
                         if claim not in exclude_claims}

    client_id = settings.AAD_CONFIG.client.client_id
    aad_link = f'https://portal.azure.com/#blade/\
                 Microsoft_AAD_RegisteredApps/ApplicationMenuBlade/\
                 Authentication/appId/{client_id}/isMSAApp/'

    return dict(
        claims_to_display=claims_to_display,
        redirect_uri_external_link=request.build_absolute_uri(
            reverse(settings.AAD_CONFIG.django.auth_endpoints.redirect)),
        aad_link=aad_link)
