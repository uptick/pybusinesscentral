# CustomerPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central customerPayment entity | [optional] 
**journal_display_name** | **str** | (v1.0) The journalDisplayName property for the Dynamics 365 Business Central customerPayment entity | [optional] 
**line_number** | **int** | (v1.0) The lineNumber property for the Dynamics 365 Business Central customerPayment entity | [optional] 
**customer_id** | **str** | (v1.0) The customerId property for the Dynamics 365 Business Central customerPayment entity | [optional] 
**customer_number** | **str** | (v1.0) The customerNumber property for the Dynamics 365 Business Central customerPayment entity | [optional] 
**contact_id** | **str** | (v1.0) The contactId property for the Dynamics 365 Business Central customerPayment entity | [optional] 
**posting_date** | **datetime** | (v1.0) The postingDate property for the Dynamics 365 Business Central customerPayment entity | [optional] 
**document_number** | **str** | (v1.0) The documentNumber property for the Dynamics 365 Business Central customerPayment entity | [optional] 
**external_document_number** | **str** | (v1.0) The externalDocumentNumber property for the Dynamics 365 Business Central customerPayment entity | [optional] 
**amount** | **float** | (v1.0) The amount property for the Dynamics 365 Business Central customerPayment entity | [optional] 
**applies_to_invoice_id** | **str** | (v1.0) The appliesToInvoiceId property for the Dynamics 365 Business Central customerPayment entity | [optional] 
**applies_to_invoice_number** | **str** | (v1.0) The appliesToInvoiceNumber property for the Dynamics 365 Business Central customerPayment entity | [optional] 
**description** | **str** | (v1.0) The description property for the Dynamics 365 Business Central customerPayment entity | [optional] 
**comment** | **str** | (v1.0) The comment property for the Dynamics 365 Business Central customerPayment entity | [optional] 
**dimensions** | [**List[GeneralLedgerEntryDimensionsInner]**](GeneralLedgerEntryDimensionsInner.md) |  | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central customerPayment entity | [optional] 
**customer** | [**Customer**](Customer.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.customer_payment import CustomerPayment

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerPayment from a JSON string
customer_payment_instance = CustomerPayment.from_json(json)
# print the JSON string representation of the object
print(CustomerPayment.to_json())

# convert the object into a dict
customer_payment_dict = customer_payment_instance.to_dict()
# create an instance of CustomerPayment from a dict
customer_payment_from_dict = CustomerPayment.from_dict(customer_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


