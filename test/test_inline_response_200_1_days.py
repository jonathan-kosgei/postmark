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
from postmark.models.inline_response_200_1_days import InlineResponse2001Days


class TestInlineResponse2001Days(unittest.TestCase):
    """ InlineResponse2001Days unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testInlineResponse2001Days(self):
        """
        Test InlineResponse2001Days
        """
        model = postmark.models.inline_response_200_1_days.InlineResponse2001Days()


if __name__ == '__main__':
    unittest.main()