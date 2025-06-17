# CountryRegion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central countryRegion entity | [optional] 
**code** | **str** | (v1.0) The code property for the Dynamics 365 Business Central countryRegion entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central countryRegion entity | [optional] 
**address_format** | **str** | (v1.0) The addressFormat property for the Dynamics 365 Business Central countryRegion entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central countryRegion entity | [optional] 

## Example

```python
from pybusinesscentral.model.country_region import CountryRegion

# TODO update the JSON string below
json = "{}"
# create an instance of CountryRegion from a JSON string
country_region_instance = CountryRegion.from_json(json)
# print the JSON string representation of the object
print(CountryRegion.to_json())

# convert the object into a dict
country_region_dict = country_region_instance.to_dict()
# create an instance of CountryRegion from a dict
country_region_from_dict = CountryRegion.from_dict(country_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


