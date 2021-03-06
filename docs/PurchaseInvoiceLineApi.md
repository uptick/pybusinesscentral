# pybusinesscentral.PurchaseInvoiceLineApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_purchase_invoice_line**](PurchaseInvoiceLineApi.md#delete_purchase_invoice_line) | **DELETE** /companies({company_id})/purchaseInvoiceLines(&#39;{purchaseInvoiceLine_id}&#39;) | Deletes an object of type purchaseInvoiceLine in Dynamics 365 Business Central
[**delete_purchase_invoice_line_for_purchase_invoice**](PurchaseInvoiceLineApi.md#delete_purchase_invoice_line_for_purchase_invoice) | **DELETE** /companies({company_id})/purchaseInvoices({purchaseInvoice_id})/purchaseInvoiceLines(&#39;{purchaseInvoiceLine_id}&#39;) | Deletes an object of type purchaseInvoiceLine in Dynamics 365 Business Central
[**get_purchase_invoice_line**](PurchaseInvoiceLineApi.md#get_purchase_invoice_line) | **GET** /companies({company_id})/purchaseInvoiceLines(&#39;{purchaseInvoiceLine_id}&#39;) | Retrieve the properties and relationships of an object of type purchaseInvoiceLine for Dynamics 365 Business Central.
[**get_purchase_invoice_line_for_purchase_invoice**](PurchaseInvoiceLineApi.md#get_purchase_invoice_line_for_purchase_invoice) | **GET** /companies({company_id})/purchaseInvoices({purchaseInvoice_id})/purchaseInvoiceLines(&#39;{purchaseInvoiceLine_id}&#39;) | Retrieve the properties and relationships of an object of type purchaseInvoiceLine for Dynamics 365 Business Central.
[**list_purchase_invoice_lines**](PurchaseInvoiceLineApi.md#list_purchase_invoice_lines) | **GET** /companies({company_id})/purchaseInvoiceLines | Returns a list of purchaseInvoiceLines
[**list_purchase_invoice_lines_for_purchase_invoice**](PurchaseInvoiceLineApi.md#list_purchase_invoice_lines_for_purchase_invoice) | **GET** /companies({company_id})/purchaseInvoices({purchaseInvoice_id})/purchaseInvoiceLines | Returns a list of purchaseInvoiceLines
[**patch_purchase_invoice_line**](PurchaseInvoiceLineApi.md#patch_purchase_invoice_line) | **PATCH** /companies({company_id})/purchaseInvoiceLines(&#39;{purchaseInvoiceLine_id}&#39;) | Updates an object of type purchaseInvoiceLine in Dynamics 365 Business Central
[**patch_purchase_invoice_line_for_purchase_invoice**](PurchaseInvoiceLineApi.md#patch_purchase_invoice_line_for_purchase_invoice) | **PATCH** /companies({company_id})/purchaseInvoices({purchaseInvoice_id})/purchaseInvoiceLines(&#39;{purchaseInvoiceLine_id}&#39;) | Updates an object of type purchaseInvoiceLine in Dynamics 365 Business Central
[**post_purchase_invoice_line**](PurchaseInvoiceLineApi.md#post_purchase_invoice_line) | **POST** /companies({company_id})/purchaseInvoiceLines | Creates an object of type purchaseInvoiceLine in Dynamics 365 Business Central
[**post_purchase_invoice_line_for_purchase_invoice**](PurchaseInvoiceLineApi.md#post_purchase_invoice_line_for_purchase_invoice) | **POST** /companies({company_id})/purchaseInvoices({purchaseInvoice_id})/purchaseInvoiceLines | Creates an object of type purchaseInvoiceLine in Dynamics 365 Business Central


# **delete_purchase_invoice_line**
> delete_purchase_invoice_line(company_id, purchase_invoice_line_id)

Deletes an object of type purchaseInvoiceLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import purchase_invoice_line_api
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
    api_instance = purchase_invoice_line_api.PurchaseInvoiceLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    purchase_invoice_line_id = "purchaseInvoiceLine_id_example" # str | (v1.0) id for purchaseInvoiceLine

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type purchaseInvoiceLine in Dynamics 365 Business Central
        api_instance.delete_purchase_invoice_line(company_id, purchase_invoice_line_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceLineApi->delete_purchase_invoice_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **purchase_invoice_line_id** | **str**| (v1.0) id for purchaseInvoiceLine |

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
**204** | (v1.0) Succesfully deleted the specified purchaseInvoiceLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_purchase_invoice_line_for_purchase_invoice**
> delete_purchase_invoice_line_for_purchase_invoice(company_id, purchase_invoice_id, purchase_invoice_line_id)

Deletes an object of type purchaseInvoiceLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import purchase_invoice_line_api
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
    api_instance = purchase_invoice_line_api.PurchaseInvoiceLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    purchase_invoice_id = "purchaseInvoice_id_example" # str | (v1.0) id for purchaseInvoice
    purchase_invoice_line_id = "purchaseInvoiceLine_id_example" # str | (v1.0) id for purchaseInvoiceLine

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type purchaseInvoiceLine in Dynamics 365 Business Central
        api_instance.delete_purchase_invoice_line_for_purchase_invoice(company_id, purchase_invoice_id, purchase_invoice_line_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceLineApi->delete_purchase_invoice_line_for_purchase_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **purchase_invoice_id** | **str**| (v1.0) id for purchaseInvoice |
 **purchase_invoice_line_id** | **str**| (v1.0) id for purchaseInvoiceLine |

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
**204** | (v1.0) Succesfully deleted the specified purchaseInvoiceLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase_invoice_line**
> PurchaseInvoiceLine get_purchase_invoice_line(company_id, purchase_invoice_line_id)

Retrieve the properties and relationships of an object of type purchaseInvoiceLine for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import purchase_invoice_line_api
from pybusinesscentral.model.purchase_invoice_line import PurchaseInvoiceLine
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
    api_instance = purchase_invoice_line_api.PurchaseInvoiceLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    purchase_invoice_line_id = "purchaseInvoiceLine_id_example" # str | (v1.0) id for purchaseInvoiceLine
    expand = [
        "item",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type purchaseInvoiceLine for Dynamics 365 Business Central.
        api_response = api_instance.get_purchase_invoice_line(company_id, purchase_invoice_line_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceLineApi->get_purchase_invoice_line: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type purchaseInvoiceLine for Dynamics 365 Business Central.
        api_response = api_instance.get_purchase_invoice_line(company_id, purchase_invoice_line_id, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceLineApi->get_purchase_invoice_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **purchase_invoice_line_id** | **str**| (v1.0) id for purchaseInvoiceLine |
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**PurchaseInvoiceLine**](PurchaseInvoiceLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested purchaseInvoiceLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase_invoice_line_for_purchase_invoice**
> PurchaseInvoiceLine get_purchase_invoice_line_for_purchase_invoice(company_id, purchase_invoice_id, purchase_invoice_line_id)

Retrieve the properties and relationships of an object of type purchaseInvoiceLine for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import purchase_invoice_line_api
from pybusinesscentral.model.purchase_invoice_line import PurchaseInvoiceLine
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
    api_instance = purchase_invoice_line_api.PurchaseInvoiceLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    purchase_invoice_id = "purchaseInvoice_id_example" # str | (v1.0) id for purchaseInvoice
    purchase_invoice_line_id = "purchaseInvoiceLine_id_example" # str | (v1.0) id for purchaseInvoiceLine
    expand = [
        "item",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type purchaseInvoiceLine for Dynamics 365 Business Central.
        api_response = api_instance.get_purchase_invoice_line_for_purchase_invoice(company_id, purchase_invoice_id, purchase_invoice_line_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceLineApi->get_purchase_invoice_line_for_purchase_invoice: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type purchaseInvoiceLine for Dynamics 365 Business Central.
        api_response = api_instance.get_purchase_invoice_line_for_purchase_invoice(company_id, purchase_invoice_id, purchase_invoice_line_id, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceLineApi->get_purchase_invoice_line_for_purchase_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **purchase_invoice_id** | **str**| (v1.0) id for purchaseInvoice |
 **purchase_invoice_line_id** | **str**| (v1.0) id for purchaseInvoiceLine |
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**PurchaseInvoiceLine**](PurchaseInvoiceLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested purchaseInvoiceLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_purchase_invoice_lines**
> InlineResponse20047 list_purchase_invoice_lines(company_id)

Returns a list of purchaseInvoiceLines

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import purchase_invoice_line_api
from pybusinesscentral.model.inline_response20047 import InlineResponse20047
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
    api_instance = purchase_invoice_line_api.PurchaseInvoiceLineApi(api_client)
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
        # Returns a list of purchaseInvoiceLines
        api_response = api_instance.list_purchase_invoice_lines(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceLineApi->list_purchase_invoice_lines: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of purchaseInvoiceLines
        api_response = api_instance.list_purchase_invoice_lines(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceLineApi->list_purchase_invoice_lines: %s\n" % e)
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

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of purchaseInvoiceLines |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_purchase_invoice_lines_for_purchase_invoice**
> InlineResponse20047 list_purchase_invoice_lines_for_purchase_invoice(company_id, purchase_invoice_id)

Returns a list of purchaseInvoiceLines

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import purchase_invoice_line_api
from pybusinesscentral.model.inline_response20047 import InlineResponse20047
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
    api_instance = purchase_invoice_line_api.PurchaseInvoiceLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    purchase_invoice_id = "purchaseInvoice_id_example" # str | (v1.0) id for purchaseInvoice
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
        # Returns a list of purchaseInvoiceLines
        api_response = api_instance.list_purchase_invoice_lines_for_purchase_invoice(company_id, purchase_invoice_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceLineApi->list_purchase_invoice_lines_for_purchase_invoice: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of purchaseInvoiceLines
        api_response = api_instance.list_purchase_invoice_lines_for_purchase_invoice(company_id, purchase_invoice_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceLineApi->list_purchase_invoice_lines_for_purchase_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **purchase_invoice_id** | **str**| (v1.0) id for purchaseInvoice |
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional]
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional]
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional]
 **filter** | **str**| (v1.0) Filtering expression | [optional]
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse20047**](InlineResponse20047.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of purchaseInvoiceLines |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_purchase_invoice_line**
> PurchaseInvoiceLine patch_purchase_invoice_line(company_id, purchase_invoice_line_id, content_type, if_match, unknown_base_type)

Updates an object of type purchaseInvoiceLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import purchase_invoice_line_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.purchase_invoice_line import PurchaseInvoiceLine
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
    api_instance = purchase_invoice_line_api.PurchaseInvoiceLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    purchase_invoice_line_id = "purchaseInvoiceLine_id_example" # str | (v1.0) id for purchaseInvoiceLine
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
        unit_of_measure=,
        unit_cost=3.14,
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
        expected_receipt_date=dateutil_parser('1970-01-01').date(),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type purchaseInvoiceLine in Dynamics 365 Business Central
        api_response = api_instance.patch_purchase_invoice_line(company_id, purchase_invoice_line_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceLineApi->patch_purchase_invoice_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **purchase_invoice_line_id** | **str**| (v1.0) id for purchaseInvoiceLine |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**PurchaseInvoiceLine**](PurchaseInvoiceLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedpurchaseInvoiceLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_purchase_invoice_line_for_purchase_invoice**
> PurchaseInvoiceLine patch_purchase_invoice_line_for_purchase_invoice(company_id, purchase_invoice_id, purchase_invoice_line_id, content_type, if_match, unknown_base_type)

Updates an object of type purchaseInvoiceLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import purchase_invoice_line_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.purchase_invoice_line import PurchaseInvoiceLine
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
    api_instance = purchase_invoice_line_api.PurchaseInvoiceLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    purchase_invoice_id = "purchaseInvoice_id_example" # str | (v1.0) id for purchaseInvoice
    purchase_invoice_line_id = "purchaseInvoiceLine_id_example" # str | (v1.0) id for purchaseInvoiceLine
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
        unit_of_measure=,
        unit_cost=3.14,
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
        expected_receipt_date=dateutil_parser('1970-01-01').date(),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type purchaseInvoiceLine in Dynamics 365 Business Central
        api_response = api_instance.patch_purchase_invoice_line_for_purchase_invoice(company_id, purchase_invoice_id, purchase_invoice_line_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceLineApi->patch_purchase_invoice_line_for_purchase_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **purchase_invoice_id** | **str**| (v1.0) id for purchaseInvoice |
 **purchase_invoice_line_id** | **str**| (v1.0) id for purchaseInvoiceLine |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**PurchaseInvoiceLine**](PurchaseInvoiceLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedpurchaseInvoiceLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_purchase_invoice_line**
> PurchaseInvoiceLine post_purchase_invoice_line(company_id, content_type, unknown_base_type)

Creates an object of type purchaseInvoiceLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import purchase_invoice_line_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.purchase_invoice_line import PurchaseInvoiceLine
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
    api_instance = purchase_invoice_line_api.PurchaseInvoiceLineApi(api_client)
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
        unit_of_measure=,
        unit_cost=3.14,
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
        expected_receipt_date=dateutil_parser('1970-01-01').date(),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type purchaseInvoiceLine in Dynamics 365 Business Central
        api_response = api_instance.post_purchase_invoice_line(company_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceLineApi->post_purchase_invoice_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**PurchaseInvoiceLine**](PurchaseInvoiceLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new purchaseInvoiceLine has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_purchase_invoice_line_for_purchase_invoice**
> PurchaseInvoiceLine post_purchase_invoice_line_for_purchase_invoice(company_id, purchase_invoice_id, content_type, unknown_base_type)

Creates an object of type purchaseInvoiceLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import purchase_invoice_line_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.purchase_invoice_line import PurchaseInvoiceLine
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
    api_instance = purchase_invoice_line_api.PurchaseInvoiceLineApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    purchase_invoice_id = "purchaseInvoice_id_example" # str | (v1.0) id for purchaseInvoice
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
        unit_of_measure=,
        unit_cost=3.14,
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
        expected_receipt_date=dateutil_parser('1970-01-01').date(),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type purchaseInvoiceLine in Dynamics 365 Business Central
        api_response = api_instance.post_purchase_invoice_line_for_purchase_invoice(company_id, purchase_invoice_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceLineApi->post_purchase_invoice_line_for_purchase_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **purchase_invoice_id** | **str**| (v1.0) id for purchaseInvoice |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**PurchaseInvoiceLine**](PurchaseInvoiceLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new purchaseInvoiceLine has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

