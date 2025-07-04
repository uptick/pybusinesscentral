# coding: utf-8

"""
    (v2.0) Dynamics 365 Business Central

    (v2.0) Business Central Standard APIs

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pybusinesscentral.model.payment_term import PaymentTerm

class TestPaymentTerm(unittest.TestCase):
    """PaymentTerm unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PaymentTerm:
        """Test PaymentTerm
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PaymentTerm`
        """
        model = PaymentTerm()
        if include_optional:
            return PaymentTerm(
                id = '',
                code = '',
                display_name = '',
                due_date_calculation = '',
                discount_date_calculation = '',
                discount_percent = 1.337,
                calculate_discount_on_credit_memos = True,
                last_modified_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return PaymentTerm(
        )
        """

    def testPaymentTerm(self):
        """Test PaymentTerm"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
