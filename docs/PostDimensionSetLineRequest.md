# PostDimensionSetLineRequest


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
from pybusinesscentral.model.post_dimension_set_line_request import PostDimensionSetLineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDimensionSetLineRequest from a JSON string
post_dimension_set_line_request_instance = PostDimensionSetLineRequest.from_json(json)
# print the JSON string representation of the object
print(PostDimensionSetLineRequest.to_json())

# convert the object into a dict
post_dimension_set_line_request_dict = post_dimension_set_line_request_instance.to_dict()
# create an instance of PostDimensionSetLineRequest from a dict
post_dimension_set_line_request_from_dict = PostDimensionSetLineRequest.from_dict(post_dimension_set_line_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


