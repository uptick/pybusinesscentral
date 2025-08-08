# pybusinesscentral.PurchaseInvoiceApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_purchase_invoice**](PurchaseInvoiceApi.md#delete_purchase_invoice) | **DELETE** /companies({company_id})/purchaseInvoices({purchaseInvoice_id}) | Deletes an object of type purchaseInvoice in Dynamics 365 Business Central
[**get_purchase_invoice**](PurchaseInvoiceApi.md#get_purchase_invoice) | **GET** /companies({company_id})/purchaseInvoices({purchaseInvoice_id}) | Retrieve the properties and relationships of an object of type purchaseInvoice for Dynamics 365 Business Central.
[**list_purchase_invoices**](PurchaseInvoiceApi.md#list_purchase_invoices) | **GET** /companies({company_id})/purchaseInvoices | Returns a list of purchaseInvoices
[**patch_purchase_invoice**](PurchaseInvoiceApi.md#patch_purchase_invoice) | **PATCH** /companies({company_id})/purchaseInvoices({purchaseInvoice_id}) | Updates an object of type purchaseInvoice in Dynamics 365 Business Central
[**post_action_purchase_invoices**](PurchaseInvoiceApi.md#post_action_purchase_invoices) | **POST** /companies({company_id})/purchaseInvoices({purchaseInvoice_id})/Microsoft.NAV.post | Performs the post action for purchaseInvoices entity
[**post_purchase_invoice**](PurchaseInvoiceApi.md#post_purchase_invoice) | **POST** /companies({company_id})/purchaseInvoices | Creates an object of type purchaseInvoice in Dynamics 365 Business Central


# **delete_purchase_invoice**
> delete_purchase_invoice(company_id, purchase_invoice_id)

Deletes an object of type purchaseInvoice in Dynamics 365 Business Central

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
    api_instance = pybusinesscentral.PurchaseInvoiceApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    purchase_invoice_id = 'purchase_invoice_id_example' # str | (v1.0) id for purchaseInvoice

    try:
        # Deletes an object of type purchaseInvoice in Dynamics 365 Business Central
        api_instance.delete_purchase_invoice(company_id, purchase_invoice_id)
    except Exception as e:
        print("Exception when calling PurchaseInvoiceApi->delete_purchase_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **purchase_invoice_id** | **str**| (v1.0) id for purchaseInvoice | 

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
**204** | (v1.0) Succesfully deleted the specified purchaseInvoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase_invoice**
> PurchaseInvoice get_purchase_invoice(company_id, purchase_invoice_id, expand=expand, select=select)

Retrieve the properties and relationships of an object of type purchaseInvoice for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.purchase_invoice import PurchaseInvoice
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
    api_instance = pybusinesscentral.PurchaseInvoiceApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    purchase_invoice_id = 'purchase_invoice_id_example' # str | (v1.0) id for purchaseInvoice
    expand = ['expand_example'] # List[str] | (v1.0) Entities to expand (optional)
    select = ['select_example'] # List[str] | (v1.0) Selected properties to be retrieved (optional)

    try:
        # Retrieve the properties and relationships of an object of type purchaseInvoice for Dynamics 365 Business Central.
        api_response = api_instance.get_purchase_invoice(company_id, purchase_invoice_id, expand=expand, select=select)
        print("The response of PurchaseInvoiceApi->get_purchase_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseInvoiceApi->get_purchase_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **purchase_invoice_id** | **str**| (v1.0) id for purchaseInvoice | 
 **expand** | [**List[str]**](str.md)| (v1.0) Entities to expand | [optional] 
 **select** | [**List[str]**](str.md)| (v1.0) Selected properties to be retrieved | [optional] 

### Return type

[**PurchaseInvoice**](PurchaseInvoice.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested purchaseInvoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_purchase_invoices**
> ListPurchaseInvoices200Response list_purchase_invoices(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)

Returns a list of purchaseInvoices

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.list_purchase_invoices200_response import ListPurchaseInvoices200Response
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
    api_instance = pybusinesscentral.PurchaseInvoiceApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    top = 56 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 56 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 56 # int | (v1.0) Number of items to return from the list (optional)
    filter = 'filter_example' # str | (v1.0) Filtering expression (optional)
    expand = ['expand_example'] # List[str] | (v1.0) Entities to expand (optional)
    select = ['select_example'] # List[str] | (v1.0) Selected properties to be retrieved (optional)

    try:
        # Returns a list of purchaseInvoices
        api_response = api_instance.list_purchase_invoices(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        print("The response of PurchaseInvoiceApi->list_purchase_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseInvoiceApi->list_purchase_invoices: %s\n" % e)
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

[**ListPurchaseInvoices200Response**](ListPurchaseInvoices200Response.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of purchaseInvoices |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_purchase_invoice**
> PurchaseInvoice patch_purchase_invoice(company_id, purchase_invoice_id, content_type, if_match, post_purchase_invoice_request)

Updates an object of type purchaseInvoice in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.post_purchase_invoice_request import PostPurchaseInvoiceRequest
from pybusinesscentral.model.purchase_invoice import PurchaseInvoice
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
    api_instance = pybusinesscentral.PurchaseInvoiceApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    purchase_invoice_id = 'purchase_invoice_id_example' # str | (v1.0) id for purchaseInvoice
    content_type = 'content_type_example' # str | (v1.0) application/json
    if_match = 'if_match_example' # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    post_purchase_invoice_request = pybusinesscentral.PostPurchaseInvoiceRequest() # PostPurchaseInvoiceRequest | 

    try:
        # Updates an object of type purchaseInvoice in Dynamics 365 Business Central
        api_response = api_instance.patch_purchase_invoice(company_id, purchase_invoice_id, content_type, if_match, post_purchase_invoice_request)
        print("The response of PurchaseInvoiceApi->patch_purchase_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseInvoiceApi->patch_purchase_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **purchase_invoice_id** | **str**| (v1.0) id for purchaseInvoice | 
 **content_type** | **str**| (v1.0) application/json | 
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. | 
 **post_purchase_invoice_request** | [**PostPurchaseInvoiceRequest**](PostPurchaseInvoiceRequest.md)|  | 

### Return type

[**PurchaseInvoice**](PurchaseInvoice.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedpurchaseInvoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_action_purchase_invoices**
> post_action_purchase_invoices(company_id, purchase_invoice_id)

Performs the post action for purchaseInvoices entity

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
    api_instance = pybusinesscentral.PurchaseInvoiceApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    purchase_invoice_id = 'purchase_invoice_id_example' # str | (v1.0) id for purchaseInvoice

    try:
        # Performs the post action for purchaseInvoices entity
        api_instance.post_action_purchase_invoices(company_id, purchase_invoice_id)
    except Exception as e:
        print("Exception when calling PurchaseInvoiceApi->post_action_purchase_invoices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **purchase_invoice_id** | **str**| (v1.0) id for purchaseInvoice | 

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
**204** | (v1.0) Succesfully performed a post action on the Dynamic 365 Business Central purchaseInvoices entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_purchase_invoice**
> PurchaseInvoice post_purchase_invoice(company_id, content_type, post_purchase_invoice_request, expand=expand)

Creates an object of type purchaseInvoice in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.post_purchase_invoice_request import PostPurchaseInvoiceRequest
from pybusinesscentral.model.purchase_invoice import PurchaseInvoice
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
    api_instance = pybusinesscentral.PurchaseInvoiceApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    content_type = 'content_type_example' # str | (v1.0) application/json
    post_purchase_invoice_request = pybusinesscentral.PostPurchaseInvoiceRequest() # PostPurchaseInvoiceRequest | 
    expand = ['expand_example'] # List[str] | (v1.0) Entities to expand (optional)

    try:
        # Creates an object of type purchaseInvoice in Dynamics 365 Business Central
        api_response = api_instance.post_purchase_invoice(company_id, content_type, post_purchase_invoice_request, expand=expand)
        print("The response of PurchaseInvoiceApi->post_purchase_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PurchaseInvoiceApi->post_purchase_invoice: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **content_type** | **str**| (v1.0) application/json | 
 **post_purchase_invoice_request** | [**PostPurchaseInvoiceRequest**](PostPurchaseInvoiceRequest.md)|  | 
 **expand** | [**List[str]**](str.md)| (v1.0) Entities to expand | [optional] 

### Return type

[**PurchaseInvoice**](PurchaseInvoice.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new purchaseInvoice has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

