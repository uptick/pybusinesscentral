# GeneralLedgerEntryDimensionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | (v1.0) The code property for the Dynamics 365 Business Central dimensiontype entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central dimensiontype entity | [optional] 
**value_code** | **str** | (v1.0) The valueCode property for the Dynamics 365 Business Central dimensiontype entity | [optional] 
**value_display_name** | **str** | (v1.0) The valueDisplayName property for the Dynamics 365 Business Central dimensiontype entity | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.general_ledger_entry_dimensions_inner import GeneralLedgerEntryDimensionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralLedgerEntryDimensionsInner from a JSON string
general_ledger_entry_dimensions_inner_instance = GeneralLedgerEntryDimensionsInner.from_json(json)
# print the JSON string representation of the object
print(GeneralLedgerEntryDimensionsInner.to_json())

# convert the object into a dict
general_ledger_entry_dimensions_inner_dict = general_ledger_entry_dimensions_inner_instance.to_dict()
# create an instance of GeneralLedgerEntryDimensionsInner from a dict
general_ledger_entry_dimensions_inner_from_dict = GeneralLedgerEntryDimensionsInner.from_dict(general_ledger_entry_dimensions_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


