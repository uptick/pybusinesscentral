# PostPurchaseInvoiceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**number** | **str** | (v1.0) The number property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**invoice_date** | **datetime** | (v1.0) The invoiceDate property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**due_date** | **datetime** | (v1.0) The dueDate property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**vendor_invoice_number** | **str** | (v1.0) The vendorInvoiceNumber property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**vendor_id** | **str** | (v1.0) The vendorId property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**vendor_number** | **str** | (v1.0) The vendorNumber property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**vendor_name** | **str** | (v1.0) The vendorName property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**pay_to_name** | **str** | (v1.0) The payToName property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**pay_to_contact** | **str** | (v1.0) The payToContact property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**pay_to_vendor_id** | **str** | (v1.0) The payToVendorId property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**pay_to_vendor_number** | **str** | (v1.0) The payToVendorNumber property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**ship_to_name** | **str** | (v1.0) The shipToName property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**ship_to_contact** | **str** | (v1.0) The shipToContact property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**buy_from_address** | [**Postaladdresstype**](Postaladdresstype.md) |  | [optional] 
**pay_to_address** | [**Postaladdresstype**](Postaladdresstype.md) |  | [optional] 
**ship_to_address** | [**Postaladdresstype**](Postaladdresstype.md) |  | [optional] 
**currency_id** | **str** | (v1.0) The currencyId property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**currency_code** | **str** | (v1.0) The currencyCode property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**prices_include_tax** | **bool** | (v1.0) The pricesIncludeTax property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**discount_amount** | **float** | (v1.0) The discountAmount property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**discount_applied_before_tax** | **bool** | (v1.0) The discountAppliedBeforeTax property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**total_amount_excluding_tax** | **float** | (v1.0) The totalAmountExcludingTax property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**total_tax_amount** | **float** | (v1.0) The totalTaxAmount property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**total_amount_including_tax** | **float** | (v1.0) The totalAmountIncludingTax property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**status** | **str** | (v1.0) The status property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central purchaseInvoice entity | [optional] 

## Example

```python
from pybusinesscentral.model.post_purchase_invoice_request import PostPurchaseInvoiceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostPurchaseInvoiceRequest from a JSON string
post_purchase_invoice_request_instance = PostPurchaseInvoiceRequest.from_json(json)
# print the JSON string representation of the object
print(PostPurchaseInvoiceRequest.to_json())

# convert the object into a dict
post_purchase_invoice_request_dict = post_purchase_invoice_request_instance.to_dict()
# create an instance of PostPurchaseInvoiceRequest from a dict
post_purchase_invoice_request_from_dict = PostPurchaseInvoiceRequest.from_dict(post_purchase_invoice_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


