# AgedAccountsReceivable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | (v1.0) The customerId property for the Dynamics 365 Business Central agedAccountsReceivable entity | [optional] 
**customer_number** | **str** | (v1.0) The customerNumber property for the Dynamics 365 Business Central agedAccountsReceivable entity | [optional] 
**name** | **str** | (v1.0) The name property for the Dynamics 365 Business Central agedAccountsReceivable entity | [optional] 
**currency_code** | **str** | (v1.0) The currencyCode property for the Dynamics 365 Business Central agedAccountsReceivable entity | [optional] 
**balance_due** | **float** | (v1.0) The balanceDue property for the Dynamics 365 Business Central agedAccountsReceivable entity | [optional] 
**current_amount** | **float** | (v1.0) The currentAmount property for the Dynamics 365 Business Central agedAccountsReceivable entity | [optional] 
**period1_amount** | **float** | (v1.0) The period1Amount property for the Dynamics 365 Business Central agedAccountsReceivable entity | [optional] 
**period2_amount** | **float** | (v1.0) The period2Amount property for the Dynamics 365 Business Central agedAccountsReceivable entity | [optional] 
**period3_amount** | **float** | (v1.0) The period3Amount property for the Dynamics 365 Business Central agedAccountsReceivable entity | [optional] 
**aged_as_of_date** | **datetime** | (v1.0) The agedAsOfDate property for the Dynamics 365 Business Central agedAccountsReceivable entity | [optional] 
**period_length_filter** | **str** | (v1.0) The periodLengthFilter property for the Dynamics 365 Business Central agedAccountsReceivable entity | [optional] 

## Example

```python
from pybusinesscentral.model.aged_accounts_receivable import AgedAccountsReceivable

# TODO update the JSON string below
json = "{}"
# create an instance of AgedAccountsReceivable from a JSON string
aged_accounts_receivable_instance = AgedAccountsReceivable.from_json(json)
# print the JSON string representation of the object
print(AgedAccountsReceivable.to_json())

# convert the object into a dict
aged_accounts_receivable_dict = aged_accounts_receivable_instance.to_dict()
# create an instance of AgedAccountsReceivable from a dict
aged_accounts_receivable_from_dict = AgedAccountsReceivable.from_dict(aged_accounts_receivable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


