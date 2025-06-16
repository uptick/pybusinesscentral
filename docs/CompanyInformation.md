# CompanyInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central companyInformation entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central companyInformation entity | [optional] 
**address** | [**Postaladdresstype**](Postaladdresstype.md) |  | [optional] 
**phone_number** | **str** | (v1.0) The phoneNumber property for the Dynamics 365 Business Central companyInformation entity | [optional] 
**fax_number** | **str** | (v1.0) The faxNumber property for the Dynamics 365 Business Central companyInformation entity | [optional] 
**email** | **str** | (v1.0) The email property for the Dynamics 365 Business Central companyInformation entity | [optional] 
**website** | **str** | (v1.0) The website property for the Dynamics 365 Business Central companyInformation entity | [optional] 
**tax_registration_number** | **str** | (v1.0) The taxRegistrationNumber property for the Dynamics 365 Business Central companyInformation entity | [optional] 
**currency_code** | **str** | (v1.0) The currencyCode property for the Dynamics 365 Business Central companyInformation entity | [optional] 
**current_fiscal_year_start_date** | **datetime** | (v1.0) The currentFiscalYearStartDate property for the Dynamics 365 Business Central companyInformation entity | [optional] 
**industry** | **str** | (v1.0) The industry property for the Dynamics 365 Business Central companyInformation entity | [optional] 
**picture** | **bytearray** | (v1.0) The picture property for the Dynamics 365 Business Central companyInformation entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central companyInformation entity | [optional] 

## Example

```python
from pybusinesscentral.model.company_information import CompanyInformation

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyInformation from a JSON string
company_information_instance = CompanyInformation.from_json(json)
# print the JSON string representation of the object
print(CompanyInformation.to_json())

# convert the object into a dict
company_information_dict = company_information_instance.to_dict()
# create an instance of CompanyInformation from a dict
company_information_from_dict = CompanyInformation.from_dict(company_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


