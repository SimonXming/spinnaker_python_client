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
from swagger_client.api.artifact_controller_api import ArtifactControllerApi  # noqa: E501
from swagger_client.rest import ApiException


class TestArtifactControllerApi(unittest.TestCase):
    """ArtifactControllerApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.artifact_controller_api.ArtifactControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_all_using_get(self):
        """Test case for all_using_get

        Retrieve the list of artifact accounts configured in Clouddriver.  # noqa: E501
        """
        pass

    def test_artifact_versions_using_get(self):
        """Test case for artifact_versions_using_get

        Retrieve the list of artifact versions by account and artifact names  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
