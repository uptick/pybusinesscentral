"""
    (v1.0) Dynamics 365 Business Central

    (v1.0) Business Central Standard APIs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pybusinesscentral
from pybusinesscentral.model.pdf_document import PdfDocument
from pybusinesscentral.model.sales_invoice_line import SalesInvoiceLine
globals()['PdfDocument'] = PdfDocument
globals()['SalesInvoiceLine'] = SalesInvoiceLine
from pybusinesscentral.model.sales_invoice import SalesInvoice


class TestSalesInvoice(unittest.TestCase):
    """SalesInvoice unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSalesInvoice(self):
        """Test SalesInvoice"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SalesInvoice()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
