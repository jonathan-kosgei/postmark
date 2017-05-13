# coding: utf-8

"""
    Postmark API

    Postmark makes sending and receiving email incredibly easy. 

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import postmark
from postmark.rest import ApiException
from postmark.apis.templates_api_api import TemplatesAPIApi


class TestTemplatesAPIApi(unittest.TestCase):
    """ TemplatesAPIApi unit test stubs """

    def setUp(self):
        self.api = postmark.apis.templates_api_api.TemplatesAPIApi()

    def tearDown(self):
        pass

    def test_delete_template(self):
        """
        Test case for delete_template

        Delete a Template
        """
        pass

    def test_get_single_template(self):
        """
        Test case for get_single_template

        Get a Template
        """
        pass

    def test_list_templates(self):
        """
        Test case for list_templates

        Get the Templates associated with this Server
        """
        pass

    def test_send_email_with_template(self):
        """
        Test case for send_email_with_template

        Send an email using a Template
        """
        pass

    def test_templates_post(self):
        """
        Test case for templates_post

        Create a Template
        """
        pass

    def test_test_template_content(self):
        """
        Test case for test_template_content

        Test Template Content
        """
        pass

    def test_update_template(self):
        """
        Test case for update_template

        Update a Template
        """
        pass


if __name__ == '__main__':
    unittest.main()
