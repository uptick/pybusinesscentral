# Project


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central project entity | [optional] 
**number** | **str** | (v1.0) The number property for the Dynamics 365 Business Central project entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central project entity | [optional] 

## Example

```python
from pybusinesscentral.model.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print(Project.to_json())

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


