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
from postmark.models.bounce_search_response import BounceSearchResponse


class TestBounceSearchResponse(unittest.TestCase):
    """ BounceSearchResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testBounceSearchResponse(self):
        """
        Test BounceSearchResponse
        """
        model = postmark.models.bounce_search_response.BounceSearchResponse()


if __name__ == '__main__':
    unittest.main()
