# UnitOfMeasure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central unitOfMeasure entity | [optional] 
**code** | **str** | (v1.0) The code property for the Dynamics 365 Business Central unitOfMeasure entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central unitOfMeasure entity | [optional] 
**international_standard_code** | **str** | (v1.0) The internationalStandardCode property for the Dynamics 365 Business Central unitOfMeasure entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central unitOfMeasure entity | [optional] 

## Example

```python
from pybusinesscentral.model.unit_of_measure import UnitOfMeasure

# TODO update the JSON string below
json = "{}"
# create an instance of UnitOfMeasure from a JSON string
unit_of_measure_instance = UnitOfMeasure.from_json(json)
# print the JSON string representation of the object
print(UnitOfMeasure.to_json())

# convert the object into a dict
unit_of_measure_dict = unit_of_measure_instance.to_dict()
# create an instance of UnitOfMeasure from a dict
unit_of_measure_from_dict = UnitOfMeasure.from_dict(unit_of_measure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


