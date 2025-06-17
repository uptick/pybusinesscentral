# TaxGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central taxGroup entity | [optional] 
**code** | **str** | (v1.0) The code property for the Dynamics 365 Business Central taxGroup entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central taxGroup entity | [optional] 
**tax_type** | **str** | (v1.0) The taxType property for the Dynamics 365 Business Central taxGroup entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central taxGroup entity | [optional] 

## Example

```python
from pybusinesscentral.model.tax_group import TaxGroup

# TODO update the JSON string below
json = "{}"
# create an instance of TaxGroup from a JSON string
tax_group_instance = TaxGroup.from_json(json)
# print the JSON string representation of the object
print(TaxGroup.to_json())

# convert the object into a dict
tax_group_dict = tax_group_instance.to_dict()
# create an instance of TaxGroup from a dict
tax_group_from_dict = TaxGroup.from_dict(tax_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


