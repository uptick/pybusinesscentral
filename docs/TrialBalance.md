# TrialBalance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | (v1.0) The number property for the Dynamics 365 Business Central trialBalance entity | [optional] 
**account_id** | **str** | (v1.0) The accountId property for the Dynamics 365 Business Central trialBalance entity | [optional] 
**account_type** | **str** | (v1.0) The accountType property for the Dynamics 365 Business Central trialBalance entity | [optional] 
**display** | **str** | (v1.0) The display property for the Dynamics 365 Business Central trialBalance entity | [optional] 
**total_debit** | **str** | (v1.0) The totalDebit property for the Dynamics 365 Business Central trialBalance entity | [optional] 
**total_credit** | **str** | (v1.0) The totalCredit property for the Dynamics 365 Business Central trialBalance entity | [optional] 
**balance_at_date_debit** | **str** | (v1.0) The balanceAtDateDebit property for the Dynamics 365 Business Central trialBalance entity | [optional] 
**balance_at_date_credit** | **str** | (v1.0) The balanceAtDateCredit property for the Dynamics 365 Business Central trialBalance entity | [optional] 
**date_filter** | **datetime** | (v1.0) The dateFilter property for the Dynamics 365 Business Central trialBalance entity | [optional] 
**account** | [**Account**](Account.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.trial_balance import TrialBalance

# TODO update the JSON string below
json = "{}"
# create an instance of TrialBalance from a JSON string
trial_balance_instance = TrialBalance.from_json(json)
# print the JSON string representation of the object
print(TrialBalance.to_json())

# convert the object into a dict
trial_balance_dict = trial_balance_instance.to_dict()
# create an instance of TrialBalance from a dict
trial_balance_from_dict = TrialBalance.from_dict(trial_balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


