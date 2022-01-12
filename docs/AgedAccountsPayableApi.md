# pybusinesscentral.AgedAccountsPayableApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aged_accounts_payable**](AgedAccountsPayableApi.md#get_aged_accounts_payable) | **GET** /companies({company_id})/agedAccountsPayable({agedAccountsPayable_vendorId}) | Retrieve the properties and relationships of an object of type agedAccountsPayable for Dynamics 365 Business Central.
[**list_aged_accounts_payable**](AgedAccountsPayableApi.md#list_aged_accounts_payable) | **GET** /companies({company_id})/agedAccountsPayable | Returns a list of agedAccountsPayable


# **get_aged_accounts_payable**
> AgedAccountsPayable get_aged_accounts_payable(company_id, aged_accounts_payable_vendor_id)

Retrieve the properties and relationships of an object of type agedAccountsPayable for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import aged_accounts_payable_api
from pybusinesscentral.model.aged_accounts_payable import AgedAccountsPayable
from pprint import pprint
# Defining the host is optional and defaults to https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = pybusinesscentral.Configuration(
    host = "https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth
configuration = pybusinesscentral.Configuration(
    host = "https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pybusinesscentral.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aged_accounts_payable_api.AgedAccountsPayableApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    aged_accounts_payable_vendor_id = "agedAccountsPayable_vendorId_example" # str | (v1.0) vendorId for agedAccountsPayable
    select = [
        "vendorId",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type agedAccountsPayable for Dynamics 365 Business Central.
        api_response = api_instance.get_aged_accounts_payable(company_id, aged_accounts_payable_vendor_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AgedAccountsPayableApi->get_aged_accounts_payable: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type agedAccountsPayable for Dynamics 365 Business Central.
        api_response = api_instance.get_aged_accounts_payable(company_id, aged_accounts_payable_vendor_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AgedAccountsPayableApi->get_aged_accounts_payable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **aged_accounts_payable_vendor_id** | **str**| (v1.0) vendorId for agedAccountsPayable |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**AgedAccountsPayable**](AgedAccountsPayable.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested agedAccountsPayable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_aged_accounts_payable**
> InlineResponse20036 list_aged_accounts_payable(company_id)

Returns a list of agedAccountsPayable

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import aged_accounts_payable_api
from pybusinesscentral.model.inline_response20036 import InlineResponse20036
from pprint import pprint
# Defining the host is optional and defaults to https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0
# See configuration.py for a list of all supported configuration parameters.
configuration = pybusinesscentral.Configuration(
    host = "https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure OAuth2 access token for authorization: oAuth
configuration = pybusinesscentral.Configuration(
    host = "https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pybusinesscentral.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = aged_accounts_payable_api.AgedAccountsPayableApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "vendorId",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of agedAccountsPayable
        api_response = api_instance.list_aged_accounts_payable(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AgedAccountsPayableApi->list_aged_accounts_payable: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of agedAccountsPayable
        api_response = api_instance.list_aged_accounts_payable(company_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AgedAccountsPayableApi->list_aged_accounts_payable: %s\n" % e)
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

[**InlineResponse20036**](InlineResponse20036.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of agedAccountsPayable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

