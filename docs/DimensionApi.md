# pybusinesscentral.DimensionApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dimension**](DimensionApi.md#get_dimension) | **GET** /companies({company_id})/dimensions({dimension_id}) | Retrieve the properties and relationships of an object of type dimension for Dynamics 365 Business Central.
[**list_dimensions**](DimensionApi.md#list_dimensions) | **GET** /companies({company_id})/dimensions | Returns a list of dimensions


# **get_dimension**
> Dimension get_dimension(company_id, dimension_id)

Retrieve the properties and relationships of an object of type dimension for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):

```python
import time
import pybusinesscentral
from pybusinesscentral.api import dimension_api
from pybusinesscentral.model.dimension import Dimension
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
    api_instance = dimension_api.DimensionApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    dimension_id = "dimension_id_example" # str | (v1.0) id for dimension
    expand = [
        "dimensionValues",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type dimension for Dynamics 365 Business Central.
        api_response = api_instance.get_dimension(company_id, dimension_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling DimensionApi->get_dimension: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type dimension for Dynamics 365 Business Central.
        api_response = api_instance.get_dimension(company_id, dimension_id, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling DimensionApi->get_dimension: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **dimension_id** | **str**| (v1.0) id for dimension |
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**Dimension**](Dimension.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested dimension |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dimensions**
> InlineResponse2006 list_dimensions(company_id)

Returns a list of dimensions

### Example

* OAuth Authentication (oAuth):

```python
import time
import pybusinesscentral
from pybusinesscentral.api import dimension_api
from pybusinesscentral.model.inline_response2006 import InlineResponse2006
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
    api_instance = dimension_api.DimensionApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    expand = [
        "dimensionValues",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of dimensions
        api_response = api_instance.list_dimensions(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling DimensionApi->list_dimensions: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of dimensions
        api_response = api_instance.list_dimensions(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling DimensionApi->list_dimensions: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional]
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional]
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional]
 **filter** | **str**| (v1.0) Filtering expression | [optional]
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse2006**](InlineResponse2006.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of dimensions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

