# DefaultDimensions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **str** | (v1.0) The parentId property for the Dynamics 365 Business Central defaultDimensions entity | [optional] 
**dimension_id** | **str** | (v1.0) The dimensionId property for the Dynamics 365 Business Central defaultDimensions entity | [optional] 
**dimension_code** | **str** | (v1.0) The dimensionCode property for the Dynamics 365 Business Central defaultDimensions entity | [optional] 
**dimension_value_id** | **str** | (v1.0) The dimensionValueId property for the Dynamics 365 Business Central defaultDimensions entity | [optional] 
**dimension_value_code** | **str** | (v1.0) The dimensionValueCode property for the Dynamics 365 Business Central defaultDimensions entity | [optional] 
**posting_validation** | **str** | (v1.0) The postingValidation property for the Dynamics 365 Business Central defaultDimensions entity | [optional] 
**account** | [**Account**](Account.md) |  | [optional] 
**dimension** | [**Dimension**](Dimension.md) |  | [optional] 
**dimension_value** | [**DimensionValue**](DimensionValue.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.default_dimensions import DefaultDimensions

# TODO update the JSON string below
json = "{}"
# create an instance of DefaultDimensions from a JSON string
default_dimensions_instance = DefaultDimensions.from_json(json)
# print the JSON string representation of the object
print(DefaultDimensions.to_json())

# convert the object into a dict
default_dimensions_dict = default_dimensions_instance.to_dict()
# create an instance of DefaultDimensions from a dict
default_dimensions_from_dict = DefaultDimensions.from_dict(default_dimensions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


