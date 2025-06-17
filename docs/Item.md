# Item


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central item entity | [optional] 
**number** | **str** | (v1.0) The number property for the Dynamics 365 Business Central item entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central item entity | [optional] 
**type** | **str** | (v1.0) The type property for the Dynamics 365 Business Central item entity | [optional] 
**item_category_id** | **str** | (v1.0) The itemCategoryId property for the Dynamics 365 Business Central item entity | [optional] 
**item_category_code** | **str** | (v1.0) The itemCategoryCode property for the Dynamics 365 Business Central item entity | [optional] 
**blocked** | **bool** | (v1.0) The blocked property for the Dynamics 365 Business Central item entity | [optional] 
**base_unit_of_measure_id** | **str** | (v1.0) The baseUnitOfMeasureId property for the Dynamics 365 Business Central item entity | [optional] 
**base_unit_of_measure** | [**Unitofmeasuretype**](Unitofmeasuretype.md) |  | [optional] 
**gtin** | **str** | (v1.0) The gtin property for the Dynamics 365 Business Central item entity | [optional] 
**inventory** | **float** | (v1.0) The inventory property for the Dynamics 365 Business Central item entity | [optional] 
**unit_price** | **float** | (v1.0) The unitPrice property for the Dynamics 365 Business Central item entity | [optional] 
**price_includes_tax** | **bool** | (v1.0) The priceIncludesTax property for the Dynamics 365 Business Central item entity | [optional] 
**unit_cost** | **float** | (v1.0) The unitCost property for the Dynamics 365 Business Central item entity | [optional] 
**tax_group_id** | **str** | (v1.0) The taxGroupId property for the Dynamics 365 Business Central item entity | [optional] 
**tax_group_code** | **str** | (v1.0) The taxGroupCode property for the Dynamics 365 Business Central item entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central item entity | [optional] 
**picture** | [**List[Picture]**](Picture.md) |  | [optional] 
**default_dimensions** | [**List[DefaultDimensions]**](DefaultDimensions.md) |  | [optional] 
**item_category** | [**ItemCategory**](ItemCategory.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.item import Item

# TODO update the JSON string below
json = "{}"
# create an instance of Item from a JSON string
item_instance = Item.from_json(json)
# print the JSON string representation of the object
print(Item.to_json())

# convert the object into a dict
item_dict = item_instance.to_dict()
# create an instance of Item from a dict
item_from_dict = Item.from_dict(item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


