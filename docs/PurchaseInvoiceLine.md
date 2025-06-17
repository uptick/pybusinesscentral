# PurchaseInvoiceLine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**document_id** | **str** | (v1.0) The documentId property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**sequence** | **int** | (v1.0) The sequence property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**item_id** | **str** | (v1.0) The itemId property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**account_id** | **str** | (v1.0) The accountId property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**line_type** | **str** | (v1.0) The lineType property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**line_details** | [**Documentlineobjectdetailstype**](Documentlineobjectdetailstype.md) |  | [optional] 
**description** | **str** | (v1.0) The description property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**unit_of_measure** | [**Unitofmeasuretype**](Unitofmeasuretype.md) |  | [optional] 
**unit_cost** | **float** | (v1.0) The unitCost property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**quantity** | **float** | (v1.0) The quantity property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**discount_amount** | **float** | (v1.0) The discountAmount property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**discount_percent** | **float** | (v1.0) The discountPercent property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**discount_applied_before_tax** | **bool** | (v1.0) The discountAppliedBeforeTax property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**amount_excluding_tax** | **float** | (v1.0) The amountExcludingTax property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**tax_code** | **str** | (v1.0) The taxCode property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**tax_percent** | **float** | (v1.0) The taxPercent property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**total_tax_amount** | **float** | (v1.0) The totalTaxAmount property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**amount_including_tax** | **float** | (v1.0) The amountIncludingTax property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**invoice_discount_allocation** | **float** | (v1.0) The invoiceDiscountAllocation property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**net_amount** | **float** | (v1.0) The netAmount property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**net_tax_amount** | **float** | (v1.0) The netTaxAmount property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**net_amount_including_tax** | **float** | (v1.0) The netAmountIncludingTax property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**expected_receipt_date** | **date** | (v1.0) The expectedReceiptDate property for the Dynamics 365 Business Central purchaseInvoiceLine entity | [optional] 
**item** | [**Item**](Item.md) |  | [optional] 
**account** | [**Account**](Account.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.purchase_invoice_line import PurchaseInvoiceLine

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseInvoiceLine from a JSON string
purchase_invoice_line_instance = PurchaseInvoiceLine.from_json(json)
# print the JSON string representation of the object
print(PurchaseInvoiceLine.to_json())

# convert the object into a dict
purchase_invoice_line_dict = purchase_invoice_line_instance.to_dict()
# create an instance of PurchaseInvoiceLine from a dict
purchase_invoice_line_from_dict = PurchaseInvoiceLine.from_dict(purchase_invoice_line_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


