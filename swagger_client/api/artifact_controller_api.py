# coding: utf-8

"""
    Spinnaker API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ArtifactControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def all_using_get(self, **kwargs):  # noqa: E501
        """Retrieve the list of artifact accounts configured in Clouddriver.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.all_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_rate_limit_app: X-RateLimit-App
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.all_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.all_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def all_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve the list of artifact accounts configured in Clouddriver.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.all_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str x_rate_limit_app: X-RateLimit-App
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['x_rate_limit_app']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method all_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}
        if 'x_rate_limit_app' in params:
            header_params['X-RateLimit-App'] = params['x_rate_limit_app']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/artifacts/credentials', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[object]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def artifact_versions_using_get(self, account_name, type, artifact_name, **kwargs):  # noqa: E501
        """Retrieve the list of artifact versions by account and artifact names  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.artifact_versions_using_get(account_name, type, artifact_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_name: accountName (required)
        :param str type: type (required)
        :param str artifact_name: artifactName (required)
        :param str x_rate_limit_app: X-RateLimit-App
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.artifact_versions_using_get_with_http_info(account_name, type, artifact_name, **kwargs)  # noqa: E501
        else:
            (data) = self.artifact_versions_using_get_with_http_info(account_name, type, artifact_name, **kwargs)  # noqa: E501
            return data

    def artifact_versions_using_get_with_http_info(self, account_name, type, artifact_name, **kwargs):  # noqa: E501
        """Retrieve the list of artifact versions by account and artifact names  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.artifact_versions_using_get_with_http_info(account_name, type, artifact_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str account_name: accountName (required)
        :param str type: type (required)
        :param str artifact_name: artifactName (required)
        :param str x_rate_limit_app: X-RateLimit-App
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_name', 'type', 'artifact_name', 'x_rate_limit_app']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method artifact_versions_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_name' is set
        if ('account_name' not in params or
                params['account_name'] is None):
            raise ValueError("Missing the required parameter `account_name` when calling `artifact_versions_using_get`")  # noqa: E501
        # verify the required parameter 'type' is set
        if ('type' not in params or
                params['type'] is None):
            raise ValueError("Missing the required parameter `type` when calling `artifact_versions_using_get`")  # noqa: E501
        # verify the required parameter 'artifact_name' is set
        if ('artifact_name' not in params or
                params['artifact_name'] is None):
            raise ValueError("Missing the required parameter `artifact_name` when calling `artifact_versions_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'account_name' in params:
            path_params['accountName'] = params['account_name']  # noqa: E501

        query_params = []
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'artifact_name' in params:
            query_params.append(('artifactName', params['artifact_name']))  # noqa: E501

        header_params = {}
        if 'x_rate_limit_app' in params:
            header_params['X-RateLimit-App'] = params['x_rate_limit_app']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/artifacts/account/{accountName}/versions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[str]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
