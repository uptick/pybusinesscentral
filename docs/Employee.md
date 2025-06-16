# Employee


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central employee entity | [optional] 
**number** | **str** | (v1.0) The number property for the Dynamics 365 Business Central employee entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central employee entity | [optional] 
**given_name** | **str** | (v1.0) The givenName property for the Dynamics 365 Business Central employee entity | [optional] 
**middle_name** | **str** | (v1.0) The middleName property for the Dynamics 365 Business Central employee entity | [optional] 
**surname** | **str** | (v1.0) The surname property for the Dynamics 365 Business Central employee entity | [optional] 
**job_title** | **str** | (v1.0) The jobTitle property for the Dynamics 365 Business Central employee entity | [optional] 
**address** | [**Postaladdresstype**](Postaladdresstype.md) |  | [optional] 
**phone_number** | **str** | (v1.0) The phoneNumber property for the Dynamics 365 Business Central employee entity | [optional] 
**mobile_phone** | **str** | (v1.0) The mobilePhone property for the Dynamics 365 Business Central employee entity | [optional] 
**email** | **str** | (v1.0) The email property for the Dynamics 365 Business Central employee entity | [optional] 
**personal_email** | **str** | (v1.0) The personalEmail property for the Dynamics 365 Business Central employee entity | [optional] 
**employment_date** | **datetime** | (v1.0) The employmentDate property for the Dynamics 365 Business Central employee entity | [optional] 
**termination_date** | **datetime** | (v1.0) The terminationDate property for the Dynamics 365 Business Central employee entity | [optional] 
**status** | **str** | (v1.0) The status property for the Dynamics 365 Business Central employee entity | [optional] 
**birth_date** | **datetime** | (v1.0) The birthDate property for the Dynamics 365 Business Central employee entity | [optional] 
**statistics_group_code** | **str** | (v1.0) The statisticsGroupCode property for the Dynamics 365 Business Central employee entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central employee entity | [optional] 
**picture** | [**List[Picture]**](Picture.md) |  | [optional] 
**default_dimensions** | [**List[DefaultDimensions]**](DefaultDimensions.md) |  | [optional] 
**time_registration_entries** | [**List[TimeRegistrationEntry]**](TimeRegistrationEntry.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.employee import Employee

# TODO update the JSON string below
json = "{}"
# create an instance of Employee from a JSON string
employee_instance = Employee.from_json(json)
# print the JSON string representation of the object
print(Employee.to_json())

# convert the object into a dict
employee_dict = employee_instance.to_dict()
# create an instance of Employee from a dict
employee_from_dict = Employee.from_dict(employee_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


