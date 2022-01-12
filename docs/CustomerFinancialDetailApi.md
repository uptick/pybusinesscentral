# pybusinesscentral.CustomerFinancialDetailApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_customer_financial_detail**](CustomerFinancialDetailApi.md#get_customer_financial_detail) | **GET** /companies({company_id})/customerFinancialDetails({customerFinancialDetail_id}) | Retrieve the properties and relationships of an object of type customerFinancialDetail for Dynamics 365 Business Central.
[**get_customer_financial_detail_for_customer**](CustomerFinancialDetailApi.md#get_customer_financial_detail_for_customer) | **GET** /companies({company_id})/customers({customer_id})/customerFinancialDetails({customerFinancialDetail_id}) | Retrieve the properties and relationships of an object of type customerFinancialDetail for Dynamics 365 Business Central.
[**list_customer_financial_details**](CustomerFinancialDetailApi.md#list_customer_financial_details) | **GET** /companies({company_id})/customerFinancialDetails | Returns a list of customerFinancialDetails
[**list_customer_financial_details_for_customer**](CustomerFinancialDetailApi.md#list_customer_financial_details_for_customer) | **GET** /companies({company_id})/customers({customer_id})/customerFinancialDetails | Returns a list of customerFinancialDetails


# **get_customer_financial_detail**
> CustomerFinancialDetail get_customer_financial_detail(company_id, customer_financial_detail_id)

Retrieve the properties and relationships of an object of type customerFinancialDetail for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import customer_financial_detail_api
from pybusinesscentral.model.customer_financial_detail import CustomerFinancialDetail
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
    api_instance = customer_financial_detail_api.CustomerFinancialDetailApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    customer_financial_detail_id = "customerFinancialDetail_id_example" # str | (v1.0) id for customerFinancialDetail
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type customerFinancialDetail for Dynamics 365 Business Central.
        api_response = api_instance.get_customer_financial_detail(company_id, customer_financial_detail_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerFinancialDetailApi->get_customer_financial_detail: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type customerFinancialDetail for Dynamics 365 Business Central.
        api_response = api_instance.get_customer_financial_detail(company_id, customer_financial_detail_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerFinancialDetailApi->get_customer_financial_detail: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **customer_financial_detail_id** | **str**| (v1.0) id for customerFinancialDetail |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**CustomerFinancialDetail**](CustomerFinancialDetail.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested customerFinancialDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_financial_detail_for_customer**
> CustomerFinancialDetail get_customer_financial_detail_for_customer(company_id, customer_id, customer_financial_detail_id)

Retrieve the properties and relationships of an object of type customerFinancialDetail for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import customer_financial_detail_api
from pybusinesscentral.model.customer_financial_detail import CustomerFinancialDetail
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
    api_instance = customer_financial_detail_api.CustomerFinancialDetailApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    customer_id = "customer_id_example" # str | (v1.0) id for customer
    customer_financial_detail_id = "customerFinancialDetail_id_example" # str | (v1.0) id for customerFinancialDetail
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type customerFinancialDetail for Dynamics 365 Business Central.
        api_response = api_instance.get_customer_financial_detail_for_customer(company_id, customer_id, customer_financial_detail_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerFinancialDetailApi->get_customer_financial_detail_for_customer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type customerFinancialDetail for Dynamics 365 Business Central.
        api_response = api_instance.get_customer_financial_detail_for_customer(company_id, customer_id, customer_financial_detail_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerFinancialDetailApi->get_customer_financial_detail_for_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **customer_id** | **str**| (v1.0) id for customer |
 **customer_financial_detail_id** | **str**| (v1.0) id for customerFinancialDetail |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**CustomerFinancialDetail**](CustomerFinancialDetail.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested customerFinancialDetail |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_financial_details**
> InlineResponse2005 list_customer_financial_details(company_id)

Returns a list of customerFinancialDetails

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import customer_financial_detail_api
from pybusinesscentral.model.inline_response2005 import InlineResponse2005
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
    api_instance = customer_financial_detail_api.CustomerFinancialDetailApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of customerFinancialDetails
        api_response = api_instance.list_customer_financial_details(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerFinancialDetailApi->list_customer_financial_details: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of customerFinancialDetails
        api_response = api_instance.list_customer_financial_details(company_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerFinancialDetailApi->list_customer_financial_details: %s\n" % e)
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

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of customerFinancialDetails |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_financial_details_for_customer**
> InlineResponse2005 list_customer_financial_details_for_customer(company_id, customer_id)

Returns a list of customerFinancialDetails

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import customer_financial_detail_api
from pybusinesscentral.model.inline_response2005 import InlineResponse2005
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
    api_instance = customer_financial_detail_api.CustomerFinancialDetailApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    customer_id = "customer_id_example" # str | (v1.0) id for customer
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of customerFinancialDetails
        api_response = api_instance.list_customer_financial_details_for_customer(company_id, customer_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerFinancialDetailApi->list_customer_financial_details_for_customer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of customerFinancialDetails
        api_response = api_instance.list_customer_financial_details_for_customer(company_id, customer_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerFinancialDetailApi->list_customer_financial_details_for_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **customer_id** | **str**| (v1.0) id for customer |
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional]
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional]
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional]
 **filter** | **str**| (v1.0) Filtering expression | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse2005**](InlineResponse2005.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of customerFinancialDetails |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

