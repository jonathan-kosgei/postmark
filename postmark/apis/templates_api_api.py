# coding: utf-8

"""
    Postmark API

    Postmark makes sending and receiving email incredibly easy. 

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class TemplatesAPIApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def delete_template(self, x_postmark_server_token, templateid, **kwargs):
        """
        Delete a Template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_template(x_postmark_server_token, templateid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str x_postmark_server_token: The token associated with the Server on which this request will operate. (required)
        :param int templateid: The ID for the Template you wish to delete. (required)
        :return: TemplateDetailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_template_with_http_info(x_postmark_server_token, templateid, **kwargs)
        else:
            (data) = self.delete_template_with_http_info(x_postmark_server_token, templateid, **kwargs)
            return data

    def delete_template_with_http_info(self, x_postmark_server_token, templateid, **kwargs):
        """
        Delete a Template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_template_with_http_info(x_postmark_server_token, templateid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str x_postmark_server_token: The token associated with the Server on which this request will operate. (required)
        :param int templateid: The ID for the Template you wish to delete. (required)
        :return: TemplateDetailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_postmark_server_token', 'templateid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_postmark_server_token' is set
        if ('x_postmark_server_token' not in params) or (params['x_postmark_server_token'] is None):
            raise ValueError("Missing the required parameter `x_postmark_server_token` when calling `delete_template`")
        # verify the required parameter 'templateid' is set
        if ('templateid' not in params) or (params['templateid'] is None):
            raise ValueError("Missing the required parameter `templateid` when calling `delete_template`")


        collection_formats = {}

        path_params = {}
        if 'templateid' in params:
            path_params['templateid'] = params['templateid']

        query_params = {}

        header_params = {}
        if 'x_postmark_server_token' in params:
            header_params['X-Postmark-Server-Token'] = params['x_postmark_server_token']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/templates/{templateid}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TemplateDetailResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_single_template(self, x_postmark_server_token, templateid, **kwargs):
        """
        Get a Template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_single_template(x_postmark_server_token, templateid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str x_postmark_server_token: The token associated with the Server on which this request will operate. (required)
        :param int templateid: The ID for the Template you wish to retrieve. (required)
        :return: TemplateDetailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_single_template_with_http_info(x_postmark_server_token, templateid, **kwargs)
        else:
            (data) = self.get_single_template_with_http_info(x_postmark_server_token, templateid, **kwargs)
            return data

    def get_single_template_with_http_info(self, x_postmark_server_token, templateid, **kwargs):
        """
        Get a Template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_single_template_with_http_info(x_postmark_server_token, templateid, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str x_postmark_server_token: The token associated with the Server on which this request will operate. (required)
        :param int templateid: The ID for the Template you wish to retrieve. (required)
        :return: TemplateDetailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_postmark_server_token', 'templateid']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_single_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_postmark_server_token' is set
        if ('x_postmark_server_token' not in params) or (params['x_postmark_server_token'] is None):
            raise ValueError("Missing the required parameter `x_postmark_server_token` when calling `get_single_template`")
        # verify the required parameter 'templateid' is set
        if ('templateid' not in params) or (params['templateid'] is None):
            raise ValueError("Missing the required parameter `templateid` when calling `get_single_template`")


        collection_formats = {}

        path_params = {}
        if 'templateid' in params:
            path_params['templateid'] = params['templateid']

        query_params = {}

        header_params = {}
        if 'x_postmark_server_token' in params:
            header_params['X-Postmark-Server-Token'] = params['x_postmark_server_token']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/templates/{templateid}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TemplateDetailResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_templates(self, x_postmark_server_token, count, offset, **kwargs):
        """
        Get the Templates associated with this Server
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_templates(x_postmark_server_token, count, offset, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str x_postmark_server_token: The token associated with the Server on which this request will operate. (required)
        :param float count: The number of Templates to return (required)
        :param float offset: The number of Templates to \"skip\" before returning results. (required)
        :return: TemplateListingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_templates_with_http_info(x_postmark_server_token, count, offset, **kwargs)
        else:
            (data) = self.list_templates_with_http_info(x_postmark_server_token, count, offset, **kwargs)
            return data

    def list_templates_with_http_info(self, x_postmark_server_token, count, offset, **kwargs):
        """
        Get the Templates associated with this Server
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_templates_with_http_info(x_postmark_server_token, count, offset, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str x_postmark_server_token: The token associated with the Server on which this request will operate. (required)
        :param float count: The number of Templates to return (required)
        :param float offset: The number of Templates to \"skip\" before returning results. (required)
        :return: TemplateListingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_postmark_server_token', 'count', 'offset']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_templates" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_postmark_server_token' is set
        if ('x_postmark_server_token' not in params) or (params['x_postmark_server_token'] is None):
            raise ValueError("Missing the required parameter `x_postmark_server_token` when calling `list_templates`")
        # verify the required parameter 'count' is set
        if ('count' not in params) or (params['count'] is None):
            raise ValueError("Missing the required parameter `count` when calling `list_templates`")
        # verify the required parameter 'offset' is set
        if ('offset' not in params) or (params['offset'] is None):
            raise ValueError("Missing the required parameter `offset` when calling `list_templates`")


        collection_formats = {}

        path_params = {}

        query_params = {}
        if 'count' in params:
            query_params['Count'] = params['count']
        if 'offset' in params:
            query_params['Offset'] = params['offset']

        header_params = {}
        if 'x_postmark_server_token' in params:
            header_params['X-Postmark-Server-Token'] = params['x_postmark_server_token']

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/templates', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TemplateListingResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def send_email_with_template(self, x_postmark_server_token, body, **kwargs):
        """
        Send an email using a Template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.send_email_with_template(x_postmark_server_token, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str x_postmark_server_token: The token associated with the Server on which this request will operate. (required)
        :param EmailWithTemplateRequest body: (required)
        :return: SendEmailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.send_email_with_template_with_http_info(x_postmark_server_token, body, **kwargs)
        else:
            (data) = self.send_email_with_template_with_http_info(x_postmark_server_token, body, **kwargs)
            return data

    def send_email_with_template_with_http_info(self, x_postmark_server_token, body, **kwargs):
        """
        Send an email using a Template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.send_email_with_template_with_http_info(x_postmark_server_token, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str x_postmark_server_token: The token associated with the Server on which this request will operate. (required)
        :param EmailWithTemplateRequest body: (required)
        :return: SendEmailResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_postmark_server_token', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method send_email_with_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_postmark_server_token' is set
        if ('x_postmark_server_token' not in params) or (params['x_postmark_server_token'] is None):
            raise ValueError("Missing the required parameter `x_postmark_server_token` when calling `send_email_with_template`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `send_email_with_template`")


        collection_formats = {}

        path_params = {}

        query_params = {}

        header_params = {}
        if 'x_postmark_server_token' in params:
            header_params['X-Postmark-Server-Token'] = params['x_postmark_server_token']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/email/withTemplate', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SendEmailResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def templates_post(self, x_postmark_server_token, body, **kwargs):
        """
        Create a Template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.templates_post(x_postmark_server_token, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str x_postmark_server_token: The token associated with the Server on which this request will operate. (required)
        :param CreateTemplateRequest body: (required)
        :return: TemplateRecordResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.templates_post_with_http_info(x_postmark_server_token, body, **kwargs)
        else:
            (data) = self.templates_post_with_http_info(x_postmark_server_token, body, **kwargs)
            return data

    def templates_post_with_http_info(self, x_postmark_server_token, body, **kwargs):
        """
        Create a Template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.templates_post_with_http_info(x_postmark_server_token, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str x_postmark_server_token: The token associated with the Server on which this request will operate. (required)
        :param CreateTemplateRequest body: (required)
        :return: TemplateRecordResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_postmark_server_token', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method templates_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_postmark_server_token' is set
        if ('x_postmark_server_token' not in params) or (params['x_postmark_server_token'] is None):
            raise ValueError("Missing the required parameter `x_postmark_server_token` when calling `templates_post`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `templates_post`")


        collection_formats = {}

        path_params = {}

        query_params = {}

        header_params = {}
        if 'x_postmark_server_token' in params:
            header_params['X-Postmark-Server-Token'] = params['x_postmark_server_token']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/templates', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TemplateRecordResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def test_template_content(self, x_postmark_server_token, **kwargs):
        """
        Test Template Content
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.test_template_content(x_postmark_server_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str x_postmark_server_token: The token associated with the Server on which this request will operate. (required)
        :param TemplateValidationRequest body:
        :return: TemplateValidationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.test_template_content_with_http_info(x_postmark_server_token, **kwargs)
        else:
            (data) = self.test_template_content_with_http_info(x_postmark_server_token, **kwargs)
            return data

    def test_template_content_with_http_info(self, x_postmark_server_token, **kwargs):
        """
        Test Template Content
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.test_template_content_with_http_info(x_postmark_server_token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str x_postmark_server_token: The token associated with the Server on which this request will operate. (required)
        :param TemplateValidationRequest body:
        :return: TemplateValidationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_postmark_server_token', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method test_template_content" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_postmark_server_token' is set
        if ('x_postmark_server_token' not in params) or (params['x_postmark_server_token'] is None):
            raise ValueError("Missing the required parameter `x_postmark_server_token` when calling `test_template_content`")


        collection_formats = {}

        path_params = {}

        query_params = {}

        header_params = {}
        if 'x_postmark_server_token' in params:
            header_params['X-Postmark-Server-Token'] = params['x_postmark_server_token']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/templates/validate', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TemplateValidationResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_template(self, x_postmark_server_token, templateid, body, **kwargs):
        """
        Update a Template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_template(x_postmark_server_token, templateid, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str x_postmark_server_token: The token associated with the Server on which this request will operate. (required)
        :param int templateid: The ID for the Template you wish to update. (required)
        :param EditTemplateRequest body: (required)
        :return: TemplateRecordResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_template_with_http_info(x_postmark_server_token, templateid, body, **kwargs)
        else:
            (data) = self.update_template_with_http_info(x_postmark_server_token, templateid, body, **kwargs)
            return data

    def update_template_with_http_info(self, x_postmark_server_token, templateid, body, **kwargs):
        """
        Update a Template
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_template_with_http_info(x_postmark_server_token, templateid, body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str x_postmark_server_token: The token associated with the Server on which this request will operate. (required)
        :param int templateid: The ID for the Template you wish to update. (required)
        :param EditTemplateRequest body: (required)
        :return: TemplateRecordResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_postmark_server_token', 'templateid', 'body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_template" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'x_postmark_server_token' is set
        if ('x_postmark_server_token' not in params) or (params['x_postmark_server_token'] is None):
            raise ValueError("Missing the required parameter `x_postmark_server_token` when calling `update_template`")
        # verify the required parameter 'templateid' is set
        if ('templateid' not in params) or (params['templateid'] is None):
            raise ValueError("Missing the required parameter `templateid` when calling `update_template`")
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_template`")


        collection_formats = {}

        path_params = {}
        if 'templateid' in params:
            path_params['templateid'] = params['templateid']

        query_params = {}

        header_params = {}
        if 'x_postmark_server_token' in params:
            header_params['X-Postmark-Server-Token'] = params['x_postmark_server_token']

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/templates/{templateid}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TemplateRecordResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
