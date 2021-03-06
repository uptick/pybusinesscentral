"""
    (v1.0) Dynamics 365 Business Central

    (v1.0) Business Central Standard APIs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import unittest

import pybusinesscentral
from pybusinesscentral.api.general_ledger_entry_api import GeneralLedgerEntryApi  # noqa: E501


class TestGeneralLedgerEntryApi(unittest.TestCase):
    """GeneralLedgerEntryApi unit test stubs"""

    def setUp(self):
        self.api = GeneralLedgerEntryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_general_ledger_entry(self):
        """Test case for get_general_ledger_entry

        Retrieve the properties and relationships of an object of type generalLedgerEntry for Dynamics 365 Business Central.  # noqa: E501
        """
        pass

    def test_list_general_ledger_entries(self):
        """Test case for list_general_ledger_entries

        Returns a list of generalLedgerEntries  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
