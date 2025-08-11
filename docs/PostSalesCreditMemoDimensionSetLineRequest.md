# PostSalesCreditMemoDimensionSetLineRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **str** | (v1.0) The parentId property for the Dynamics 365 Business Central salesCreditMemoDimensionSetLine entity | [optional] 
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central salesCreditMemoDimensionSetLine entity | [optional] 
**code** | **str** | (v1.0) The code property for the Dynamics 365 Business Central salesCreditMemoDimensionSetLine entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central salesCreditMemoDimensionSetLine entity | [optional] 
**value_id** | **str** | (v1.0) The valueId property for the Dynamics 365 Business Central salesCreditMemoDimensionSetLine entity | [optional] 
**value_code** | **str** | (v1.0) The valueCode property for the Dynamics 365 Business Central salesCreditMemoDimensionSetLine entity | [optional] 
**value_display_name** | **str** | (v1.0) The valueDisplayName property for the Dynamics 365 Business Central salesCreditMemoDimensionSetLine entity | [optional] 

## Example

```python
from pybusinesscentral.model.post_sales_credit_memo_dimension_set_line_request import PostSalesCreditMemoDimensionSetLineRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSalesCreditMemoDimensionSetLineRequest from a JSON string
post_sales_credit_memo_dimension_set_line_request_instance = PostSalesCreditMemoDimensionSetLineRequest.from_json(json)
# print the JSON string representation of the object
print(PostSalesCreditMemoDimensionSetLineRequest.to_json())

# convert the object into a dict
post_sales_credit_memo_dimension_set_line_request_dict = post_sales_credit_memo_dimension_set_line_request_instance.to_dict()
# create an instance of PostSalesCreditMemoDimensionSetLineRequest from a dict
post_sales_credit_memo_dimension_set_line_request_from_dict = PostSalesCreditMemoDimensionSetLineRequest.from_dict(post_sales_credit_memo_dimension_set_line_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


