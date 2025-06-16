# Unitofmeasuretype


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | (v1.0) The code property for the Dynamics 365 Business Central unitofmeasuretype entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central unitofmeasuretype entity | [optional] 
**symbol** | **str** | (v1.0) The symbol property for the Dynamics 365 Business Central unitofmeasuretype entity | [optional] 
**unit_conversion** | [**Itemunitofmeasureconversiontype**](Itemunitofmeasureconversiontype.md) |  | [optional] 
**picture** | [**List[Picture]**](Picture.md) |  | [optional] 
**default_dimensions** | [**List[DefaultDimensions]**](DefaultDimensions.md) |  | [optional] 
**item_category** | [**ItemCategory**](ItemCategory.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.unitofmeasuretype import Unitofmeasuretype

# TODO update the JSON string below
json = "{}"
# create an instance of Unitofmeasuretype from a JSON string
unitofmeasuretype_instance = Unitofmeasuretype.from_json(json)
# print the JSON string representation of the object
print(Unitofmeasuretype.to_json())

# convert the object into a dict
unitofmeasuretype_dict = unitofmeasuretype_instance.to_dict()
# create an instance of Unitofmeasuretype from a dict
unitofmeasuretype_from_dict = Unitofmeasuretype.from_dict(unitofmeasuretype_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


