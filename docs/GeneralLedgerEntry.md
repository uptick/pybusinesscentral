# GeneralLedgerEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | (v1.0) The id property for the Dynamics 365 Business Central generalLedgerEntry entity | [optional] 
**posting_date** | **datetime** | (v1.0) The postingDate property for the Dynamics 365 Business Central generalLedgerEntry entity | [optional] 
**document_number** | **str** | (v1.0) The documentNumber property for the Dynamics 365 Business Central generalLedgerEntry entity | [optional] 
**document_type** | **str** | (v1.0) The documentType property for the Dynamics 365 Business Central generalLedgerEntry entity | [optional] 
**account_id** | **str** | (v1.0) The accountId property for the Dynamics 365 Business Central generalLedgerEntry entity | [optional] 
**account_number** | **str** | (v1.0) The accountNumber property for the Dynamics 365 Business Central generalLedgerEntry entity | [optional] 
**description** | **str** | (v1.0) The description property for the Dynamics 365 Business Central generalLedgerEntry entity | [optional] 
**debit_amount** | **float** | (v1.0) The debitAmount property for the Dynamics 365 Business Central generalLedgerEntry entity | [optional] 
**credit_amount** | **float** | (v1.0) The creditAmount property for the Dynamics 365 Business Central generalLedgerEntry entity | [optional] 
**dimensions** | [**List[GeneralLedgerEntryDimensionsInner]**](GeneralLedgerEntryDimensionsInner.md) |  | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central generalLedgerEntry entity | [optional] 
**account** | [**Account**](Account.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.general_ledger_entry import GeneralLedgerEntry

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralLedgerEntry from a JSON string
general_ledger_entry_instance = GeneralLedgerEntry.from_json(json)
# print the JSON string representation of the object
print(GeneralLedgerEntry.to_json())

# convert the object into a dict
general_ledger_entry_dict = general_ledger_entry_instance.to_dict()
# create an instance of GeneralLedgerEntry from a dict
general_ledger_entry_from_dict = GeneralLedgerEntry.from_dict(general_ledger_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


