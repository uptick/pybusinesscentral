# Attachments


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**parent_id** | **str** | (v1.0) The parentId property for the Dynamics 365 Business Central attachments entity | [optional] 
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central attachments entity | [optional] 
**file_name** | **str** | (v1.0) The fileName property for the Dynamics 365 Business Central attachments entity | [optional] 
**byte_size** | **int** | (v1.0) The byteSize property for the Dynamics 365 Business Central attachments entity | [optional] 
**content** | **bytearray** | (v1.0) The content property for the Dynamics 365 Business Central attachments entity | [optional] 
**last_modified_date_time** | **datetime** | (v1.0) The lastModifiedDateTime property for the Dynamics 365 Business Central attachments entity | [optional] 

## Example

```python
from pybusinesscentral.model.attachments import Attachments

# TODO update the JSON string below
json = "{}"
# create an instance of Attachments from a JSON string
attachments_instance = Attachments.from_json(json)
# print the JSON string representation of the object
print(Attachments.to_json())

# convert the object into a dict
attachments_dict = attachments_instance.to_dict()
# create an instance of Attachments from a dict
attachments_from_dict = Attachments.from_dict(attachments_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


