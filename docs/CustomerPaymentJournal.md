# CustomerPaymentJournal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central customerPaymentJournal entity | [optional] 
**code** | **str** | (v1.0) The code property for the Dynamics 365 Business Central customerPaymentJournal entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central customerPaymentJournal entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central customerPaymentJournal entity | [optional] 
**balancing_account_id** | **str** | (v1.0) The balancingAccountId property for the Dynamics 365 Business Central customerPaymentJournal entity | [optional] 
**balancing_account_number** | **str** | (v1.0) The balancingAccountNumber property for the Dynamics 365 Business Central customerPaymentJournal entity | [optional] 
**customer_payments** | [**List[CustomerPayment]**](CustomerPayment.md) |  | [optional] 
**account** | [**Account**](Account.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.customer_payment_journal import CustomerPaymentJournal

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerPaymentJournal from a JSON string
customer_payment_journal_instance = CustomerPaymentJournal.from_json(json)
# print the JSON string representation of the object
print(CustomerPaymentJournal.to_json())

# convert the object into a dict
customer_payment_journal_dict = customer_payment_journal_instance.to_dict()
# create an instance of CustomerPaymentJournal from a dict
customer_payment_journal_from_dict = CustomerPaymentJournal.from_dict(customer_payment_journal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


