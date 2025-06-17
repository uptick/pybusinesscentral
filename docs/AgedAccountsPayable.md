# AgedAccountsPayable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**vendor_id** | **str** | (v1.0) The vendorId property for the Dynamics 365 Business Central agedAccountsPayable entity | [optional] 
**vendor_number** | **str** | (v1.0) The vendorNumber property for the Dynamics 365 Business Central agedAccountsPayable entity | [optional] 
**name** | **str** | (v1.0) The name property for the Dynamics 365 Business Central agedAccountsPayable entity | [optional] 
**currency_code** | **str** | (v1.0) The currencyCode property for the Dynamics 365 Business Central agedAccountsPayable entity | [optional] 
**balance_due** | **float** | (v1.0) The balanceDue property for the Dynamics 365 Business Central agedAccountsPayable entity | [optional] 
**current_amount** | **float** | (v1.0) The currentAmount property for the Dynamics 365 Business Central agedAccountsPayable entity | [optional] 
**period1_amount** | **float** | (v1.0) The period1Amount property for the Dynamics 365 Business Central agedAccountsPayable entity | [optional] 
**period2_amount** | **float** | (v1.0) The period2Amount property for the Dynamics 365 Business Central agedAccountsPayable entity | [optional] 
**period3_amount** | **float** | (v1.0) The period3Amount property for the Dynamics 365 Business Central agedAccountsPayable entity | [optional] 
**aged_as_of_date** | **datetime** | (v1.0) The agedAsOfDate property for the Dynamics 365 Business Central agedAccountsPayable entity | [optional] 
**period_length_filter** | **str** | (v1.0) The periodLengthFilter property for the Dynamics 365 Business Central agedAccountsPayable entity | [optional] 

## Example

```python
from pybusinesscentral.model.aged_accounts_payable import AgedAccountsPayable

# TODO update the JSON string below
json = "{}"
# create an instance of AgedAccountsPayable from a JSON string
aged_accounts_payable_instance = AgedAccountsPayable.from_json(json)
# print the JSON string representation of the object
print(AgedAccountsPayable.to_json())

# convert the object into a dict
aged_accounts_payable_dict = aged_accounts_payable_instance.to_dict()
# create an instance of AgedAccountsPayable from a dict
aged_accounts_payable_from_dict = AgedAccountsPayable.from_dict(aged_accounts_payable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


