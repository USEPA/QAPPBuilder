# urls.py (support)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# pylint: skip-file
# We disable the invalid name because urlpatterns is the Django default

"""URLs and routing for the Support module."""

from django.conf.urls import url
from .views import index, UserManualView, EventsView, \
    event_file_download, SuggestionCreateView, \
    SuggestionEditView, delete_support, list_supports, show_support, \
    file_upload_support, delete_support_attachment, create_support_type, \
    edit_support_type, delete_support_type, list_support_types, \
    show_support_type, create_priority, edit_priority, delete_priority, \
    list_priorities, show_priority

app_name = 'support'

urlpatterns = [
    url(r'^$', index),
    url(r'^index/$', index, name='go_to_support'),

    url(r'^documentation/$', UserManualView.as_view(), name="documentation"),
    # url(r'^download_manual/$', download_manual, name="download_manual"),
    url(r'events/', EventsView.as_view(), name='events'),

    url(r'^files/(?P<file_name>.+)', event_file_download,
        name='event_file_download'),

    url(r'^create/(?P<support_type_name>\w+)/$',
        SuggestionCreateView.as_view(), name='create_support'),
    url(r'^edit/(?P<support_type_name>\w+)/(?P<obj_id>\d+)/$',
        SuggestionEditView.as_view(), name='edit_support'),
    url(r'^delete/(?P<support_type_name>\w+)/(?P<obj_id>\d+)/$',
        delete_support, name='delete_support'),
    url(r'^list/(?P<support_type_name>\w+)/$',
        list_supports, name='list_supports'),
    url(r'^show/(?P<support_type_name>\w+)/(?P<obj_id>\d+)/$',
        show_support, name='show_support'),

    # new
    url(r'^file/upload/(?P<obj_id>\d+)/$', file_upload_support,
        name='file_upload_support'),
    url(r'^support_attachment/delete/(?P<obj_id>\d+)/$',
        delete_support_attachment, name='delete_support_attachment'),

    url(r'^type/create/$', create_support_type, name='create_support_type'),
    url(r'^type/edit/(?P<obj_id>\d+)/$',
        edit_support_type, name='edit_support_type'),
    url(r'^type/delete/(?P<obj_id>\d+)/$',
        delete_support_type, name='delete_support_type'),
    url(r'^type/list/$', list_support_types, name='list_support_types'),
    url(r'^type/show/(?P<obj_id>\d+)/$', show_support_type,
        name='show_support_type'),

    url(r'^priority/create/$', create_priority, name='create_priority'),
    url(r'^priority/edit/(?P<obj_id>\d+)/$', edit_priority,
        name='edit_priority'),
    url(r'^priority/delete/(?P<obj_id>\d+)/$', delete_priority,
        name='delete_priority'),
    url(r'^priority/list/$', list_priorities, name='list_priorities'),
    url(r'^priority/show/(?P<obj_id>\d+)/$', show_priority,
        name='show_priority'),
]
