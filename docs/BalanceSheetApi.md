# pybusinesscentral.BalanceSheetApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_balance_sheet**](BalanceSheetApi.md#get_balance_sheet) | **GET** /companies({company_id})/balanceSheet({balanceSheet_lineNumber}) | Retrieve the properties and relationships of an object of type balanceSheet for Dynamics 365 Business Central.
[**list_balance_sheet**](BalanceSheetApi.md#list_balance_sheet) | **GET** /companies({company_id})/balanceSheet | Returns a list of balanceSheet


# **get_balance_sheet**
> BalanceSheet get_balance_sheet(company_id, balance_sheet_line_number)

Retrieve the properties and relationships of an object of type balanceSheet for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import balance_sheet_api
from pybusinesscentral.model.balance_sheet import BalanceSheet
from pprint import pprint
# Defining the host is optional and defaults to https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = pybusinesscentral.Configuration(
    host = "https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth
configuration = pybusinesscentral.Configuration(
    host = "https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pybusinesscentral.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_sheet_api.BalanceSheetApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    balance_sheet_line_number = 1 # int | (v1.0) lineNumber for balanceSheet
    select = [
        "lineNumber",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type balanceSheet for Dynamics 365 Business Central.
        api_response = api_instance.get_balance_sheet(company_id, balance_sheet_line_number)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling BalanceSheetApi->get_balance_sheet: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type balanceSheet for Dynamics 365 Business Central.
        api_response = api_instance.get_balance_sheet(company_id, balance_sheet_line_number, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling BalanceSheetApi->get_balance_sheet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **balance_sheet_line_number** | **int**| (v1.0) lineNumber for balanceSheet |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**BalanceSheet**](BalanceSheet.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested balanceSheet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_balance_sheet**
> InlineResponse20037 list_balance_sheet(company_id)

Returns a list of balanceSheet

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import balance_sheet_api
from pybusinesscentral.model.inline_response20037 import InlineResponse20037
from pprint import pprint
# Defining the host is optional and defaults to https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = pybusinesscentral.Configuration(
    host = "https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth
configuration = pybusinesscentral.Configuration(
    host = "https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pybusinesscentral.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = balance_sheet_api.BalanceSheetApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "lineNumber",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of balanceSheet
        api_response = api_instance.list_balance_sheet(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling BalanceSheetApi->list_balance_sheet: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of balanceSheet
        api_response = api_instance.list_balance_sheet(company_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling BalanceSheetApi->list_balance_sheet: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional]
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional]
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional]
 **filter** | **str**| (v1.0) Filtering expression | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse20037**](InlineResponse20037.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of balanceSheet |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

