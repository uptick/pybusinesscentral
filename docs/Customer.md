# Customer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central customer entity | [optional] 
**number** | **str** | (v1.0) The number property for the Dynamics 365 Business Central customer entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central customer entity | [optional] 
**type** | **str** | (v1.0) The type property for the Dynamics 365 Business Central customer entity | [optional] 
**address_line1** | **str** | (v1.0) The street property for the Dynamics 365 Business Central postaladdresstype entity | [optional] 
**address_line2** | **str** | (v1.0) The street property for the Dynamics 365 Business Central postaladdresstype entity | [optional] 
**city** | **str** | (v1.0) The city property for the Dynamics 365 Business Central postaladdresstype entity | [optional] 
**state** | **str** | (v1.0) The state property for the Dynamics 365 Business Central postaladdresstype entity | [optional] 
**country** | **str** | (v1.0) The countryLetterCode property for the Dynamics 365 Business Central postaladdresstype entity | [optional] 
**postal_code** | **str** | (v1.0) The postalCode property for the Dynamics 365 Business Central postaladdresstype entity | [optional] 
**phone_number** | **str** | (v1.0) The phoneNumber property for the Dynamics 365 Business Central customer entity | [optional] 
**email** | **str** | (v1.0) The email property for the Dynamics 365 Business Central customer entity | [optional] 
**website** | **str** | (v1.0) The website property for the Dynamics 365 Business Central customer entity | [optional] 
**tax_liable** | **bool** | (v1.0) The taxLiable property for the Dynamics 365 Business Central customer entity | [optional] 
**tax_area_id** | **str** | (v1.0) The taxAreaId property for the Dynamics 365 Business Central customer entity | [optional] 
**tax_area_display_name** | **str** | (v1.0) The taxAreaDisplayName property for the Dynamics 365 Business Central customer entity | [optional] 
**tax_registration_number** | **str** | (v1.0) The taxRegistrationNumber property for the Dynamics 365 Business Central customer entity | [optional] 
**currency_id** | **str** | (v1.0) The currencyId property for the Dynamics 365 Business Central customer entity | [optional] 
**currency_code** | **str** | (v1.0) The currencyCode property for the Dynamics 365 Business Central customer entity | [optional] 
**payment_terms_id** | **str** | (v1.0) The paymentTermsId property for the Dynamics 365 Business Central customer entity | [optional] 
**shipment_method_id** | **str** | (v1.0) The shipmentMethodId property for the Dynamics 365 Business Central customer entity | [optional] 
**payment_method_id** | **str** | (v1.0) The paymentMethodId property for the Dynamics 365 Business Central customer entity | [optional] 
**blocked** | **str** | (v1.0) The blocked property for the Dynamics 365 Business Central customer entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central customer entity | [optional] 
**customer_financial_details** | [**List[CustomerFinancialDetail]**](CustomerFinancialDetail.md) |  | [optional] 
**picture** | [**List[Picture]**](Picture.md) |  | [optional] 
**default_dimensions** | [**List[DefaultDimensions]**](DefaultDimensions.md) |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**payment_term** | [**PaymentTerm**](PaymentTerm.md) |  | [optional] 
**shipment_method** | [**ShipmentMethod**](ShipmentMethod.md) |  | [optional] 
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.customer import Customer

# TODO update the JSON string below
json = "{}"
# create an instance of Customer from a JSON string
customer_instance = Customer.from_json(json)
# print the JSON string representation of the object
print(Customer.to_json())

# convert the object into a dict
customer_dict = customer_instance.to_dict()
# create an instance of Customer from a dict
customer_from_dict = Customer.from_dict(customer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


