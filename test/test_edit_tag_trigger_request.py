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
from postmark.models.edit_tag_trigger_request import EditTagTriggerRequest


class TestEditTagTriggerRequest(unittest.TestCase):
    """ EditTagTriggerRequest unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testEditTagTriggerRequest(self):
        """
        Test EditTagTriggerRequest
        """
        model = postmark.models.edit_tag_trigger_request.EditTagTriggerRequest()


if __name__ == '__main__':
    unittest.main()
