# ListPurchaseInvoices200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**List[PurchaseInvoice]**](PurchaseInvoice.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.list_purchase_invoices200_response import ListPurchaseInvoices200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ListPurchaseInvoices200Response from a JSON string
list_purchase_invoices200_response_instance = ListPurchaseInvoices200Response.from_json(json)
# print the JSON string representation of the object
print(ListPurchaseInvoices200Response.to_json())

# convert the object into a dict
list_purchase_invoices200_response_dict = list_purchase_invoices200_response_instance.to_dict()
# create an instance of ListPurchaseInvoices200Response from a dict
list_purchase_invoices200_response_from_dict = ListPurchaseInvoices200Response.from_dict(list_purchase_invoices200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


