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
from swagger_client.api.version_controller_api import VersionControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestVersionControllerApi(unittest.TestCase):
    """VersionControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.version_controller_api.VersionControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_version_using_get(self):
        """Test case for get_version_using_get

        Fetch Gate's current version  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
