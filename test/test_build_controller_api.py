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
from swagger_client.api.build_controller_api import BuildControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBuildControllerApi(unittest.TestCase):
    """BuildControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.build_controller_api.BuildControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_build_masters_using_get(self):
        """Test case for get_build_masters_using_get

        Get build masters  # noqa: E501
        """
        pass

    def test_get_build_using_get(self):
        """Test case for get_build_using_get

        Get build for build master  # noqa: E501
        """
        pass

    def test_get_builds_using_get(self):
        """Test case for get_builds_using_get

        Get builds for build master  # noqa: E501
        """
        pass

    def test_get_job_config_using_get(self):
        """Test case for get_job_config_using_get

        Get job config  # noqa: E501
        """
        pass

    def test_get_jobs_for_build_master_using_get(self):
        """Test case for get_jobs_for_build_master_using_get

        Get jobs for build master  # noqa: E501
        """
        pass

    def test_v3_get_build_masters_using_get(self):
        """Test case for v3_get_build_masters_using_get

        Get build masters  # noqa: E501
        """
        pass

    def test_v3_get_build_using_get(self):
        """Test case for v3_get_build_using_get

        Get build for build master  # noqa: E501
        """
        pass

    def test_v3_get_builds_using_get(self):
        """Test case for v3_get_builds_using_get

        Get builds for build master  # noqa: E501
        """
        pass

    def test_v3_get_job_config_using_get(self):
        """Test case for v3_get_job_config_using_get

        Get job config  # noqa: E501
        """
        pass

    def test_v3_get_jobs_for_build_master_using_get(self):
        """Test case for v3_get_jobs_for_build_master_using_get

        Get jobs for build master  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()