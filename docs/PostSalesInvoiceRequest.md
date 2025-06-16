# PostSalesInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**number** | **str** | (v1.0) The number property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**external_document_number** | **str** | (v1.0) The externalDocumentNumber property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**invoice_date** | **datetime** | (v1.0) The invoiceDate property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**due_date** | **datetime** | (v1.0) The dueDate property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**customer_purchase_order_reference** | **str** | (v1.0) The customerPurchaseOrderReference property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**customer_id** | **str** | (v1.0) The customerId property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**contact_id** | **str** | (v1.0) The contactId property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**customer_number** | **str** | (v1.0) The customerNumber property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**customer_name** | **str** | (v1.0) The customerName property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**bill_to_name** | **str** | (v1.0) The billToName property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**bill_to_customer_id** | **str** | (v1.0) The billToCustomerId property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**bill_to_customer_number** | **str** | (v1.0) The billToCustomerNumber property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**ship_to_name** | **str** | (v1.0) The shipToName property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**ship_to_contact** | **str** | (v1.0) The shipToContact property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**selling_postal_address** | [**Postaladdresstype**](Postaladdresstype.md) |  | [optional] 
**billing_postal_address** | [**Postaladdresstype**](Postaladdresstype.md) |  | [optional] 
**shipping_postal_address** | [**Postaladdresstype**](Postaladdresstype.md) |  | [optional] 
**currency_id** | **str** | (v1.0) The currencyId property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**currency_code** | **str** | (v1.0) The currencyCode property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**order_id** | **str** | (v1.0) The orderId property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**order_number** | **str** | (v1.0) The orderNumber property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**payment_terms_id** | **str** | (v1.0) The paymentTermsId property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**shipment_method_id** | **str** | (v1.0) The shipmentMethodId property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**salesperson** | **str** | (v1.0) The salesperson property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**prices_include_tax** | **bool** | (v1.0) The pricesIncludeTax property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**remaining_amount** | **float** | (v1.0) The remainingAmount property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**discount_amount** | **float** | (v1.0) The discountAmount property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**discount_applied_before_tax** | **bool** | (v1.0) The discountAppliedBeforeTax property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**total_amount_excluding_tax** | **float** | (v1.0) The totalAmountExcludingTax property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**total_tax_amount** | **float** | (v1.0) The totalTaxAmount property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**total_amount_including_tax** | **float** | (v1.0) The totalAmountIncludingTax property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**status** | **str** | (v1.0) The status property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**phone_number** | **str** | (v1.0) The phoneNumber property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**email** | **str** | (v1.0) The email property for the Dynamics 365 Business Central salesInvoice entity | [optional] 

## Example

```python
from pybusinesscentral.model.post_sales_invoice_request import PostSalesInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSalesInvoiceRequest from a JSON string
post_sales_invoice_request_instance = PostSalesInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(PostSalesInvoiceRequest.to_json())

# convert the object into a dict
post_sales_invoice_request_dict = post_sales_invoice_request_instance.to_dict()
# create an instance of PostSalesInvoiceRequest from a dict
post_sales_invoice_request_from_dict = PostSalesInvoiceRequest.from_dict(post_sales_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


