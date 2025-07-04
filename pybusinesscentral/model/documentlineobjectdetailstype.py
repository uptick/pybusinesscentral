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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from pybusinesscentral.model.account import Account
from pybusinesscentral.model.item import Item
from typing import Optional, Set
from typing_extensions import Self

class Documentlineobjectdetailstype(BaseModel):
    """
    Documentlineobjectdetailstype
    """ # noqa: E501
    number: Optional[Annotated[str, Field(strict=True, max_length=20)]] = Field(default=None, description="(v1.0) The number property for the Dynamics 365 Business Central documentlineobjectdetailstype entity")
    display_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="(v1.0) The displayName property for the Dynamics 365 Business Central documentlineobjectdetailstype entity", alias="displayName")
    item: Optional[Item] = None
    account: Optional[Account] = None
    __properties: ClassVar[List[str]] = ["number", "displayName", "item", "account"]

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
        """Create an instance of Documentlineobjectdetailstype from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of item
        if self.item:
            _dict['item'] = self.item.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # set to None if number (nullable) is None
        # and model_fields_set contains the field
        if self.number is None and "number" in self.model_fields_set:
            _dict['number'] = None

        # set to None if display_name (nullable) is None
        # and model_fields_set contains the field
        if self.display_name is None and "display_name" in self.model_fields_set:
            _dict['displayName'] = None

        # set to None if item (nullable) is None
        # and model_fields_set contains the field
        if self.item is None and "item" in self.model_fields_set:
            _dict['item'] = None

        # set to None if account (nullable) is None
        # and model_fields_set contains the field
        if self.account is None and "account" in self.model_fields_set:
            _dict['account'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Documentlineobjectdetailstype from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "number": obj.get("number"),
            "displayName": obj.get("displayName"),
            "item": Item.from_dict(obj["item"]) if obj.get("item") is not None else None,
            "account": Account.from_dict(obj["account"]) if obj.get("account") is not None else None
        })
        return _obj


