# coding: utf-8

"""
    Spinnaker API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.pipeline_config_controller_api import PipelineConfigControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestPipelineConfigControllerApi(unittest.TestCase):
    """PipelineConfigControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.pipeline_config_controller_api.PipelineConfigControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_convert_pipeline_config_to_pipeline_template_using_get(self):
        """Test case for convert_pipeline_config_to_pipeline_template_using_get

        Convert a pipeline config to a pipeline template.  # noqa: E501
        """
        pass

    def test_get_all_pipeline_configs_using_get(self):
        """Test case for get_all_pipeline_configs_using_get

        Get all pipeline configs.  # noqa: E501
        """
        pass

    def test_get_pipeline_config_history_using_get(self):
        """Test case for get_pipeline_config_history_using_get

        Get pipeline config history.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
