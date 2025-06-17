# CashFlowStatement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_number** | **int** | (v1.0) The lineNumber property for the Dynamics 365 Business Central cashFlowStatement entity | [optional] 
**display** | **str** | (v1.0) The display property for the Dynamics 365 Business Central cashFlowStatement entity | [optional] 
**net_change** | **float** | (v1.0) The netChange property for the Dynamics 365 Business Central cashFlowStatement entity | [optional] 
**line_type** | **str** | (v1.0) The lineType property for the Dynamics 365 Business Central cashFlowStatement entity | [optional] 
**indentation** | **int** | (v1.0) The indentation property for the Dynamics 365 Business Central cashFlowStatement entity | [optional] 
**date_filter** | **datetime** | (v1.0) The dateFilter property for the Dynamics 365 Business Central cashFlowStatement entity | [optional] 

## Example

```python
from pybusinesscentral.model.cash_flow_statement import CashFlowStatement

# TODO update the JSON string below
json = "{}"
# create an instance of CashFlowStatement from a JSON string
cash_flow_statement_instance = CashFlowStatement.from_json(json)
# print the JSON string representation of the object
print(CashFlowStatement.to_json())

# convert the object into a dict
cash_flow_statement_dict = cash_flow_statement_instance.to_dict()
# create an instance of CashFlowStatement from a dict
cash_flow_statement_from_dict = CashFlowStatement.from_dict(cash_flow_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


