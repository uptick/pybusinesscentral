# ListJournals200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[Journal]**](Journal.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.list_journals200_response import ListJournals200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListJournals200Response from a JSON string
list_journals200_response_instance = ListJournals200Response.from_json(json)
# print the JSON string representation of the object
print(ListJournals200Response.to_json())

# convert the object into a dict
list_journals200_response_dict = list_journals200_response_instance.to_dict()
# create an instance of ListJournals200Response from a dict
list_journals200_response_from_dict = ListJournals200Response.from_dict(list_journals200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


