# Currency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central currency entity | [optional] 
**code** | **str** | (v1.0) The code property for the Dynamics 365 Business Central currency entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central currency entity | [optional] 
**symbol** | **str** | (v1.0) The symbol property for the Dynamics 365 Business Central currency entity | [optional] 
**amount_decimal_places** | **str** | (v1.0) The amountDecimalPlaces property for the Dynamics 365 Business Central currency entity | [optional] 
**amount_rounding_precision** | **float** | (v1.0) The amountRoundingPrecision property for the Dynamics 365 Business Central currency entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central currency entity | [optional] 

## Example

```python
from pybusinesscentral.model.currency import Currency

# TODO update the JSON string below
json = "{}"
# create an instance of Currency from a JSON string
currency_instance = Currency.from_json(json)
# print the JSON string representation of the object
print(Currency.to_json())

# convert the object into a dict
currency_dict = currency_instance.to_dict()
# create an instance of Currency from a dict
currency_from_dict = Currency.from_dict(currency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


