# coding: utf-8

"""
    Postmark

    Send emails with Postmark

    OpenAPI spec version: 1.0.0
    Contact: jonathan@saharacluster.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import postmark
from postmark.rest import ApiException
from postmark.models.email import Email


class TestEmail(unittest.TestCase):
    """ Email unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEmail(self):
        """
        Test Email
        """
        model = postmark.models.email.Email()


if __name__ == '__main__':
    unittest.main()
