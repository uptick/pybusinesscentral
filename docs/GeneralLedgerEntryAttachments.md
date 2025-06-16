# GeneralLedgerEntryAttachments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**general_ledger_entry_number** | **int** | (v1.0) The generalLedgerEntryNumber property for the Dynamics 365 Business Central generalLedgerEntryAttachments entity | [optional] 
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central generalLedgerEntryAttachments entity | [optional] 
**file_name** | **str** | (v1.0) The fileName property for the Dynamics 365 Business Central generalLedgerEntryAttachments entity | [optional] 
**byte_size** | **int** | (v1.0) The byteSize property for the Dynamics 365 Business Central generalLedgerEntryAttachments entity | [optional] 
**content** | **bytearray** | (v1.0) The content property for the Dynamics 365 Business Central generalLedgerEntryAttachments entity | [optional] 
**created_date_time** | **datetime** | (v1.0) The createdDateTime property for the Dynamics 365 Business Central generalLedgerEntryAttachments entity | [optional] 
**general_ledger_entry** | [**GeneralLedgerEntry**](GeneralLedgerEntry.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.general_ledger_entry_attachments import GeneralLedgerEntryAttachments

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralLedgerEntryAttachments from a JSON string
general_ledger_entry_attachments_instance = GeneralLedgerEntryAttachments.from_json(json)
# print the JSON string representation of the object
print(GeneralLedgerEntryAttachments.to_json())

# convert the object into a dict
general_ledger_entry_attachments_dict = general_ledger_entry_attachments_instance.to_dict()
# create an instance of GeneralLedgerEntryAttachments from a dict
general_ledger_entry_attachments_from_dict = GeneralLedgerEntryAttachments.from_dict(general_ledger_entry_attachments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


