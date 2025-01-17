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
from swagger_client.api.concourse_controller_api import ConcourseControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestConcourseControllerApi(unittest.TestCase):
    """ConcourseControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.concourse_controller_api.ConcourseControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_jobs_using_get(self):
        """Test case for jobs_using_get

        Retrieve the list of job names for a given pipeline available to triggers  # noqa: E501
        """
        pass

    def test_pipelines_using_get(self):
        """Test case for pipelines_using_get

        Retrieve the list of pipeline names for a given team available to triggers  # noqa: E501
        """
        pass

    def test_resources_using_get(self):
        """Test case for resources_using_get

        Retrieve the list of resource names for a given pipeline available to the Concourse stage  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
