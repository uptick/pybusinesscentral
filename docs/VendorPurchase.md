# VendorPurchase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **str** | (v1.0) The vendorId property for the Dynamics 365 Business Central vendorPurchase entity | [optional] 
**vendor_number** | **str** | (v1.0) The vendorNumber property for the Dynamics 365 Business Central vendorPurchase entity | [optional] 
**name** | **str** | (v1.0) The name property for the Dynamics 365 Business Central vendorPurchase entity | [optional] 
**total_purchase_amount** | **float** | (v1.0) The totalPurchaseAmount property for the Dynamics 365 Business Central vendorPurchase entity | [optional] 
**date_filter_filter_only** | **datetime** | (v1.0) The dateFilter_FilterOnly property for the Dynamics 365 Business Central vendorPurchase entity | [optional] 

## Example

```python
from pybusinesscentral.model.vendor_purchase import VendorPurchase

# TODO update the JSON string below
json = "{}"
# create an instance of VendorPurchase from a JSON string
vendor_purchase_instance = VendorPurchase.from_json(json)
# print the JSON string representation of the object
print(VendorPurchase.to_json())

# convert the object into a dict
vendor_purchase_dict = vendor_purchase_instance.to_dict()
# create an instance of VendorPurchase from a dict
vendor_purchase_from_dict = VendorPurchase.from_dict(vendor_purchase_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


