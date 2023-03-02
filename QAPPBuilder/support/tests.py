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

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.test.client import RequestFactory
# from django.core.mail import EmailMultiAlternatives
# from support.views import index, SuggestionEditView, create_help_request
from support.views import create_help_request
# from support.forms import SupportForm


class TestSupport(TestCase):
    """Test the functions related to UsernameReminderRequestView."""

    def setUp(self):
        """Prepare objects for testing the Support module."""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.factory = RequestFactory()

    def test_home(self):
        """Test the home page."""
        # response = self.client.get('/support/index')
        response = self.client.get('/support/index/')
        self.assertContains(response, 'Help/Suggestions', 2, 200)

    def test_support_ticket_create_one(self):
        """Test the support ticket form when you use suggestion."""
        # create/(?P<support_type_name>\w+)
        response = self.client.get('/support/create/suggestion/')
        self.assertContains(
            response, 'Describe your suggestion for GWSC below.', 1, 200)

    def test_support_ticket_create_two(self):
        """Test the support ticket form when you do not use suggestion."""
        # create/(?P<support_type_name>\w+)
        response = self.client.get('/support/create/OtherWordsHERE/')
        self.assertContains(
            response,
            'Describe the problem you encountered with GWSC below.', 1, 200)

    def test_support_post_one(self):
        """Tests the support ticket post method on an invalid form."""
        self.client.post("/support/create/suggestion/", {})

    # def test_support_post_two(self):
    #    """Tests the support ticket post method on an Valid form."""
    #    data = SUPPORT_PASS_ONE.__dict__
    #    data = replace_none_empty_str(data)
    #    response = self.client.post("/support/create/suggestion/", data)

    # def test_Support_Suggestion_Edit_View_two(self):
    #    """Test the view for the Suggestion Edit view."""
    #    data = SUPPORT_PASS_ONE.__dict__
    #    data = replace_none_empty_str(data)
    #    response = self.client.get("/support/edit/suggestion/1/", data)

    # self.assertContains(response, 'Suggestions', 2, 200)

    # def test_Support_Suggestion_Edit_View_one(self):
    #    """Test the view for the Suggestion Edit view."""
    #    data = SUPPORT_PASS_ONE.__dict__
    #    data = replace_none_empty_str(data)
    #    response = self.client.post("/support/edit/suggestion/1/", data)

    def test_model_environment_with_environment(self):
        """Tests the environment of model if it has a environment."""
        self.client.post(create_help_request)

    # def test_suggestion_edit_view(self):
    #     """Tests the view for suggestion edit"""

# GET VIEWS
# def test_support_ticket_create_one(self):
#     """Test the support ticket form when you use suggestion"""
#     # create/(?P<support_type_name>\w+)
#     results = self.client.get('/support/create/suggestion/')
#     response = self.client.get('/support/edit/suggestion/')
#     print(response)
#     self.assertContains(response, "id", 5, 200)

# def test_show_support(self):
#     """Test the show support method"""
#     #show/(?P<support_type_name>\w+)/(?P<obj_id>\d+)/$'
#     response = self.client.post("/support/show/suggestion/1")
#     self.assertContains(response, 'Show Support', 1, 301)

# def test_Support_Suggestion_Edit_View_three(self):
#     """Test the view for the Suggestion Edit view"""
#     results = Sediment.__str__(self)

# def test_model_environment_with_environment(self):
#     """Tests the environment of model if it has a environment"""
#     self.environment = "1"
#     RequestFactory.request.user = User.objects.create_user(
#         username='testuser2', password='12345')
#     results = SuggestionEditView.get(
#         self, RequestFactory.request, "suggestion", 1)
#     self.assertEqual(results, "1 - 1")
