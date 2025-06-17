# PostSalesCreditMemoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**number** | **str** | (v1.0) The number property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**external_document_number** | **str** | (v1.0) The externalDocumentNumber property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**credit_memo_date** | **datetime** | (v1.0) The creditMemoDate property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**due_date** | **datetime** | (v1.0) The dueDate property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**customer_id** | **str** | (v1.0) The customerId property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**contact_id** | **str** | (v1.0) The contactId property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**customer_number** | **str** | (v1.0) The customerNumber property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**customer_name** | **str** | (v1.0) The customerName property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**bill_to_name** | **str** | (v1.0) The billToName property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**bill_to_customer_id** | **str** | (v1.0) The billToCustomerId property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**bill_to_customer_number** | **str** | (v1.0) The billToCustomerNumber property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**selling_postal_address** | [**Postaladdresstype**](Postaladdresstype.md) |  | [optional] 
**billing_postal_address** | [**Postaladdresstype**](Postaladdresstype.md) |  | [optional] 
**currency_id** | **str** | (v1.0) The currencyId property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**currency_code** | **str** | (v1.0) The currencyCode property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**payment_terms_id** | **str** | (v1.0) The paymentTermsId property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**shipment_method_id** | **str** | (v1.0) The shipmentMethodId property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**salesperson** | **str** | (v1.0) The salesperson property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**prices_include_tax** | **bool** | (v1.0) The pricesIncludeTax property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**discount_amount** | **float** | (v1.0) The discountAmount property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**discount_applied_before_tax** | **bool** | (v1.0) The discountAppliedBeforeTax property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**total_amount_excluding_tax** | **float** | (v1.0) The totalAmountExcludingTax property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**total_tax_amount** | **float** | (v1.0) The totalTaxAmount property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**total_amount_including_tax** | **float** | (v1.0) The totalAmountIncludingTax property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**status** | **str** | (v1.0) The status property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**invoice_id** | **str** | (v1.0) The invoiceId property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**invoice_number** | **str** | (v1.0) The invoiceNumber property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**phone_number** | **str** | (v1.0) The phoneNumber property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 
**email** | **str** | (v1.0) The email property for the Dynamics 365 Business Central salesCreditMemo entity | [optional] 

## Example

```python
from pybusinesscentral.model.post_sales_credit_memo_request import PostSalesCreditMemoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSalesCreditMemoRequest from a JSON string
post_sales_credit_memo_request_instance = PostSalesCreditMemoRequest.from_json(json)
# print the JSON string representation of the object
print(PostSalesCreditMemoRequest.to_json())

# convert the object into a dict
post_sales_credit_memo_request_dict = post_sales_credit_memo_request_instance.to_dict()
# create an instance of PostSalesCreditMemoRequest from a dict
post_sales_credit_memo_request_from_dict = PostSalesCreditMemoRequest.from_dict(post_sales_credit_memo_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


