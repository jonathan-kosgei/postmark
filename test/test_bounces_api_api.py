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
from postmark.apis.bounces_api_api import BouncesAPIApi


class TestBouncesAPIApi(unittest.TestCase):
    """ BouncesAPIApi unit test stubs """

    def setUp(self):
        self.api = postmark.apis.bounces_api_api.BouncesAPIApi()

    def tearDown(self):
        pass

    def test_activate_bounce(self):
        """
        Test case for activate_bounce

        Activate a bounce
        """
        pass

    def test_bounces_bounceid_dump_get(self):
        """
        Test case for bounces_bounceid_dump_get

        Get bounce dump
        """
        pass

    def test_get_bounced_tags(self):
        """
        Test case for get_bounced_tags

        Get bounced tags
        """
        pass

    def test_get_bounces(self):
        """
        Test case for get_bounces

        Get bounces
        """
        pass

    def test_get_delivery_stats(self):
        """
        Test case for get_delivery_stats

        Get delivery stats
        """
        pass

    def test_get_single_bounce(self):
        """
        Test case for get_single_bounce

        Get a single bounce
        """
        pass


if __name__ == '__main__':
    unittest.main()
