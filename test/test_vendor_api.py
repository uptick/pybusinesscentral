# coding: utf-8

"""
    (v2.0) Dynamics 365 Business Central

    (v2.0) Business Central Standard APIs

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pybusinesscentral.api.vendor_api import VendorApi


class TestVendorApi(unittest.TestCase):
    """VendorApi unit test stubs"""

    def setUp(self) -> None:
        self.api = VendorApi()

    def tearDown(self) -> None:
        pass

    def test_delete_vendor(self) -> None:
        """Test case for delete_vendor

        Deletes an object of type vendor in Dynamics 365 Business Central
        """
        pass

    def test_get_vendor(self) -> None:
        """Test case for get_vendor

        Retrieve the properties and relationships of an object of type vendor for Dynamics 365 Business Central.
        """
        pass

    def test_list_vendors(self) -> None:
        """Test case for list_vendors

        Returns a list of vendors
        """
        pass

    def test_patch_vendor(self) -> None:
        """Test case for patch_vendor

        Updates an object of type vendor in Dynamics 365 Business Central
        """
        pass

    def test_post_vendor(self) -> None:
        """Test case for post_vendor

        Creates an object of type vendor in Dynamics 365 Business Central
        """
        pass


if __name__ == '__main__':
    unittest.main()
