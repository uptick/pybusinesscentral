# SalesOrder


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**number** | **str, none_type** | (v1.0) The number property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**external_document_number** | **str, none_type** | (v1.0) The externalDocumentNumber property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**order_date** | **datetime, none_type** | (v1.0) The orderDate property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**customer_id** | **str, none_type** | (v1.0) The customerId property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**contact_id** | **str, none_type** | (v1.0) The contactId property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**customer_number** | **str, none_type** | (v1.0) The customerNumber property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**customer_name** | **str, none_type** | (v1.0) The customerName property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**bill_to_name** | **str, none_type** | (v1.0) The billToName property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**bill_to_customer_id** | **str, none_type** | (v1.0) The billToCustomerId property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**bill_to_customer_number** | **str, none_type** | (v1.0) The billToCustomerNumber property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**ship_to_name** | **str, none_type** | (v1.0) The shipToName property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**ship_to_contact** | **str, none_type** | (v1.0) The shipToContact property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**selling_postal_address** | **dict** |  | [optional] 
**billing_postal_address** | **dict** |  | [optional] 
**shipping_postal_address** | **dict** |  | [optional] 
**currency_id** | **str, none_type** | (v1.0) The currencyId property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**currency_code** | **str, none_type** | (v1.0) The currencyCode property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**prices_include_tax** | **bool, none_type** | (v1.0) The pricesIncludeTax property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**payment_terms_id** | **str, none_type** | (v1.0) The paymentTermsId property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**shipment_method_id** | **str, none_type** | (v1.0) The shipmentMethodId property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**salesperson** | **str, none_type** | (v1.0) The salesperson property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**partial_shipping** | **bool, none_type** | (v1.0) The partialShipping property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**requested_delivery_date** | **datetime, none_type** | (v1.0) The requestedDeliveryDate property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**discount_amount** | **float, none_type** | (v1.0) The discountAmount property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**discount_applied_before_tax** | **bool, none_type** | (v1.0) The discountAppliedBeforeTax property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**total_amount_excluding_tax** | **float, none_type** | (v1.0) The totalAmountExcludingTax property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**total_tax_amount** | **float, none_type** | (v1.0) The totalTaxAmount property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**total_amount_including_tax** | **float, none_type** | (v1.0) The totalAmountIncludingTax property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**fully_shipped** | **bool, none_type** | (v1.0) The fullyShipped property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**status** | **str, none_type** | (v1.0) The status property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**last_modified_date_time** | **datetime, none_type** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**phone_number** | **str, none_type** | (v1.0) The phoneNumber property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**email** | **str, none_type** | (v1.0) The email property for the Dynamics 365 Business Central salesOrder entity | [optional] 
**sales_order_lines** | [**[SalesOrderLine], none_type**](SalesOrderLine.md) |  | [optional] 
**customer** | **dict** |  | [optional] 
**currency** | **dict** |  | [optional] 
**payment_term** | **dict** |  | [optional] 
**shipment_method** | **dict** |  | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


