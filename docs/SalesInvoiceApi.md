# pybusinesscentral.SalesInvoiceApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_invoice**](SalesInvoiceApi.md#delete_sales_invoice) | **DELETE** /companies({company_id})/salesInvoices({salesInvoice_id}) | Deletes an object of type salesInvoice in Dynamics 365 Business Central
[**get_sales_invoice**](SalesInvoiceApi.md#get_sales_invoice) | **GET** /companies({company_id})/salesInvoices({salesInvoice_id}) | Retrieve the properties and relationships of an object of type salesInvoice for Dynamics 365 Business Central.
[**list_sales_invoices**](SalesInvoiceApi.md#list_sales_invoices) | **GET** /companies({company_id})/salesInvoices | Returns a list of salesInvoices
[**patch_sales_invoice**](SalesInvoiceApi.md#patch_sales_invoice) | **PATCH** /companies({company_id})/salesInvoices({salesInvoice_id}) | Updates an object of type salesInvoice in Dynamics 365 Business Central
[**post_action_sales_invoices**](SalesInvoiceApi.md#post_action_sales_invoices) | **POST** /companies({company_id})/salesInvoices({salesInvoice_id})/Microsoft.NAV.post | Performs the post action for salesInvoices entity
[**post_sales_invoice**](SalesInvoiceApi.md#post_sales_invoice) | **POST** /companies({company_id})/salesInvoices | Creates an object of type salesInvoice in Dynamics 365 Business Central


# **delete_sales_invoice**
> delete_sales_invoice(company_id, sales_invoice_id)

Deletes an object of type salesInvoice in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pybusinesscentral.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pybusinesscentral.SalesInvoiceApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    sales_invoice_id = 'sales_invoice_id_example' # str | (v1.0) id for salesInvoice

    try:
        # Deletes an object of type salesInvoice in Dynamics 365 Business Central
        api_instance.delete_sales_invoice(company_id, sales_invoice_id)
    except Exception as e:
        print("Exception when calling SalesInvoiceApi->delete_sales_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **sales_invoice_id** | **str**| (v1.0) id for salesInvoice | 

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
**204** | (v1.0) Succesfully deleted the specified salesInvoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_invoice**
> SalesInvoice get_sales_invoice(company_id, sales_invoice_id, expand=expand, select=select)

Retrieve the properties and relationships of an object of type salesInvoice for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.sales_invoice import SalesInvoice
from pybusinesscentral.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pybusinesscentral.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pybusinesscentral.SalesInvoiceApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    sales_invoice_id = 'sales_invoice_id_example' # str | (v1.0) id for salesInvoice
    expand = ['expand_example'] # List[str] | (v1.0) Entities to expand (optional)
    select = ['select_example'] # List[str] | (v1.0) Selected properties to be retrieved (optional)

    try:
        # Retrieve the properties and relationships of an object of type salesInvoice for Dynamics 365 Business Central.
        api_response = api_instance.get_sales_invoice(company_id, sales_invoice_id, expand=expand, select=select)
        print("The response of SalesInvoiceApi->get_sales_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesInvoiceApi->get_sales_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **sales_invoice_id** | **str**| (v1.0) id for salesInvoice | 
 **expand** | [**List[str]**](str.md)| (v1.0) Entities to expand | [optional] 
 **select** | [**List[str]**](str.md)| (v1.0) Selected properties to be retrieved | [optional] 

### Return type

[**SalesInvoice**](SalesInvoice.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested salesInvoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sales_invoices**
> ListSalesInvoices200Response list_sales_invoices(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)

Returns a list of salesInvoices

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.list_sales_invoices200_response import ListSalesInvoices200Response
from pybusinesscentral.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pybusinesscentral.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pybusinesscentral.SalesInvoiceApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    top = 56 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 56 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 56 # int | (v1.0) Number of items to return from the list (optional)
    filter = 'filter_example' # str | (v1.0) Filtering expression (optional)
    expand = ['expand_example'] # List[str] | (v1.0) Entities to expand (optional)
    select = ['select_example'] # List[str] | (v1.0) Selected properties to be retrieved (optional)

    try:
        # Returns a list of salesInvoices
        api_response = api_instance.list_sales_invoices(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        print("The response of SalesInvoiceApi->list_sales_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesInvoiceApi->list_sales_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional] 
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional] 
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional] 
 **filter** | **str**| (v1.0) Filtering expression | [optional] 
 **expand** | [**List[str]**](str.md)| (v1.0) Entities to expand | [optional] 
 **select** | [**List[str]**](str.md)| (v1.0) Selected properties to be retrieved | [optional] 

### Return type

[**ListSalesInvoices200Response**](ListSalesInvoices200Response.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of salesInvoices |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sales_invoice**
> SalesInvoice patch_sales_invoice(company_id, sales_invoice_id, content_type, if_match, post_sales_invoice_request)

Updates an object of type salesInvoice in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.post_sales_invoice_request import PostSalesInvoiceRequest
from pybusinesscentral.model.sales_invoice import SalesInvoice
from pybusinesscentral.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pybusinesscentral.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pybusinesscentral.SalesInvoiceApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    sales_invoice_id = 'sales_invoice_id_example' # str | (v1.0) id for salesInvoice
    content_type = 'content_type_example' # str | (v1.0) application/json
    if_match = 'if_match_example' # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    post_sales_invoice_request = pybusinesscentral.PostSalesInvoiceRequest() # PostSalesInvoiceRequest | 

    try:
        # Updates an object of type salesInvoice in Dynamics 365 Business Central
        api_response = api_instance.patch_sales_invoice(company_id, sales_invoice_id, content_type, if_match, post_sales_invoice_request)
        print("The response of SalesInvoiceApi->patch_sales_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesInvoiceApi->patch_sales_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **sales_invoice_id** | **str**| (v1.0) id for salesInvoice | 
 **content_type** | **str**| (v1.0) application/json | 
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. | 
 **post_sales_invoice_request** | [**PostSalesInvoiceRequest**](PostSalesInvoiceRequest.md)|  | 

### Return type

[**SalesInvoice**](SalesInvoice.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedsalesInvoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_action_sales_invoices**
> post_action_sales_invoices(company_id, sales_invoice_id)

Performs the post action for salesInvoices entity

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pybusinesscentral.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pybusinesscentral.SalesInvoiceApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    sales_invoice_id = 'sales_invoice_id_example' # str | (v1.0) id for salesInvoice

    try:
        # Performs the post action for salesInvoices entity
        api_instance.post_action_sales_invoices(company_id, sales_invoice_id)
    except Exception as e:
        print("Exception when calling SalesInvoiceApi->post_action_sales_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **sales_invoice_id** | **str**| (v1.0) id for salesInvoice | 

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
**204** | (v1.0) Succesfully performed a post action on the Dynamic 365 Business Central salesInvoices entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_invoice**
> SalesInvoice post_sales_invoice(company_id, content_type, post_sales_invoice_request, expand=expand)

Creates an object of type salesInvoice in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.post_sales_invoice_request import PostSalesInvoiceRequest
from pybusinesscentral.model.sales_invoice import SalesInvoice
from pybusinesscentral.rest import ApiException
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
with pybusinesscentral.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pybusinesscentral.SalesInvoiceApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    content_type = 'content_type_example' # str | (v1.0) application/json
    post_sales_invoice_request = pybusinesscentral.PostSalesInvoiceRequest() # PostSalesInvoiceRequest | 
    expand = ['expand_example'] # List[str] | (v1.0) Entities to expand (optional)

    try:
        # Creates an object of type salesInvoice in Dynamics 365 Business Central
        api_response = api_instance.post_sales_invoice(company_id, content_type, post_sales_invoice_request, expand=expand)
        print("The response of SalesInvoiceApi->post_sales_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesInvoiceApi->post_sales_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **content_type** | **str**| (v1.0) application/json | 
 **post_sales_invoice_request** | [**PostSalesInvoiceRequest**](PostSalesInvoiceRequest.md)|  | 
 **expand** | [**List[str]**](str.md)| (v1.0) Entities to expand | [optional] 

### Return type

[**SalesInvoice**](SalesInvoice.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new salesInvoice has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

