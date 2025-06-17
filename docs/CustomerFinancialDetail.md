# CustomerFinancialDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central customerFinancialDetail entity | [optional] 
**number** | **str** | (v1.0) The number property for the Dynamics 365 Business Central customerFinancialDetail entity | [optional] 
**balance** | **float** | (v1.0) The balance property for the Dynamics 365 Business Central customerFinancialDetail entity | [optional] 
**total_sales_excluding_tax** | **float** | (v1.0) The totalSalesExcludingTax property for the Dynamics 365 Business Central customerFinancialDetail entity | [optional] 
**overdue_amount** | **float** | (v1.0) The overdueAmount property for the Dynamics 365 Business Central customerFinancialDetail entity | [optional] 

## Example

```python
from pybusinesscentral.model.customer_financial_detail import CustomerFinancialDetail

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerFinancialDetail from a JSON string
customer_financial_detail_instance = CustomerFinancialDetail.from_json(json)
# print the JSON string representation of the object
print(CustomerFinancialDetail.to_json())

# convert the object into a dict
customer_financial_detail_dict = customer_financial_detail_instance.to_dict()
# create an instance of CustomerFinancialDetail from a dict
customer_financial_detail_from_dict = CustomerFinancialDetail.from_dict(customer_financial_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


