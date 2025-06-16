# Company


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central company entity | [optional] 
**system_version** | **str** | (v1.0) The systemVersion property for the Dynamics 365 Business Central company entity | [optional] 
**name** | **str** | (v1.0) The name property for the Dynamics 365 Business Central company entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central company entity | [optional] 
**business_profile_id** | **str** | (v1.0) The businessProfileId property for the Dynamics 365 Business Central company entity | [optional] 
**items** | [**List[Item]**](Item.md) |  | [optional] 
**picture** | [**List[Picture]**](Picture.md) |  | [optional] 
**default_dimensions** | [**List[DefaultDimensions]**](DefaultDimensions.md) |  | [optional] 
**customers** | [**List[Customer]**](Customer.md) |  | [optional] 
**customer_financial_details** | [**List[CustomerFinancialDetail]**](CustomerFinancialDetail.md) |  | [optional] 
**vendors** | [**List[Vendor]**](Vendor.md) |  | [optional] 
**company_information** | [**List[CompanyInformation]**](CompanyInformation.md) |  | [optional] 
**sales_invoices** | [**List[SalesInvoice]**](SalesInvoice.md) |  | [optional] 
**sales_invoice_lines** | [**List[SalesInvoiceLine]**](SalesInvoiceLine.md) |  | [optional] 
**pdf_document** | [**List[PdfDocument]**](PdfDocument.md) |  | [optional] 
**customer_payment_journals** | [**List[CustomerPaymentJournal]**](CustomerPaymentJournal.md) |  | [optional] 
**customer_payments** | [**List[CustomerPayment]**](CustomerPayment.md) |  | [optional] 
**accounts** | [**List[Account]**](Account.md) |  | [optional] 
**tax_groups** | [**List[TaxGroup]**](TaxGroup.md) |  | [optional] 
**journals** | [**List[Journal]**](Journal.md) |  | [optional] 
**journal_lines** | [**List[JournalLine]**](JournalLine.md) |  | [optional] 
**attachments** | [**List[Attachments]**](Attachments.md) |  | [optional] 
**employees** | [**List[Employee]**](Employee.md) |  | [optional] 
**time_registration_entries** | [**List[TimeRegistrationEntry]**](TimeRegistrationEntry.md) |  | [optional] 
**general_ledger_entries** | [**List[GeneralLedgerEntry]**](GeneralLedgerEntry.md) |  | [optional] 
**currencies** | [**List[Currency]**](Currency.md) |  | [optional] 
**payment_methods** | [**List[PaymentMethod]**](PaymentMethod.md) |  | [optional] 
**dimensions** | [**List[Dimension]**](Dimension.md) |  | [optional] 
**dimension_values** | [**List[DimensionValue]**](DimensionValue.md) |  | [optional] 
**dimension_lines** | [**List[DimensionLine]**](DimensionLine.md) |  | [optional] 
**payment_terms** | [**List[PaymentTerm]**](PaymentTerm.md) |  | [optional] 
**shipment_methods** | [**List[ShipmentMethod]**](ShipmentMethod.md) |  | [optional] 
**item_categories** | [**List[ItemCategory]**](ItemCategory.md) |  | [optional] 
**cash_flow_statement** | [**List[CashFlowStatement]**](CashFlowStatement.md) |  | [optional] 
**countries_regions** | [**List[CountryRegion]**](CountryRegion.md) |  | [optional] 
**sales_orders** | [**List[SalesOrder]**](SalesOrder.md) |  | [optional] 
**sales_order_lines** | [**List[SalesOrderLine]**](SalesOrderLine.md) |  | [optional] 
**retained_earnings_statement** | [**List[RetainedEarningsStatement]**](RetainedEarningsStatement.md) |  | [optional] 
**units_of_measure** | [**List[UnitOfMeasure]**](UnitOfMeasure.md) |  | [optional] 
**aged_accounts_receivable** | [**List[AgedAccountsReceivable]**](AgedAccountsReceivable.md) |  | [optional] 
**aged_accounts_payable** | [**List[AgedAccountsPayable]**](AgedAccountsPayable.md) |  | [optional] 
**balance_sheet** | [**List[BalanceSheet]**](BalanceSheet.md) |  | [optional] 
**trial_balance** | [**List[TrialBalance]**](TrialBalance.md) |  | [optional] 
**income_statement** | [**List[IncomeStatement]**](IncomeStatement.md) |  | [optional] 
**tax_areas** | [**List[TaxArea]**](TaxArea.md) |  | [optional] 
**sales_quotes** | [**List[SalesQuote]**](SalesQuote.md) |  | [optional] 
**sales_quote_lines** | [**List[SalesQuoteLine]**](SalesQuoteLine.md) |  | [optional] 
**sales_credit_memos** | [**List[SalesCreditMemo]**](SalesCreditMemo.md) |  | [optional] 
**sales_credit_memo_lines** | [**List[SalesCreditMemoLine]**](SalesCreditMemoLine.md) |  | [optional] 
**general_ledger_entry_attachments** | [**List[GeneralLedgerEntryAttachments]**](GeneralLedgerEntryAttachments.md) |  | [optional] 
**purchase_invoices** | [**List[PurchaseInvoice]**](PurchaseInvoice.md) |  | [optional] 
**purchase_invoice_lines** | [**List[PurchaseInvoiceLine]**](PurchaseInvoiceLine.md) |  | [optional] 
**projects** | [**List[Project]**](Project.md) |  | [optional] 
**bank_accounts** | [**List[BankAccount]**](BankAccount.md) |  | [optional] 
**customer_sales** | [**List[CustomerSale]**](CustomerSale.md) |  | [optional] 
**vendor_purchases** | [**List[VendorPurchase]**](VendorPurchase.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.company import Company

# TODO update the JSON string below
json = "{}"
# create an instance of Company from a JSON string
company_instance = Company.from_json(json)
# print the JSON string representation of the object
print(Company.to_json())

# convert the object into a dict
company_dict = company_instance.to_dict()
# create an instance of Company from a dict
company_from_dict = Company.from_dict(company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


