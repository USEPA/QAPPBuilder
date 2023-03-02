# views_tests.py (accounts)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov

"""These should pass when you run "manage.py test"."""

from django.test import Client, TestCase
from django.test.client import RequestFactory
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from accounts.models import User
from accounts.views import UsernameReminderRequestView, \
    PasswordResetRequestView


class TestUsernameReminderRequestView(TestCase):
    """Tests for the account UsernameReminderRequestView class."""

    def setUp(self):
        """Test client user with generic password not on server."""
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.email = 'young.daniel@epa.gov'
        self.client.login(username='testuser', password='12345')

    def test_email_validate_pass(self):
        """Test the email validator against a valid email address."""
        email = 'test@epa.gov'
        valid = UsernameReminderRequestView.validate_email_address(email)
        self.assertTrue(valid)

    def test_email_validate_fail(self):
        """Test the email validator against an invalid email address."""
        email = 'test@epa@gov'
        valid = UsernameReminderRequestView.validate_email_address(email)
        self.assertFalse(valid)

    def test_post_pass(self):
        """Test the POST method with a user that exists."""
        data = {'email': self.email}
        response = self.client.post(
            '/accounts/username/', data=data, HTTP_HOST='localhost')
        self.assertEqual(response.status_code, 200)

    def test_post_email_dne(self):
        """Test the POST method with a user email that does not exist."""
        data = {'email': 'test@epa.gov'}
        response = self.client.post(
            '/accounts/username/', data=data, HTTP_HOST='localhost')
        self.assertEqual(response.status_code, 200)

    def test_post_bad_email(self):
        """Test the POST method with a bad user email."""
        data = {'email': 'bad_email@epa@gov'}
        response = self.client.post(
            '/accounts/username/', data=data, HTTP_HOST='localhost')
        self.assertEqual(response.status_code, 200)

    def test_post_exception(self):
        """Test the POST method without the HTTP_HOST specified."""
        data = {'email': self.email}
        response = self.client.post(
            '/accounts/username/', data=data)
        self.assertEqual(response.status_code, 200)


class TestPasswordResetRequestView(TestCase):
    """Tests for the account PasswordResetRequestView class."""

    def setUp(self):
        """Test client user with generic password not on server."""
        self.client = Client()
        self.username = 'dyoung11'
        self.email = 'young.daniel@epa.gov'
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')

    def test_email_validate_pass(self):
        """Test the email validator against a valid email address."""
        email = 'test@epa.gov'
        valid = PasswordResetRequestView.validate_email_address(email)
        self.assertTrue(valid)

    def test_email_validate_fail(self):
        """Test the email validator against an invalid email address."""
        email = 'test@epa@gov'
        valid = PasswordResetRequestView.validate_email_address(email)
        self.assertFalse(valid)

    def test_post_email_pass(self):
        """Test the POST method with a user that exists."""
        data = {'email_or_username': self.email}
        response = self.client.post(
            '/accounts/password/reset/', data=data, HTTP_HOST='localhost')
        self.assertEqual(response.status_code, 200)

    def test_post_username_pass(self):
        """Test the POST method with a user that exists."""
        data = {'email_or_username': self.username}
        response = self.client.post(
            '/accounts/password/reset/', data=data, HTTP_HOST='localhost')
        self.assertEqual(response.status_code, 200)

    def test_post_fail(self):
        """Test the POST method with a user that exists."""
        data = {'bad_form_data': self.email}
        response = self.client.post(
            '/accounts/password/reset/', data=data, HTTP_HOST='localhost')
        self.assertEqual(response.status_code, 200)

    def test_post_email_dne(self):
        """Test the POST method with a user email that does not exist."""
        data = {'email_or_username': 'test@epa.gov'}
        response = self.client.post(
            '/accounts/password/reset/', data=data, HTTP_HOST='localhost')
        self.assertEqual(response.status_code, 200)

    def test_post_bad_email(self):
        """Test the POST method with a bad user email."""
        data = {'email_or_username': 'bad_email@epa@gov'}
        response = self.client.post(
            '/accounts/password/reset/', data=data, HTTP_HOST='localhost')
        self.assertEqual(response.status_code, 200)


class TestPasswordResetConfirmView(TestCase):
    """Tests for the account PasswordResetConfirmView class."""

    def setUp(self):
        """Test client user with generic password not on server."""
        self.client = Client()
        self.email = 'young.daniel@epa.gov'
        self.user = User.objects.create_user(
            username='testuser', password='12345')
        self.client.login(username='testuser', password='12345')
        self.factory = RequestFactory()
        self.uidb64 = urlsafe_base64_encode(
            force_bytes(self.client.session['_auth_user_id']))
        self.token = ''
        self.reset_url = f'/password/reset/confirm/{self.uidb64}-{self.token}'
        self.reset_url_no_token = '/password/reset/confirm/'

    def test_get_no_http_host(self):
        response = self.client.get(self.reset_url_no_token)
        self.assertEqual(response.status_code, 404)

    def test_get_no_token(self):
        """Test the GET method..."""
        response = self.client.get(self.reset_url_no_token,
                                   HTTP_HOST='localhost')
        print('-----------------------------------')
        print('-----------------------------------')
        print('-----------------------------------')
        for key in response:
            print(f'{key}:')
        print('-----------------------------------')
        print('-----------------------------------')
        print('-----------------------------------')
        self.assertEqual(response.status_code, 404)

    # def test_post_pass(self):
    #     """Test the POST method with a user that exists."""
    #     data = {'email': self.email}
    #     response = self.client.post(
    #         '/accounts/username/', data=data, HTTP_HOST='localhost')
    #     self.assertEqual(response.status_code, 200)

    # def test_post_email_dne(self):
    #     """Test the POST method with a user email that does not exist."""
    #     data = {'email': 'test@epa.gov'}
    #     response = self.client.post(
    #         '/accounts/username/', data=data, HTTP_HOST='localhost')
    #     self.assertEqual(response.status_code, 200)

    # def test_post_bad_email(self):
    #     """Test the POST method with a bad user email."""
    #     data = {'email': 'bad_email@epa@gov'}
    #     response = self.client.post(
    #         '/accounts/username/', data=data, HTTP_HOST='localhost')
    #     self.assertEqual(response.status_code, 200)

    # def test_post_exception(self):
    #     """Test the POST method without the HTTP_HOST specified."""
    #     data = {'email': self.email}
    #     response = self.client.post(
    #         '/accounts/username/', data=data)
    #     self.assertEqual(response.status_code, 200)
