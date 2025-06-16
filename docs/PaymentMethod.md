# PaymentMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central paymentMethod entity | [optional] 
**code** | **str** | (v1.0) The code property for the Dynamics 365 Business Central paymentMethod entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central paymentMethod entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central paymentMethod entity | [optional] 

## Example

```python
from pybusinesscentral.model.payment_method import PaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethod from a JSON string
payment_method_instance = PaymentMethod.from_json(json)
# print the JSON string representation of the object
print(PaymentMethod.to_json())

# convert the object into a dict
payment_method_dict = payment_method_instance.to_dict()
# create an instance of PaymentMethod from a dict
payment_method_from_dict = PaymentMethod.from_dict(payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


