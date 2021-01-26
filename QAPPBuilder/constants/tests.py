# tests.py (constants)
# !/usr/bin/env python3
# coding=utf-8
# young.daniel@epa.gov
# py-lint: disable=C0301

"""
This file houses test cases for the constants module.

Available functions:
- None
"""

import django
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.mail import EmailMultiAlternatives
from django.test import TestCase
from constants.utils import split_email_list, is_epa_email, \
    non_epa_email_message, create_qt_email_message, xstr, sort_rap_numbers, \
    get_rap_fields, is_float, get_attachment_storage_path, \
    download_files, download_file
from accounts.models import User
from QAPP_Builder.models import Attachment


class TestUtils(TestCase):
    """Test utils."""

    if django.VERSION[:2] >= (1, 7):
        # Django 1.7 requires an explicit setup() when running tests in PTVS.
        @classmethod
        def setUpClass(cls):
            """Prepare objects for testing."""
            super(TestUtils, cls).setUpClass()
            django.setup()

    def setUp(self):
        """Prepare various objects for this class of tests."""
        self.test_str = 'Test'
        self.client.login(username='dyoung11', password='***REMOVED***')
        self.user = User.objects.get(id=1)
        self.file = SimpleUploadedFile('test.txt', b'This is a test file.')
        self.excel_file = SimpleUploadedFile(
            'test.xlsx', b'This is a test file.')
        self.attachment_excel = Attachment.objects.create(
            name=self.test_str, file=self.excel_file, uploaded_by=self.user)
        self.attachment_1 = Attachment.objects.create(
            name=self.test_str, file=self.file, uploaded_by=self.user)
        # Attachment 2 will not be found since we don't call objects.create()
        self.attachment_2 = Attachment(
            name=self.test_str, file=self.file, uploaded_by=self.user)

    def test_split_email_list_pass_one(self):
        """Runs the char split on an email that will be equal."""
        self.assertEqual(split_email_list(
            "t;e,s\tt@t|est.com"), ['t', 'e', 's', 't@t', 'est.com'])

    def test_split_email_list_fail_one(self):
        """Runs the char split on an email that will not be equal."""
        self.assertNotEqual(split_email_list(
            "t;e,s\tt@t|est.com"), ['t', 'e', 's', 't@test.com'])

    def test_is_epa_email_pass_one(self):
        """
        test_is_epa_email_pass_one.

        Runs the test to check if an email address is in the right
        format to be an epa email address.
        """
        self.assertEqual(is_epa_email("test@epa.gov"), True)

    def test_is_epa_email_fail_one(self):
        """
        test_is_epa_email_fail_one.

        Runs the test to check if an email address is in the right
        format to be an epa email address.
        """
        self.assertEqual(is_epa_email("test@test.com"), False)

    def test_is_epa_email_fail_two(self):
        """
        test_is_epa_email_fail_two.

        Runs the test to check if an email address is in the right
        format to be an epa email address.
        """
        self.assertEqual(is_epa_email("test@test.gov"), False)

    def test_is_epa_email_fail_three(self):
        """
        test_is_epa_email_fail_three.

        Runs the test to check if an email address is in
        the right format to be an epa email address.
        """
        self.assertEqual(is_epa_email("test@epa.com"), False)

    def test_is_epa_email_fail_seven(self):
        """
        test_is_epa_email_fail_seven.

        Runs the test to check if an email address is in the right
        format to be an epa email address.
        """
        self.assertEqual(is_epa_email("test@Aepa.gov"), False)

    def test_is_epa_email_fail_eight(self):
        """test_is_epa_email_fail_eight.

        Runs the test to check if an email address is in
        the right format to be an epa email address.
        """
        self.assertEqual(is_epa_email("test@repa.govR"), False)

    def test_is_epa_email_fail_nine(self):
        """
        test_is_epa_email_fail_nine.

        Runs the test to check if an email address is in the right
        format to be an epa email address.
        """
        self.assertEqual(is_epa_email("test@4epa.gov"), False)

    def test_non_epa_email_message_fail_one(self):
        """
        test_non_epa_email_message_fail_one.

        Runs the test to check if an email address is not EPA
        that it sends the correct message.
        """
        self.assertIn(
            """Email list may only contain @epa.gov addresses.""",
            non_epa_email_message("test@test.com"), msg=None)

    def test_create_qt_email_message(self):
        """Returns EmailMultiAlternatives object."""
        to_emails = ["testTo@test.com"]
        self.assertIsInstance(
            create_qt_email_message(
                "email Subject", "text content", "testFrom@test.com",
                to_emails, None, None),
            EmailMultiAlternatives, msg=None)

    def test_xstr_one(self):
        """
        test_xstr_one.

        Test the method that Checks for and replaces
        None objects with empty strings.
        """
        self.assertEqual(xstr(None), "")

    def test_xstr_two(self):
        """
        test_xstr_two.

        Test the method that Checks for and replaces
        None objects with empty strings.
        """
        self.assertEqual(xstr("test"), "test")

    def test_sort_rap_numbers(self):
        """Test the sort rap numbers."""
        raplist = {"15.42", "15.45", "12.12"}
        results = sort_rap_numbers(raplist)
        self.assertEqual(results, ["12.12", "15.42", "15.45"])

    def test_sort_rap_numbers_fail(self):
        """Test the sort rap numbers."""
        raplist = {"15.42", "test", "12.12"}
        results = sort_rap_numbers(raplist)
        # print(results)
        self.assertEqual(results, ["12.12", "15.42", "test"])

    def test_get_rap_fields(self):
        """Test the get rap fields with form."""
        fields = "form"
        results = get_rap_fields(fields)
        # print(results)
        self.assertEqual(results, [
            ['ace', 'ace_rap_numbers'], ['css', 'css_rap_numbers'],
            ['sswr', 'sswr_rap_numbers'], ['hhra', 'hhra_rap_numbers'],
            ['hsrp', 'hsrp_rap_numbers'], ['hsre', 'hsrp_rap_extensions'],
            ['shc', 'shc_rap_numbers']])

    def test_get_rap_fields_two(self):
        """Test the get rap fields without form."""
        fields = "notform"
        results = get_rap_fields(fields)
        # print(results)
        self.assertEqual(results, [
            'ace_rap_numbers', 'css_rap_numbers', 'sswr_rap_numbers',
            'hhra_rap_numbers', 'hsrp_rap_numbers',
            'hsrp_rap_extensions', 'shc_rap_numbers'])

    def test_is_float_one(self):
        """Test the is float method with a float."""
        val_str = "1.2"
        results = is_float(val_str)
        # Print(results).
        self.assertEqual(results, True)

    def test_is_float_two(self):
        """Test the is float method with a char string."""
        val_str = "notAFloat"
        results = is_float(val_str)
        # Print(results).
        self.assertEqual(results, False)

    def test_get_attachment_storage_path(self):
        """Test that the QAPP_Builder Attachment path is returned properly."""
        response = get_attachment_storage_path(
            instance=self.attachment_1, filename=self.test_str)
        self.assertTrue('dyoung11/attachments/' in response)

    def test_download_files(self):
        """Test the function to download multiple files as a zip."""
        zip_name = 'test.zip'
        files_list = [self.attachment_1, self.attachment_2]
        response = download_files(files_list, zip_name)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(b'PK' in response.content)

    def test_download_file(self):
        """Test the function to download multiple files as a zip."""
        response = download_file(self.attachment_1)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(b'This is a test file.' in response.content)

    def test_download_file_excel(self):
        """Test the function to download multiple files as a zip."""
        response = download_file(self.attachment_excel)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(b'This is a test file.' in response.content)
