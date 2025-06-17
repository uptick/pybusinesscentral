# CustomerSale


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customer_id** | **str** | (v1.0) The customerId property for the Dynamics 365 Business Central customerSale entity | [optional] 
**customer_number** | **str** | (v1.0) The customerNumber property for the Dynamics 365 Business Central customerSale entity | [optional] 
**name** | **str** | (v1.0) The name property for the Dynamics 365 Business Central customerSale entity | [optional] 
**total_sales_amount** | **float** | (v1.0) The totalSalesAmount property for the Dynamics 365 Business Central customerSale entity | [optional] 
**date_filter_filter_only** | **datetime** | (v1.0) The dateFilter_FilterOnly property for the Dynamics 365 Business Central customerSale entity | [optional] 

## Example

```python
from pybusinesscentral.model.customer_sale import CustomerSale

# TODO update the JSON string below
json = "{}"
# create an instance of CustomerSale from a JSON string
customer_sale_instance = CustomerSale.from_json(json)
# print the JSON string representation of the object
print(CustomerSale.to_json())

# convert the object into a dict
customer_sale_dict = customer_sale_instance.to_dict()
# create an instance of CustomerSale from a dict
customer_sale_from_dict = CustomerSale.from_dict(customer_sale_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


