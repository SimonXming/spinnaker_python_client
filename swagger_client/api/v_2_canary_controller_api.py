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


class V2CanaryControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_canary_result_using_get(self, canary_config_id, canary_execution_id, **kwargs):  # noqa: E501
        """Retrieve a canary result  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_canary_result_using_get(canary_config_id, canary_execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str canary_config_id: canaryConfigId (required)
        :param str canary_execution_id: canaryExecutionId (required)
        :param str storage_account_name: storageAccountName
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_canary_result_using_get_with_http_info(canary_config_id, canary_execution_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_canary_result_using_get_with_http_info(canary_config_id, canary_execution_id, **kwargs)  # noqa: E501
            return data

    def get_canary_result_using_get_with_http_info(self, canary_config_id, canary_execution_id, **kwargs):  # noqa: E501
        """Retrieve a canary result  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_canary_result_using_get_with_http_info(canary_config_id, canary_execution_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str canary_config_id: canaryConfigId (required)
        :param str canary_execution_id: canaryExecutionId (required)
        :param str storage_account_name: storageAccountName
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['canary_config_id', 'canary_execution_id', 'storage_account_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_canary_result_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'canary_config_id' is set
        if ('canary_config_id' not in params or
                params['canary_config_id'] is None):
            raise ValueError("Missing the required parameter `canary_config_id` when calling `get_canary_result_using_get`")  # noqa: E501
        # verify the required parameter 'canary_execution_id' is set
        if ('canary_execution_id' not in params or
                params['canary_execution_id'] is None):
            raise ValueError("Missing the required parameter `canary_execution_id` when calling `get_canary_result_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'canary_config_id' in params:
            path_params['canaryConfigId'] = params['canary_config_id']  # noqa: E501
        if 'canary_execution_id' in params:
            path_params['canaryExecutionId'] = params['canary_execution_id']  # noqa: E501

        query_params = []
        if 'storage_account_name' in params:
            query_params.append(('storageAccountName', params['storage_account_name']))  # noqa: E501

        header_params = {}

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
            '/v2/canaries/canary/{canaryConfigId}/{canaryExecutionId}', 'GET',
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

    def get_canary_results_by_application_using_get(self, application, limit, **kwargs):  # noqa: E501
        """Retrieve a list of an application's canary results  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_canary_results_by_application_using_get(application, limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application: application (required)
        :param int limit: limit (required)
        :param str statuses: Comma-separated list of statuses, e.g.: RUNNING, SUCCEEDED, TERMINAL
        :param str storage_account_name: storageAccountName
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_canary_results_by_application_using_get_with_http_info(application, limit, **kwargs)  # noqa: E501
        else:
            (data) = self.get_canary_results_by_application_using_get_with_http_info(application, limit, **kwargs)  # noqa: E501
            return data

    def get_canary_results_by_application_using_get_with_http_info(self, application, limit, **kwargs):  # noqa: E501
        """Retrieve a list of an application's canary results  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_canary_results_by_application_using_get_with_http_info(application, limit, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str application: application (required)
        :param int limit: limit (required)
        :param str statuses: Comma-separated list of statuses, e.g.: RUNNING, SUCCEEDED, TERMINAL
        :param str storage_account_name: storageAccountName
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['application', 'limit', 'statuses', 'storage_account_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_canary_results_by_application_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'application' is set
        if ('application' not in params or
                params['application'] is None):
            raise ValueError("Missing the required parameter `application` when calling `get_canary_results_by_application_using_get`")  # noqa: E501
        # verify the required parameter 'limit' is set
        if ('limit' not in params or
                params['limit'] is None):
            raise ValueError("Missing the required parameter `limit` when calling `get_canary_results_by_application_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'application' in params:
            path_params['application'] = params['application']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'statuses' in params:
            query_params.append(('statuses', params['statuses']))  # noqa: E501
        if 'storage_account_name' in params:
            query_params.append(('storageAccountName', params['storage_account_name']))  # noqa: E501

        header_params = {}

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
            '/v2/canaries/{application}/executions', 'GET',
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

    def get_metric_set_pair_list_using_get(self, metric_set_pair_list_id, **kwargs):  # noqa: E501
        """Retrieve a metric set pair list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metric_set_pair_list_using_get(metric_set_pair_list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str metric_set_pair_list_id: metricSetPairListId (required)
        :param str storage_account_name: storageAccountName
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_metric_set_pair_list_using_get_with_http_info(metric_set_pair_list_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_metric_set_pair_list_using_get_with_http_info(metric_set_pair_list_id, **kwargs)  # noqa: E501
            return data

    def get_metric_set_pair_list_using_get_with_http_info(self, metric_set_pair_list_id, **kwargs):  # noqa: E501
        """Retrieve a metric set pair list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_metric_set_pair_list_using_get_with_http_info(metric_set_pair_list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str metric_set_pair_list_id: metricSetPairListId (required)
        :param str storage_account_name: storageAccountName
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['metric_set_pair_list_id', 'storage_account_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_metric_set_pair_list_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'metric_set_pair_list_id' is set
        if ('metric_set_pair_list_id' not in params or
                params['metric_set_pair_list_id'] is None):
            raise ValueError("Missing the required parameter `metric_set_pair_list_id` when calling `get_metric_set_pair_list_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'metric_set_pair_list_id' in params:
            path_params['metricSetPairListId'] = params['metric_set_pair_list_id']  # noqa: E501

        query_params = []
        if 'storage_account_name' in params:
            query_params.append(('storageAccountName', params['storage_account_name']))  # noqa: E501

        header_params = {}

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
            '/v2/canaries/metricSetPairList/{metricSetPairListId}', 'GET',
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

    def initiate_canary_using_post(self, canary_config_id, execution_request, **kwargs):  # noqa: E501
        """Start a canary execution  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.initiate_canary_using_post(canary_config_id, execution_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str canary_config_id: canaryConfigId (required)
        :param object execution_request: executionRequest (required)
        :param str application: application
        :param str parent_pipeline_execution_id: parentPipelineExecutionId
        :param str metrics_account_name: metricsAccountName
        :param str storage_account_name: storageAccountName
        :param str configuration_account_name: configurationAccountName
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.initiate_canary_using_post_with_http_info(canary_config_id, execution_request, **kwargs)  # noqa: E501
        else:
            (data) = self.initiate_canary_using_post_with_http_info(canary_config_id, execution_request, **kwargs)  # noqa: E501
            return data

    def initiate_canary_using_post_with_http_info(self, canary_config_id, execution_request, **kwargs):  # noqa: E501
        """Start a canary execution  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.initiate_canary_using_post_with_http_info(canary_config_id, execution_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str canary_config_id: canaryConfigId (required)
        :param object execution_request: executionRequest (required)
        :param str application: application
        :param str parent_pipeline_execution_id: parentPipelineExecutionId
        :param str metrics_account_name: metricsAccountName
        :param str storage_account_name: storageAccountName
        :param str configuration_account_name: configurationAccountName
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['canary_config_id', 'execution_request', 'application', 'parent_pipeline_execution_id', 'metrics_account_name', 'storage_account_name', 'configuration_account_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method initiate_canary_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'canary_config_id' is set
        if ('canary_config_id' not in params or
                params['canary_config_id'] is None):
            raise ValueError("Missing the required parameter `canary_config_id` when calling `initiate_canary_using_post`")  # noqa: E501
        # verify the required parameter 'execution_request' is set
        if ('execution_request' not in params or
                params['execution_request'] is None):
            raise ValueError("Missing the required parameter `execution_request` when calling `initiate_canary_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'canary_config_id' in params:
            path_params['canaryConfigId'] = params['canary_config_id']  # noqa: E501

        query_params = []
        if 'application' in params:
            query_params.append(('application', params['application']))  # noqa: E501
        if 'parent_pipeline_execution_id' in params:
            query_params.append(('parentPipelineExecutionId', params['parent_pipeline_execution_id']))  # noqa: E501
        if 'metrics_account_name' in params:
            query_params.append(('metricsAccountName', params['metrics_account_name']))  # noqa: E501
        if 'storage_account_name' in params:
            query_params.append(('storageAccountName', params['storage_account_name']))  # noqa: E501
        if 'configuration_account_name' in params:
            query_params.append(('configurationAccountName', params['configuration_account_name']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'execution_request' in params:
            body_params = params['execution_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v2/canaries/canary/{canaryConfigId}', 'POST',
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

    def list_credentials_using_get(self, **kwargs):  # noqa: E501
        """Retrieve a list of configured Kayenta accounts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_credentials_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_credentials_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_credentials_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_credentials_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a list of configured Kayenta accounts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_credentials_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_credentials_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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
            '/v2/canaries/credentials', 'GET',
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

    def list_judges_using_get(self, **kwargs):  # noqa: E501
        """Retrieve a list of all configured canary judges  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_judges_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_judges_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_judges_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_judges_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a list of all configured canary judges  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_judges_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_judges_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

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
            '/v2/canaries/judges', 'GET',
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

    def list_metrics_service_metadata_using_get(self, **kwargs):  # noqa: E501
        """Retrieve a list of descriptors for use in populating the canary config ui  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_metrics_service_metadata_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter: filter
        :param str metrics_account_name: metricsAccountName
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_metrics_service_metadata_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_metrics_service_metadata_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_metrics_service_metadata_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Retrieve a list of descriptors for use in populating the canary config ui  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_metrics_service_metadata_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filter: filter
        :param str metrics_account_name: metricsAccountName
        :return: list[object]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filter', 'metrics_account_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_metrics_service_metadata_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filter' in params:
            query_params.append(('filter', params['filter']))  # noqa: E501
        if 'metrics_account_name' in params:
            query_params.append(('metricsAccountName', params['metrics_account_name']))  # noqa: E501

        header_params = {}

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
            '/v2/canaries/metadata/metricsService', 'GET',
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
