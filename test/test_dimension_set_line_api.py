"""
    (v2.0) Dynamics 365 Business Central

    (v2.0) Business Central Standard APIs  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import pybusinesscentral
from pybusinesscentral.api.dimension_set_line_api import DimensionSetLineApi  # noqa: E501


class TestDimensionSetLineApi(unittest.TestCase):
    """DimensionSetLineApi unit test stubs"""

    def setUp(self):
        self.api = DimensionSetLineApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_dimension_set_lines_for_sales_invoice_line(self):
        """Test case for get_dimension_set_lines_for_sales_invoice_line

        Retrieve the properties and relationships of the list of dimensionSetLines for a salesInvoiceLine.  # noqa: E501
        """
        pass

    def test_post_dimension_set_line(self):
        """Test case for post_dimension_set_line

        Creates an object of type dimensionSetLine in Dynamics 365 Business Central  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
