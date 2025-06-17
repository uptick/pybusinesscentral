# PaymentTerm


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central paymentTerm entity | [optional] 
**code** | **str** | (v1.0) The code property for the Dynamics 365 Business Central paymentTerm entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central paymentTerm entity | [optional] 
**due_date_calculation** | **str** | (v1.0) The dueDateCalculation property for the Dynamics 365 Business Central paymentTerm entity | [optional] 
**discount_date_calculation** | **str** | (v1.0) The discountDateCalculation property for the Dynamics 365 Business Central paymentTerm entity | [optional] 
**discount_percent** | **float** | (v1.0) The discountPercent property for the Dynamics 365 Business Central paymentTerm entity | [optional] 
**calculate_discount_on_credit_memos** | **bool** | (v1.0) The calculateDiscountOnCreditMemos property for the Dynamics 365 Business Central paymentTerm entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central paymentTerm entity | [optional] 

## Example

```python
from pybusinesscentral.model.payment_term import PaymentTerm

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentTerm from a JSON string
payment_term_instance = PaymentTerm.from_json(json)
# print the JSON string representation of the object
print(PaymentTerm.to_json())

# convert the object into a dict
payment_term_dict = payment_term_instance.to_dict()
# create an instance of PaymentTerm from a dict
payment_term_from_dict = PaymentTerm.from_dict(payment_term_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


