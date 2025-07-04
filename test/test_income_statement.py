# coding: utf-8

"""
    (v2.0) Dynamics 365 Business Central

    (v2.0) Business Central Standard APIs

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pybusinesscentral.model.income_statement import IncomeStatement

class TestIncomeStatement(unittest.TestCase):
    """IncomeStatement unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IncomeStatement:
        """Test IncomeStatement
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IncomeStatement`
        """
        model = IncomeStatement()
        if include_optional:
            return IncomeStatement(
                line_number = 56,
                display = '',
                net_change = 1.337,
                line_type = '',
                indentation = 56,
                date_filter = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return IncomeStatement(
        )
        """

    def testIncomeStatement(self):
        """Test IncomeStatement"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
