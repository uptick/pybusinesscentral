# DimensionValue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central dimensionValue entity | [optional] 
**code** | **str** | (v1.0) The code property for the Dynamics 365 Business Central dimensionValue entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central dimensionValue entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central dimensionValue entity | [optional] 

## Example

```python
from pybusinesscentral.model.dimension_value import DimensionValue

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionValue from a JSON string
dimension_value_instance = DimensionValue.from_json(json)
# print the JSON string representation of the object
print(DimensionValue.to_json())

# convert the object into a dict
dimension_value_dict = dimension_value_instance.to_dict()
# create an instance of DimensionValue from a dict
dimension_value_from_dict = DimensionValue.from_dict(dimension_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


