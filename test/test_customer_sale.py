# coding: utf-8

"""
    (v2.0) Dynamics 365 Business Central

    (v2.0) Business Central Standard APIs

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pybusinesscentral.model.customer_sale import CustomerSale

class TestCustomerSale(unittest.TestCase):
    """CustomerSale unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CustomerSale:
        """Test CustomerSale
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CustomerSale`
        """
        model = CustomerSale()
        if include_optional:
            return CustomerSale(
                customer_id = '',
                customer_number = '',
                name = '',
                total_sales_amount = 1.337,
                date_filter_filter_only = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return CustomerSale(
        )
        """

    def testCustomerSale(self):
        """Test CustomerSale"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
