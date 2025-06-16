# RetainedEarningsStatement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**line_number** | **int** | (v1.0) The lineNumber property for the Dynamics 365 Business Central retainedEarningsStatement entity | [optional] 
**display** | **str** | (v1.0) The display property for the Dynamics 365 Business Central retainedEarningsStatement entity | [optional] 
**net_change** | **float** | (v1.0) The netChange property for the Dynamics 365 Business Central retainedEarningsStatement entity | [optional] 
**line_type** | **str** | (v1.0) The lineType property for the Dynamics 365 Business Central retainedEarningsStatement entity | [optional] 
**indentation** | **int** | (v1.0) The indentation property for the Dynamics 365 Business Central retainedEarningsStatement entity | [optional] 
**date_filter** | **datetime** | (v1.0) The dateFilter property for the Dynamics 365 Business Central retainedEarningsStatement entity | [optional] 

## Example

```python
from pybusinesscentral.model.retained_earnings_statement import RetainedEarningsStatement

# TODO update the JSON string below
json = "{}"
# create an instance of RetainedEarningsStatement from a JSON string
retained_earnings_statement_instance = RetainedEarningsStatement.from_json(json)
# print the JSON string representation of the object
print(RetainedEarningsStatement.to_json())

# convert the object into a dict
retained_earnings_statement_dict = retained_earnings_statement_instance.to_dict()
# create an instance of RetainedEarningsStatement from a dict
retained_earnings_statement_from_dict = RetainedEarningsStatement.from_dict(retained_earnings_statement_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


