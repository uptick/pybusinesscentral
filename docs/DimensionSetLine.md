# DimensionSetLine


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

## Example

```python
from pybusinesscentral.model.dimension_set_line import DimensionSetLine

# TODO update the JSON string below
json = "{}"
# create an instance of DimensionSetLine from a JSON string
dimension_set_line_instance = DimensionSetLine.from_json(json)
# print the JSON string representation of the object
print(DimensionSetLine.to_json())

# convert the object into a dict
dimension_set_line_dict = dimension_set_line_instance.to_dict()
# create an instance of DimensionSetLine from a dict
dimension_set_line_from_dict = DimensionSetLine.from_dict(dimension_set_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


