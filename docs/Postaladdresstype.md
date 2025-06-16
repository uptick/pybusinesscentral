# Postaladdresstype


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | **str** | (v1.0) The street property for the Dynamics 365 Business Central postaladdresstype entity | [optional] 
**city** | **str** | (v1.0) The city property for the Dynamics 365 Business Central postaladdresstype entity | [optional] 
**state** | **str** | (v1.0) The state property for the Dynamics 365 Business Central postaladdresstype entity | [optional] 
**country_letter_code** | **str** | (v1.0) The countryLetterCode property for the Dynamics 365 Business Central postaladdresstype entity | [optional] 
**postal_code** | **str** | (v1.0) The postalCode property for the Dynamics 365 Business Central postaladdresstype entity | [optional] 
**customer_financial_details** | [**List[CustomerFinancialDetail]**](CustomerFinancialDetail.md) |  | [optional] 
**picture** | [**List[Picture]**](Picture.md) |  | [optional] 
**default_dimensions** | [**List[DefaultDimensions]**](DefaultDimensions.md) |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**payment_term** | [**PaymentTerm**](PaymentTerm.md) |  | [optional] 
**shipment_method** | [**ShipmentMethod**](ShipmentMethod.md) |  | [optional] 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.postaladdresstype import Postaladdresstype

# TODO update the JSON string below
json = "{}"
# create an instance of Postaladdresstype from a JSON string
postaladdresstype_instance = Postaladdresstype.from_json(json)
# print the JSON string representation of the object
print(Postaladdresstype.to_json())

# convert the object into a dict
postaladdresstype_dict = postaladdresstype_instance.to_dict()
# create an instance of Postaladdresstype from a dict
postaladdresstype_from_dict = Postaladdresstype.from_dict(postaladdresstype_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


