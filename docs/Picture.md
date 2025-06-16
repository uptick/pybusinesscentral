# Picture


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | (v1.0) The id property for the Dynamics 365 Business Central picture entity | [optional] 
**width** | **int** | (v1.0) The width property for the Dynamics 365 Business Central picture entity | [optional] 
**height** | **int** | (v1.0) The height property for the Dynamics 365 Business Central picture entity | [optional] 
**content_type** | **str** | (v1.0) The contentType property for the Dynamics 365 Business Central picture entity | [optional] 
**contentodata_media_edit_link** | **str** | (v1.0) The content@odata.mediaEditLink property for the Dynamics 365 Business Central picture entity | [optional] 
**contentodata_media_read_link** | **str** | (v1.0) The content@odata.mediaReadLink property for the Dynamics 365 Business Central picture entity | [optional] 

## Example

```python
from pybusinesscentral.model.picture import Picture

# TODO update the JSON string below
json = "{}"
# create an instance of Picture from a JSON string
picture_instance = Picture.from_json(json)
# print the JSON string representation of the object
print(Picture.to_json())

# convert the object into a dict
picture_dict = picture_instance.to_dict()
# create an instance of Picture from a dict
picture_from_dict = Picture.from_dict(picture_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


