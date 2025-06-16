# IncomeStatement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_number** | **int** | (v1.0) The lineNumber property for the Dynamics 365 Business Central incomeStatement entity | [optional] 
**display** | **str** | (v1.0) The display property for the Dynamics 365 Business Central incomeStatement entity | [optional] 
**net_change** | **float** | (v1.0) The netChange property for the Dynamics 365 Business Central incomeStatement entity | [optional] 
**line_type** | **str** | (v1.0) The lineType property for the Dynamics 365 Business Central incomeStatement entity | [optional] 
**indentation** | **int** | (v1.0) The indentation property for the Dynamics 365 Business Central incomeStatement entity | [optional] 
**date_filter** | **datetime** | (v1.0) The dateFilter property for the Dynamics 365 Business Central incomeStatement entity | [optional] 

## Example

```python
from pybusinesscentral.model.income_statement import IncomeStatement

# TODO update the JSON string below
json = "{}"
# create an instance of IncomeStatement from a JSON string
income_statement_instance = IncomeStatement.from_json(json)
# print the JSON string representation of the object
print(IncomeStatement.to_json())

# convert the object into a dict
income_statement_dict = income_statement_instance.to_dict()
# create an instance of IncomeStatement from a dict
income_statement_from_dict = IncomeStatement.from_dict(income_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


