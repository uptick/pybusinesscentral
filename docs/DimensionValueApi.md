# pybusinesscentral.DimensionValueApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dimension_value**](DimensionValueApi.md#get_dimension_value) | **GET** /companies({company_id})/dimensionValues({dimensionValue_id}) | Retrieve the properties and relationships of an object of type dimensionValue for Dynamics 365 Business Central.
[**get_dimension_value_for_dimension**](DimensionValueApi.md#get_dimension_value_for_dimension) | **GET** /companies({company_id})/dimensions({dimension_id})/dimensionValues({dimensionValue_id}) | Retrieve the properties and relationships of an object of type dimensionValue for Dynamics 365 Business Central.
[**list_dimension_values**](DimensionValueApi.md#list_dimension_values) | **GET** /companies({company_id})/dimensionValues | Returns a list of dimensionValues
[**list_dimension_values_for_dimension**](DimensionValueApi.md#list_dimension_values_for_dimension) | **GET** /companies({company_id})/dimensions({dimension_id})/dimensionValues | Returns a list of dimensionValues


# **get_dimension_value**
> DimensionValue get_dimension_value(company_id, dimension_value_id)

Retrieve the properties and relationships of an object of type dimensionValue for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import dimension_value_api
from pybusinesscentral.model.dimension_value import DimensionValue
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
    api_instance = dimension_value_api.DimensionValueApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    dimension_value_id = "dimensionValue_id_example" # str | (v1.0) id for dimensionValue
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type dimensionValue for Dynamics 365 Business Central.
        api_response = api_instance.get_dimension_value(company_id, dimension_value_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling DimensionValueApi->get_dimension_value: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type dimensionValue for Dynamics 365 Business Central.
        api_response = api_instance.get_dimension_value(company_id, dimension_value_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling DimensionValueApi->get_dimension_value: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **dimension_value_id** | **str**| (v1.0) id for dimensionValue |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**DimensionValue**](DimensionValue.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested dimensionValue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dimension_value_for_dimension**
> DimensionValue get_dimension_value_for_dimension(company_id, dimension_id, dimension_value_id)

Retrieve the properties and relationships of an object of type dimensionValue for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import dimension_value_api
from pybusinesscentral.model.dimension_value import DimensionValue
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
    api_instance = dimension_value_api.DimensionValueApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    dimension_id = "dimension_id_example" # str | (v1.0) id for dimension
    dimension_value_id = "dimensionValue_id_example" # str | (v1.0) id for dimensionValue
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type dimensionValue for Dynamics 365 Business Central.
        api_response = api_instance.get_dimension_value_for_dimension(company_id, dimension_id, dimension_value_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling DimensionValueApi->get_dimension_value_for_dimension: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type dimensionValue for Dynamics 365 Business Central.
        api_response = api_instance.get_dimension_value_for_dimension(company_id, dimension_id, dimension_value_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling DimensionValueApi->get_dimension_value_for_dimension: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **dimension_id** | **str**| (v1.0) id for dimension |
 **dimension_value_id** | **str**| (v1.0) id for dimensionValue |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**DimensionValue**](DimensionValue.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested dimensionValue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dimension_values**
> InlineResponse20024 list_dimension_values(company_id)

Returns a list of dimensionValues

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import dimension_value_api
from pybusinesscentral.model.inline_response20024 import InlineResponse20024
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
    api_instance = dimension_value_api.DimensionValueApi(api_client)
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
        # Returns a list of dimensionValues
        api_response = api_instance.list_dimension_values(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling DimensionValueApi->list_dimension_values: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of dimensionValues
        api_response = api_instance.list_dimension_values(company_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling DimensionValueApi->list_dimension_values: %s\n" % e)
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

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of dimensionValues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dimension_values_for_dimension**
> InlineResponse20024 list_dimension_values_for_dimension(company_id, dimension_id)

Returns a list of dimensionValues

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import dimension_value_api
from pybusinesscentral.model.inline_response20024 import InlineResponse20024
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
    api_instance = dimension_value_api.DimensionValueApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    dimension_id = "dimension_id_example" # str | (v1.0) id for dimension
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of dimensionValues
        api_response = api_instance.list_dimension_values_for_dimension(company_id, dimension_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling DimensionValueApi->list_dimension_values_for_dimension: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of dimensionValues
        api_response = api_instance.list_dimension_values_for_dimension(company_id, dimension_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling DimensionValueApi->list_dimension_values_for_dimension: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **dimension_id** | **str**| (v1.0) id for dimension |
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional]
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional]
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional]
 **filter** | **str**| (v1.0) Filtering expression | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse20024**](InlineResponse20024.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of dimensionValues |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

