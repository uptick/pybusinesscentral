"""
    (v2.0) Dynamics 365 Business Central

    (v2.0) Business Central Standard APIs  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pybusinesscentral.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from pybusinesscentral.exceptions import ApiAttributeError


def lazy_import():
    from pybusinesscentral.model.account import Account
    from pybusinesscentral.model.aged_accounts_payable import AgedAccountsPayable
    from pybusinesscentral.model.aged_accounts_receivable import AgedAccountsReceivable
    from pybusinesscentral.model.attachments import Attachments
    from pybusinesscentral.model.balance_sheet import BalanceSheet
    from pybusinesscentral.model.bank_account import BankAccount
    from pybusinesscentral.model.cash_flow_statement import CashFlowStatement
    from pybusinesscentral.model.company_information import CompanyInformation
    from pybusinesscentral.model.country_region import CountryRegion
    from pybusinesscentral.model.currency import Currency
    from pybusinesscentral.model.customer import Customer
    from pybusinesscentral.model.customer_financial_detail import CustomerFinancialDetail
    from pybusinesscentral.model.customer_payment import CustomerPayment
    from pybusinesscentral.model.customer_payment_journal import CustomerPaymentJournal
    from pybusinesscentral.model.customer_sale import CustomerSale
    from pybusinesscentral.model.default_dimensions import DefaultDimensions
    from pybusinesscentral.model.dimension import Dimension
    from pybusinesscentral.model.dimension_line import DimensionLine
    from pybusinesscentral.model.dimension_value import DimensionValue
    from pybusinesscentral.model.employee import Employee
    from pybusinesscentral.model.general_ledger_entry import GeneralLedgerEntry
    from pybusinesscentral.model.general_ledger_entry_attachments import GeneralLedgerEntryAttachments
    from pybusinesscentral.model.income_statement import IncomeStatement
    from pybusinesscentral.model.item import Item
    from pybusinesscentral.model.item_category import ItemCategory
    from pybusinesscentral.model.journal import Journal
    from pybusinesscentral.model.journal_line import JournalLine
    from pybusinesscentral.model.payment_method import PaymentMethod
    from pybusinesscentral.model.payment_term import PaymentTerm
    from pybusinesscentral.model.pdf_document import PdfDocument
    from pybusinesscentral.model.picture import Picture
    from pybusinesscentral.model.project import Project
    from pybusinesscentral.model.purchase_invoice import PurchaseInvoice
    from pybusinesscentral.model.purchase_invoice_line import PurchaseInvoiceLine
    from pybusinesscentral.model.retained_earnings_statement import RetainedEarningsStatement
    from pybusinesscentral.model.sales_credit_memo import SalesCreditMemo
    from pybusinesscentral.model.sales_credit_memo_line import SalesCreditMemoLine
    from pybusinesscentral.model.sales_invoice import SalesInvoice
    from pybusinesscentral.model.sales_invoice_line import SalesInvoiceLine
    from pybusinesscentral.model.sales_order import SalesOrder
    from pybusinesscentral.model.sales_order_line import SalesOrderLine
    from pybusinesscentral.model.sales_quote import SalesQuote
    from pybusinesscentral.model.sales_quote_line import SalesQuoteLine
    from pybusinesscentral.model.shipment_method import ShipmentMethod
    from pybusinesscentral.model.tax_area import TaxArea
    from pybusinesscentral.model.tax_group import TaxGroup
    from pybusinesscentral.model.time_registration_entry import TimeRegistrationEntry
    from pybusinesscentral.model.trial_balance import TrialBalance
    from pybusinesscentral.model.unit_of_measure import UnitOfMeasure
    from pybusinesscentral.model.vendor import Vendor
    from pybusinesscentral.model.vendor_purchase import VendorPurchase
    globals()['Account'] = Account
    globals()['AgedAccountsPayable'] = AgedAccountsPayable
    globals()['AgedAccountsReceivable'] = AgedAccountsReceivable
    globals()['Attachments'] = Attachments
    globals()['BalanceSheet'] = BalanceSheet
    globals()['BankAccount'] = BankAccount
    globals()['CashFlowStatement'] = CashFlowStatement
    globals()['CompanyInformation'] = CompanyInformation
    globals()['CountryRegion'] = CountryRegion
    globals()['Currency'] = Currency
    globals()['Customer'] = Customer
    globals()['CustomerFinancialDetail'] = CustomerFinancialDetail
    globals()['CustomerPayment'] = CustomerPayment
    globals()['CustomerPaymentJournal'] = CustomerPaymentJournal
    globals()['CustomerSale'] = CustomerSale
    globals()['DefaultDimensions'] = DefaultDimensions
    globals()['Dimension'] = Dimension
    globals()['DimensionLine'] = DimensionLine
    globals()['DimensionValue'] = DimensionValue
    globals()['Employee'] = Employee
    globals()['GeneralLedgerEntry'] = GeneralLedgerEntry
    globals()['GeneralLedgerEntryAttachments'] = GeneralLedgerEntryAttachments
    globals()['IncomeStatement'] = IncomeStatement
    globals()['Item'] = Item
    globals()['ItemCategory'] = ItemCategory
    globals()['Journal'] = Journal
    globals()['JournalLine'] = JournalLine
    globals()['PaymentMethod'] = PaymentMethod
    globals()['PaymentTerm'] = PaymentTerm
    globals()['PdfDocument'] = PdfDocument
    globals()['Picture'] = Picture
    globals()['Project'] = Project
    globals()['PurchaseInvoice'] = PurchaseInvoice
    globals()['PurchaseInvoiceLine'] = PurchaseInvoiceLine
    globals()['RetainedEarningsStatement'] = RetainedEarningsStatement
    globals()['SalesCreditMemo'] = SalesCreditMemo
    globals()['SalesCreditMemoLine'] = SalesCreditMemoLine
    globals()['SalesInvoice'] = SalesInvoice
    globals()['SalesInvoiceLine'] = SalesInvoiceLine
    globals()['SalesOrder'] = SalesOrder
    globals()['SalesOrderLine'] = SalesOrderLine
    globals()['SalesQuote'] = SalesQuote
    globals()['SalesQuoteLine'] = SalesQuoteLine
    globals()['ShipmentMethod'] = ShipmentMethod
    globals()['TaxArea'] = TaxArea
    globals()['TaxGroup'] = TaxGroup
    globals()['TimeRegistrationEntry'] = TimeRegistrationEntry
    globals()['TrialBalance'] = TrialBalance
    globals()['UnitOfMeasure'] = UnitOfMeasure
    globals()['Vendor'] = Vendor
    globals()['VendorPurchase'] = VendorPurchase


class Company(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
        ('name',): {
            'max_length': 30,
        },
        ('display_name',): {
            'max_length': 250,
        },
        ('business_profile_id',): {
            'max_length': 250,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'system_version': (str, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'display_name': (str, none_type,),  # noqa: E501
            'business_profile_id': (str, none_type,),  # noqa: E501
            'items': ([Item], none_type,),  # noqa: E501
            'picture': ([Picture], none_type,),  # noqa: E501
            'default_dimensions': ([DefaultDimensions], none_type,),  # noqa: E501
            'customers': ([Customer], none_type,),  # noqa: E501
            'customer_financial_details': ([CustomerFinancialDetail], none_type,),  # noqa: E501
            'vendors': ([Vendor], none_type,),  # noqa: E501
            'company_information': ([CompanyInformation], none_type,),  # noqa: E501
            'sales_invoices': ([SalesInvoice], none_type,),  # noqa: E501
            'sales_invoice_lines': ([SalesInvoiceLine], none_type,),  # noqa: E501
            'pdf_document': ([PdfDocument], none_type,),  # noqa: E501
            'customer_payment_journals': ([CustomerPaymentJournal], none_type,),  # noqa: E501
            'customer_payments': ([CustomerPayment], none_type,),  # noqa: E501
            'accounts': ([Account], none_type,),  # noqa: E501
            'tax_groups': ([TaxGroup], none_type,),  # noqa: E501
            'journals': ([Journal], none_type,),  # noqa: E501
            'journal_lines': ([JournalLine], none_type,),  # noqa: E501
            'attachments': ([Attachments], none_type,),  # noqa: E501
            'employees': ([Employee], none_type,),  # noqa: E501
            'time_registration_entries': ([TimeRegistrationEntry], none_type,),  # noqa: E501
            'general_ledger_entries': ([GeneralLedgerEntry], none_type,),  # noqa: E501
            'currencies': ([Currency], none_type,),  # noqa: E501
            'payment_methods': ([PaymentMethod], none_type,),  # noqa: E501
            'dimensions': ([Dimension], none_type,),  # noqa: E501
            'dimension_values': ([DimensionValue], none_type,),  # noqa: E501
            'dimension_lines': ([DimensionLine], none_type,),  # noqa: E501
            'payment_terms': ([PaymentTerm], none_type,),  # noqa: E501
            'shipment_methods': ([ShipmentMethod], none_type,),  # noqa: E501
            'item_categories': ([ItemCategory], none_type,),  # noqa: E501
            'cash_flow_statement': ([CashFlowStatement], none_type,),  # noqa: E501
            'countries_regions': ([CountryRegion], none_type,),  # noqa: E501
            'sales_orders': ([SalesOrder], none_type,),  # noqa: E501
            'sales_order_lines': ([SalesOrderLine], none_type,),  # noqa: E501
            'retained_earnings_statement': ([RetainedEarningsStatement], none_type,),  # noqa: E501
            'units_of_measure': ([UnitOfMeasure], none_type,),  # noqa: E501
            'aged_accounts_receivable': ([AgedAccountsReceivable], none_type,),  # noqa: E501
            'aged_accounts_payable': ([AgedAccountsPayable], none_type,),  # noqa: E501
            'balance_sheet': ([BalanceSheet], none_type,),  # noqa: E501
            'trial_balance': ([TrialBalance], none_type,),  # noqa: E501
            'income_statement': ([IncomeStatement], none_type,),  # noqa: E501
            'tax_areas': ([TaxArea], none_type,),  # noqa: E501
            'sales_quotes': ([SalesQuote], none_type,),  # noqa: E501
            'sales_quote_lines': ([SalesQuoteLine], none_type,),  # noqa: E501
            'sales_credit_memos': ([SalesCreditMemo], none_type,),  # noqa: E501
            'sales_credit_memo_lines': ([SalesCreditMemoLine], none_type,),  # noqa: E501
            'general_ledger_entry_attachments': ([GeneralLedgerEntryAttachments], none_type,),  # noqa: E501
            'purchase_invoices': ([PurchaseInvoice], none_type,),  # noqa: E501
            'purchase_invoice_lines': ([PurchaseInvoiceLine], none_type,),  # noqa: E501
            'projects': ([Project], none_type,),  # noqa: E501
            'bank_accounts': ([BankAccount], none_type,),  # noqa: E501
            'customer_sales': ([CustomerSale], none_type,),  # noqa: E501
            'vendor_purchases': ([VendorPurchase], none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'system_version': 'systemVersion',  # noqa: E501
        'name': 'name',  # noqa: E501
        'display_name': 'displayName',  # noqa: E501
        'business_profile_id': 'businessProfileId',  # noqa: E501
        'items': 'items',  # noqa: E501
        'picture': 'picture',  # noqa: E501
        'default_dimensions': 'defaultDimensions',  # noqa: E501
        'customers': 'customers',  # noqa: E501
        'customer_financial_details': 'customerFinancialDetails',  # noqa: E501
        'vendors': 'vendors',  # noqa: E501
        'company_information': 'companyInformation',  # noqa: E501
        'sales_invoices': 'salesInvoices',  # noqa: E501
        'sales_invoice_lines': 'salesInvoiceLines',  # noqa: E501
        'pdf_document': 'pdfDocument',  # noqa: E501
        'customer_payment_journals': 'customerPaymentJournals',  # noqa: E501
        'customer_payments': 'customerPayments',  # noqa: E501
        'accounts': 'accounts',  # noqa: E501
        'tax_groups': 'taxGroups',  # noqa: E501
        'journals': 'journals',  # noqa: E501
        'journal_lines': 'journalLines',  # noqa: E501
        'attachments': 'attachments',  # noqa: E501
        'employees': 'employees',  # noqa: E501
        'time_registration_entries': 'timeRegistrationEntries',  # noqa: E501
        'general_ledger_entries': 'generalLedgerEntries',  # noqa: E501
        'currencies': 'currencies',  # noqa: E501
        'payment_methods': 'paymentMethods',  # noqa: E501
        'dimensions': 'dimensions',  # noqa: E501
        'dimension_values': 'dimensionValues',  # noqa: E501
        'dimension_lines': 'dimensionLines',  # noqa: E501
        'payment_terms': 'paymentTerms',  # noqa: E501
        'shipment_methods': 'shipmentMethods',  # noqa: E501
        'item_categories': 'itemCategories',  # noqa: E501
        'cash_flow_statement': 'cashFlowStatement',  # noqa: E501
        'countries_regions': 'countriesRegions',  # noqa: E501
        'sales_orders': 'salesOrders',  # noqa: E501
        'sales_order_lines': 'salesOrderLines',  # noqa: E501
        'retained_earnings_statement': 'retainedEarningsStatement',  # noqa: E501
        'units_of_measure': 'unitsOfMeasure',  # noqa: E501
        'aged_accounts_receivable': 'agedAccountsReceivable',  # noqa: E501
        'aged_accounts_payable': 'agedAccountsPayable',  # noqa: E501
        'balance_sheet': 'balanceSheet',  # noqa: E501
        'trial_balance': 'trialBalance',  # noqa: E501
        'income_statement': 'incomeStatement',  # noqa: E501
        'tax_areas': 'taxAreas',  # noqa: E501
        'sales_quotes': 'salesQuotes',  # noqa: E501
        'sales_quote_lines': 'salesQuoteLines',  # noqa: E501
        'sales_credit_memos': 'salesCreditMemos',  # noqa: E501
        'sales_credit_memo_lines': 'salesCreditMemoLines',  # noqa: E501
        'general_ledger_entry_attachments': 'generalLedgerEntryAttachments',  # noqa: E501
        'purchase_invoices': 'purchaseInvoices',  # noqa: E501
        'purchase_invoice_lines': 'purchaseInvoiceLines',  # noqa: E501
        'projects': 'projects',  # noqa: E501
        'bank_accounts': 'bankAccounts',  # noqa: E501
        'customer_sales': 'customerSales',  # noqa: E501
        'vendor_purchases': 'vendorPurchases',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Company - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): (v1.0) The id property for the Dynamics 365 Business Central company entity. [optional]  # noqa: E501
            system_version (str, none_type): (v1.0) The systemVersion property for the Dynamics 365 Business Central company entity. [optional]  # noqa: E501
            name (str, none_type): (v1.0) The name property for the Dynamics 365 Business Central company entity. [optional]  # noqa: E501
            display_name (str, none_type): (v1.0) The displayName property for the Dynamics 365 Business Central company entity. [optional]  # noqa: E501
            business_profile_id (str, none_type): (v1.0) The businessProfileId property for the Dynamics 365 Business Central company entity. [optional]  # noqa: E501
            items ([Item], none_type): [optional]  # noqa: E501
            picture ([Picture], none_type): [optional]  # noqa: E501
            default_dimensions ([DefaultDimensions], none_type): [optional]  # noqa: E501
            customers ([Customer], none_type): [optional]  # noqa: E501
            customer_financial_details ([CustomerFinancialDetail], none_type): [optional]  # noqa: E501
            vendors ([Vendor], none_type): [optional]  # noqa: E501
            company_information ([CompanyInformation], none_type): [optional]  # noqa: E501
            sales_invoices ([SalesInvoice], none_type): [optional]  # noqa: E501
            sales_invoice_lines ([SalesInvoiceLine], none_type): [optional]  # noqa: E501
            pdf_document ([PdfDocument], none_type): [optional]  # noqa: E501
            customer_payment_journals ([CustomerPaymentJournal], none_type): [optional]  # noqa: E501
            customer_payments ([CustomerPayment], none_type): [optional]  # noqa: E501
            accounts ([Account], none_type): [optional]  # noqa: E501
            tax_groups ([TaxGroup], none_type): [optional]  # noqa: E501
            journals ([Journal], none_type): [optional]  # noqa: E501
            journal_lines ([JournalLine], none_type): [optional]  # noqa: E501
            attachments ([Attachments], none_type): [optional]  # noqa: E501
            employees ([Employee], none_type): [optional]  # noqa: E501
            time_registration_entries ([TimeRegistrationEntry], none_type): [optional]  # noqa: E501
            general_ledger_entries ([GeneralLedgerEntry], none_type): [optional]  # noqa: E501
            currencies ([Currency], none_type): [optional]  # noqa: E501
            payment_methods ([PaymentMethod], none_type): [optional]  # noqa: E501
            dimensions ([Dimension], none_type): [optional]  # noqa: E501
            dimension_values ([DimensionValue], none_type): [optional]  # noqa: E501
            dimension_lines ([DimensionLine], none_type): [optional]  # noqa: E501
            payment_terms ([PaymentTerm], none_type): [optional]  # noqa: E501
            shipment_methods ([ShipmentMethod], none_type): [optional]  # noqa: E501
            item_categories ([ItemCategory], none_type): [optional]  # noqa: E501
            cash_flow_statement ([CashFlowStatement], none_type): [optional]  # noqa: E501
            countries_regions ([CountryRegion], none_type): [optional]  # noqa: E501
            sales_orders ([SalesOrder], none_type): [optional]  # noqa: E501
            sales_order_lines ([SalesOrderLine], none_type): [optional]  # noqa: E501
            retained_earnings_statement ([RetainedEarningsStatement], none_type): [optional]  # noqa: E501
            units_of_measure ([UnitOfMeasure], none_type): [optional]  # noqa: E501
            aged_accounts_receivable ([AgedAccountsReceivable], none_type): [optional]  # noqa: E501
            aged_accounts_payable ([AgedAccountsPayable], none_type): [optional]  # noqa: E501
            balance_sheet ([BalanceSheet], none_type): [optional]  # noqa: E501
            trial_balance ([TrialBalance], none_type): [optional]  # noqa: E501
            income_statement ([IncomeStatement], none_type): [optional]  # noqa: E501
            tax_areas ([TaxArea], none_type): [optional]  # noqa: E501
            sales_quotes ([SalesQuote], none_type): [optional]  # noqa: E501
            sales_quote_lines ([SalesQuoteLine], none_type): [optional]  # noqa: E501
            sales_credit_memos ([SalesCreditMemo], none_type): [optional]  # noqa: E501
            sales_credit_memo_lines ([SalesCreditMemoLine], none_type): [optional]  # noqa: E501
            general_ledger_entry_attachments ([GeneralLedgerEntryAttachments], none_type): [optional]  # noqa: E501
            purchase_invoices ([PurchaseInvoice], none_type): [optional]  # noqa: E501
            purchase_invoice_lines ([PurchaseInvoiceLine], none_type): [optional]  # noqa: E501
            projects ([Project], none_type): [optional]  # noqa: E501
            bank_accounts ([BankAccount], none_type): [optional]  # noqa: E501
            customer_sales ([CustomerSale], none_type): [optional]  # noqa: E501
            vendor_purchases ([VendorPurchase], none_type): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Company - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            id (str): (v1.0) The id property for the Dynamics 365 Business Central company entity. [optional]  # noqa: E501
            system_version (str, none_type): (v1.0) The systemVersion property for the Dynamics 365 Business Central company entity. [optional]  # noqa: E501
            name (str, none_type): (v1.0) The name property for the Dynamics 365 Business Central company entity. [optional]  # noqa: E501
            display_name (str, none_type): (v1.0) The displayName property for the Dynamics 365 Business Central company entity. [optional]  # noqa: E501
            business_profile_id (str, none_type): (v1.0) The businessProfileId property for the Dynamics 365 Business Central company entity. [optional]  # noqa: E501
            items ([Item], none_type): [optional]  # noqa: E501
            picture ([Picture], none_type): [optional]  # noqa: E501
            default_dimensions ([DefaultDimensions], none_type): [optional]  # noqa: E501
            customers ([Customer], none_type): [optional]  # noqa: E501
            customer_financial_details ([CustomerFinancialDetail], none_type): [optional]  # noqa: E501
            vendors ([Vendor], none_type): [optional]  # noqa: E501
            company_information ([CompanyInformation], none_type): [optional]  # noqa: E501
            sales_invoices ([SalesInvoice], none_type): [optional]  # noqa: E501
            sales_invoice_lines ([SalesInvoiceLine], none_type): [optional]  # noqa: E501
            pdf_document ([PdfDocument], none_type): [optional]  # noqa: E501
            customer_payment_journals ([CustomerPaymentJournal], none_type): [optional]  # noqa: E501
            customer_payments ([CustomerPayment], none_type): [optional]  # noqa: E501
            accounts ([Account], none_type): [optional]  # noqa: E501
            tax_groups ([TaxGroup], none_type): [optional]  # noqa: E501
            journals ([Journal], none_type): [optional]  # noqa: E501
            journal_lines ([JournalLine], none_type): [optional]  # noqa: E501
            attachments ([Attachments], none_type): [optional]  # noqa: E501
            employees ([Employee], none_type): [optional]  # noqa: E501
            time_registration_entries ([TimeRegistrationEntry], none_type): [optional]  # noqa: E501
            general_ledger_entries ([GeneralLedgerEntry], none_type): [optional]  # noqa: E501
            currencies ([Currency], none_type): [optional]  # noqa: E501
            payment_methods ([PaymentMethod], none_type): [optional]  # noqa: E501
            dimensions ([Dimension], none_type): [optional]  # noqa: E501
            dimension_values ([DimensionValue], none_type): [optional]  # noqa: E501
            dimension_lines ([DimensionLine], none_type): [optional]  # noqa: E501
            payment_terms ([PaymentTerm], none_type): [optional]  # noqa: E501
            shipment_methods ([ShipmentMethod], none_type): [optional]  # noqa: E501
            item_categories ([ItemCategory], none_type): [optional]  # noqa: E501
            cash_flow_statement ([CashFlowStatement], none_type): [optional]  # noqa: E501
            countries_regions ([CountryRegion], none_type): [optional]  # noqa: E501
            sales_orders ([SalesOrder], none_type): [optional]  # noqa: E501
            sales_order_lines ([SalesOrderLine], none_type): [optional]  # noqa: E501
            retained_earnings_statement ([RetainedEarningsStatement], none_type): [optional]  # noqa: E501
            units_of_measure ([UnitOfMeasure], none_type): [optional]  # noqa: E501
            aged_accounts_receivable ([AgedAccountsReceivable], none_type): [optional]  # noqa: E501
            aged_accounts_payable ([AgedAccountsPayable], none_type): [optional]  # noqa: E501
            balance_sheet ([BalanceSheet], none_type): [optional]  # noqa: E501
            trial_balance ([TrialBalance], none_type): [optional]  # noqa: E501
            income_statement ([IncomeStatement], none_type): [optional]  # noqa: E501
            tax_areas ([TaxArea], none_type): [optional]  # noqa: E501
            sales_quotes ([SalesQuote], none_type): [optional]  # noqa: E501
            sales_quote_lines ([SalesQuoteLine], none_type): [optional]  # noqa: E501
            sales_credit_memos ([SalesCreditMemo], none_type): [optional]  # noqa: E501
            sales_credit_memo_lines ([SalesCreditMemoLine], none_type): [optional]  # noqa: E501
            general_ledger_entry_attachments ([GeneralLedgerEntryAttachments], none_type): [optional]  # noqa: E501
            purchase_invoices ([PurchaseInvoice], none_type): [optional]  # noqa: E501
            purchase_invoice_lines ([PurchaseInvoiceLine], none_type): [optional]  # noqa: E501
            projects ([Project], none_type): [optional]  # noqa: E501
            bank_accounts ([BankAccount], none_type): [optional]  # noqa: E501
            customer_sales ([CustomerSale], none_type): [optional]  # noqa: E501
            vendor_purchases ([VendorPurchase], none_type): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
