# Dimensiontype


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | (v1.0) The code property for the Dynamics 365 Business Central dimensiontype entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central dimensiontype entity | [optional] 
**value_code** | **str** | (v1.0) The valueCode property for the Dynamics 365 Business Central dimensiontype entity | [optional] 
**value_display_name** | **str** | (v1.0) The valueDisplayName property for the Dynamics 365 Business Central dimensiontype entity | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.dimensiontype import Dimensiontype

# TODO update the JSON string below
json = "{}"
# create an instance of Dimensiontype from a JSON string
dimensiontype_instance = Dimensiontype.from_json(json)
# print the JSON string representation of the object
print(Dimensiontype.to_json())

# convert the object into a dict
dimensiontype_dict = dimensiontype_instance.to_dict()
# create an instance of Dimensiontype from a dict
dimensiontype_from_dict = Dimensiontype.from_dict(dimensiontype_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


