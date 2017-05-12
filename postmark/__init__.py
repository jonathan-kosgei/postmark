# coding: utf-8

"""
    Postmark

    Send emails with Postmark

    OpenAPI spec version: 1.0.0
    Contact: jonathan@saharacluster.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into sdk package
from .models.email import Email
from .models.email_attachments import EmailAttachments
from .models.email_headers import EmailHeaders
from .models.emailwith_template import EmailwithTemplate

# import apis into sdk package
from .apis.postmark_api import PostmarkApi

# import ApiClient
from .api_client import ApiClient

from .configuration import Configuration

configuration = Configuration()
