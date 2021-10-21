# pybusinesscentral.DimensionLineApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_dimension_line**](DimensionLineApi.md#delete_dimension_line) | **DELETE** /companies({company_id})/dimensionLines({dimensionLine_parentId},{dimensionLine_id}) | Deletes an object of type dimensionLine in Dynamics 365 Business Central
[**get_dimension_line**](DimensionLineApi.md#get_dimension_line) | **GET** /companies({company_id})/dimensionLines({dimensionLine_parentId},{dimensionLine_id}) | Retrieve the properties and relationships of an object of type dimensionLine for Dynamics 365 Business Central.
[**list_dimension_lines**](DimensionLineApi.md#list_dimension_lines) | **GET** /companies({company_id})/dimensionLines | Returns a list of dimensionLines
[**patch_dimension_line**](DimensionLineApi.md#patch_dimension_line) | **PATCH** /companies({company_id})/dimensionLines({dimensionLine_parentId},{dimensionLine_id}) | Updates an object of type dimensionLine in Dynamics 365 Business Central
[**post_dimension_line**](DimensionLineApi.md#post_dimension_line) | **POST** /companies({company_id})/dimensionLines | Creates an object of type dimensionLine in Dynamics 365 Business Central


# **delete_dimension_line**
> delete_dimension_line(company_id, dimension_line_parent_id, dimension_line_id)

Deletes an object of type dimensionLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import dimension_line_api
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
    api_instance = dimension_line_api.DimensionLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    dimension_line_parent_id = "dimensionLine_parentId_example" # str | (v1.0) parentId for dimensionLine
    dimension_line_id = "dimensionLine_id_example" # str | (v1.0) id for dimensionLine

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type dimensionLine in Dynamics 365 Business Central
        api_instance.delete_dimension_line(company_id, dimension_line_parent_id, dimension_line_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling DimensionLineApi->delete_dimension_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **dimension_line_parent_id** | **str**| (v1.0) parentId for dimensionLine |
 **dimension_line_id** | **str**| (v1.0) id for dimensionLine |

### Return type

void (empty response body)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | (v1.0) Succesfully deleted the specified dimensionLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_dimension_line**
> DimensionLine get_dimension_line(company_id, dimension_line_parent_id, dimension_line_id)

Retrieve the properties and relationships of an object of type dimensionLine for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import dimension_line_api
from pybusinesscentral.model.dimension_line import DimensionLine
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
    api_instance = dimension_line_api.DimensionLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    dimension_line_parent_id = "dimensionLine_parentId_example" # str | (v1.0) parentId for dimensionLine
    dimension_line_id = "dimensionLine_id_example" # str | (v1.0) id for dimensionLine
    expand = [
        "dimension",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "parentId",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type dimensionLine for Dynamics 365 Business Central.
        api_response = api_instance.get_dimension_line(company_id, dimension_line_parent_id, dimension_line_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling DimensionLineApi->get_dimension_line: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type dimensionLine for Dynamics 365 Business Central.
        api_response = api_instance.get_dimension_line(company_id, dimension_line_parent_id, dimension_line_id, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling DimensionLineApi->get_dimension_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **dimension_line_parent_id** | **str**| (v1.0) parentId for dimensionLine |
 **dimension_line_id** | **str**| (v1.0) id for dimensionLine |
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**DimensionLine**](DimensionLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested dimensionLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dimension_lines**
> InlineResponse20025 list_dimension_lines(company_id)

Returns a list of dimensionLines

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import dimension_line_api
from pybusinesscentral.model.inline_response20025 import InlineResponse20025
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
    api_instance = dimension_line_api.DimensionLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    expand = [
        "dimension",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "parentId",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of dimensionLines
        api_response = api_instance.list_dimension_lines(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling DimensionLineApi->list_dimension_lines: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of dimensionLines
        api_response = api_instance.list_dimension_lines(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling DimensionLineApi->list_dimension_lines: %s\n" % e)
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

[**InlineResponse20025**](InlineResponse20025.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of dimensionLines |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_dimension_line**
> DimensionLine patch_dimension_line(company_id, dimension_line_parent_id, dimension_line_id, content_type, if_match, unknown_base_type)

Updates an object of type dimensionLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import dimension_line_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.dimension_line import DimensionLine
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
    api_instance = dimension_line_api.DimensionLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    dimension_line_parent_id = "dimensionLine_parentId_example" # str | (v1.0) parentId for dimensionLine
    dimension_line_id = "dimensionLine_id_example" # str | (v1.0) id for dimensionLine
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        parent_id="parent_id_example",
        id="id_example",
        code="code_example",
        display_name="display_name_example",
        value_id="value_id_example",
        value_code="value_code_example",
        value_display_name="value_display_name_example",
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type dimensionLine in Dynamics 365 Business Central
        api_response = api_instance.patch_dimension_line(company_id, dimension_line_parent_id, dimension_line_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling DimensionLineApi->patch_dimension_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **dimension_line_parent_id** | **str**| (v1.0) parentId for dimensionLine |
 **dimension_line_id** | **str**| (v1.0) id for dimensionLine |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**DimensionLine**](DimensionLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifieddimensionLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_dimension_line**
> DimensionLine post_dimension_line(company_id, content_type, unknown_base_type)

Creates an object of type dimensionLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import dimension_line_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.dimension_line import DimensionLine
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
    api_instance = dimension_line_api.DimensionLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    content_type = "Content-Type_example" # str | (v1.0) application/json
    unknown_base_type = {
        parent_id="parent_id_example",
        id="id_example",
        code="code_example",
        display_name="display_name_example",
        value_id="value_id_example",
        value_code="value_code_example",
        value_display_name="value_display_name_example",
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type dimensionLine in Dynamics 365 Business Central
        api_response = api_instance.post_dimension_line(company_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling DimensionLineApi->post_dimension_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**DimensionLine**](DimensionLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new dimensionLine has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

