# ListDimensions200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[Dimension]**](Dimension.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.list_dimensions200_response import ListDimensions200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListDimensions200Response from a JSON string
list_dimensions200_response_instance = ListDimensions200Response.from_json(json)
# print the JSON string representation of the object
print(ListDimensions200Response.to_json())

# convert the object into a dict
list_dimensions200_response_dict = list_dimensions200_response_instance.to_dict()
# create an instance of ListDimensions200Response from a dict
list_dimensions200_response_from_dict = ListDimensions200Response.from_dict(list_dimensions200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


