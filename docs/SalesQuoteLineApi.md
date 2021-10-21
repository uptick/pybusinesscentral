# pybusinesscentral.SalesQuoteLineApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_quote_line**](SalesQuoteLineApi.md#delete_sales_quote_line) | **DELETE** /companies({company_id})/salesQuoteLines(&#39;{salesQuoteLine_id}&#39;) | Deletes an object of type salesQuoteLine in Dynamics 365 Business Central
[**delete_sales_quote_line_for_sales_quote**](SalesQuoteLineApi.md#delete_sales_quote_line_for_sales_quote) | **DELETE** /companies({company_id})/salesQuotes({salesQuote_id})/salesQuoteLines(&#39;{salesQuoteLine_id}&#39;) | Deletes an object of type salesQuoteLine in Dynamics 365 Business Central
[**get_sales_quote_line**](SalesQuoteLineApi.md#get_sales_quote_line) | **GET** /companies({company_id})/salesQuoteLines(&#39;{salesQuoteLine_id}&#39;) | Retrieve the properties and relationships of an object of type salesQuoteLine for Dynamics 365 Business Central.
[**get_sales_quote_line_for_sales_quote**](SalesQuoteLineApi.md#get_sales_quote_line_for_sales_quote) | **GET** /companies({company_id})/salesQuotes({salesQuote_id})/salesQuoteLines(&#39;{salesQuoteLine_id}&#39;) | Retrieve the properties and relationships of an object of type salesQuoteLine for Dynamics 365 Business Central.
[**list_sales_quote_lines**](SalesQuoteLineApi.md#list_sales_quote_lines) | **GET** /companies({company_id})/salesQuoteLines | Returns a list of salesQuoteLines
[**list_sales_quote_lines_for_sales_quote**](SalesQuoteLineApi.md#list_sales_quote_lines_for_sales_quote) | **GET** /companies({company_id})/salesQuotes({salesQuote_id})/salesQuoteLines | Returns a list of salesQuoteLines
[**patch_sales_quote_line**](SalesQuoteLineApi.md#patch_sales_quote_line) | **PATCH** /companies({company_id})/salesQuoteLines(&#39;{salesQuoteLine_id}&#39;) | Updates an object of type salesQuoteLine in Dynamics 365 Business Central
[**patch_sales_quote_line_for_sales_quote**](SalesQuoteLineApi.md#patch_sales_quote_line_for_sales_quote) | **PATCH** /companies({company_id})/salesQuotes({salesQuote_id})/salesQuoteLines(&#39;{salesQuoteLine_id}&#39;) | Updates an object of type salesQuoteLine in Dynamics 365 Business Central
[**post_sales_quote_line**](SalesQuoteLineApi.md#post_sales_quote_line) | **POST** /companies({company_id})/salesQuoteLines | Creates an object of type salesQuoteLine in Dynamics 365 Business Central
[**post_sales_quote_line_for_sales_quote**](SalesQuoteLineApi.md#post_sales_quote_line_for_sales_quote) | **POST** /companies({company_id})/salesQuotes({salesQuote_id})/salesQuoteLines | Creates an object of type salesQuoteLine in Dynamics 365 Business Central


# **delete_sales_quote_line**
> delete_sales_quote_line(company_id, sales_quote_line_id)

Deletes an object of type salesQuoteLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_quote_line_api
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
    api_instance = sales_quote_line_api.SalesQuoteLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_quote_line_id = "salesQuoteLine_id_example" # str | (v1.0) id for salesQuoteLine

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type salesQuoteLine in Dynamics 365 Business Central
        api_instance.delete_sales_quote_line(company_id, sales_quote_line_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteLineApi->delete_sales_quote_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_quote_line_id** | **str**| (v1.0) id for salesQuoteLine |

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
**204** | (v1.0) Succesfully deleted the specified salesQuoteLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sales_quote_line_for_sales_quote**
> delete_sales_quote_line_for_sales_quote(company_id, sales_quote_id, sales_quote_line_id)

Deletes an object of type salesQuoteLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_quote_line_api
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
    api_instance = sales_quote_line_api.SalesQuoteLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_quote_id = "salesQuote_id_example" # str | (v1.0) id for salesQuote
    sales_quote_line_id = "salesQuoteLine_id_example" # str | (v1.0) id for salesQuoteLine

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type salesQuoteLine in Dynamics 365 Business Central
        api_instance.delete_sales_quote_line_for_sales_quote(company_id, sales_quote_id, sales_quote_line_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteLineApi->delete_sales_quote_line_for_sales_quote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_quote_id** | **str**| (v1.0) id for salesQuote |
 **sales_quote_line_id** | **str**| (v1.0) id for salesQuoteLine |

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
**204** | (v1.0) Succesfully deleted the specified salesQuoteLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_quote_line**
> SalesQuoteLine get_sales_quote_line(company_id, sales_quote_line_id)

Retrieve the properties and relationships of an object of type salesQuoteLine for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_quote_line_api
from pybusinesscentral.model.sales_quote_line import SalesQuoteLine
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
    api_instance = sales_quote_line_api.SalesQuoteLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_quote_line_id = "salesQuoteLine_id_example" # str | (v1.0) id for salesQuoteLine
    expand = [
        "item",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type salesQuoteLine for Dynamics 365 Business Central.
        api_response = api_instance.get_sales_quote_line(company_id, sales_quote_line_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteLineApi->get_sales_quote_line: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type salesQuoteLine for Dynamics 365 Business Central.
        api_response = api_instance.get_sales_quote_line(company_id, sales_quote_line_id, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteLineApi->get_sales_quote_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_quote_line_id** | **str**| (v1.0) id for salesQuoteLine |
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**SalesQuoteLine**](SalesQuoteLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested salesQuoteLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_quote_line_for_sales_quote**
> SalesQuoteLine get_sales_quote_line_for_sales_quote(company_id, sales_quote_id, sales_quote_line_id)

Retrieve the properties and relationships of an object of type salesQuoteLine for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_quote_line_api
from pybusinesscentral.model.sales_quote_line import SalesQuoteLine
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
    api_instance = sales_quote_line_api.SalesQuoteLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_quote_id = "salesQuote_id_example" # str | (v1.0) id for salesQuote
    sales_quote_line_id = "salesQuoteLine_id_example" # str | (v1.0) id for salesQuoteLine
    expand = [
        "item",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type salesQuoteLine for Dynamics 365 Business Central.
        api_response = api_instance.get_sales_quote_line_for_sales_quote(company_id, sales_quote_id, sales_quote_line_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteLineApi->get_sales_quote_line_for_sales_quote: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type salesQuoteLine for Dynamics 365 Business Central.
        api_response = api_instance.get_sales_quote_line_for_sales_quote(company_id, sales_quote_id, sales_quote_line_id, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteLineApi->get_sales_quote_line_for_sales_quote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_quote_id** | **str**| (v1.0) id for salesQuote |
 **sales_quote_line_id** | **str**| (v1.0) id for salesQuoteLine |
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**SalesQuoteLine**](SalesQuoteLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested salesQuoteLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sales_quote_lines**
> InlineResponse20042 list_sales_quote_lines(company_id)

Returns a list of salesQuoteLines

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_quote_line_api
from pybusinesscentral.model.inline_response20042 import InlineResponse20042
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
    api_instance = sales_quote_line_api.SalesQuoteLineApi(api_client)
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
        # Returns a list of salesQuoteLines
        api_response = api_instance.list_sales_quote_lines(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteLineApi->list_sales_quote_lines: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of salesQuoteLines
        api_response = api_instance.list_sales_quote_lines(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteLineApi->list_sales_quote_lines: %s\n" % e)
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

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of salesQuoteLines |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sales_quote_lines_for_sales_quote**
> InlineResponse20042 list_sales_quote_lines_for_sales_quote(company_id, sales_quote_id)

Returns a list of salesQuoteLines

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_quote_line_api
from pybusinesscentral.model.inline_response20042 import InlineResponse20042
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
    api_instance = sales_quote_line_api.SalesQuoteLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_quote_id = "salesQuote_id_example" # str | (v1.0) id for salesQuote
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
        # Returns a list of salesQuoteLines
        api_response = api_instance.list_sales_quote_lines_for_sales_quote(company_id, sales_quote_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteLineApi->list_sales_quote_lines_for_sales_quote: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of salesQuoteLines
        api_response = api_instance.list_sales_quote_lines_for_sales_quote(company_id, sales_quote_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteLineApi->list_sales_quote_lines_for_sales_quote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_quote_id** | **str**| (v1.0) id for salesQuote |
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional]
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional]
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional]
 **filter** | **str**| (v1.0) Filtering expression | [optional]
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse20042**](InlineResponse20042.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of salesQuoteLines |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sales_quote_line**
> SalesQuoteLine patch_sales_quote_line(company_id, sales_quote_line_id, content_type, if_match, unknown_base_type)

Updates an object of type salesQuoteLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_quote_line_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.sales_quote_line import SalesQuoteLine
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
    api_instance = sales_quote_line_api.SalesQuoteLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_quote_line_id = "salesQuoteLine_id_example" # str | (v1.0) id for salesQuoteLine
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
        net_amount=3.14,
        net_tax_amount=3.14,
        net_amount_including_tax=3.14,
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type salesQuoteLine in Dynamics 365 Business Central
        api_response = api_instance.patch_sales_quote_line(company_id, sales_quote_line_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteLineApi->patch_sales_quote_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_quote_line_id** | **str**| (v1.0) id for salesQuoteLine |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**SalesQuoteLine**](SalesQuoteLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedsalesQuoteLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sales_quote_line_for_sales_quote**
> SalesQuoteLine patch_sales_quote_line_for_sales_quote(company_id, sales_quote_id, sales_quote_line_id, content_type, if_match, unknown_base_type)

Updates an object of type salesQuoteLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_quote_line_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.sales_quote_line import SalesQuoteLine
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
    api_instance = sales_quote_line_api.SalesQuoteLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_quote_id = "salesQuote_id_example" # str | (v1.0) id for salesQuote
    sales_quote_line_id = "salesQuoteLine_id_example" # str | (v1.0) id for salesQuoteLine
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
        net_amount=3.14,
        net_tax_amount=3.14,
        net_amount_including_tax=3.14,
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type salesQuoteLine in Dynamics 365 Business Central
        api_response = api_instance.patch_sales_quote_line_for_sales_quote(company_id, sales_quote_id, sales_quote_line_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteLineApi->patch_sales_quote_line_for_sales_quote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_quote_id** | **str**| (v1.0) id for salesQuote |
 **sales_quote_line_id** | **str**| (v1.0) id for salesQuoteLine |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**SalesQuoteLine**](SalesQuoteLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedsalesQuoteLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_quote_line**
> SalesQuoteLine post_sales_quote_line(company_id, content_type, unknown_base_type)

Creates an object of type salesQuoteLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_quote_line_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.sales_quote_line import SalesQuoteLine
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
    api_instance = sales_quote_line_api.SalesQuoteLineApi(api_client)
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
        net_amount=3.14,
        net_tax_amount=3.14,
        net_amount_including_tax=3.14,
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type salesQuoteLine in Dynamics 365 Business Central
        api_response = api_instance.post_sales_quote_line(company_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteLineApi->post_sales_quote_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**SalesQuoteLine**](SalesQuoteLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new salesQuoteLine has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_quote_line_for_sales_quote**
> SalesQuoteLine post_sales_quote_line_for_sales_quote(company_id, sales_quote_id, content_type, unknown_base_type)

Creates an object of type salesQuoteLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_quote_line_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.sales_quote_line import SalesQuoteLine
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
    api_instance = sales_quote_line_api.SalesQuoteLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_quote_id = "salesQuote_id_example" # str | (v1.0) id for salesQuote
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
        net_amount=3.14,
        net_tax_amount=3.14,
        net_amount_including_tax=3.14,
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type salesQuoteLine in Dynamics 365 Business Central
        api_response = api_instance.post_sales_quote_line_for_sales_quote(company_id, sales_quote_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteLineApi->post_sales_quote_line_for_sales_quote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_quote_id** | **str**| (v1.0) id for salesQuote |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**SalesQuoteLine**](SalesQuoteLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new salesQuoteLine has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

