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
from postmark.apis.inbound_rules_api_api import InboundRulesAPIApi


class TestInboundRulesAPIApi(unittest.TestCase):
    """ InboundRulesAPIApi unit test stubs """

    def setUp(self):
        self.api = postmark.apis.inbound_rules_api_api.InboundRulesAPIApi()

    def tearDown(self):
        pass

    def test_create_inbound_rule(self):
        """
        Test case for create_inbound_rule

        Create an inbound rule trigger
        """
        pass

    def test_delete_inbound_rule(self):
        """
        Test case for delete_inbound_rule

        Delete a single trigger
        """
        pass

    def test_list_inbound_rules(self):
        """
        Test case for list_inbound_rules

        List inbound rule triggers
        """
        pass


if __name__ == '__main__':
    unittest.main()
