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
from postmark.models.outbound_message_dump_response import OutboundMessageDumpResponse


class TestOutboundMessageDumpResponse(unittest.TestCase):
    """ OutboundMessageDumpResponse unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOutboundMessageDumpResponse(self):
        """
        Test OutboundMessageDumpResponse
        """
        model = postmark.models.outbound_message_dump_response.OutboundMessageDumpResponse()


if __name__ == '__main__':
    unittest.main()
