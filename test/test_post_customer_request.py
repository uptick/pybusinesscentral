# coding: utf-8

"""
    (v2.0) Dynamics 365 Business Central

    (v2.0) Business Central Standard APIs

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pybusinesscentral.model.post_customer_request import PostCustomerRequest

class TestPostCustomerRequest(unittest.TestCase):
    """PostCustomerRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostCustomerRequest:
        """Test PostCustomerRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostCustomerRequest`
        """
        model = PostCustomerRequest()
        if include_optional:
            return PostCustomerRequest(
                id = '',
                number = '',
                display_name = '',
                type = '',
                address_line1 = '',
                address_line2 = '',
                city = '',
                state = '',
                country = '',
                postal_code = '',
                phone_number = '',
                email = '',
                website = '',
                tax_liable = True,
                tax_area_id = '',
                tax_area_display_name = '',
                tax_registration_number = '',
                currency_id = '',
                currency_code = '',
                payment_terms_id = '',
                shipment_method_id = '',
                payment_method_id = '',
                blocked = '',
                last_modified_date_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return PostCustomerRequest(
        )
        """

    def testPostCustomerRequest(self):
        """Test PostCustomerRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
