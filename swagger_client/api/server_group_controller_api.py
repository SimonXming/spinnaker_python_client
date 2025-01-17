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


class ServerGroupControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_server_group_details_using_get(self, application_name, account, region, server_group_name, **kwargs):  # noqa: E501
        """Retrieve a server group's details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_server_group_details_using_get(application_name, account, region, server_group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_name: applicationName (required)
        :param str account: account (required)
        :param str region: region (required)
        :param str server_group_name: serverGroupName (required)
        :param str x_rate_limit_app: X-RateLimit-App
        :param str include_details: includeDetails
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_server_group_details_using_get_with_http_info(application_name, account, region, server_group_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_server_group_details_using_get_with_http_info(application_name, account, region, server_group_name, **kwargs)  # noqa: E501
            return data

    def get_server_group_details_using_get_with_http_info(self, application_name, account, region, server_group_name, **kwargs):  # noqa: E501
        """Retrieve a server group's details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_server_group_details_using_get_with_http_info(application_name, account, region, server_group_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_name: applicationName (required)
        :param str account: account (required)
        :param str region: region (required)
        :param str server_group_name: serverGroupName (required)
        :param str x_rate_limit_app: X-RateLimit-App
        :param str include_details: includeDetails
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_name', 'account', 'region', 'server_group_name', 'x_rate_limit_app', 'include_details']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_server_group_details_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_name' is set
        if ('application_name' not in params or
                params['application_name'] is None):
            raise ValueError("Missing the required parameter `application_name` when calling `get_server_group_details_using_get`")  # noqa: E501
        # verify the required parameter 'account' is set
        if ('account' not in params or
                params['account'] is None):
            raise ValueError("Missing the required parameter `account` when calling `get_server_group_details_using_get`")  # noqa: E501
        # verify the required parameter 'region' is set
        if ('region' not in params or
                params['region'] is None):
            raise ValueError("Missing the required parameter `region` when calling `get_server_group_details_using_get`")  # noqa: E501
        # verify the required parameter 'server_group_name' is set
        if ('server_group_name' not in params or
                params['server_group_name'] is None):
            raise ValueError("Missing the required parameter `server_group_name` when calling `get_server_group_details_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_name' in params:
            path_params['applicationName'] = params['application_name']  # noqa: E501
        if 'account' in params:
            path_params['account'] = params['account']  # noqa: E501
        if 'region' in params:
            path_params['region'] = params['region']  # noqa: E501
        if 'server_group_name' in params:
            path_params['serverGroupName'] = params['server_group_name']  # noqa: E501

        query_params = []
        if 'include_details' in params:
            query_params.append(('includeDetails', params['include_details']))  # noqa: E501

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
            '/applications/{applicationName}/serverGroups/{account}/{region}/{serverGroupName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_server_groups_for_application_using_get(self, application_name, **kwargs):  # noqa: E501
        """Retrieve a list of server groups for a given application  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_server_groups_for_application_using_get(application_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_name: applicationName (required)
        :param str expand: expand
        :param str cloud_provider: cloudProvider
        :param str clusters: clusters
        :param str x_rate_limit_app: X-RateLimit-App
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_server_groups_for_application_using_get_with_http_info(application_name, **kwargs)  # noqa: E501
        else:
            (data) = self.get_server_groups_for_application_using_get_with_http_info(application_name, **kwargs)  # noqa: E501
            return data

    def get_server_groups_for_application_using_get_with_http_info(self, application_name, **kwargs):  # noqa: E501
        """Retrieve a list of server groups for a given application  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_server_groups_for_application_using_get_with_http_info(application_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application_name: applicationName (required)
        :param str expand: expand
        :param str cloud_provider: cloudProvider
        :param str clusters: clusters
        :param str x_rate_limit_app: X-RateLimit-App
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application_name', 'expand', 'cloud_provider', 'clusters', 'x_rate_limit_app']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_server_groups_for_application_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application_name' is set
        if ('application_name' not in params or
                params['application_name'] is None):
            raise ValueError("Missing the required parameter `application_name` when calling `get_server_groups_for_application_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application_name' in params:
            path_params['applicationName'] = params['application_name']  # noqa: E501

        query_params = []
        if 'expand' in params:
            query_params.append(('expand', params['expand']))  # noqa: E501
        if 'cloud_provider' in params:
            query_params.append(('cloudProvider', params['cloud_provider']))  # noqa: E501
        if 'clusters' in params:
            query_params.append(('clusters', params['clusters']))  # noqa: E501

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
            '/applications/{applicationName}/serverGroups', 'GET',
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
