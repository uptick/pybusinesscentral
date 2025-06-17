# ListCompanies200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[Company]**](Company.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.list_companies200_response import ListCompanies200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListCompanies200Response from a JSON string
list_companies200_response_instance = ListCompanies200Response.from_json(json)
# print the JSON string representation of the object
print(ListCompanies200Response.to_json())

# convert the object into a dict
list_companies200_response_dict = list_companies200_response_instance.to_dict()
# create an instance of ListCompanies200Response from a dict
list_companies200_response_from_dict = ListCompanies200Response.from_dict(list_companies200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


