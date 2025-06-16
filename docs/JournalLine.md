# JournalLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central journalLine entity | [optional] 
**journal_display_name** | **str** | (v1.0) The journalDisplayName property for the Dynamics 365 Business Central journalLine entity | [optional] 
**line_number** | **int** | (v1.0) The lineNumber property for the Dynamics 365 Business Central journalLine entity | [optional] 
**account_type** | **str** | (v1.0) The accountType property for the Dynamics 365 Business Central journalLine entity | [optional] 
**account_id** | **str** | (v1.0) The accountId property for the Dynamics 365 Business Central journalLine entity | [optional] 
**account_number** | **str** | (v1.0) The accountNumber property for the Dynamics 365 Business Central journalLine entity | [optional] 
**posting_date** | **datetime** | (v1.0) The postingDate property for the Dynamics 365 Business Central journalLine entity | [optional] 
**document_number** | **str** | (v1.0) The documentNumber property for the Dynamics 365 Business Central journalLine entity | [optional] 
**external_document_number** | **str** | (v1.0) The externalDocumentNumber property for the Dynamics 365 Business Central journalLine entity | [optional] 
**amount** | **float** | (v1.0) The amount property for the Dynamics 365 Business Central journalLine entity | [optional] 
**description** | **str** | (v1.0) The description property for the Dynamics 365 Business Central journalLine entity | [optional] 
**comment** | **str** | (v1.0) The comment property for the Dynamics 365 Business Central journalLine entity | [optional] 
**dimensions** | [**List[GeneralLedgerEntryDimensionsInner]**](GeneralLedgerEntryDimensionsInner.md) |  | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central journalLine entity | [optional] 
**attachments** | [**List[Attachments]**](Attachments.md) |  | [optional] 
**account** | [**Account**](Account.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.journal_line import JournalLine

# TODO update the JSON string below
json = "{}"
# create an instance of JournalLine from a JSON string
journal_line_instance = JournalLine.from_json(json)
# print the JSON string representation of the object
print(JournalLine.to_json())

# convert the object into a dict
journal_line_dict = journal_line_instance.to_dict()
# create an instance of JournalLine from a dict
journal_line_from_dict = JournalLine.from_dict(journal_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


