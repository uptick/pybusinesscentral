# pybusinesscentral.SalesCreditMemoApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_credit_memo**](SalesCreditMemoApi.md#delete_sales_credit_memo) | **DELETE** /companies({company_id})/salesCreditMemos({salesCreditMemo_id}) | Deletes an object of type salesCreditMemo in Dynamics 365 Business Central
[**get_sales_credit_memo**](SalesCreditMemoApi.md#get_sales_credit_memo) | **GET** /companies({company_id})/salesCreditMemos({salesCreditMemo_id}) | Retrieve the properties and relationships of an object of type salesCreditMemo for Dynamics 365 Business Central.
[**list_sales_credit_memos**](SalesCreditMemoApi.md#list_sales_credit_memos) | **GET** /companies({company_id})/salesCreditMemos | Returns a list of salesCreditMemos
[**patch_sales_credit_memo**](SalesCreditMemoApi.md#patch_sales_credit_memo) | **PATCH** /companies({company_id})/salesCreditMemos({salesCreditMemo_id}) | Updates an object of type salesCreditMemo in Dynamics 365 Business Central
[**post_action_sales_credit_memos**](SalesCreditMemoApi.md#post_action_sales_credit_memos) | **POST** /companies({company_id})/salesCreditMemos({salesCreditMemo_id})/Microsoft.NAV.post | Performs the post action for salesCreditMemos entity
[**post_and_send_action_sales_credit_memos**](SalesCreditMemoApi.md#post_and_send_action_sales_credit_memos) | **POST** /companies({company_id})/salesCreditMemos({salesCreditMemo_id}) | Performs the postAndSend action for salesCreditMemos entity
[**post_sales_credit_memo**](SalesCreditMemoApi.md#post_sales_credit_memo) | **POST** /companies({company_id})/salesCreditMemos | Creates an object of type salesCreditMemo in Dynamics 365 Business Central


# **delete_sales_credit_memo**
> delete_sales_credit_memo(company_id, sales_credit_memo_id)

Deletes an object of type salesCreditMemo in Dynamics 365 Business Central

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
    api_instance = pybusinesscentral.SalesCreditMemoApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    sales_credit_memo_id = 'sales_credit_memo_id_example' # str | (v1.0) id for salesCreditMemo

    try:
        # Deletes an object of type salesCreditMemo in Dynamics 365 Business Central
        api_instance.delete_sales_credit_memo(company_id, sales_credit_memo_id)
    except Exception as e:
        print("Exception when calling SalesCreditMemoApi->delete_sales_credit_memo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **sales_credit_memo_id** | **str**| (v1.0) id for salesCreditMemo | 

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
**204** | (v1.0) Succesfully deleted the specified salesCreditMemo |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_credit_memo**
> SalesCreditMemo get_sales_credit_memo(company_id, sales_credit_memo_id, expand=expand, select=select)

Retrieve the properties and relationships of an object of type salesCreditMemo for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.sales_credit_memo import SalesCreditMemo
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
    api_instance = pybusinesscentral.SalesCreditMemoApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    sales_credit_memo_id = 'sales_credit_memo_id_example' # str | (v1.0) id for salesCreditMemo
    expand = ['expand_example'] # List[str] | (v1.0) Entities to expand (optional)
    select = ['select_example'] # List[str] | (v1.0) Selected properties to be retrieved (optional)

    try:
        # Retrieve the properties and relationships of an object of type salesCreditMemo for Dynamics 365 Business Central.
        api_response = api_instance.get_sales_credit_memo(company_id, sales_credit_memo_id, expand=expand, select=select)
        print("The response of SalesCreditMemoApi->get_sales_credit_memo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesCreditMemoApi->get_sales_credit_memo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **sales_credit_memo_id** | **str**| (v1.0) id for salesCreditMemo | 
 **expand** | [**List[str]**](str.md)| (v1.0) Entities to expand | [optional] 
 **select** | [**List[str]**](str.md)| (v1.0) Selected properties to be retrieved | [optional] 

### Return type

[**SalesCreditMemo**](SalesCreditMemo.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested salesCreditMemo |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sales_credit_memos**
> ListSalesCreditMemos200Response list_sales_credit_memos(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)

Returns a list of salesCreditMemos

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.list_sales_credit_memos200_response import ListSalesCreditMemos200Response
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
    api_instance = pybusinesscentral.SalesCreditMemoApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    top = 56 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 56 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 56 # int | (v1.0) Number of items to return from the list (optional)
    filter = 'filter_example' # str | (v1.0) Filtering expression (optional)
    expand = ['expand_example'] # List[str] | (v1.0) Entities to expand (optional)
    select = ['select_example'] # List[str] | (v1.0) Selected properties to be retrieved (optional)

    try:
        # Returns a list of salesCreditMemos
        api_response = api_instance.list_sales_credit_memos(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        print("The response of SalesCreditMemoApi->list_sales_credit_memos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesCreditMemoApi->list_sales_credit_memos: %s\n" % e)
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

[**ListSalesCreditMemos200Response**](ListSalesCreditMemos200Response.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of salesCreditMemos |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sales_credit_memo**
> SalesCreditMemo patch_sales_credit_memo(company_id, sales_credit_memo_id, content_type, if_match, post_sales_credit_memo_request)

Updates an object of type salesCreditMemo in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.post_sales_credit_memo_request import PostSalesCreditMemoRequest
from pybusinesscentral.model.sales_credit_memo import SalesCreditMemo
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
    api_instance = pybusinesscentral.SalesCreditMemoApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    sales_credit_memo_id = 'sales_credit_memo_id_example' # str | (v1.0) id for salesCreditMemo
    content_type = 'content_type_example' # str | (v1.0) application/json
    if_match = 'if_match_example' # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    post_sales_credit_memo_request = pybusinesscentral.PostSalesCreditMemoRequest() # PostSalesCreditMemoRequest | 

    try:
        # Updates an object of type salesCreditMemo in Dynamics 365 Business Central
        api_response = api_instance.patch_sales_credit_memo(company_id, sales_credit_memo_id, content_type, if_match, post_sales_credit_memo_request)
        print("The response of SalesCreditMemoApi->patch_sales_credit_memo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesCreditMemoApi->patch_sales_credit_memo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **sales_credit_memo_id** | **str**| (v1.0) id for salesCreditMemo | 
 **content_type** | **str**| (v1.0) application/json | 
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. | 
 **post_sales_credit_memo_request** | [**PostSalesCreditMemoRequest**](PostSalesCreditMemoRequest.md)|  | 

### Return type

[**SalesCreditMemo**](SalesCreditMemo.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedsalesCreditMemo |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_action_sales_credit_memos**
> post_action_sales_credit_memos(company_id, sales_credit_memo_id)

Performs the post action for salesCreditMemos entity

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
    api_instance = pybusinesscentral.SalesCreditMemoApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    sales_credit_memo_id = 'sales_credit_memo_id_example' # str | (v1.0) id for salesCreditMemo

    try:
        # Performs the post action for salesCreditMemos entity
        api_instance.post_action_sales_credit_memos(company_id, sales_credit_memo_id)
    except Exception as e:
        print("Exception when calling SalesCreditMemoApi->post_action_sales_credit_memos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **sales_credit_memo_id** | **str**| (v1.0) id for salesCreditMemo | 

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
**204** | (v1.0) Succesfully performed a post action on the Dynamic 365 Business Central salesCreditMemos entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_and_send_action_sales_credit_memos**
> post_and_send_action_sales_credit_memos(company_id, sales_credit_memo_id)

Performs the postAndSend action for salesCreditMemos entity

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
    api_instance = pybusinesscentral.SalesCreditMemoApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    sales_credit_memo_id = 'sales_credit_memo_id_example' # str | (v1.0) id for salesCreditMemo

    try:
        # Performs the postAndSend action for salesCreditMemos entity
        api_instance.post_and_send_action_sales_credit_memos(company_id, sales_credit_memo_id)
    except Exception as e:
        print("Exception when calling SalesCreditMemoApi->post_and_send_action_sales_credit_memos: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **sales_credit_memo_id** | **str**| (v1.0) id for salesCreditMemo | 

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
**204** | (v1.0) Succesfully performed a postAndSend action on the Dynamic 365 Business Central salesCreditMemos entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_credit_memo**
> SalesCreditMemo post_sales_credit_memo(company_id, content_type, post_sales_credit_memo_request, expand=expand)

Creates an object of type salesCreditMemo in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.post_sales_credit_memo_request import PostSalesCreditMemoRequest
from pybusinesscentral.model.sales_credit_memo import SalesCreditMemo
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
    api_instance = pybusinesscentral.SalesCreditMemoApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    content_type = 'content_type_example' # str | (v1.0) application/json
    post_sales_credit_memo_request = pybusinesscentral.PostSalesCreditMemoRequest() # PostSalesCreditMemoRequest | 
    expand = ['expand_example'] # List[str] | (v1.0) Entities to expand (optional)

    try:
        # Creates an object of type salesCreditMemo in Dynamics 365 Business Central
        api_response = api_instance.post_sales_credit_memo(company_id, content_type, post_sales_credit_memo_request, expand=expand)
        print("The response of SalesCreditMemoApi->post_sales_credit_memo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesCreditMemoApi->post_sales_credit_memo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **content_type** | **str**| (v1.0) application/json | 
 **post_sales_credit_memo_request** | [**PostSalesCreditMemoRequest**](PostSalesCreditMemoRequest.md)|  | 
 **expand** | [**List[str]**](str.md)| (v1.0) Entities to expand | [optional] 

### Return type

[**SalesCreditMemo**](SalesCreditMemo.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new salesCreditMemo has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

