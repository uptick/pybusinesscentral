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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from pybusinesscentral.model.currency import Currency
from pybusinesscentral.model.default_dimensions import DefaultDimensions
from pybusinesscentral.model.payment_method import PaymentMethod
from pybusinesscentral.model.payment_term import PaymentTerm
from pybusinesscentral.model.picture import Picture
from typing import Optional, Set
from typing_extensions import Self

class Vendor(BaseModel):
    """
    Vendor
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="(v1.0) The id property for the Dynamics 365 Business Central vendor entity")
    number: Optional[Annotated[str, Field(strict=True, max_length=20)]] = Field(default=None, description="(v1.0) The number property for the Dynamics 365 Business Central vendor entity")
    display_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="(v1.0) The displayName property for the Dynamics 365 Business Central vendor entity", alias="displayName")
    address_line1: Optional[Annotated[str, Field(strict=True, max_length=152)]] = Field(default=None, description="(v1.0) The street property for the Dynamics 365 Business Central postaladdresstype entity", alias="addressLine1")
    address_line2: Optional[Annotated[str, Field(strict=True, max_length=152)]] = Field(default=None, description="(v1.0) The street property for the Dynamics 365 Business Central postaladdresstype entity", alias="addressLine2")
    city: Optional[Annotated[str, Field(strict=True, max_length=30)]] = Field(default=None, description="(v1.0) The city property for the Dynamics 365 Business Central postaladdresstype entity")
    state: Optional[Annotated[str, Field(strict=True, max_length=30)]] = Field(default=None, description="(v1.0) The state property for the Dynamics 365 Business Central postaladdresstype entity")
    country: Optional[Annotated[str, Field(strict=True, max_length=10)]] = Field(default=None, description="(v1.0) The countryLetterCode property for the Dynamics 365 Business Central postaladdresstype entity")
    postal_code: Optional[Annotated[str, Field(strict=True, max_length=20)]] = Field(default=None, description="(v1.0) The postalCode property for the Dynamics 365 Business Central postaladdresstype entity", alias="postalCode")
    phone_number: Optional[Annotated[str, Field(strict=True, max_length=30)]] = Field(default=None, description="(v1.0) The phoneNumber property for the Dynamics 365 Business Central vendor entity", alias="phoneNumber")
    email: Optional[Annotated[str, Field(strict=True, max_length=80)]] = Field(default=None, description="(v1.0) The email property for the Dynamics 365 Business Central vendor entity")
    website: Optional[Annotated[str, Field(strict=True, max_length=80)]] = Field(default=None, description="(v1.0) The website property for the Dynamics 365 Business Central vendor entity")
    tax_registration_number: Optional[Annotated[str, Field(strict=True, max_length=20)]] = Field(default=None, description="(v1.0) The taxRegistrationNumber property for the Dynamics 365 Business Central vendor entity", alias="taxRegistrationNumber")
    currency_id: Optional[StrictStr] = Field(default=None, description="(v1.0) The currencyId property for the Dynamics 365 Business Central vendor entity", alias="currencyId")
    currency_code: Optional[StrictStr] = Field(default=None, description="(v1.0) The currencyCode property for the Dynamics 365 Business Central vendor entity", alias="currencyCode")
    irs1099_code: Optional[StrictStr] = Field(default=None, description="(v1.0) The irs1099Code property for the Dynamics 365 Business Central vendor entity", alias="irs1099Code")
    payment_terms_id: Optional[StrictStr] = Field(default=None, description="(v1.0) The paymentTermsId property for the Dynamics 365 Business Central vendor entity", alias="paymentTermsId")
    payment_method_id: Optional[StrictStr] = Field(default=None, description="(v1.0) The paymentMethodId property for the Dynamics 365 Business Central vendor entity", alias="paymentMethodId")
    tax_liable: Optional[StrictBool] = Field(default=None, description="(v1.0) The taxLiable property for the Dynamics 365 Business Central vendor entity", alias="taxLiable")
    blocked: Optional[StrictStr] = Field(default=None, description="(v1.0) The blocked property for the Dynamics 365 Business Central vendor entity")
    balance: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="(v1.0) The balance property for the Dynamics 365 Business Central vendor entity")
    last_modified_date_time: Optional[datetime] = Field(default=None, description="(v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central vendor entity", alias="lastModifiedDateTime")
    picture: Optional[List[Picture]] = None
    default_dimensions: Optional[List[DefaultDimensions]] = Field(default=None, alias="defaultDimensions")
    currency: Optional[Currency] = None
    payment_term: Optional[PaymentTerm] = Field(default=None, alias="paymentTerm")
    payment_method: Optional[PaymentMethod] = Field(default=None, alias="paymentMethod")
    __properties: ClassVar[List[str]] = ["id", "number", "displayName", "addressLine1", "addressLine2", "city", "state", "country", "postalCode", "phoneNumber", "email", "website", "taxRegistrationNumber", "currencyId", "currencyCode", "irs1099Code", "paymentTermsId", "paymentMethodId", "taxLiable", "blocked", "balance", "lastModifiedDateTime", "picture", "defaultDimensions", "currency", "paymentTerm", "paymentMethod"]

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
        """Create an instance of Vendor from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in picture (list)
        _items = []
        if self.picture:
            for _item_picture in self.picture:
                if _item_picture:
                    _items.append(_item_picture.to_dict())
            _dict['picture'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in default_dimensions (list)
        _items = []
        if self.default_dimensions:
            for _item_default_dimensions in self.default_dimensions:
                if _item_default_dimensions:
                    _items.append(_item_default_dimensions.to_dict())
            _dict['defaultDimensions'] = _items
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict['currency'] = self.currency.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_term
        if self.payment_term:
            _dict['paymentTerm'] = self.payment_term.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_method
        if self.payment_method:
            _dict['paymentMethod'] = self.payment_method.to_dict()
        # set to None if number (nullable) is None
        # and model_fields_set contains the field
        if self.number is None and "number" in self.model_fields_set:
            _dict['number'] = None

        # set to None if display_name (nullable) is None
        # and model_fields_set contains the field
        if self.display_name is None and "display_name" in self.model_fields_set:
            _dict['displayName'] = None

        # set to None if address_line1 (nullable) is None
        # and model_fields_set contains the field
        if self.address_line1 is None and "address_line1" in self.model_fields_set:
            _dict['addressLine1'] = None

        # set to None if address_line2 (nullable) is None
        # and model_fields_set contains the field
        if self.address_line2 is None and "address_line2" in self.model_fields_set:
            _dict['addressLine2'] = None

        # set to None if city (nullable) is None
        # and model_fields_set contains the field
        if self.city is None and "city" in self.model_fields_set:
            _dict['city'] = None

        # set to None if state (nullable) is None
        # and model_fields_set contains the field
        if self.state is None and "state" in self.model_fields_set:
            _dict['state'] = None

        # set to None if country (nullable) is None
        # and model_fields_set contains the field
        if self.country is None and "country" in self.model_fields_set:
            _dict['country'] = None

        # set to None if postal_code (nullable) is None
        # and model_fields_set contains the field
        if self.postal_code is None and "postal_code" in self.model_fields_set:
            _dict['postalCode'] = None

        # set to None if phone_number (nullable) is None
        # and model_fields_set contains the field
        if self.phone_number is None and "phone_number" in self.model_fields_set:
            _dict['phoneNumber'] = None

        # set to None if email (nullable) is None
        # and model_fields_set contains the field
        if self.email is None and "email" in self.model_fields_set:
            _dict['email'] = None

        # set to None if website (nullable) is None
        # and model_fields_set contains the field
        if self.website is None and "website" in self.model_fields_set:
            _dict['website'] = None

        # set to None if tax_registration_number (nullable) is None
        # and model_fields_set contains the field
        if self.tax_registration_number is None and "tax_registration_number" in self.model_fields_set:
            _dict['taxRegistrationNumber'] = None

        # set to None if currency_id (nullable) is None
        # and model_fields_set contains the field
        if self.currency_id is None and "currency_id" in self.model_fields_set:
            _dict['currencyId'] = None

        # set to None if currency_code (nullable) is None
        # and model_fields_set contains the field
        if self.currency_code is None and "currency_code" in self.model_fields_set:
            _dict['currencyCode'] = None

        # set to None if irs1099_code (nullable) is None
        # and model_fields_set contains the field
        if self.irs1099_code is None and "irs1099_code" in self.model_fields_set:
            _dict['irs1099Code'] = None

        # set to None if payment_terms_id (nullable) is None
        # and model_fields_set contains the field
        if self.payment_terms_id is None and "payment_terms_id" in self.model_fields_set:
            _dict['paymentTermsId'] = None

        # set to None if payment_method_id (nullable) is None
        # and model_fields_set contains the field
        if self.payment_method_id is None and "payment_method_id" in self.model_fields_set:
            _dict['paymentMethodId'] = None

        # set to None if tax_liable (nullable) is None
        # and model_fields_set contains the field
        if self.tax_liable is None and "tax_liable" in self.model_fields_set:
            _dict['taxLiable'] = None

        # set to None if blocked (nullable) is None
        # and model_fields_set contains the field
        if self.blocked is None and "blocked" in self.model_fields_set:
            _dict['blocked'] = None

        # set to None if balance (nullable) is None
        # and model_fields_set contains the field
        if self.balance is None and "balance" in self.model_fields_set:
            _dict['balance'] = None

        # set to None if last_modified_date_time (nullable) is None
        # and model_fields_set contains the field
        if self.last_modified_date_time is None and "last_modified_date_time" in self.model_fields_set:
            _dict['lastModifiedDateTime'] = None

        # set to None if picture (nullable) is None
        # and model_fields_set contains the field
        if self.picture is None and "picture" in self.model_fields_set:
            _dict['picture'] = None

        # set to None if default_dimensions (nullable) is None
        # and model_fields_set contains the field
        if self.default_dimensions is None and "default_dimensions" in self.model_fields_set:
            _dict['defaultDimensions'] = None

        # set to None if currency (nullable) is None
        # and model_fields_set contains the field
        if self.currency is None and "currency" in self.model_fields_set:
            _dict['currency'] = None

        # set to None if payment_term (nullable) is None
        # and model_fields_set contains the field
        if self.payment_term is None and "payment_term" in self.model_fields_set:
            _dict['paymentTerm'] = None

        # set to None if payment_method (nullable) is None
        # and model_fields_set contains the field
        if self.payment_method is None and "payment_method" in self.model_fields_set:
            _dict['paymentMethod'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Vendor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "number": obj.get("number"),
            "displayName": obj.get("displayName"),
            "addressLine1": obj.get("addressLine1"),
            "addressLine2": obj.get("addressLine2"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "country": obj.get("country"),
            "postalCode": obj.get("postalCode"),
            "phoneNumber": obj.get("phoneNumber"),
            "email": obj.get("email"),
            "website": obj.get("website"),
            "taxRegistrationNumber": obj.get("taxRegistrationNumber"),
            "currencyId": obj.get("currencyId"),
            "currencyCode": obj.get("currencyCode"),
            "irs1099Code": obj.get("irs1099Code"),
            "paymentTermsId": obj.get("paymentTermsId"),
            "paymentMethodId": obj.get("paymentMethodId"),
            "taxLiable": obj.get("taxLiable"),
            "blocked": obj.get("blocked"),
            "balance": obj.get("balance"),
            "lastModifiedDateTime": obj.get("lastModifiedDateTime"),
            "picture": [Picture.from_dict(_item) for _item in obj["picture"]] if obj.get("picture") is not None else None,
            "defaultDimensions": [DefaultDimensions.from_dict(_item) for _item in obj["defaultDimensions"]] if obj.get("defaultDimensions") is not None else None,
            "currency": Currency.from_dict(obj["currency"]) if obj.get("currency") is not None else None,
            "paymentTerm": PaymentTerm.from_dict(obj["paymentTerm"]) if obj.get("paymentTerm") is not None else None,
            "paymentMethod": PaymentMethod.from_dict(obj["paymentMethod"]) if obj.get("paymentMethod") is not None else None
        })
        return _obj


