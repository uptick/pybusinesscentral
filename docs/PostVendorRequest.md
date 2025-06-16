# PostVendorRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central vendor entity | [optional] 
**number** | **str** | (v1.0) The number property for the Dynamics 365 Business Central vendor entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central vendor entity | [optional] 
**address_line1** | **str** | (v1.0) The street property for the Dynamics 365 Business Central postaladdresstype entity | [optional] 
**address_line2** | **str** | (v1.0) The street property for the Dynamics 365 Business Central postaladdresstype entity | [optional] 
**city** | **str** | (v1.0) The city property for the Dynamics 365 Business Central postaladdresstype entity | [optional] 
**state** | **str** | (v1.0) The state property for the Dynamics 365 Business Central postaladdresstype entity | [optional] 
**country** | **str** | (v1.0) The countryLetterCode property for the Dynamics 365 Business Central postaladdresstype entity | [optional] 
**postal_code** | **str** | (v1.0) The postalCode property for the Dynamics 365 Business Central postaladdresstype entity | [optional] 
**phone_number** | **str** | (v1.0) The phoneNumber property for the Dynamics 365 Business Central vendor entity | [optional] 
**email** | **str** | (v1.0) The email property for the Dynamics 365 Business Central vendor entity | [optional] 
**website** | **str** | (v1.0) The website property for the Dynamics 365 Business Central vendor entity | [optional] 
**tax_registration_number** | **str** | (v1.0) The taxRegistrationNumber property for the Dynamics 365 Business Central vendor entity | [optional] 
**currency_id** | **str** | (v1.0) The currencyId property for the Dynamics 365 Business Central vendor entity | [optional] 
**currency_code** | **str** | (v1.0) The currencyCode property for the Dynamics 365 Business Central vendor entity | [optional] 
**irs1099_code** | **str** | (v1.0) The irs1099Code property for the Dynamics 365 Business Central vendor entity | [optional] 
**payment_terms_id** | **str** | (v1.0) The paymentTermsId property for the Dynamics 365 Business Central vendor entity | [optional] 
**payment_method_id** | **str** | (v1.0) The paymentMethodId property for the Dynamics 365 Business Central vendor entity | [optional] 
**tax_liable** | **bool** | (v1.0) The taxLiable property for the Dynamics 365 Business Central vendor entity | [optional] 
**blocked** | **str** | (v1.0) The blocked property for the Dynamics 365 Business Central vendor entity | [optional] 
**balance** | **float** | (v1.0) The balance property for the Dynamics 365 Business Central vendor entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central vendor entity | [optional] 

## Example

```python
from pybusinesscentral.model.post_vendor_request import PostVendorRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostVendorRequest from a JSON string
post_vendor_request_instance = PostVendorRequest.from_json(json)
# print the JSON string representation of the object
print(PostVendorRequest.to_json())

# convert the object into a dict
post_vendor_request_dict = post_vendor_request_instance.to_dict()
# create an instance of PostVendorRequest from a dict
post_vendor_request_from_dict = PostVendorRequest.from_dict(post_vendor_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


