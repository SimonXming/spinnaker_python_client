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
from swagger_client.api.subnet_controller_api import SubnetControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSubnetControllerApi(unittest.TestCase):
    """SubnetControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.subnet_controller_api.SubnetControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_all_by_cloud_provider_using_get1(self):
        """Test case for all_by_cloud_provider_using_get1

        Retrieve a list of subnets for a given cloud provider  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
