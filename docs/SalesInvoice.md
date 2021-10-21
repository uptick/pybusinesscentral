# SalesInvoice


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**number** | **str, none_type** | (v1.0) The number property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**external_document_number** | **str, none_type** | (v1.0) The externalDocumentNumber property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**invoice_date** | **date, none_type** | (v1.0) The invoiceDate property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**due_date** | **date, none_type** | (v1.0) The dueDate property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**customer_purchase_order_reference** | **str, none_type** | (v1.0) The customerPurchaseOrderReference property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**customer_id** | **str, none_type** | (v1.0) The customerId property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**contact_id** | **str, none_type** | (v1.0) The contactId property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**customer_number** | **str, none_type** | (v1.0) The customerNumber property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**customer_name** | **str, none_type** | (v1.0) The customerName property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**bill_to_name** | **str, none_type** | (v1.0) The billToName property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**bill_to_customer_id** | **str, none_type** | (v1.0) The billToCustomerId property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**bill_to_customer_number** | **str, none_type** | (v1.0) The billToCustomerNumber property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**ship_to_name** | **str, none_type** | (v1.0) The shipToName property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**ship_to_contact** | **str, none_type** | (v1.0) The shipToContact property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**selling_postal_address** | **dict, none_type** |  | [optional] 
**billing_postal_address** | **dict, none_type** |  | [optional] 
**shipping_postal_address** | **dict, none_type** |  | [optional] 
**currency_id** | **str, none_type** | (v1.0) The currencyId property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**currency_code** | **str, none_type** | (v1.0) The currencyCode property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**order_id** | **str, none_type** | (v1.0) The orderId property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**order_number** | **str, none_type** | (v1.0) The orderNumber property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**payment_terms_id** | **str, none_type** | (v1.0) The paymentTermsId property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**shipment_method_id** | **str, none_type** | (v1.0) The shipmentMethodId property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**salesperson** | **str, none_type** | (v1.0) The salesperson property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**prices_include_tax** | **bool, none_type** | (v1.0) The pricesIncludeTax property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**remaining_amount** | **float, none_type** | (v1.0) The remainingAmount property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**discount_amount** | **float, none_type** | (v1.0) The discountAmount property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**discount_applied_before_tax** | **bool, none_type** | (v1.0) The discountAppliedBeforeTax property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**total_amount_excluding_tax** | **float, none_type** | (v1.0) The totalAmountExcludingTax property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**total_tax_amount** | **float, none_type** | (v1.0) The totalTaxAmount property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**total_amount_including_tax** | **float, none_type** | (v1.0) The totalAmountIncludingTax property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**status** | **str, none_type** | (v1.0) The status property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**last_modified_date_time** | **datetime, none_type** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**phone_number** | **str, none_type** | (v1.0) The phoneNumber property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**email** | **str, none_type** | (v1.0) The email property for the Dynamics 365 Business Central salesInvoice entity | [optional] 
**sales_invoice_lines** | [**[SalesInvoiceLine], none_type**](SalesInvoiceLine.md) |  | [optional] 
**pdf_document** | [**[PdfDocument], none_type**](PdfDocument.md) |  | [optional] 
**customer** | **dict, none_type** |  | [optional] 
**currency** | **dict, none_type** |  | [optional] 
**payment_term** | **dict, none_type** |  | [optional] 
**shipment_method** | **dict, none_type** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


