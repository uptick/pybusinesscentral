"""
    (v1.0) Dynamics 365 Business Central

    (v1.0) Business Central Standard APIs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import pybusinesscentral
from pybusinesscentral.api.payment_method_api import PaymentMethodApi  # noqa: E501


class TestPaymentMethodApi(unittest.TestCase):
    """PaymentMethodApi unit test stubs"""

    def setUp(self):
        self.api = PaymentMethodApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_payment_method(self):
        """Test case for delete_payment_method

        Deletes an object of type paymentMethod in Dynamics 365 Business Central  # noqa: E501
        """
        pass

    def test_get_payment_method(self):
        """Test case for get_payment_method

        Retrieve the properties and relationships of an object of type paymentMethod for Dynamics 365 Business Central.  # noqa: E501
        """
        pass

    def test_list_payment_methods(self):
        """Test case for list_payment_methods

        Returns a list of paymentMethods  # noqa: E501
        """
        pass

    def test_patch_payment_method(self):
        """Test case for patch_payment_method

        Updates an object of type paymentMethod in Dynamics 365 Business Central  # noqa: E501
        """
        pass

    def test_post_payment_method(self):
        """Test case for post_payment_method

        Creates an object of type paymentMethod in Dynamics 365 Business Central  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
