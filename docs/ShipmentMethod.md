# ShipmentMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central shipmentMethod entity | [optional] 
**code** | **str** | (v1.0) The code property for the Dynamics 365 Business Central shipmentMethod entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central shipmentMethod entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central shipmentMethod entity | [optional] 

## Example

```python
from pybusinesscentral.model.shipment_method import ShipmentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of ShipmentMethod from a JSON string
shipment_method_instance = ShipmentMethod.from_json(json)
# print the JSON string representation of the object
print(ShipmentMethod.to_json())

# convert the object into a dict
shipment_method_dict = shipment_method_instance.to_dict()
# create an instance of ShipmentMethod from a dict
shipment_method_from_dict = ShipmentMethod.from_dict(shipment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


