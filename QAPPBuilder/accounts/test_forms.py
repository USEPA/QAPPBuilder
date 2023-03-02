# forms_tests.py (accounts)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov

"""These should pass when you run "manage.py test"."""

from django.core.exceptions import ValidationError
from django.test import Client, TestCase
from accounts.forms import ProfileCreationForm, ProfileUpdateForm, \
    SetPasswordForm
from accounts.models import Country, Role, Sector, State, UserProfile
from accounts.views import User


class TestSetPasswordForm(TestCase):
    """Tests for the account SetPasswordForm class."""

    def setUp(self):
        """Test client user with generic password not on server."""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.password = 'P@ssword123'

    def test_clean_new_password_pass(self):
        """Test two matching passwords."""
        data = {'new_password1': self.password, 'new_password2': self.password}
        form = SetPasswordForm(data=data)
        form.is_valid()
        self.assertEqual(form.clean_new_password2(), self.password)

    def test_clean_new_password_error(self):
        """Test two unmatching passwords."""
        data = {'new_password1': 'MISMATCH', 'new_password2': self.password}
        form = SetPasswordForm(data=data)
        self.assertFalse(form.is_valid())


class TestProfileCreationForm(TestCase):
    """Tests for the accounts ProfileCreationForm."""

    def setUp(self):
        """Test client user with generic password not on server."""
        self.client = Client()
        self.username = 'testuser'
        self.username2 = 'testuser2'
        self.password = '12345'
        self.user = User.objects.create_user(
            username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)

        self.profile_form_data = {
            'username': self.username,
            'password1': self.password, 'password2': self.password,
            'first_name': 'Test', 'last_name': 'User',
            'email': 'testuser@test.com', 'affiliation': 'EPA',
            'sector': 1, 'job_title': 'Dev', 'role': 1,
            'address_line1': '123 Street Name', 'address_line2': 'Ste 104',
            'city': 'Cincinnati', 'state': 1, 'zipcode': '12345',
            'country': 1}

    def test_create_save_profile(self):
        """Test creating a new profile for user2."""
        form_data = self.profile_form_data
        form_data['username'] = self.username2
        new_profile = ProfileCreationForm(data=form_data)
        self.assertTrue(new_profile.is_valid())

    def test_profile_str(self):
        """Test the stringify method."""
        form_data = self.profile_form_data
        form_data['username'] = self.username2
        new_profile = ProfileCreationForm(data=form_data)
        self.assertTrue(new_profile.is_valid())
        self.assertEqual(str(new_profile), self.username2)

    def test_save(self):
        """Test the save method."""
        form_data = self.profile_form_data
        form_data['username'] = self.username2
        new_profile = ProfileCreationForm(data=form_data)
        self.assertTrue(new_profile.is_valid())
        self.assertIsNotNone(new_profile.save())

    # def test_clean_username(self):
    #     """Test the clean username method."""
    #     form_data = self.profile_form_data
    #     new_profile = ProfileCreationForm(data=form_data)
    #     self.assertFalse(new_profile.is_valid())
    #     try:
    #         new_profile.clean_username()
    #         self.assertTrue(False)
    #     except ValidationError:
    #         self.assertTrue(True)

    # def test_clean_password2(self):
    #     """"Test the clean_password2 method raises ValidationError."""
    #     form_data = self.profile_form_data
    #     form_data['username'] = self.username2
    #     form_data['password2'] = ''
    #     new_profile = ProfileCreationForm(data=form_data)
    #     self.assertFalse(new_profile.is_valid())
    #     try:
    #         new_profile.clean_password2()
    #         self.assertTrue(False)
    #     except ValidationError:
    #         self.assertTrue(True)

    # def test_clean(self):
    #     """"Test the clean method."""
    #     form_data = self.profile_form_data
    #     form_data['username'] = self.username2
    #     new_profile = ProfileCreationForm(data=form_data)


class TestProfileUpdateForm(TestCase):
    """Tests for the accounts ProfileUpdateForm."""

    def setUp(self):
        self.client = Client()
        self.username = 'testuser'
        self.password = '12345'
        self.user = User.objects.create_user(
            username=self.username, password=self.password)
        self.client.login(username=self.username, password=self.password)

        self.sector = Sector.objects.get(id=1)
        self.role = Role.objects.get(id=1)
        self.state = State.objects.get(id=1)
        self.country = Country.objects.get(id=1)

        self.profile_form_data = {
            'user': self.user, 'affiliation': 'EPA',
            'sector': self.sector, 'job_title': 'Dev', 'role': self.role,
            'address_line1': '123 Street Name', 'address_line2': 'Ste 104',
            'city': 'Cincinnati', 'state': self.state, 'zipcode': '12345',
            'country': self.country}

        self.profile = UserProfile.objects.create(**self.profile_form_data)

    def test_clean_pass(self):
        """Test the clean method."""
        form_data = self.profile_form_data
        form_data['first_name'] = 'Test Clean'
        update_form = ProfileUpdateForm(data=form_data)
        self.assertTrue(update_form.is_valid())
        self.assertIsNotNone(update_form.clean())
