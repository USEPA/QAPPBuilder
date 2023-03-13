# qar5_pdf.py (qapp_builder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov

"""Definition of qar5 pdf export views."""

from io import BytesIO
import tempfile
from zipfile import ZipFile
from wkhtmltopdf.views import PDFTemplateResponse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.utils.text import slugify
from constants.qar5_sectionb import SECTION_B_INFO
from qapp_builder.views import get_qapp_info, get_qar5_for_team, \
    get_qar5_for_user


@login_required
def export_pdf(request, *args, **kwargs):
    """Export multiple QAPP objects as PDF documents."""
    if 'user' in request.path:
        user_id = kwargs.get('pk', None)
        team_id = qapp_id = None
    elif 'team' in request.path:
        team_id = kwargs.get('pk', None)
        user_id = qapp_id = None
    else:
        qapp_id = kwargs.get('pk', None)
        team_id = user_id = None

    if qapp_id is None or user_id or team_id:
        if user_id:
            qapp_ids = get_qar5_for_user(
                user_id).values_list('id', flat=True)
        else:
            qapp_ids = get_qar5_for_team(
                team_id).values_list('id', flat=True)

        # Create a zip archive to return multiple PDFs
        zip_mem = BytesIO()
        archive = ZipFile(zip_mem, 'w')
        for q_id in qapp_ids:
            resp = export_pdf_single(request, pk=q_id)
            filename = resp.filename
            if filename:
                temp_file_name = '%d_%s' % (q_id, filename)
                resp.render()
                with tempfile.SpooledTemporaryFile():
                    archive.writestr(temp_file_name, resp.content)

        archive.close()
        response = HttpResponse(
            zip_mem.getvalue(), content_type='application/force-download')
        response['Content-Disposition'] = \
            'attachment; filename="%s_qapps.zip"' % request.user.username
        response['Content-length'] = zip_mem.tell()
        return response


def export_pdf_single(request, *args, **kwargs):
    """Export a single QAPP object as a PDF document."""
    template_name = 'export/qar5_pdf_template.html'
    # Get all required data before populating the PDF Export Template

    qapp_id = kwargs.get('pk', None)
    qapp_info = get_qapp_info(request.user, qapp_id)
    qapp_info['qapp'] = qapp_info['qapp']

    if not qapp_info:
        return HttpResponse(request)

    # Prepare a list of dictionaries to replace the default sectionb objects
    section_b_list = []
    for sectionb in qapp_info['section_b']:
        sectionb_type = sectionb.sectionb_type.name
        section_b_info = SECTION_B_INFO[sectionb_type]
        section_b = {'sectionb_type': sectionb_type}
        for key in section_b_info:
            section_b[key] = {}
            val = getattr(sectionb, key, '')
            if section_b_info[key].get('heading', False):
                section_b[key]['heading'] = section_b_info[key]['heading']
            section_b[key]['label'] = section_b_info[key]['label']
            section_b[key]['value'] = val
        section_b_list.append(section_b)
    # Replace the sectionb object with the prepared dictionary
    qapp_info['section_b'] = section_b_list

    filename = '%s.pdf' % slugify(qapp_info['qapp'].title)
    options = {'enable-local-file-access': ""}
    resp = PDFTemplateResponse(
        request=request,
        template=template_name,
        filename=filename,
        context=qapp_info,
        show_content_in_browser=False,
        cmd_options=options,
    )
    return resp
