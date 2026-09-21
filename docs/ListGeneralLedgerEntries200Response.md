# ListGeneralLedgerEntries200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[GeneralLedgerEntry]**](GeneralLedgerEntry.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.list_general_ledger_entries200_response import ListGeneralLedgerEntries200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListGeneralLedgerEntries200Response from a JSON string
list_general_ledger_entries200_response_instance = ListGeneralLedgerEntries200Response.from_json(json)
# print the JSON string representation of the object
print(ListGeneralLedgerEntries200Response.to_json())

# convert the object into a dict
list_general_ledger_entries200_response_dict = list_general_ledger_entries200_response_instance.to_dict()
# create an instance of ListGeneralLedgerEntries200Response from a dict
list_general_ledger_entries200_response_from_dict = ListGeneralLedgerEntries200Response.from_dict(list_general_ledger_entries200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


