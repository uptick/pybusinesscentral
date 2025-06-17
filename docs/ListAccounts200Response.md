# ListAccounts200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[Account]**](Account.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.list_accounts200_response import ListAccounts200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListAccounts200Response from a JSON string
list_accounts200_response_instance = ListAccounts200Response.from_json(json)
# print the JSON string representation of the object
print(ListAccounts200Response.to_json())

# convert the object into a dict
list_accounts200_response_dict = list_accounts200_response_instance.to_dict()
# create an instance of ListAccounts200Response from a dict
list_accounts200_response_from_dict = ListAccounts200Response.from_dict(list_accounts200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


