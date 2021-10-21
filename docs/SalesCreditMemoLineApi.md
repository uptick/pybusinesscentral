# pybusinesscentral.SalesCreditMemoLineApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_credit_memo_line**](SalesCreditMemoLineApi.md#delete_sales_credit_memo_line) | **DELETE** /companies({company_id})/salesCreditMemoLines(&#39;{salesCreditMemoLine_id}&#39;) | Deletes an object of type salesCreditMemoLine in Dynamics 365 Business Central
[**delete_sales_credit_memo_line_for_sales_credit_memo**](SalesCreditMemoLineApi.md#delete_sales_credit_memo_line_for_sales_credit_memo) | **DELETE** /companies({company_id})/salesCreditMemos({salesCreditMemo_id})/salesCreditMemoLines(&#39;{salesCreditMemoLine_id}&#39;) | Deletes an object of type salesCreditMemoLine in Dynamics 365 Business Central
[**get_sales_credit_memo_line**](SalesCreditMemoLineApi.md#get_sales_credit_memo_line) | **GET** /companies({company_id})/salesCreditMemoLines(&#39;{salesCreditMemoLine_id}&#39;) | Retrieve the properties and relationships of an object of type salesCreditMemoLine for Dynamics 365 Business Central.
[**get_sales_credit_memo_line_for_sales_credit_memo**](SalesCreditMemoLineApi.md#get_sales_credit_memo_line_for_sales_credit_memo) | **GET** /companies({company_id})/salesCreditMemos({salesCreditMemo_id})/salesCreditMemoLines(&#39;{salesCreditMemoLine_id}&#39;) | Retrieve the properties and relationships of an object of type salesCreditMemoLine for Dynamics 365 Business Central.
[**list_sales_credit_memo_lines**](SalesCreditMemoLineApi.md#list_sales_credit_memo_lines) | **GET** /companies({company_id})/salesCreditMemoLines | Returns a list of salesCreditMemoLines
[**list_sales_credit_memo_lines_for_sales_credit_memo**](SalesCreditMemoLineApi.md#list_sales_credit_memo_lines_for_sales_credit_memo) | **GET** /companies({company_id})/salesCreditMemos({salesCreditMemo_id})/salesCreditMemoLines | Returns a list of salesCreditMemoLines
[**patch_sales_credit_memo_line**](SalesCreditMemoLineApi.md#patch_sales_credit_memo_line) | **PATCH** /companies({company_id})/salesCreditMemoLines(&#39;{salesCreditMemoLine_id}&#39;) | Updates an object of type salesCreditMemoLine in Dynamics 365 Business Central
[**patch_sales_credit_memo_line_for_sales_credit_memo**](SalesCreditMemoLineApi.md#patch_sales_credit_memo_line_for_sales_credit_memo) | **PATCH** /companies({company_id})/salesCreditMemos({salesCreditMemo_id})/salesCreditMemoLines(&#39;{salesCreditMemoLine_id}&#39;) | Updates an object of type salesCreditMemoLine in Dynamics 365 Business Central
[**post_sales_credit_memo_line**](SalesCreditMemoLineApi.md#post_sales_credit_memo_line) | **POST** /companies({company_id})/salesCreditMemoLines | Creates an object of type salesCreditMemoLine in Dynamics 365 Business Central
[**post_sales_credit_memo_line_for_sales_credit_memo**](SalesCreditMemoLineApi.md#post_sales_credit_memo_line_for_sales_credit_memo) | **POST** /companies({company_id})/salesCreditMemos({salesCreditMemo_id})/salesCreditMemoLines | Creates an object of type salesCreditMemoLine in Dynamics 365 Business Central


# **delete_sales_credit_memo_line**
> delete_sales_credit_memo_line(company_id, sales_credit_memo_line_id)

Deletes an object of type salesCreditMemoLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_credit_memo_line_api
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
    api_instance = sales_credit_memo_line_api.SalesCreditMemoLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_credit_memo_line_id = "salesCreditMemoLine_id_example" # str | (v1.0) id for salesCreditMemoLine

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type salesCreditMemoLine in Dynamics 365 Business Central
        api_instance.delete_sales_credit_memo_line(company_id, sales_credit_memo_line_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesCreditMemoLineApi->delete_sales_credit_memo_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_credit_memo_line_id** | **str**| (v1.0) id for salesCreditMemoLine |

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
**204** | (v1.0) Succesfully deleted the specified salesCreditMemoLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sales_credit_memo_line_for_sales_credit_memo**
> delete_sales_credit_memo_line_for_sales_credit_memo(company_id, sales_credit_memo_id, sales_credit_memo_line_id)

Deletes an object of type salesCreditMemoLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_credit_memo_line_api
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
    api_instance = sales_credit_memo_line_api.SalesCreditMemoLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_credit_memo_id = "salesCreditMemo_id_example" # str | (v1.0) id for salesCreditMemo
    sales_credit_memo_line_id = "salesCreditMemoLine_id_example" # str | (v1.0) id for salesCreditMemoLine

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type salesCreditMemoLine in Dynamics 365 Business Central
        api_instance.delete_sales_credit_memo_line_for_sales_credit_memo(company_id, sales_credit_memo_id, sales_credit_memo_line_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesCreditMemoLineApi->delete_sales_credit_memo_line_for_sales_credit_memo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_credit_memo_id** | **str**| (v1.0) id for salesCreditMemo |
 **sales_credit_memo_line_id** | **str**| (v1.0) id for salesCreditMemoLine |

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
**204** | (v1.0) Succesfully deleted the specified salesCreditMemoLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_credit_memo_line**
> SalesCreditMemoLine get_sales_credit_memo_line(company_id, sales_credit_memo_line_id)

Retrieve the properties and relationships of an object of type salesCreditMemoLine for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_credit_memo_line_api
from pybusinesscentral.model.sales_credit_memo_line import SalesCreditMemoLine
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
    api_instance = sales_credit_memo_line_api.SalesCreditMemoLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_credit_memo_line_id = "salesCreditMemoLine_id_example" # str | (v1.0) id for salesCreditMemoLine
    expand = [
        "item",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type salesCreditMemoLine for Dynamics 365 Business Central.
        api_response = api_instance.get_sales_credit_memo_line(company_id, sales_credit_memo_line_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesCreditMemoLineApi->get_sales_credit_memo_line: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type salesCreditMemoLine for Dynamics 365 Business Central.
        api_response = api_instance.get_sales_credit_memo_line(company_id, sales_credit_memo_line_id, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesCreditMemoLineApi->get_sales_credit_memo_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_credit_memo_line_id** | **str**| (v1.0) id for salesCreditMemoLine |
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**SalesCreditMemoLine**](SalesCreditMemoLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested salesCreditMemoLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_credit_memo_line_for_sales_credit_memo**
> SalesCreditMemoLine get_sales_credit_memo_line_for_sales_credit_memo(company_id, sales_credit_memo_id, sales_credit_memo_line_id)

Retrieve the properties and relationships of an object of type salesCreditMemoLine for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_credit_memo_line_api
from pybusinesscentral.model.sales_credit_memo_line import SalesCreditMemoLine
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
    api_instance = sales_credit_memo_line_api.SalesCreditMemoLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_credit_memo_id = "salesCreditMemo_id_example" # str | (v1.0) id for salesCreditMemo
    sales_credit_memo_line_id = "salesCreditMemoLine_id_example" # str | (v1.0) id for salesCreditMemoLine
    expand = [
        "item",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type salesCreditMemoLine for Dynamics 365 Business Central.
        api_response = api_instance.get_sales_credit_memo_line_for_sales_credit_memo(company_id, sales_credit_memo_id, sales_credit_memo_line_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesCreditMemoLineApi->get_sales_credit_memo_line_for_sales_credit_memo: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type salesCreditMemoLine for Dynamics 365 Business Central.
        api_response = api_instance.get_sales_credit_memo_line_for_sales_credit_memo(company_id, sales_credit_memo_id, sales_credit_memo_line_id, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesCreditMemoLineApi->get_sales_credit_memo_line_for_sales_credit_memo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_credit_memo_id** | **str**| (v1.0) id for salesCreditMemo |
 **sales_credit_memo_line_id** | **str**| (v1.0) id for salesCreditMemoLine |
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**SalesCreditMemoLine**](SalesCreditMemoLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested salesCreditMemoLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sales_credit_memo_lines**
> InlineResponse20044 list_sales_credit_memo_lines(company_id)

Returns a list of salesCreditMemoLines

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_credit_memo_line_api
from pybusinesscentral.model.inline_response20044 import InlineResponse20044
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
    api_instance = sales_credit_memo_line_api.SalesCreditMemoLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    expand = [
        "item",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of salesCreditMemoLines
        api_response = api_instance.list_sales_credit_memo_lines(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesCreditMemoLineApi->list_sales_credit_memo_lines: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of salesCreditMemoLines
        api_response = api_instance.list_sales_credit_memo_lines(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesCreditMemoLineApi->list_sales_credit_memo_lines: %s\n" % e)
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

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of salesCreditMemoLines |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sales_credit_memo_lines_for_sales_credit_memo**
> InlineResponse20044 list_sales_credit_memo_lines_for_sales_credit_memo(company_id, sales_credit_memo_id)

Returns a list of salesCreditMemoLines

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_credit_memo_line_api
from pybusinesscentral.model.inline_response20044 import InlineResponse20044
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
    api_instance = sales_credit_memo_line_api.SalesCreditMemoLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_credit_memo_id = "salesCreditMemo_id_example" # str | (v1.0) id for salesCreditMemo
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    expand = [
        "item",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of salesCreditMemoLines
        api_response = api_instance.list_sales_credit_memo_lines_for_sales_credit_memo(company_id, sales_credit_memo_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesCreditMemoLineApi->list_sales_credit_memo_lines_for_sales_credit_memo: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of salesCreditMemoLines
        api_response = api_instance.list_sales_credit_memo_lines_for_sales_credit_memo(company_id, sales_credit_memo_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesCreditMemoLineApi->list_sales_credit_memo_lines_for_sales_credit_memo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_credit_memo_id** | **str**| (v1.0) id for salesCreditMemo |
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional]
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional]
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional]
 **filter** | **str**| (v1.0) Filtering expression | [optional]
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse20044**](InlineResponse20044.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of salesCreditMemoLines |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sales_credit_memo_line**
> SalesCreditMemoLine patch_sales_credit_memo_line(company_id, sales_credit_memo_line_id, content_type, if_match, unknown_base_type)

Updates an object of type salesCreditMemoLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_credit_memo_line_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.sales_credit_memo_line import SalesCreditMemoLine
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
    api_instance = sales_credit_memo_line_api.SalesCreditMemoLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_credit_memo_line_id = "salesCreditMemoLine_id_example" # str | (v1.0) id for salesCreditMemoLine
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        id="id_example",
        document_id="document_id_example",
        sequence=1,
        item_id="item_id_example",
        account_id="account_id_example",
        line_type="line_type_example",
        line_details=,
        description="description_example",
        unit_of_measure_id="unit_of_measure_id_example",
        unit_of_measure=,
        unit_price=3.14,
        quantity=3.14,
        discount_amount=3.14,
        discount_percent=3.14,
        discount_applied_before_tax=True,
        amount_excluding_tax=3.14,
        tax_code="tax_code_example",
        tax_percent=3.14,
        total_tax_amount=3.14,
        amount_including_tax=3.14,
        invoice_discount_allocation=3.14,
        net_amount=3.14,
        net_tax_amount=3.14,
        net_amount_including_tax=3.14,
        shipment_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type salesCreditMemoLine in Dynamics 365 Business Central
        api_response = api_instance.patch_sales_credit_memo_line(company_id, sales_credit_memo_line_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesCreditMemoLineApi->patch_sales_credit_memo_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_credit_memo_line_id** | **str**| (v1.0) id for salesCreditMemoLine |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**SalesCreditMemoLine**](SalesCreditMemoLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedsalesCreditMemoLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sales_credit_memo_line_for_sales_credit_memo**
> SalesCreditMemoLine patch_sales_credit_memo_line_for_sales_credit_memo(company_id, sales_credit_memo_id, sales_credit_memo_line_id, content_type, if_match, unknown_base_type)

Updates an object of type salesCreditMemoLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_credit_memo_line_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.sales_credit_memo_line import SalesCreditMemoLine
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
    api_instance = sales_credit_memo_line_api.SalesCreditMemoLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_credit_memo_id = "salesCreditMemo_id_example" # str | (v1.0) id for salesCreditMemo
    sales_credit_memo_line_id = "salesCreditMemoLine_id_example" # str | (v1.0) id for salesCreditMemoLine
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        id="id_example",
        document_id="document_id_example",
        sequence=1,
        item_id="item_id_example",
        account_id="account_id_example",
        line_type="line_type_example",
        line_details=,
        description="description_example",
        unit_of_measure_id="unit_of_measure_id_example",
        unit_of_measure=,
        unit_price=3.14,
        quantity=3.14,
        discount_amount=3.14,
        discount_percent=3.14,
        discount_applied_before_tax=True,
        amount_excluding_tax=3.14,
        tax_code="tax_code_example",
        tax_percent=3.14,
        total_tax_amount=3.14,
        amount_including_tax=3.14,
        invoice_discount_allocation=3.14,
        net_amount=3.14,
        net_tax_amount=3.14,
        net_amount_including_tax=3.14,
        shipment_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type salesCreditMemoLine in Dynamics 365 Business Central
        api_response = api_instance.patch_sales_credit_memo_line_for_sales_credit_memo(company_id, sales_credit_memo_id, sales_credit_memo_line_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesCreditMemoLineApi->patch_sales_credit_memo_line_for_sales_credit_memo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_credit_memo_id** | **str**| (v1.0) id for salesCreditMemo |
 **sales_credit_memo_line_id** | **str**| (v1.0) id for salesCreditMemoLine |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**SalesCreditMemoLine**](SalesCreditMemoLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedsalesCreditMemoLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_credit_memo_line**
> SalesCreditMemoLine post_sales_credit_memo_line(company_id, content_type, unknown_base_type)

Creates an object of type salesCreditMemoLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_credit_memo_line_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.sales_credit_memo_line import SalesCreditMemoLine
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
    api_instance = sales_credit_memo_line_api.SalesCreditMemoLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    content_type = "Content-Type_example" # str | (v1.0) application/json
    unknown_base_type = {
        id="id_example",
        document_id="document_id_example",
        sequence=1,
        item_id="item_id_example",
        account_id="account_id_example",
        line_type="line_type_example",
        line_details=,
        description="description_example",
        unit_of_measure_id="unit_of_measure_id_example",
        unit_of_measure=,
        unit_price=3.14,
        quantity=3.14,
        discount_amount=3.14,
        discount_percent=3.14,
        discount_applied_before_tax=True,
        amount_excluding_tax=3.14,
        tax_code="tax_code_example",
        tax_percent=3.14,
        total_tax_amount=3.14,
        amount_including_tax=3.14,
        invoice_discount_allocation=3.14,
        net_amount=3.14,
        net_tax_amount=3.14,
        net_amount_including_tax=3.14,
        shipment_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type salesCreditMemoLine in Dynamics 365 Business Central
        api_response = api_instance.post_sales_credit_memo_line(company_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesCreditMemoLineApi->post_sales_credit_memo_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**SalesCreditMemoLine**](SalesCreditMemoLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new salesCreditMemoLine has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_credit_memo_line_for_sales_credit_memo**
> SalesCreditMemoLine post_sales_credit_memo_line_for_sales_credit_memo(company_id, sales_credit_memo_id, content_type, unknown_base_type)

Creates an object of type salesCreditMemoLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_credit_memo_line_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.sales_credit_memo_line import SalesCreditMemoLine
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
    api_instance = sales_credit_memo_line_api.SalesCreditMemoLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_credit_memo_id = "salesCreditMemo_id_example" # str | (v1.0) id for salesCreditMemo
    content_type = "Content-Type_example" # str | (v1.0) application/json
    unknown_base_type = {
        id="id_example",
        document_id="document_id_example",
        sequence=1,
        item_id="item_id_example",
        account_id="account_id_example",
        line_type="line_type_example",
        line_details=,
        description="description_example",
        unit_of_measure_id="unit_of_measure_id_example",
        unit_of_measure=,
        unit_price=3.14,
        quantity=3.14,
        discount_amount=3.14,
        discount_percent=3.14,
        discount_applied_before_tax=True,
        amount_excluding_tax=3.14,
        tax_code="tax_code_example",
        tax_percent=3.14,
        total_tax_amount=3.14,
        amount_including_tax=3.14,
        invoice_discount_allocation=3.14,
        net_amount=3.14,
        net_tax_amount=3.14,
        net_amount_including_tax=3.14,
        shipment_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type salesCreditMemoLine in Dynamics 365 Business Central
        api_response = api_instance.post_sales_credit_memo_line_for_sales_credit_memo(company_id, sales_credit_memo_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesCreditMemoLineApi->post_sales_credit_memo_line_for_sales_credit_memo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_credit_memo_id** | **str**| (v1.0) id for salesCreditMemo |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**SalesCreditMemoLine**](SalesCreditMemoLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new salesCreditMemoLine has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

