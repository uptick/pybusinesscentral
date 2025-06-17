# ItemCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central itemCategory entity | [optional] 
**code** | **str** | (v1.0) The code property for the Dynamics 365 Business Central itemCategory entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central itemCategory entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central itemCategory entity | [optional] 

## Example

```python
from pybusinesscentral.model.item_category import ItemCategory

# TODO update the JSON string below
json = "{}"
# create an instance of ItemCategory from a JSON string
item_category_instance = ItemCategory.from_json(json)
# print the JSON string representation of the object
print(ItemCategory.to_json())

# convert the object into a dict
item_category_dict = item_category_instance.to_dict()
# create an instance of ItemCategory from a dict
item_category_from_dict = ItemCategory.from_dict(item_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


