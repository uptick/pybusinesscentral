# PostJournalRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central journal entity | [optional] 
**code** | **str** | (v1.0) The code property for the Dynamics 365 Business Central journal entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central journal entity | [optional] 
**template_display_name** | **str** | (v1.0) The templateDisplayName property for the Dynamics 365 Business Central journal entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central journal entity | [optional] 
**balancing_account_id** | **str** | (v1.0) The balancingAccountId property for the Dynamics 365 Business Central journal entity | [optional] 
**balancing_account_number** | **str** | (v1.0) The balancingAccountNumber property for the Dynamics 365 Business Central journal entity | [optional] 
**journal_lines** | [**List[JournalLine]**](JournalLine.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.post_journal_request import PostJournalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostJournalRequest from a JSON string
post_journal_request_instance = PostJournalRequest.from_json(json)
# print the JSON string representation of the object
print(PostJournalRequest.to_json())

# convert the object into a dict
post_journal_request_dict = post_journal_request_instance.to_dict()
# create an instance of PostJournalRequest from a dict
post_journal_request_from_dict = PostJournalRequest.from_dict(post_journal_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


