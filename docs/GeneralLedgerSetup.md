# GeneralLedgerSetup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The id property for the Dynamics 365 Business Central generalLedgerSetup entity | [optional] 
**allow_posting_from** | **datetime** | The allowPostingFrom property for the Dynamics 365 Business Central generalLedgerSetup entity | [optional] 
**allow_posting_to** | **datetime** | The allowPostingTo property for the Dynamics 365 Business Central generalLedgerSetup entity | [optional] 
**additional_reporting_currency** | **str** | The additionalReportingCurrency property for the Dynamics 365 Business Central generalLedgerSetup entity | [optional] 
**local_currency_code** | **str** | The localCurrencyCode property for the Dynamics 365 Business Central generalLedgerSetup entity | [optional] 
**local_currency_symbol** | **str** | The localCurrencySymbol property for the Dynamics 365 Business Central generalLedgerSetup entity | [optional] 
**last_modified_date_time** | **datetime** | The lastModifiedDateTime property for the Dynamics 365 Business Central generalLedgerSetup entity | [optional] 
**allow_query_from_consolidation** | **bool** | the allowQueryFromConsolidation property for the Dynamics 365 Business Central generalLedgerSetup entity | [optional] 
**shortcut_dimension1_code** | **str** | The shortcutDimension1Code property for the Dynamics 365 Business Central generalLedgerSetup entity | [optional] 
**shortcut_dimension2_code** | **str** | The shortcutDimension2Code property for the Dynamics 365 Business Central generalLedgerSetup entity | [optional] 
**shortcut_dimension3_code** | **str** | The shortcutDimension3Code property for the Dynamics 365 Business Central generalLedgerSetup entity | [optional] 
**shortcut_dimension4_code** | **str** | The shortcutDimension4Code property for the Dynamics 365 Business Central generalLedgerSetup entity | [optional] 
**shortcut_dimension5_code** | **str** | The shortcutDimension5Code property for the Dynamics 365 Business Central generalLedgerSetup entity | [optional] 
**shortcut_dimension6_code** | **str** | The shortcutDimension6Code property for the Dynamics 365 Business Central generalLedgerSetup entity | [optional] 
**shortcut_dimension7_code** | **str** | The shortcutDimension7Code property for the Dynamics 365 Business Central generalLedgerSetup entity | [optional] 
**shortcut_dimension8_code** | **str** | The shortcutDimension8Code property for the Dynamics 365 Business Central generalLedgerSetup entity | [optional] 

## Example

```python
from openapi_client.models.general_ledger_setup import GeneralLedgerSetup

# TODO update the JSON string below
json = "{}"
# create an instance of GeneralLedgerSetup from a JSON string
general_ledger_setup_instance = GeneralLedgerSetup.from_json(json)
# print the JSON string representation of the object
print(GeneralLedgerSetup.to_json())

# convert the object into a dict
general_ledger_setup_dict = general_ledger_setup_instance.to_dict()
# create an instance of GeneralLedgerSetup from a dict
general_ledger_setup_from_dict = GeneralLedgerSetup.from_dict(general_ledger_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


