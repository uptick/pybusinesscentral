# coding: utf-8

"""
    (v2.0) Dynamics 365 Business Central

    (v2.0) Business Central Standard APIs

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pybusinesscentral.api.dimension_api import DimensionApi


class TestDimensionApi(unittest.TestCase):
    """DimensionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DimensionApi()

    def tearDown(self) -> None:
        pass

    def test_get_dimension(self) -> None:
        """Test case for get_dimension

        Retrieve the properties and relationships of an object of type dimension for Dynamics 365 Business Central.
        """
        pass

    def test_list_dimensions(self) -> None:
        """Test case for list_dimensions

        Returns a list of dimensions
        """
        pass


if __name__ == '__main__':
    unittest.main()
