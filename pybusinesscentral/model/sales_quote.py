# coding: utf-8

"""
    (v2.0) Dynamics 365 Business Central

    (v2.0) Business Central Standard APIs

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from pybusinesscentral.model.currency import Currency
from pybusinesscentral.model.customer import Customer
from pybusinesscentral.model.payment_term import PaymentTerm
from pybusinesscentral.model.pdf_document import PdfDocument
from pybusinesscentral.model.postaladdresstype import Postaladdresstype
from pybusinesscentral.model.sales_quote_line import SalesQuoteLine
from pybusinesscentral.model.shipment_method import ShipmentMethod
from typing import Optional, Set
from typing_extensions import Self

class SalesQuote(BaseModel):
    """
    SalesQuote
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="(v1.0) The id property for the Dynamics 365 Business Central salesQuote entity")
    number: Optional[Annotated[str, Field(strict=True, max_length=20)]] = Field(default=None, description="(v1.0) The number property for the Dynamics 365 Business Central salesQuote entity")
    external_document_number: Optional[Annotated[str, Field(strict=True, max_length=35)]] = Field(default=None, description="(v1.0) The externalDocumentNumber property for the Dynamics 365 Business Central salesQuote entity", alias="externalDocumentNumber")
    document_date: Optional[datetime] = Field(default=None, description="(v1.0) The documentDate property for the Dynamics 365 Business Central salesQuote entity", alias="documentDate")
    due_date: Optional[datetime] = Field(default=None, description="(v1.0) The dueDate property for the Dynamics 365 Business Central salesQuote entity", alias="dueDate")
    customer_id: Optional[StrictStr] = Field(default=None, description="(v1.0) The customerId property for the Dynamics 365 Business Central salesQuote entity", alias="customerId")
    contact_id: Optional[Annotated[str, Field(strict=True, max_length=250)]] = Field(default=None, description="(v1.0) The contactId property for the Dynamics 365 Business Central salesQuote entity", alias="contactId")
    customer_number: Optional[Annotated[str, Field(strict=True, max_length=20)]] = Field(default=None, description="(v1.0) The customerNumber property for the Dynamics 365 Business Central salesQuote entity", alias="customerNumber")
    customer_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="(v1.0) The customerName property for the Dynamics 365 Business Central salesQuote entity", alias="customerName")
    bill_to_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="(v1.0) The billToName property for the Dynamics 365 Business Central salesQuote entity", alias="billToName")
    bill_to_customer_id: Optional[StrictStr] = Field(default=None, description="(v1.0) The billToCustomerId property for the Dynamics 365 Business Central salesQuote entity", alias="billToCustomerId")
    bill_to_customer_number: Optional[Annotated[str, Field(strict=True, max_length=20)]] = Field(default=None, description="(v1.0) The billToCustomerNumber property for the Dynamics 365 Business Central salesQuote entity", alias="billToCustomerNumber")
    ship_to_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="(v1.0) The shipToName property for the Dynamics 365 Business Central salesQuote entity", alias="shipToName")
    ship_to_contact: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="(v1.0) The shipToContact property for the Dynamics 365 Business Central salesQuote entity", alias="shipToContact")
    selling_postal_address: Optional[Postaladdresstype] = Field(default=None, alias="sellingPostalAddress")
    billing_postal_address: Optional[Postaladdresstype] = Field(default=None, alias="billingPostalAddress")
    shipping_postal_address: Optional[Postaladdresstype] = Field(default=None, alias="shippingPostalAddress")
    currency_id: Optional[StrictStr] = Field(default=None, description="(v1.0) The currencyId property for the Dynamics 365 Business Central salesQuote entity", alias="currencyId")
    currency_code: Optional[StrictStr] = Field(default=None, description="(v1.0) The currencyCode property for the Dynamics 365 Business Central salesQuote entity", alias="currencyCode")
    payment_terms_id: Optional[StrictStr] = Field(default=None, description="(v1.0) The paymentTermsId property for the Dynamics 365 Business Central salesQuote entity", alias="paymentTermsId")
    shipment_method_id: Optional[StrictStr] = Field(default=None, description="(v1.0) The shipmentMethodId property for the Dynamics 365 Business Central salesQuote entity", alias="shipmentMethodId")
    salesperson: Optional[Annotated[str, Field(strict=True, max_length=20)]] = Field(default=None, description="(v1.0) The salesperson property for the Dynamics 365 Business Central salesQuote entity")
    discount_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="(v1.0) The discountAmount property for the Dynamics 365 Business Central salesQuote entity", alias="discountAmount")
    total_amount_excluding_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="(v1.0) The totalAmountExcludingTax property for the Dynamics 365 Business Central salesQuote entity", alias="totalAmountExcludingTax")
    total_tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="(v1.0) The totalTaxAmount property for the Dynamics 365 Business Central salesQuote entity", alias="totalTaxAmount")
    total_amount_including_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="(v1.0) The totalAmountIncludingTax property for the Dynamics 365 Business Central salesQuote entity", alias="totalAmountIncludingTax")
    status: Optional[StrictStr] = Field(default=None, description="(v1.0) The status property for the Dynamics 365 Business Central salesQuote entity")
    sent_date: Optional[datetime] = Field(default=None, description="(v1.0) The sentDate property for the Dynamics 365 Business Central salesQuote entity", alias="sentDate")
    valid_until_date: Optional[datetime] = Field(default=None, description="(v1.0) The validUntilDate property for the Dynamics 365 Business Central salesQuote entity", alias="validUntilDate")
    accepted_date: Optional[datetime] = Field(default=None, description="(v1.0) The acceptedDate property for the Dynamics 365 Business Central salesQuote entity", alias="acceptedDate")
    last_modified_date_time: Optional[datetime] = Field(default=None, description="(v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central salesQuote entity", alias="lastModifiedDateTime")
    phone_number: Optional[Annotated[str, Field(strict=True, max_length=30)]] = Field(default=None, description="(v1.0) The phoneNumber property for the Dynamics 365 Business Central salesQuote entity", alias="phoneNumber")
    email: Optional[Annotated[str, Field(strict=True, max_length=80)]] = Field(default=None, description="(v1.0) The email property for the Dynamics 365 Business Central salesQuote entity")
    sales_quote_lines: Optional[List[SalesQuoteLine]] = Field(default=None, alias="salesQuoteLines")
    pdf_document: Optional[List[PdfDocument]] = Field(default=None, alias="pdfDocument")
    customer: Optional[Customer] = None
    currency: Optional[Currency] = None
    payment_term: Optional[PaymentTerm] = Field(default=None, alias="paymentTerm")
    shipment_method: Optional[ShipmentMethod] = Field(default=None, alias="shipmentMethod")
    __properties: ClassVar[List[str]] = ["id", "number", "externalDocumentNumber", "documentDate", "dueDate", "customerId", "contactId", "customerNumber", "customerName", "billToName", "billToCustomerId", "billToCustomerNumber", "shipToName", "shipToContact", "sellingPostalAddress", "billingPostalAddress", "shippingPostalAddress", "currencyId", "currencyCode", "paymentTermsId", "shipmentMethodId", "salesperson", "discountAmount", "totalAmountExcludingTax", "totalTaxAmount", "totalAmountIncludingTax", "status", "sentDate", "validUntilDate", "acceptedDate", "lastModifiedDateTime", "phoneNumber", "email", "salesQuoteLines", "pdfDocument", "customer", "currency", "paymentTerm", "shipmentMethod"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SalesQuote from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of selling_postal_address
        if self.selling_postal_address:
            _dict['sellingPostalAddress'] = self.selling_postal_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing_postal_address
        if self.billing_postal_address:
            _dict['billingPostalAddress'] = self.billing_postal_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_postal_address
        if self.shipping_postal_address:
            _dict['shippingPostalAddress'] = self.shipping_postal_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in sales_quote_lines (list)
        _items = []
        if self.sales_quote_lines:
            for _item_sales_quote_lines in self.sales_quote_lines:
                if _item_sales_quote_lines:
                    _items.append(_item_sales_quote_lines.to_dict())
            _dict['salesQuoteLines'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in pdf_document (list)
        _items = []
        if self.pdf_document:
            for _item_pdf_document in self.pdf_document:
                if _item_pdf_document:
                    _items.append(_item_pdf_document.to_dict())
            _dict['pdfDocument'] = _items
        # override the default output from pydantic by calling `to_dict()` of customer
        if self.customer:
            _dict['customer'] = self.customer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict['currency'] = self.currency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_term
        if self.payment_term:
            _dict['paymentTerm'] = self.payment_term.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipment_method
        if self.shipment_method:
            _dict['shipmentMethod'] = self.shipment_method.to_dict()
        # set to None if number (nullable) is None
        # and model_fields_set contains the field
        if self.number is None and "number" in self.model_fields_set:
            _dict['number'] = None

        # set to None if external_document_number (nullable) is None
        # and model_fields_set contains the field
        if self.external_document_number is None and "external_document_number" in self.model_fields_set:
            _dict['externalDocumentNumber'] = None

        # set to None if document_date (nullable) is None
        # and model_fields_set contains the field
        if self.document_date is None and "document_date" in self.model_fields_set:
            _dict['documentDate'] = None

        # set to None if due_date (nullable) is None
        # and model_fields_set contains the field
        if self.due_date is None and "due_date" in self.model_fields_set:
            _dict['dueDate'] = None

        # set to None if customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.customer_id is None and "customer_id" in self.model_fields_set:
            _dict['customerId'] = None

        # set to None if contact_id (nullable) is None
        # and model_fields_set contains the field
        if self.contact_id is None and "contact_id" in self.model_fields_set:
            _dict['contactId'] = None

        # set to None if customer_number (nullable) is None
        # and model_fields_set contains the field
        if self.customer_number is None and "customer_number" in self.model_fields_set:
            _dict['customerNumber'] = None

        # set to None if customer_name (nullable) is None
        # and model_fields_set contains the field
        if self.customer_name is None and "customer_name" in self.model_fields_set:
            _dict['customerName'] = None

        # set to None if bill_to_name (nullable) is None
        # and model_fields_set contains the field
        if self.bill_to_name is None and "bill_to_name" in self.model_fields_set:
            _dict['billToName'] = None

        # set to None if bill_to_customer_id (nullable) is None
        # and model_fields_set contains the field
        if self.bill_to_customer_id is None and "bill_to_customer_id" in self.model_fields_set:
            _dict['billToCustomerId'] = None

        # set to None if bill_to_customer_number (nullable) is None
        # and model_fields_set contains the field
        if self.bill_to_customer_number is None and "bill_to_customer_number" in self.model_fields_set:
            _dict['billToCustomerNumber'] = None

        # set to None if ship_to_name (nullable) is None
        # and model_fields_set contains the field
        if self.ship_to_name is None and "ship_to_name" in self.model_fields_set:
            _dict['shipToName'] = None

        # set to None if ship_to_contact (nullable) is None
        # and model_fields_set contains the field
        if self.ship_to_contact is None and "ship_to_contact" in self.model_fields_set:
            _dict['shipToContact'] = None

        # set to None if selling_postal_address (nullable) is None
        # and model_fields_set contains the field
        if self.selling_postal_address is None and "selling_postal_address" in self.model_fields_set:
            _dict['sellingPostalAddress'] = None

        # set to None if billing_postal_address (nullable) is None
        # and model_fields_set contains the field
        if self.billing_postal_address is None and "billing_postal_address" in self.model_fields_set:
            _dict['billingPostalAddress'] = None

        # set to None if shipping_postal_address (nullable) is None
        # and model_fields_set contains the field
        if self.shipping_postal_address is None and "shipping_postal_address" in self.model_fields_set:
            _dict['shippingPostalAddress'] = None

        # set to None if currency_id (nullable) is None
        # and model_fields_set contains the field
        if self.currency_id is None and "currency_id" in self.model_fields_set:
            _dict['currencyId'] = None

        # set to None if currency_code (nullable) is None
        # and model_fields_set contains the field
        if self.currency_code is None and "currency_code" in self.model_fields_set:
            _dict['currencyCode'] = None

        # set to None if payment_terms_id (nullable) is None
        # and model_fields_set contains the field
        if self.payment_terms_id is None and "payment_terms_id" in self.model_fields_set:
            _dict['paymentTermsId'] = None

        # set to None if shipment_method_id (nullable) is None
        # and model_fields_set contains the field
        if self.shipment_method_id is None and "shipment_method_id" in self.model_fields_set:
            _dict['shipmentMethodId'] = None

        # set to None if salesperson (nullable) is None
        # and model_fields_set contains the field
        if self.salesperson is None and "salesperson" in self.model_fields_set:
            _dict['salesperson'] = None

        # set to None if discount_amount (nullable) is None
        # and model_fields_set contains the field
        if self.discount_amount is None and "discount_amount" in self.model_fields_set:
            _dict['discountAmount'] = None

        # set to None if total_amount_excluding_tax (nullable) is None
        # and model_fields_set contains the field
        if self.total_amount_excluding_tax is None and "total_amount_excluding_tax" in self.model_fields_set:
            _dict['totalAmountExcludingTax'] = None

        # set to None if total_tax_amount (nullable) is None
        # and model_fields_set contains the field
        if self.total_tax_amount is None and "total_tax_amount" in self.model_fields_set:
            _dict['totalTaxAmount'] = None

        # set to None if total_amount_including_tax (nullable) is None
        # and model_fields_set contains the field
        if self.total_amount_including_tax is None and "total_amount_including_tax" in self.model_fields_set:
            _dict['totalAmountIncludingTax'] = None

        # set to None if status (nullable) is None
        # and model_fields_set contains the field
        if self.status is None and "status" in self.model_fields_set:
            _dict['status'] = None

        # set to None if sent_date (nullable) is None
        # and model_fields_set contains the field
        if self.sent_date is None and "sent_date" in self.model_fields_set:
            _dict['sentDate'] = None

        # set to None if valid_until_date (nullable) is None
        # and model_fields_set contains the field
        if self.valid_until_date is None and "valid_until_date" in self.model_fields_set:
            _dict['validUntilDate'] = None

        # set to None if accepted_date (nullable) is None
        # and model_fields_set contains the field
        if self.accepted_date is None and "accepted_date" in self.model_fields_set:
            _dict['acceptedDate'] = None

        # set to None if last_modified_date_time (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified_date_time is None and "last_modified_date_time" in self.model_fields_set:
            _dict['lastModifiedDateTime'] = None

        # set to None if phone_number (nullable) is None
        # and model_fields_set contains the field
        if self.phone_number is None and "phone_number" in self.model_fields_set:
            _dict['phoneNumber'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if sales_quote_lines (nullable) is None
        # and model_fields_set contains the field
        if self.sales_quote_lines is None and "sales_quote_lines" in self.model_fields_set:
            _dict['salesQuoteLines'] = None

        # set to None if pdf_document (nullable) is None
        # and model_fields_set contains the field
        if self.pdf_document is None and "pdf_document" in self.model_fields_set:
            _dict['pdfDocument'] = None

        # set to None if customer (nullable) is None
        # and model_fields_set contains the field
        if self.customer is None and "customer" in self.model_fields_set:
            _dict['customer'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if payment_term (nullable) is None
        # and model_fields_set contains the field
        if self.payment_term is None and "payment_term" in self.model_fields_set:
            _dict['paymentTerm'] = None

        # set to None if shipment_method (nullable) is None
        # and model_fields_set contains the field
        if self.shipment_method is None and "shipment_method" in self.model_fields_set:
            _dict['shipmentMethod'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SalesQuote from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "number": obj.get("number"),
            "externalDocumentNumber": obj.get("externalDocumentNumber"),
            "documentDate": obj.get("documentDate"),
            "dueDate": obj.get("dueDate"),
            "customerId": obj.get("customerId"),
            "contactId": obj.get("contactId"),
            "customerNumber": obj.get("customerNumber"),
            "customerName": obj.get("customerName"),
            "billToName": obj.get("billToName"),
            "billToCustomerId": obj.get("billToCustomerId"),
            "billToCustomerNumber": obj.get("billToCustomerNumber"),
            "shipToName": obj.get("shipToName"),
            "shipToContact": obj.get("shipToContact"),
            "sellingPostalAddress": Postaladdresstype.from_dict(obj["sellingPostalAddress"]) if obj.get("sellingPostalAddress") is not None else None,
            "billingPostalAddress": Postaladdresstype.from_dict(obj["billingPostalAddress"]) if obj.get("billingPostalAddress") is not None else None,
            "shippingPostalAddress": Postaladdresstype.from_dict(obj["shippingPostalAddress"]) if obj.get("shippingPostalAddress") is not None else None,
            "currencyId": obj.get("currencyId"),
            "currencyCode": obj.get("currencyCode"),
            "paymentTermsId": obj.get("paymentTermsId"),
            "shipmentMethodId": obj.get("shipmentMethodId"),
            "salesperson": obj.get("salesperson"),
            "discountAmount": obj.get("discountAmount"),
            "totalAmountExcludingTax": obj.get("totalAmountExcludingTax"),
            "totalTaxAmount": obj.get("totalTaxAmount"),
            "totalAmountIncludingTax": obj.get("totalAmountIncludingTax"),
            "status": obj.get("status"),
            "sentDate": obj.get("sentDate"),
            "validUntilDate": obj.get("validUntilDate"),
            "acceptedDate": obj.get("acceptedDate"),
            "lastModifiedDateTime": obj.get("lastModifiedDateTime"),
            "phoneNumber": obj.get("phoneNumber"),
            "email": obj.get("email"),
            "salesQuoteLines": [SalesQuoteLine.from_dict(_item) for _item in obj["salesQuoteLines"]] if obj.get("salesQuoteLines") is not None else None,
            "pdfDocument": [PdfDocument.from_dict(_item) for _item in obj["pdfDocument"]] if obj.get("pdfDocument") is not None else None,
            "customer": Customer.from_dict(obj["customer"]) if obj.get("customer") is not None else None,
            "currency": Currency.from_dict(obj["currency"]) if obj.get("currency") is not None else None,
            "paymentTerm": PaymentTerm.from_dict(obj["paymentTerm"]) if obj.get("paymentTerm") is not None else None,
            "shipmentMethod": ShipmentMethod.from_dict(obj["shipmentMethod"]) if obj.get("shipmentMethod") is not None else None
        })
        return _obj


