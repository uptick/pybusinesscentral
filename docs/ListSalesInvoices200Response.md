# ListSalesInvoices200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[SalesInvoice]**](SalesInvoice.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.list_sales_invoices200_response import ListSalesInvoices200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListSalesInvoices200Response from a JSON string
list_sales_invoices200_response_instance = ListSalesInvoices200Response.from_json(json)
# print the JSON string representation of the object
print(ListSalesInvoices200Response.to_json())

# convert the object into a dict
list_sales_invoices200_response_dict = list_sales_invoices200_response_instance.to_dict()
# create an instance of ListSalesInvoices200Response from a dict
list_sales_invoices200_response_from_dict = ListSalesInvoices200Response.from_dict(list_sales_invoices200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


