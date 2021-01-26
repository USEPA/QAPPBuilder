# tests.py (teams)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=C0301

"""
Team test cases.

Available functions:
- TBD
"""

from django.test import Client, TestCase
from accounts.models import User
from teams.forms import TeamManagementForm


class TestTeams(TestCase):
    """Tests for the Teams module."""

    def setUp(self):
        """Prepare necessary objects for testing the Teams module."""
        self.type_texture = "1"
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_team_create_view_get(self):
        """Tests the Team Create View get method on an empty form."""
        response = self.client.get("/teams/team/")
        self.assertContains(response, 'create', 3, 200)

    def test_team_create_view_post(self):
        """Tests the Team Create View post method on an empty form."""
        response = self.client.post("/teams/team/")
        self.assertContains(response, 'create', 3, 200)

    def test_team_create_view_post_with_form(self):
        """Tests the Team Create View post method."""
        form = TeamManagementForm(data={'name': "test1"})
        self.assertTrue(form.is_valid())
        results = self.client.post("/teams/team/", {'name': "test1"})
        self.assertEqual(results.status_code, 302)

    def test_team_edit_view_get(self):
        """Tests the Team Edit View get method."""
        results = self.client.post("/teams/team/", {'name': "test1"})
        create_url = str(results)
        create_url_split_array = create_url.split("/")
        url_object_number = create_url_split_array[4]
        response = self.client.get(
            "/teams/team/" + url_object_number + "/edit")
        self.assertContains(response, 'edit', 1, 200)

    def test_team_edit_view_get_two(self):
        """Tests the Team Edit View get method."""
        results = self.client.post("/teams/team/", {'name': "test1"})
        create_url = str(results)
        create_url_split_array = create_url.split("/")
        url_object_number = create_url_split_array[4]
        response = self.client.get(
            "/teams/team/" + url_object_number + "/edit", {"team_id": ""})
        self.assertContains(response, 'edit', 1, 200)

    def test_team_edit_view_post(self):
        """Tests the Team edit View post method on an empty form."""
        results = self.client.post("/teams/team/", {'name': "test1"})
        create_url = str(results)
        create_url_split_array = create_url.split("/")
        url_object_number = create_url_split_array[4]
        response = self.client.post(
            "/teams/team/" + url_object_number + "/edit", {'name': "test2"})
        self.assertContains(response, 'edit', 1, 200)

    def test_team_edit_view_post_two(self):
        """Tests the Team edit View post method on an empty form."""
        results = self.client.post("/teams/team/", {'name': "test1"})
        create_url = str(results)
        create_url_split_array = create_url.split("/")
        url_object_number = create_url_split_array[4]
        response = self.client.post(
            "/teams/team/" + url_object_number + "/edit", {'name': ""})
        self.assertContains(response, 'edit', 1, 200)

    def test_team_management_view_get(self):
        """Tests the Team Management View get method."""
        results = self.client.post("/teams/team/", {'name': "test1"})

        create_url = str(results)
        create_url_split_array = create_url.split("/")
        url_object_number = create_url_split_array[4]
        response = self.client.get(
            "/teams/team/" + url_object_number + "/manage")
        self.assertContains(response, 'manage', 3, 200)

    def test_team_management_view_post_one(self):
        """Tests the Team management View post method."""
        results = self.client.post("/teams/team/", {'name': "test1"})
        create_url = str(results)
        create_url_split_array = create_url.split("/")
        url_object_number = create_url_split_array[4]
        response = self.client.post(
            "/teams/team/" + url_object_number + "/manage",
            {'command': "adduser"})
        self.assertContains(response, 'manage', 3, 200)

    def test_team_management_view_post_two(self):
        """Tests the Team management View post adduser method."""
        # Create a team:
        results = self.client.post("/teams/team/", {'name': "test1"})
        create_url = str(results)
        create_url_split_array = create_url.split("/")
        # Get ID of the new team:
        url_object_number = create_url_split_array[4]
        # Manage the team, adding a new user.
        response = self.client.post(
            "/teams/team/" + url_object_number + "/manage",
            {'command': "adduser", 'team_id': "", 'member_id': "user2"})
        self.assertContains(response, 'manage', 3, 200)

    def test_team_management_view_post_three(self):
        """Tests the Team management View post method."""
        results = self.client.post("/teams/team/", {'name': "test1"})
        create_url = str(results)
        create_url_split_array = create_url.split("/")
        url_object_number = create_url_split_array[4]
        response = self.client.post(
            "/teams/team/" + url_object_number + "/manage",
            {'command': "deleteuser"})
        self.assertContains(response, 'manage', 3, 200)

    def test_api_team_list_view_get(self):
        """Tests the Team list View get method."""
        results = self.client.get("/teams/api/team/")
        self.assertContains(results, "id", 0, 200)

    def test_api_team_list_view_post(self):
        """Tests the Team list View post method."""
        # Results = self.client.post("/teams/team/", {'name': "test1"}).
        response = self.client.post("/teams/api/team/", {'name': "test1"})
        self.assertContains(response, "id", 5, 201)

    def test_api_team_list_view_post_two(self):
        """Tests the Team list View post method."""
        response = self.client.post("/teams/api/team/", {'name': ""})
        self.assertContains(response, "id", 0, 400)

    def test_api_team_membership_list_view_get(self):
        """Tests the Team membership list view get method."""
        results = self.client.post("/teams/team/", {'name': "test1"})
        create_url = str(results)
        create_url_split_array = create_url.split("/")
        url_object_number = create_url_split_array[4]
        response = self.client.get(
            "/teams/api/team/" + url_object_number + "/membership/")
        self.assertContains(response, "id", 2, 200)

    def test_api_team_membership_list_view_put(self):
        """Tests the Team membership list view put method."""
        results = self.client.post("/teams/team/", {'name': "test1"})
        create_url = str(results)
        create_url_split_array = create_url.split("/")
        url_object_number = create_url_split_array[4]
        response = self.client.put(
            "/teams/api/team/" + url_object_number + "/membership/")
        self.assertContains(response, "id", 0, 405)

    def test_api_team_detail_list_view_get(self):
        """Tests the Team detail list View get method."""
        results = self.client.post("/teams/team/", {'name': "test1"})
        create_url = str(results)
        create_url_split_array = create_url.split("/")
        url_object_number = create_url_split_array[4]
        response = self.client.get(
            "/teams/api/team/" + url_object_number + "/")
        self.assertContains(response, "id", 5, 200)
