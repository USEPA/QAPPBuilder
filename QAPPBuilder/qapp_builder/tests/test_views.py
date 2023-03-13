# test_views.py (qapp_builder)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=W0511,R0904
"""
This file demonstrates writing tests using the unittest module.

These will pass when you run "manage.py test".
"""

# from unittest import TestCase
from datetime import datetime
import django
from django.db.models.query import QuerySet, EmptyQuerySet
from django.test import Client, TestCase
from django.test.client import RequestFactory
from accounts.models import User
from qapp_builder.models import Division, Qapp, QappSharingTeamMap
from qapp_builder.forms import QappForm
from qapp_builder.views import check_can_edit, get_qapp_all, QappEdit
from teams.models import Team, TeamMembership


class TestViewAuthenticated(TestCase):
    """Tests for the application views."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS.
        @classmethod
        def setUpClass(cls):
            """Prepare objects for testing."""
            super(TestViewAuthenticated, cls).setUpClass()
            django.setup()

    def setUp(self):
        """Prepare various objects for this class of tests."""
        self.request_factory = RequestFactory()
        self.test_str = 'Test'
        self.client = Client()
        # User 1 created the team, User 2 created ExistingData,
        # User 3 has no privileges
        self.user1 = User.objects.create_user(username='testuser1',
                                              password='12345')
        self.user2 = User.objects.create_user(username='testuser2',
                                              password='12345')
        self.client.login(username='testuser1', password='12345')
        self.user = User.objects.get(id=1)
        self.team = Team.objects.create(created_by=self.user1, name='testteam')
        self.team2 = Team.objects.create(created_by=self.user,
                                         name='testteam2')
        TeamMembership.objects.create(member=self.user1,
                                      team=self.team,
                                      is_owner=True,
                                      can_edit=True)
        TeamMembership.objects.create(member=self.user,
                                      team=self.team,
                                      is_owner=True,
                                      can_edit=True)
        TeamMembership.objects.create(member=self.user,
                                      team=self.team2,
                                      is_owner=True,
                                      can_edit=True)
        # Build some models to be used in this test class:
        self.division = Division.objects.first()
        self.form = QappForm()

        self.qapp_dict = {
            'division': self.division,
            'division_branch': 'Test',
            'title': 'Test',
            'qa_category': 'QA Category A',
            'intra_extra': 'Intramural',
            'revision_number': '1',
            'date': datetime.now(),
            'prepared_by': self.user,
            'strap': 'Test',
            'tracking_id': 'Test'
        }
        self.qapp = Qapp.objects.create(**self.qapp_dict)
        self.dat_team_map = QappSharingTeamMap.objects.create(qapp=self.qapp,
                                                              team=self.team,
                                                              can_edit=True)

    def test_get_qapp_all(self):
        """
        Test the get all qapp method.

        This should return the one qapp that was created during setup.
        """
        data = get_qapp_all()
        self.assertIsInstance(data, QuerySet)
        self.assertNotIsInstance(data, EmptyQuerySet)
        self.assertEqual(len(data), 1)

    def test_qapp_index(self):
        """Test the qapp module index page."""
        response = self.client.get('/')
        self.assertContains(response, 'QUALITY ASSURANCE PROJECT PLAN', 1, 200)
        self.assertContains(response, 'View QAPP documents for...', 1, 200)
        self.assertContains(response, 'or create a new QAPP...', 1, 200)

    def test_qapp_list_user(self):
        """Test the qapp list page for a User."""
        response = self.client.get('/list/user/1/')
        self.assertContains(response, 'QUALITY ASSURANCE PROJECT PLAN', 1, 200)
        self.assertContains(response, 'Create a new QAPP', 1, 200)
        self.assertContains(response, 'View or Edit Existing QAPP', 1, 200)
        self.assertContains(response, 'Export All QAPP', 3, 200)
        self.assertContains(response, 'Export All QAPP to Word Doc', 1, 200)
        self.assertContains(response, 'Export All QAPP to PDF', 1, 200)

    def test_qapp_list_team(self):
        """Test the qapp list page for a Team."""
        response = self.client.get('/list/team/1/')
        self.assertContains(response, 'QUALITY ASSURANCE PROJECT PLAN', 1, 200)
        self.assertContains(response, 'Create a new QAPP', 1, 200)
        self.assertContains(response, 'View or Edit Existing QAPP', 1, 200)
        self.assertContains(response, 'Export All QAPP', 3, 200)
        self.assertContains(response, 'Export All QAPP to Word Doc', 1, 200)
        self.assertContains(response, 'Export All QAPP to PDF', 1, 200)

    def test_check_can_edit_user_true(self):
        """Tets the check_can_edit method when the user CAN edit."""
        can_edit = check_can_edit(self.qapp, self.user)
        self.assertTrue(can_edit)

    def test_check_can_edit_team_true(self):
        """Tets the check_can_edit method when the user team CAN edit."""
        can_edit = check_can_edit(self.qapp, self.user1)
        self.assertTrue(can_edit)

    def test_check_can_edit_false(self):
        """Tets the check_can_edit method when the user CANNOT edit."""
        can_edit = check_can_edit(self.qapp, self.user2)
        self.assertFalse(can_edit)

    def test_qapp_edit_get_allowed(self):
        """Test the QappEdit view GET method with default (permitted) user."""
        response = self.client.get('/edit/1/')
        self.assertContains(response, 'Division:', 1, 200)
        self.assertContains(response, 'Division Branch:', 1, 200)
        self.assertContains(response, 'Share With Teams:', 1, 200)
        self.assertContains(response, 'Teams can edit the QAPP:', 1, 200)
        self.assertContains(response, 'Save', 1, 200)
        self.assertContains(response, 'Reset', 1, 200)
        self.assertContains(response, 'Cancel', 1, 200)

    def test_qapp_edit_get_denied(self):
        """Test the QappEdit view GET method with non-permitted user."""
        request = self.request_factory.get('/edit/1/')
        request.user = self.user2
        response = QappEdit.as_view()(pk=str(self.qapp.id), request=request)
        self.assertEqual(response.status_code, 302)

    def test_qapp_edit_form_valid(self):
        """Test the QappEdit form_valid method."""
        data = self.qapp_dict
        # When posting to form, the division should be ID not an object:
        data['division'] = self.division.id
        # Existing qapp has team 1, replace it with team2:
        data['teams'] = f'{self.team2.id}'
        response = self.client.post(f'/edit/{self.qapp.id}/', data=data)
        self.assertEqual(response.status_code, 302)

    # def test_qapp_edit_form_valid_fail(self):
    #     """Test the QappEdit form_valid method."""
    #     path = '/edit/' + str(self.qapp.id)
    #     request = self.request_factory.post(path, data={})
    #     request.user = self.user2
    #     response = QappEdit.as_view()(pk=str(self.qapp.id), request=request)
    #     self.assertEqual(response.status_code, 200)

    def test_qapp_create_get(self):
        """Test the QappCreate view GET method."""
        response = self.client.get('/create/')
        self.assertContains(response, 'Office of Research and Development', 1,
                            200)
        self.assertContains(
            response,
            'Center for Environmental Solutions & Emergency Response', 1, 200)
        self.assertContains(response, 'Next Page', 1, 200)
        self.assertContains(response, 'Reset', 1, 200)
        self.assertContains(response, 'Cancel', 1, 200)

    def test_qapp_create_post(self):
        """Test the QappCreate view POST method."""
        data = self.qapp_dict
        # When posting to form, the division should be ID not an object:
        data['division'] = self.division.id
        data['teams'] = f'{self.team.id}'
        response = self.client.post('/create/', data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Qapp.objects.count(), 2)

    def test_qapp_create_post_2(self):
        """
        Test Create Qapp with a non-valid form.

        This should render the create page again.
        """
        response = self.client.post('/create/', data={})
        self.assertContains(response, 'Office of Research and Development', 1,
                            200)
        self.assertContains(
            response,
            'Center for Environmental Solutions & Emergency Response', 1, 200)
        self.assertContains(response, 'Next Page', 1, 200)
        self.assertContains(response, 'Reset', 1, 200)
        self.assertContains(response, 'Cancel', 1, 200)
