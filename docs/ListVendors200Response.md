# ListVendors200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[Vendor]**](Vendor.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.list_vendors200_response import ListVendors200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListVendors200Response from a JSON string
list_vendors200_response_instance = ListVendors200Response.from_json(json)
# print the JSON string representation of the object
print(ListVendors200Response.to_json())

# convert the object into a dict
list_vendors200_response_dict = list_vendors200_response_instance.to_dict()
# create an instance of ListVendors200Response from a dict
list_vendors200_response_from_dict = ListVendors200Response.from_dict(list_vendors200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


