# coding: utf-8

"""
    (v2.0) Dynamics 365 Business Central

    (v2.0) Business Central Standard APIs

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pybusinesscentral.api.payment_term_api import PaymentTermApi


class TestPaymentTermApi(unittest.TestCase):
    """PaymentTermApi unit test stubs"""

    def setUp(self) -> None:
        self.api = PaymentTermApi()

    def tearDown(self) -> None:
        pass

    def test_delete_payment_term(self) -> None:
        """Test case for delete_payment_term

        Deletes an object of type paymentTerm in Dynamics 365 Business Central
        """
        pass

    def test_get_payment_term(self) -> None:
        """Test case for get_payment_term

        Retrieve the properties and relationships of an object of type paymentTerm for Dynamics 365 Business Central.
        """
        pass

    def test_list_payment_terms(self) -> None:
        """Test case for list_payment_terms

        Returns a list of paymentTerms
        """
        pass

    def test_patch_payment_term(self) -> None:
        """Test case for patch_payment_term

        Updates an object of type paymentTerm in Dynamics 365 Business Central
        """
        pass

    def test_post_payment_term(self) -> None:
        """Test case for post_payment_term

        Creates an object of type paymentTerm in Dynamics 365 Business Central
        """
        pass


if __name__ == '__main__':
    unittest.main()
