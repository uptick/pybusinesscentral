# Documentlineobjectdetailstype


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | **str** | (v1.0) The number property for the Dynamics 365 Business Central documentlineobjectdetailstype entity | [optional] 
**display_name** | **str** | (v1.0) The displayName property for the Dynamics 365 Business Central documentlineobjectdetailstype entity | [optional] 
**item** | [**Item**](Item.md) |  | [optional] 
**account** | [**Account**](Account.md) |  | [optional] 

## Example

```python
from pybusinesscentral.model.documentlineobjectdetailstype import Documentlineobjectdetailstype

# TODO update the JSON string below
json = "{}"
# create an instance of Documentlineobjectdetailstype from a JSON string
documentlineobjectdetailstype_instance = Documentlineobjectdetailstype.from_json(json)
# print the JSON string representation of the object
print(Documentlineobjectdetailstype.to_json())

# convert the object into a dict
documentlineobjectdetailstype_dict = documentlineobjectdetailstype_instance.to_dict()
# create an instance of Documentlineobjectdetailstype from a dict
documentlineobjectdetailstype_from_dict = Documentlineobjectdetailstype.from_dict(documentlineobjectdetailstype_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


