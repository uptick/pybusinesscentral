# Dimension


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central dimension entity | [optional] 
**code** | **str** | (v1.0) The code property for the Dynamics 365 Business Central dimension entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central dimension entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central dimension entity | [optional] 
**dimension_values** | [**List[DimensionValue]**](DimensionValue.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.dimension import Dimension

# TODO update the JSON string below
json = "{}"
# create an instance of Dimension from a JSON string
dimension_instance = Dimension.from_json(json)
# print the JSON string representation of the object
print(Dimension.to_json())

# convert the object into a dict
dimension_dict = dimension_instance.to_dict()
# create an instance of Dimension from a dict
dimension_from_dict = Dimension.from_dict(dimension_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


