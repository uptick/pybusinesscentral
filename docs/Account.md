# Account


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central account entity | [optional] 
**number** | **str** | (v1.0) The number property for the Dynamics 365 Business Central account entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central account entity | [optional] 
**category** | **str** | (v1.0) The category property for the Dynamics 365 Business Central account entity | [optional] 
**sub_category** | **str** | (v1.0) The subCategory property for the Dynamics 365 Business Central account entity | [optional] 
**blocked** | **bool** | (v1.0) The blocked property for the Dynamics 365 Business Central account entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central account entity | [optional] 

## Example

```python
from pybusinesscentral.model.account import Account

# TODO update the JSON string below
json = "{}"
# create an instance of Account from a JSON string
account_instance = Account.from_json(json)
# print the JSON string representation of the object
print(Account.to_json())

# convert the object into a dict
account_dict = account_instance.to_dict()
# create an instance of Account from a dict
account_from_dict = Account.from_dict(account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


