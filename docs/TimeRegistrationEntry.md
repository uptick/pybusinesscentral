# TimeRegistrationEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central timeRegistrationEntry entity | [optional] 
**employee_id** | **str** | (v1.0) The employeeId property for the Dynamics 365 Business Central timeRegistrationEntry entity | [optional] 
**employee_number** | **str** | (v1.0) The employeeNumber property for the Dynamics 365 Business Central timeRegistrationEntry entity | [optional] 
**job_id** | **str** | (v1.0) The jobId property for the Dynamics 365 Business Central timeRegistrationEntry entity | [optional] 
**job_number** | **str** | (v1.0) The jobNumber property for the Dynamics 365 Business Central timeRegistrationEntry entity | [optional] 
**absence** | **str** | (v1.0) The absence property for the Dynamics 365 Business Central timeRegistrationEntry entity | [optional] 
**line_number** | **int** | (v1.0) The lineNumber property for the Dynamics 365 Business Central timeRegistrationEntry entity | [optional] 
**var_date** | **datetime** | (v1.0) The date property for the Dynamics 365 Business Central timeRegistrationEntry entity | [optional] 
**quantity** | **float** | (v1.0) The quantity property for the Dynamics 365 Business Central timeRegistrationEntry entity | [optional] 
**status** | **str** | (v1.0) The status property for the Dynamics 365 Business Central timeRegistrationEntry entity | [optional] 
**unit_of_measure_id** | **str** | (v1.0) The unitOfMeasureId property for the Dynamics 365 Business Central timeRegistrationEntry entity | [optional] 
**unit_of_measure** | [**Unitofmeasuretype**](Unitofmeasuretype.md) |  | [optional] 
**dimensions** | [**List[GeneralLedgerEntryDimensionsInner]**](GeneralLedgerEntryDimensionsInner.md) |  | [optional] 
**last_modfied_date_time** | **datetime** | (v1.0) The lastModfiedDateTime property for the Dynamics 365 Business Central timeRegistrationEntry entity | [optional] 
**project** | [**Project**](Project.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.time_registration_entry import TimeRegistrationEntry

# TODO update the JSON string below
json = "{}"
# create an instance of TimeRegistrationEntry from a JSON string
time_registration_entry_instance = TimeRegistrationEntry.from_json(json)
# print the JSON string representation of the object
print(TimeRegistrationEntry.to_json())

# convert the object into a dict
time_registration_entry_dict = time_registration_entry_instance.to_dict()
# create an instance of TimeRegistrationEntry from a dict
time_registration_entry_from_dict = TimeRegistrationEntry.from_dict(time_registration_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


