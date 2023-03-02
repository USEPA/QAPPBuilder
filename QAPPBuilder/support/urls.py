# urls.py (support)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# pylint: skip-file
# We disable the invalid name because urlpatterns is the Django default

"""URLs and routing for the Support module."""

from django.urls import re_path
from .views import index, UserManualView, EventsView, \
    ReferencesView, event_file_download, SuggestionCreateView, \
    SuggestionEditView, delete_support, list_supports, show_support, \
    file_upload_support, delete_support_attachment, create_support_type, \
    edit_support_type, delete_support_type, list_support_types, \
    show_support_type, create_priority, edit_priority, delete_priority, \
    list_priorities, show_priority

app_name = 'support'

urlpatterns = [
    re_path(r'^$', index),
    re_path(r'^index/$', index, name='go_to_support'),

    re_path(
        r'^documentation/$', UserManualView.as_view(), name="documentation"),
    re_path(r'events/', EventsView.as_view(), name='events'),
    re_path(r'references/', ReferencesView.as_view(), name='references'),

    re_path(
        r'^files/(?P<file_name>.+)/$', event_file_download,
        name='event_file_download'),

    re_path(r'^create/(?P<support_type_name>\w+)/$',
            SuggestionCreateView.as_view(), name='create_support'),
    re_path(r'^edit/(?P<support_type_name>\w+)/(?P<obj_id>\d+)/$',
            SuggestionEditView.as_view(), name='edit_support'),
    re_path(r'^delete/(?P<support_type_name>\w+)/(?P<obj_id>\d+)/$',
            delete_support, name='delete_support'),
    re_path(r'^list/(?P<support_type_name>\w+)/$',
            list_supports, name='list_supports'),
    re_path(r'^show/(?P<obj_id>\d+)/$', show_support, name='show_support'),

    # new
    re_path(r'^file/upload/(?P<obj_id>\d+)/$',
            file_upload_support, name='file_upload_support'),
    re_path(r'^support_attachment/delete/(?P<obj_id>\d+)/$',
            delete_support_attachment, name='delete_support_attachment'),

    re_path(r'^type/create/$',
            create_support_type, name='create_support_type'),
    re_path(r'^type/edit/(?P<obj_id>\d+)/$',
            edit_support_type, name='edit_support_type'),
    re_path(r'^type/delete/(?P<obj_id>\d+)/$',
            delete_support_type, name='delete_support_type'),
    re_path(r'^type/list/$', list_support_types, name='list_support_types'),
    re_path(r'^type/show/(?P<obj_id>\d+)/$',
            show_support_type, name='show_support_type'),

    re_path(r'^priority/create/$',
            create_priority, name='create_priority'),
    re_path(r'^priority/edit/(?P<obj_id>\d+)/$',
            edit_priority, name='edit_priority'),
    re_path(r'^priority/delete/(?P<obj_id>\d+)/$',
            delete_priority, name='delete_priority'),
    re_path(r'^priority/list/$',
            list_priorities, name='list_priorities'),
    re_path(r'^priority/show/(?P<obj_id>\d+)/$',
            show_priority, name='show_priority'),
]
