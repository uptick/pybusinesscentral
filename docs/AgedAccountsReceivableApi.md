# pybusinesscentral.AgedAccountsReceivableApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_aged_accounts_receivable**](AgedAccountsReceivableApi.md#get_aged_accounts_receivable) | **GET** /companies({company_id})/agedAccountsReceivable({agedAccountsReceivable_customerId}) | Retrieve the properties and relationships of an object of type agedAccountsReceivable for Dynamics 365 Business Central.
[**list_aged_accounts_receivable**](AgedAccountsReceivableApi.md#list_aged_accounts_receivable) | **GET** /companies({company_id})/agedAccountsReceivable | Returns a list of agedAccountsReceivable


# **get_aged_accounts_receivable**
> AgedAccountsReceivable get_aged_accounts_receivable(company_id, aged_accounts_receivable_customer_id)

Retrieve the properties and relationships of an object of type agedAccountsReceivable for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import aged_accounts_receivable_api
from pybusinesscentral.model.aged_accounts_receivable import AgedAccountsReceivable
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
    api_instance = aged_accounts_receivable_api.AgedAccountsReceivableApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    aged_accounts_receivable_customer_id = "agedAccountsReceivable_customerId_example" # str | (v1.0) customerId for agedAccountsReceivable
    select = [
        "customerId",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type agedAccountsReceivable for Dynamics 365 Business Central.
        api_response = api_instance.get_aged_accounts_receivable(company_id, aged_accounts_receivable_customer_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AgedAccountsReceivableApi->get_aged_accounts_receivable: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type agedAccountsReceivable for Dynamics 365 Business Central.
        api_response = api_instance.get_aged_accounts_receivable(company_id, aged_accounts_receivable_customer_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AgedAccountsReceivableApi->get_aged_accounts_receivable: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **aged_accounts_receivable_customer_id** | **str**| (v1.0) customerId for agedAccountsReceivable |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**AgedAccountsReceivable**](AgedAccountsReceivable.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested agedAccountsReceivable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_aged_accounts_receivable**
> InlineResponse20035 list_aged_accounts_receivable(company_id)

Returns a list of agedAccountsReceivable

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import aged_accounts_receivable_api
from pybusinesscentral.model.inline_response20035 import InlineResponse20035
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
    api_instance = aged_accounts_receivable_api.AgedAccountsReceivableApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "customerId",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of agedAccountsReceivable
        api_response = api_instance.list_aged_accounts_receivable(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AgedAccountsReceivableApi->list_aged_accounts_receivable: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of agedAccountsReceivable
        api_response = api_instance.list_aged_accounts_receivable(company_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AgedAccountsReceivableApi->list_aged_accounts_receivable: %s\n" % e)
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

[**InlineResponse20035**](InlineResponse20035.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of agedAccountsReceivable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

