"""
    (v1.0) Dynamics 365 Business Central

    (v1.0) Business Central Standard APIs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import pybusinesscentral
from pybusinesscentral.api.company_information_api import CompanyInformationApi  # noqa: E501


class TestCompanyInformationApi(unittest.TestCase):
    """CompanyInformationApi unit test stubs"""

    def setUp(self):
        self.api = CompanyInformationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_company_information(self):
        """Test case for get_company_information

        Retrieve the properties and relationships of an object of type companyInformation for Dynamics 365 Business Central.  # noqa: E501
        """
        pass

    def test_list_company_information(self):
        """Test case for list_company_information

        Returns a list of companyInformation  # noqa: E501
        """
        pass

    def test_patch_company_information(self):
        """Test case for patch_company_information

        Updates an object of type companyInformation in Dynamics 365 Business Central  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
