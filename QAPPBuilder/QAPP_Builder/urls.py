# urls.py (QAPP_Builder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov


"""Definition of urls for QAPP_Builder."""

from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from QAPP_Builder.views import QappCreate, QappDetail, ProjectApprovalCreate, \
    ProjectLeadCreate, ProjectApprovalSignatureCreate, SectionAView, \
    SectionBView, SectionCView, SectionDView, SectionEView, SectionFView, \
    RevisionCreate, QappList, QappEdit, QappIndex, ProjectApprovalEdit, \
    ProjectApprovalSignatureDelete, ProjectApprovalSignatureEdit, \
    ProjectLeadDelete, ProjectLeadEdit, contact, clean_qapps, web_dev_tools
from QAPP_Builder.settings import MEDIA_ROOT, MEDIA_URL
from QAPP_Builder.qar5_docx import export_doc, export_doc_single
from QAPP_Builder.qar5_pdf import export_pdf, export_pdf_single


urlpatterns = [
    url(r'^admin', admin.site.urls),

    url(r'^$', QappIndex.as_view(), name='home'),
    url(r'^dashboard/?$', QappIndex.as_view(), name='dashboard'),
    url(r'^contact/?$', contact, name='contact'),

    url(r'^dev/?$', web_dev_tools, name='web_dev_tools'),
    url(r'^dev/clean_qapps/?$', clean_qapps, name='clean_qapps'),

    # From the original QAR5 module:
    url(r'^create/?$',
        QappCreate.as_view(),
        name='qapp_create'),

    url(r'^detail/(?P<pk>\d+)/?$',
        QappDetail.as_view(),
        name='qapp_detail'),

    url(r'^edit/(?P<pk>\d+)/?$',
        QappEdit.as_view(),
        name='qapp_edit'),

    url(r'^list/user/(?P<pk>\d+)/?$',
        QappList.as_view(),
        name='qapp_list'),
    url(r'^list/team/(?P<pk>\d+)/?$',
        QappList.as_view(),
        name='qapp_list'),

    # Single QAPP Exports (if user has access, owner or team):
    url(r'^exportdoc/(?P<pk>\d+)/?$',
        export_doc_single, name='qar5_doc'),
    url(r'^exportpdf/(?P<pk>\d+)/?$',
        export_pdf_single, name='qar5_pdf'),

    # All QAPP Exports for User:
    url(r'^exportdoc/user/(?P<pk>\d+)/?$',
        export_doc, name='qar5_all_doc'),
    url(r'^exportpdf/user/(?P<pk>\d+)/?$',
        export_pdf, name='qar5_all_pdf'),

    # All QAPP Exports for Team:
    url(r'^exportdoc/team/(?P<pk>\d+)/?$',
        export_doc, name='qar5_all_doc'),
    url(r'^exportpdf/team/(?P<pk>\d+)/?$',
        export_pdf, name='qar5_all_pdf'),

    ############################################
    # Project Approval (and signatures) URLs
    url(r'^approval/create/?$',
        ProjectApprovalCreate.as_view(),
        name='qapp_approval'),

    url(r'^approval/edit/(?P<pk>\d+)/?$',
        ProjectApprovalEdit.as_view(),
        name='qapp_approval_edit'),

    # Project Approval Signatures URLs
    url(r'^approval_signature/create/?$',
        ProjectApprovalSignatureCreate.as_view(),
        name='get_approval_signature_form'),

    url(r'^approval_signature/delete/(?P<pk>\d+)/?$',
        ProjectApprovalSignatureDelete.as_view(),
        name='delete_approval_signature'),

    url(r'^approval_signature/edit/(?P<pk>\d+)/?$',
        ProjectApprovalSignatureEdit.as_view(),
        name='edit_approval_signature'),

    ############################################
    # Project Lead URLs
    url(r'^project_lead/create/?$',
        ProjectLeadCreate.as_view(),
        name='get_project_lead_form'),

    url(r'^project_lead/delete/(?P<pk>\d+)/?$',
        ProjectLeadDelete.as_view(),
        name='delete_project_lead'),

    url(r'^project_lead/edit/(?P<pk>\d+)/?$',
        ProjectLeadEdit.as_view(),
        name='edit_project_lead'),

    ############################################
    # SectionB URLs
    url(r'^SectionA/?$', SectionAView.as_view(), name='qapp_sectiona'),
    url(r'^SectionB/?$', SectionBView.as_view(), name='qapp_sectionb'),
    url(r'^SectionC/?$', SectionCView.as_view(), name='qapp_sectionc'),
    url(r'^SectionD/?$', SectionDView.as_view(), name='qapp_sectiond'),
    url(r'^SectionE/?$', SectionEView.as_view(), name='qapp_sectione'),
    url(r'^SectionF/?$', SectionFView.as_view(), name='qapp_sectionf'),

    # Revision is part of Section F
    url(r'^revision/create/?$',
        RevisionCreate.as_view(),
        name='create_revision'),


    # Begin other module import URLs.
    url(r'^accounts/', include('accounts.urls')),
    url(r'^support/', include('support.urls')),
    url(r'^teams/', include('teams.urls')),
]

urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
