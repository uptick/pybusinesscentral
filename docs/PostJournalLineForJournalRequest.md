# PostJournalLineForJournalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central journalLine entity | [optional] 
**journal_id** | **str** | (v1.0) The journalId property for the Dynamics 365 Business Central journalLine entity | [optional] 
**journal_display_name** | **str** | (v1.0) The journalDisplayName property for the Dynamics 365 Business Central journalLine entity | [optional] 
**line_number** | **int** | (v1.0) The lineNumber property for the Dynamics 365 Business Central journalLine entity | [optional] 
**account_type** | **str** | (v1.0) The accountType property for the Dynamics 365 Business Central journalLine entity | [optional] 
**account_id** | **str** | (v1.0) The accountId property for the Dynamics 365 Business Central journalLine entity | [optional] 
**account_number** | **str** | (v1.0) The accountNumber property for the Dynamics 365 Business Central journalLine entity | [optional] 
**posting_date** | **str** | (v1.0) The postingDate property for the Dynamics 365 Business Central journalLine entity | [optional] 
**document_number** | **str** | (v1.0) The documentNumber property for the Dynamics 365 Business Central journalLine entity | [optional] 
**external_document_number** | **str** | (v1.0) The externalDocumentNumber property for the Dynamics 365 Business Central journalLine entity | [optional] 
**amount** | **float** | (v1.0) The amount property for the Dynamics 365 Business Central journalLine entity | [optional] 
**description** | **str** | (v1.0) The description property for the Dynamics 365 Business Central journalLine entity | [optional] 
**comment** | **str** | (v1.0) The comment property for the Dynamics 365 Business Central journalLine entity | [optional] 
**tax_code** | **str** | (v1.0) The taxCode property for the Dynamics 365 Business Central journalLine entity | [optional] 
**balance_account_type** | **str** | (v1.0) The balanceAccountType property for the Dynamics 365 Business Central journalLine entity | [optional] 
**balancing_account_id** | **str** | (v1.0) The balancingAccountId property for the Dynamics 365 Business Central journalLine entity | [optional] 
**balancing_account_number** | **str** | (v1.0) The balancingAccountNumber property for the Dynamics 365 Business Central journalLine entity | [optional] 
**dimensions** | [**List[Dimensiontype]**](Dimensiontype.md) |  | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central journalLine entity | [optional] 
**dimension_set_lines** | [**List[DimensionSetLine]**](DimensionSetLine.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.post_journal_line_for_journal_request import PostJournalLineForJournalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostJournalLineForJournalRequest from a JSON string
post_journal_line_for_journal_request_instance = PostJournalLineForJournalRequest.from_json(json)
# print the JSON string representation of the object
print(PostJournalLineForJournalRequest.to_json())

# convert the object into a dict
post_journal_line_for_journal_request_dict = post_journal_line_for_journal_request_instance.to_dict()
# create an instance of PostJournalLineForJournalRequest from a dict
post_journal_line_for_journal_request_from_dict = PostJournalLineForJournalRequest.from_dict(post_journal_line_for_journal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


