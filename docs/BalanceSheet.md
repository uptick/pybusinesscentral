# BalanceSheet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_number** | **int** | (v1.0) The lineNumber property for the Dynamics 365 Business Central balanceSheet entity | [optional] 
**display** | **str** | (v1.0) The display property for the Dynamics 365 Business Central balanceSheet entity | [optional] 
**balance** | **float** | (v1.0) The balance property for the Dynamics 365 Business Central balanceSheet entity | [optional] 
**line_type** | **str** | (v1.0) The lineType property for the Dynamics 365 Business Central balanceSheet entity | [optional] 
**indentation** | **int** | (v1.0) The indentation property for the Dynamics 365 Business Central balanceSheet entity | [optional] 
**date_filter** | **datetime** | (v1.0) The dateFilter property for the Dynamics 365 Business Central balanceSheet entity | [optional] 

## Example

```python
from pybusinesscentral.model.balance_sheet import BalanceSheet

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceSheet from a JSON string
balance_sheet_instance = BalanceSheet.from_json(json)
# print the JSON string representation of the object
print(BalanceSheet.to_json())

# convert the object into a dict
balance_sheet_dict = balance_sheet_instance.to_dict()
# create an instance of BalanceSheet from a dict
balance_sheet_from_dict = BalanceSheet.from_dict(balance_sheet_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


