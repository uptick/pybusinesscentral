"""
    (v1.0) Dynamics 365 Business Central

    (v1.0) Business Central Standard APIs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pybusinesscentral
from pybusinesscentral.model.customer_financial_detail import CustomerFinancialDetail
from pybusinesscentral.model.default_dimensions import DefaultDimensions
from pybusinesscentral.model.picture import Picture
globals()['CustomerFinancialDetail'] = CustomerFinancialDetail
globals()['DefaultDimensions'] = DefaultDimensions
globals()['Picture'] = Picture
from pybusinesscentral.model.customer import Customer


class TestCustomer(unittest.TestCase):
    """Customer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomer(self):
        """Test Customer"""
        # FIXME: construct object with mandatory attributes with example values
        # model = Customer()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
