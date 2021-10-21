"""
    (v1.0) Dynamics 365 Business Central

    (v1.0) Business Central Standard APIs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
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
    from pybusinesscentral.model.pdf_document import PdfDocument
    from pybusinesscentral.model.sales_quote_line import SalesQuoteLine
    globals()['PdfDocument'] = PdfDocument
    globals()['SalesQuoteLine'] = SalesQuoteLine


class SalesQuote(ModelNormal):
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
        ('number',): {
            'max_length': 20,
        },
        ('external_document_number',): {
            'max_length': 35,
        },
        ('contact_id',): {
            'max_length': 250,
        },
        ('customer_number',): {
            'max_length': 20,
        },
        ('customer_name',): {
            'max_length': 100,
        },
        ('bill_to_name',): {
            'max_length': 100,
        },
        ('bill_to_customer_number',): {
            'max_length': 20,
        },
        ('ship_to_name',): {
            'max_length': 100,
        },
        ('ship_to_contact',): {
            'max_length': 100,
        },
        ('salesperson',): {
            'max_length': 20,
        },
        ('phone_number',): {
            'max_length': 30,
        },
        ('email',): {
            'max_length': 80,
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
            'number': (str, none_type,),  # noqa: E501
            'external_document_number': (str, none_type,),  # noqa: E501
            'document_date': (datetime, none_type,),  # noqa: E501
            'due_date': (datetime, none_type,),  # noqa: E501
            'customer_id': (str, none_type,),  # noqa: E501
            'contact_id': (str, none_type,),  # noqa: E501
            'customer_number': (str, none_type,),  # noqa: E501
            'customer_name': (str, none_type,),  # noqa: E501
            'bill_to_name': (str, none_type,),  # noqa: E501
            'bill_to_customer_id': (str, none_type,),  # noqa: E501
            'bill_to_customer_number': (str, none_type,),  # noqa: E501
            'ship_to_name': (str, none_type,),  # noqa: E501
            'ship_to_contact': (str, none_type,),  # noqa: E501
            'selling_postal_address': (dict,),  # noqa: E501
            'billing_postal_address': (dict,),  # noqa: E501
            'shipping_postal_address': (dict,),  # noqa: E501
            'currency_id': (str, none_type,),  # noqa: E501
            'currency_code': (str, none_type,),  # noqa: E501
            'payment_terms_id': (str, none_type,),  # noqa: E501
            'shipment_method_id': (str, none_type,),  # noqa: E501
            'salesperson': (str, none_type,),  # noqa: E501
            'discount_amount': (float, none_type,),  # noqa: E501
            'total_amount_excluding_tax': (float, none_type,),  # noqa: E501
            'total_tax_amount': (float, none_type,),  # noqa: E501
            'total_amount_including_tax': (float, none_type,),  # noqa: E501
            'status': (str, none_type,),  # noqa: E501
            'sent_date': (datetime, none_type,),  # noqa: E501
            'valid_until_date': (datetime, none_type,),  # noqa: E501
            'accepted_date': (datetime, none_type,),  # noqa: E501
            'last_modified_date_time': (datetime, none_type,),  # noqa: E501
            'phone_number': (str, none_type,),  # noqa: E501
            'email': (str, none_type,),  # noqa: E501
            'sales_quote_lines': ([SalesQuoteLine], none_type,),  # noqa: E501
            'pdf_document': ([PdfDocument], none_type,),  # noqa: E501
            'customer': (dict,),  # noqa: E501
            'currency': (dict,),  # noqa: E501
            'payment_term': (dict,),  # noqa: E501
            'shipment_method': (dict,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'number': 'number',  # noqa: E501
        'external_document_number': 'externalDocumentNumber',  # noqa: E501
        'document_date': 'documentDate',  # noqa: E501
        'due_date': 'dueDate',  # noqa: E501
        'customer_id': 'customerId',  # noqa: E501
        'contact_id': 'contactId',  # noqa: E501
        'customer_number': 'customerNumber',  # noqa: E501
        'customer_name': 'customerName',  # noqa: E501
        'bill_to_name': 'billToName',  # noqa: E501
        'bill_to_customer_id': 'billToCustomerId',  # noqa: E501
        'bill_to_customer_number': 'billToCustomerNumber',  # noqa: E501
        'ship_to_name': 'shipToName',  # noqa: E501
        'ship_to_contact': 'shipToContact',  # noqa: E501
        'selling_postal_address': 'sellingPostalAddress',  # noqa: E501
        'billing_postal_address': 'billingPostalAddress',  # noqa: E501
        'shipping_postal_address': 'shippingPostalAddress',  # noqa: E501
        'currency_id': 'currencyId',  # noqa: E501
        'currency_code': 'currencyCode',  # noqa: E501
        'payment_terms_id': 'paymentTermsId',  # noqa: E501
        'shipment_method_id': 'shipmentMethodId',  # noqa: E501
        'salesperson': 'salesperson',  # noqa: E501
        'discount_amount': 'discountAmount',  # noqa: E501
        'total_amount_excluding_tax': 'totalAmountExcludingTax',  # noqa: E501
        'total_tax_amount': 'totalTaxAmount',  # noqa: E501
        'total_amount_including_tax': 'totalAmountIncludingTax',  # noqa: E501
        'status': 'status',  # noqa: E501
        'sent_date': 'sentDate',  # noqa: E501
        'valid_until_date': 'validUntilDate',  # noqa: E501
        'accepted_date': 'acceptedDate',  # noqa: E501
        'last_modified_date_time': 'lastModifiedDateTime',  # noqa: E501
        'phone_number': 'phoneNumber',  # noqa: E501
        'email': 'email',  # noqa: E501
        'sales_quote_lines': 'salesQuoteLines',  # noqa: E501
        'pdf_document': 'pdfDocument',  # noqa: E501
        'customer': 'customer',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'payment_term': 'paymentTerm',  # noqa: E501
        'shipment_method': 'shipmentMethod',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """SalesQuote - a model defined in OpenAPI

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
            id (str): (v1.0) The id property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            number (str, none_type): (v1.0) The number property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            external_document_number (str, none_type): (v1.0) The externalDocumentNumber property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            document_date (datetime, none_type): (v1.0) The documentDate property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            due_date (datetime, none_type): (v1.0) The dueDate property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            customer_id (str, none_type): (v1.0) The customerId property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            contact_id (str, none_type): (v1.0) The contactId property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            customer_number (str, none_type): (v1.0) The customerNumber property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            customer_name (str, none_type): (v1.0) The customerName property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            bill_to_name (str, none_type): (v1.0) The billToName property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            bill_to_customer_id (str, none_type): (v1.0) The billToCustomerId property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            bill_to_customer_number (str, none_type): (v1.0) The billToCustomerNumber property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            ship_to_name (str, none_type): (v1.0) The shipToName property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            ship_to_contact (str, none_type): (v1.0) The shipToContact property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            selling_postal_address (dict): [optional]  # noqa: E501
            billing_postal_address (dict): [optional]  # noqa: E501
            shipping_postal_address (dict): [optional]  # noqa: E501
            currency_id (str, none_type): (v1.0) The currencyId property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            currency_code (str, none_type): (v1.0) The currencyCode property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            payment_terms_id (str, none_type): (v1.0) The paymentTermsId property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            shipment_method_id (str, none_type): (v1.0) The shipmentMethodId property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            salesperson (str, none_type): (v1.0) The salesperson property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            discount_amount (float, none_type): (v1.0) The discountAmount property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            total_amount_excluding_tax (float, none_type): (v1.0) The totalAmountExcludingTax property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            total_tax_amount (float, none_type): (v1.0) The totalTaxAmount property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            total_amount_including_tax (float, none_type): (v1.0) The totalAmountIncludingTax property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            status (str, none_type): (v1.0) The status property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            sent_date (datetime, none_type): (v1.0) The sentDate property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            valid_until_date (datetime, none_type): (v1.0) The validUntilDate property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            accepted_date (datetime, none_type): (v1.0) The acceptedDate property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            last_modified_date_time (datetime, none_type): (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            phone_number (str, none_type): (v1.0) The phoneNumber property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            email (str, none_type): (v1.0) The email property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            sales_quote_lines ([SalesQuoteLine], none_type): [optional]  # noqa: E501
            pdf_document ([PdfDocument], none_type): [optional]  # noqa: E501
            customer (dict): [optional]  # noqa: E501
            currency (dict): [optional]  # noqa: E501
            payment_term (dict): [optional]  # noqa: E501
            shipment_method (dict): [optional]  # noqa: E501
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
        """SalesQuote - a model defined in OpenAPI

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
            id (str): (v1.0) The id property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            number (str, none_type): (v1.0) The number property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            external_document_number (str, none_type): (v1.0) The externalDocumentNumber property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            document_date (datetime, none_type): (v1.0) The documentDate property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            due_date (datetime, none_type): (v1.0) The dueDate property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            customer_id (str, none_type): (v1.0) The customerId property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            contact_id (str, none_type): (v1.0) The contactId property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            customer_number (str, none_type): (v1.0) The customerNumber property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            customer_name (str, none_type): (v1.0) The customerName property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            bill_to_name (str, none_type): (v1.0) The billToName property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            bill_to_customer_id (str, none_type): (v1.0) The billToCustomerId property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            bill_to_customer_number (str, none_type): (v1.0) The billToCustomerNumber property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            ship_to_name (str, none_type): (v1.0) The shipToName property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            ship_to_contact (str, none_type): (v1.0) The shipToContact property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            selling_postal_address (dict): [optional]  # noqa: E501
            billing_postal_address (dict): [optional]  # noqa: E501
            shipping_postal_address (dict): [optional]  # noqa: E501
            currency_id (str, none_type): (v1.0) The currencyId property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            currency_code (str, none_type): (v1.0) The currencyCode property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            payment_terms_id (str, none_type): (v1.0) The paymentTermsId property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            shipment_method_id (str, none_type): (v1.0) The shipmentMethodId property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            salesperson (str, none_type): (v1.0) The salesperson property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            discount_amount (float, none_type): (v1.0) The discountAmount property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            total_amount_excluding_tax (float, none_type): (v1.0) The totalAmountExcludingTax property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            total_tax_amount (float, none_type): (v1.0) The totalTaxAmount property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            total_amount_including_tax (float, none_type): (v1.0) The totalAmountIncludingTax property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            status (str, none_type): (v1.0) The status property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            sent_date (datetime, none_type): (v1.0) The sentDate property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            valid_until_date (datetime, none_type): (v1.0) The validUntilDate property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            accepted_date (datetime, none_type): (v1.0) The acceptedDate property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            last_modified_date_time (datetime, none_type): (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            phone_number (str, none_type): (v1.0) The phoneNumber property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            email (str, none_type): (v1.0) The email property for the Dynamics 365 Business Central salesQuote entity. [optional]  # noqa: E501
            sales_quote_lines ([SalesQuoteLine], none_type): [optional]  # noqa: E501
            pdf_document ([PdfDocument], none_type): [optional]  # noqa: E501
            customer (dict): [optional]  # noqa: E501
            currency (dict): [optional]  # noqa: E501
            payment_term (dict): [optional]  # noqa: E501
            shipment_method (dict): [optional]  # noqa: E501
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
