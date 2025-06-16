# Itemunitofmeasureconversiontype


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**to_unit_of_measure** | **str** | (v1.0) The toUnitOfMeasure property for the Dynamics 365 Business Central itemunitofmeasureconversiontype entity | [optional] 
**from_to_conversion_rate** | **float** | (v1.0) The fromToConversionRate property for the Dynamics 365 Business Central itemunitofmeasureconversiontype entity | [optional] 
**picture** | [**List[Picture]**](Picture.md) |  | [optional] 
**default_dimensions** | [**List[DefaultDimensions]**](DefaultDimensions.md) |  | [optional] 
**item_category** | [**ItemCategory**](ItemCategory.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.itemunitofmeasureconversiontype import Itemunitofmeasureconversiontype

# TODO update the JSON string below
json = "{}"
# create an instance of Itemunitofmeasureconversiontype from a JSON string
itemunitofmeasureconversiontype_instance = Itemunitofmeasureconversiontype.from_json(json)
# print the JSON string representation of the object
print(Itemunitofmeasureconversiontype.to_json())

# convert the object into a dict
itemunitofmeasureconversiontype_dict = itemunitofmeasureconversiontype_instance.to_dict()
# create an instance of Itemunitofmeasureconversiontype from a dict
itemunitofmeasureconversiontype_from_dict = Itemunitofmeasureconversiontype.from_dict(itemunitofmeasureconversiontype_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


