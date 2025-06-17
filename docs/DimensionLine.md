# DimensionLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **str** | (v1.0) The parentId property for the Dynamics 365 Business Central dimensionLine entity | [optional] 
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central dimensionLine entity | [optional] 
**code** | **str** | (v1.0) The code property for the Dynamics 365 Business Central dimensionLine entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central dimensionLine entity | [optional] 
**value_id** | **str** | (v1.0) The valueId property for the Dynamics 365 Business Central dimensionLine entity | [optional] 
**value_code** | **str** | (v1.0) The valueCode property for the Dynamics 365 Business Central dimensionLine entity | [optional] 
**value_display_name** | **str** | (v1.0) The valueDisplayName property for the Dynamics 365 Business Central dimensionLine entity | [optional] 
**dimension** | [**Dimension**](Dimension.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.dimension_line import DimensionLine

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionLine from a JSON string
dimension_line_instance = DimensionLine.from_json(json)
# print the JSON string representation of the object
print(DimensionLine.to_json())

# convert the object into a dict
dimension_line_dict = dimension_line_instance.to_dict()
# create an instance of DimensionLine from a dict
dimension_line_from_dict = DimensionLine.from_dict(dimension_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


