# ListSalesCreditMemos200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SalesCreditMemo]**](SalesCreditMemo.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.list_sales_credit_memos200_response import ListSalesCreditMemos200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSalesCreditMemos200Response from a JSON string
list_sales_credit_memos200_response_instance = ListSalesCreditMemos200Response.from_json(json)
# print the JSON string representation of the object
print(ListSalesCreditMemos200Response.to_json())

# convert the object into a dict
list_sales_credit_memos200_response_dict = list_sales_credit_memos200_response_instance.to_dict()
# create an instance of ListSalesCreditMemos200Response from a dict
list_sales_credit_memos200_response_from_dict = ListSalesCreditMemos200Response.from_dict(list_sales_credit_memos200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


