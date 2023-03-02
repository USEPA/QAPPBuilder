# tests.py (support)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# pylint: skip-file

"""
This file houses test cases for the Support module.

Available functions:
- None
"""

# TODO Test Email sender:
# https://stackoverflow.com/questions/3728528/testing-email-sending

from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import Client, TestCase
from django.test.client import RequestFactory
# from django.core.mail import EmailMultiAlternatives
# from GSC_SSSENR.utils import replace_none_empty_str
from support.models import SupportType
from support.views import download_file, replace_none_empty_str
from support.forms import SupportForm
from support.test_data.support_forms import SUPPORT_PASS_ONE


class TestViews(TestCase):
    """Test the functions related to UsernameReminderRequestView."""

    def setUp(self):
        """Prepare objects for testing the Support module."""
        self.support_type = SupportType.objects.all().first()
        self.client = Client()

        self.user = User.objects.create_user(
            username='testuser', password='12345', is_staff=False)
        self.user_staff = User.objects.create_user(
            username='teststaff', password='12345', is_staff=True)
        self.login_user()

        self.factory = RequestFactory()
        self.filename_docx = 'test_download.docx'
        self.filename_xls = 'test_download.xlsx'

        self.support_form = SupportForm(data=SUPPORT_PASS_ONE.__dict__)
        self.support_obj = self.support_form.save(commit=False)
        self.support_obj.support_type = self.support_type
        self.support_obj.created_by = self.user
        self.support_obj.save()

    def login_user(self):
        """Login the vanilla testing user."""
        self.client.logout()
        self.client.login(username='testuser', password='12345')

    def login_staff(self):
        """Login the staff testing user."""
        self.client.logout()
        self.client.login(username='teststaff', password='12345')

    def test_user_manual_view_get(self):
        """Test the UserManualView class GET method."""
        response = self.client.get('/support/documentation/')
        self.assertEqual(response.status_code, 200)

    def test_references_view_get(self):
        """Test the ReferencesView class GET method."""
        response = self.client.get('/support/references/')
        self.assertEqual(response.status_code, 200)

    def test_events_view_get(self):
        """Test the EventsView class GET method."""
        response = self.client.get('/support/events/')
        self.assertEqual(response.status_code, 200)

    def test_download_manual(self):
        """Test the download_manual method."""
        response = self.client.get('/support/download_manual/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('attachment; filename=',
                      response.get('Content-Disposition'))

    # TODO: TypeError: argument of type 'NoneType' is not iterable
    # def test_event_file_download(self):
    #     """Test the event_file_download method."""
    #     response = self.client.get(
    #         f'/support/files/{self.filename_docx}/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn('attachment; filename=',
    #                   response.get('Content-Disposition'))

    def test_download_file(self):
        """Test the download_file method."""
        request = self.client.get('/support/')
        response = download_file(request, self.filename_docx)
        self.assertEqual(response.status_code, 200)
        self.assertIn('attachment; filename=',
                      response.get('Content-Disposition'))

    def test_download_file_xls(self):
        """Test the download_file method."""
        request = self.client.get('/support/')
        response = download_file(request, self.filename_xls)
        self.assertEqual(response.status_code, 200)
        self.assertIn('attachment; filename=',
                      response.get('Content-Disposition'))

    def test_home(self):
        """Test the home page."""
        response = self.client.get('/support/index/')
        self.assertContains(response, 'Help/Suggestions', 2, 200)

    def test_support_ticket_create_one(self):
        """Test the support ticket form when you use suggestion."""
        # create/(?P<support_type_name>\w+)
        response = self.client.get('/support/create/suggestion/')
        self.assertContains(
            response, 'Describe your suggestion',
            1, 200)

    def test_support_ticket_create_two(self):
        """Test the support ticket form when you do not use suggestion."""
        # create/(?P<support_type_name>\w+)
        response = self.client.get('/support/create/OtherWordsHERE/')
        self.assertContains(
            response, 'Describe the problem',
            1, 200)

    def test_support_post_one(self):
        """Tests the support ticket post method on an invalid form."""
        response = self.client.post("/support/create/suggestion/", {})
        self.assertEqual(response.status_code, 200)

    def test_support_post_two(self):
        """Tests the support ticket post method on an Valid form."""
        data = SUPPORT_PASS_ONE.__dict__
        data = replace_none_empty_str(data)
        response = self.client.post("/support/create/suggestion/", data)
        self.assertEqual(response.status_code, 302)

    def test_support_suggestion_edit_view_one(self):
        """Test the view for the Suggestion Edit view."""
        data = SUPPORT_PASS_ONE.__dict__
        data = replace_none_empty_str(data)
        response = self.client.get(
            f'/support/edit/suggestion/{self.support_obj.id}/', data)
        self.assertEqual(response.status_code, 200)

    def test_show_support(self):
        """Test the show support method."""
        url = f'/support/show/{self.support_obj.id}/'
        response = self.client.post(url)
        self.assertEqual(response.status_code, 200)

    def test_suggestion_edit_get(self):
        """Test the SuggestionEditView class GET method."""
        self.login_user()
        response = self.client.get(
            f'/support/edit/suggestion/{self.support_obj.id}/')
        self.assertEqual(response.status_code, 200)

    def test_suggestion_edit_get_staff(self):
        """Test the SuggestionEditView class GET method."""
        self.login_staff()
        response = self.client.get(
            f'/support/edit/suggestion/{self.support_obj.id}/')
        self.assertEqual(response.status_code, 200)

    def test_suggestion_edit_post(self):
        """Test the SuggestionEditView class GET method."""
        self.login_user()
        response = self.client.post(
            f'/support/edit/suggestion/{self.support_obj.id}/',
            self.support_form.__dict__)
        self.assertEqual(response.status_code, 200)

    def test_suggestion_edit_post_staff(self):
        """Test the SuggestionEditView class GET method."""
        self.login_staff()
        data = SUPPORT_PASS_ONE.__dict__
        data = replace_none_empty_str(data)
        response = self.client.post(
            f'/support/edit/suggestion/{self.support_obj.id}/',
            data=data, files=[], HTTP_REFERER='http://foo/bar')
        self.assertEqual(response.status_code, 302)

    def test_file_upload_support(self):
        """Test file upload support."""
        self.login_staff()
        url = f'/support/file/upload/{self.support_obj.id}/'
        t_file = SimpleUploadedFile("test.txt", content=b'TestFile')
        files = {'upl': [t_file]}
        response = self.client.post(url, files)
        self.assertEqual(response.status_code, 302)
