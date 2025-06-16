# pybusinesscentral.SalesCreditMemoLineApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_credit_memo_line_for_sales_credit_memo**](SalesCreditMemoLineApi.md#delete_sales_credit_memo_line_for_sales_credit_memo) | **DELETE** /companies({company_id})/salesCreditMemos({salesCreditMemo_id})/salesCreditMemoLines(&#39;{salesCreditMemoLine_id}&#39;) | Deletes an object of type salesCreditMemoLine in Dynamics 365 Business Central
[**get_sales_credit_memo_line_for_sales_credit_memo**](SalesCreditMemoLineApi.md#get_sales_credit_memo_line_for_sales_credit_memo) | **GET** /companies({company_id})/salesCreditMemos({salesCreditMemo_id})/salesCreditMemoLines(&#39;{salesCreditMemoLine_id}&#39;) | Retrieve the properties and relationships of an object of type salesCreditMemoLine for Dynamics 365 Business Central.
[**list_sales_credit_memo_lines**](SalesCreditMemoLineApi.md#list_sales_credit_memo_lines) | **GET** /companies({company_id})/salesCreditMemoLines | Returns a list of salesCreditMemoLines
[**list_sales_credit_memo_lines_for_sales_credit_memo**](SalesCreditMemoLineApi.md#list_sales_credit_memo_lines_for_sales_credit_memo) | **GET** /companies({company_id})/salesCreditMemos({salesCreditMemo_id})/salesCreditMemoLines | Returns a list of salesCreditMemoLines
[**patch_sales_credit_memo_line_for_sales_credit_memo**](SalesCreditMemoLineApi.md#patch_sales_credit_memo_line_for_sales_credit_memo) | **PATCH** /companies({company_id})/salesCreditMemos({salesCreditMemo_id})/salesCreditMemoLines(&#39;{salesCreditMemoLine_id}&#39;) | Updates an object of type salesCreditMemoLine in Dynamics 365 Business Central
[**post_sales_credit_memo_line**](SalesCreditMemoLineApi.md#post_sales_credit_memo_line) | **POST** /companies({company_id})/salesCreditMemoLines | Creates an object of type salesCreditMemoLine in Dynamics 365 Business Central
[**post_sales_credit_memo_line_for_sales_credit_memo**](SalesCreditMemoLineApi.md#post_sales_credit_memo_line_for_sales_credit_memo) | **POST** /companies({company_id})/salesCreditMemos({salesCreditMemo_id})/salesCreditMemoLines | Creates an object of type salesCreditMemoLine in Dynamics 365 Business Central


# **delete_sales_credit_memo_line_for_sales_credit_memo**
> delete_sales_credit_memo_line_for_sales_credit_memo(company_id, sales_credit_memo_id, sales_credit_memo_line_id)

Deletes an object of type salesCreditMemoLine in Dynamics 365 Business Central

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
    api_instance = pybusinesscentral.SalesCreditMemoLineApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    sales_credit_memo_id = 'sales_credit_memo_id_example' # str | (v1.0) id for salesCreditMemo
    sales_credit_memo_line_id = 'sales_credit_memo_line_id_example' # str | (v1.0) id for salesCreditMemoLine

    try:
        # Deletes an object of type salesCreditMemoLine in Dynamics 365 Business Central
        api_instance.delete_sales_credit_memo_line_for_sales_credit_memo(company_id, sales_credit_memo_id, sales_credit_memo_line_id)
    except Exception as e:
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

# **get_sales_credit_memo_line_for_sales_credit_memo**
> SalesCreditMemoLine get_sales_credit_memo_line_for_sales_credit_memo(company_id, sales_credit_memo_id, sales_credit_memo_line_id, expand=expand, select=select)

Retrieve the properties and relationships of an object of type salesCreditMemoLine for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.sales_credit_memo_line import SalesCreditMemoLine
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
    api_instance = pybusinesscentral.SalesCreditMemoLineApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    sales_credit_memo_id = 'sales_credit_memo_id_example' # str | (v1.0) id for salesCreditMemo
    sales_credit_memo_line_id = 'sales_credit_memo_line_id_example' # str | (v1.0) id for salesCreditMemoLine
    expand = ['expand_example'] # List[str] | (v1.0) Entities to expand (optional)
    select = ['select_example'] # List[str] | (v1.0) Selected properties to be retrieved (optional)

    try:
        # Retrieve the properties and relationships of an object of type salesCreditMemoLine for Dynamics 365 Business Central.
        api_response = api_instance.get_sales_credit_memo_line_for_sales_credit_memo(company_id, sales_credit_memo_id, sales_credit_memo_line_id, expand=expand, select=select)
        print("The response of SalesCreditMemoLineApi->get_sales_credit_memo_line_for_sales_credit_memo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesCreditMemoLineApi->get_sales_credit_memo_line_for_sales_credit_memo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **sales_credit_memo_id** | **str**| (v1.0) id for salesCreditMemo | 
 **sales_credit_memo_line_id** | **str**| (v1.0) id for salesCreditMemoLine | 
 **expand** | [**List[str]**](str.md)| (v1.0) Entities to expand | [optional] 
 **select** | [**List[str]**](str.md)| (v1.0) Selected properties to be retrieved | [optional] 

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
> ListSalesCreditMemoLinesForSalesCreditMemo200Response list_sales_credit_memo_lines(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)

Returns a list of salesCreditMemoLines

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.list_sales_credit_memo_lines_for_sales_credit_memo200_response import ListSalesCreditMemoLinesForSalesCreditMemo200Response
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
    api_instance = pybusinesscentral.SalesCreditMemoLineApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    top = 56 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 56 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 56 # int | (v1.0) Number of items to return from the list (optional)
    filter = 'filter_example' # str | (v1.0) Filtering expression (optional)
    expand = ['expand_example'] # List[str] | (v1.0) Entities to expand (optional)
    select = ['select_example'] # List[str] | (v1.0) Selected properties to be retrieved (optional)

    try:
        # Returns a list of salesCreditMemoLines
        api_response = api_instance.list_sales_credit_memo_lines(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        print("The response of SalesCreditMemoLineApi->list_sales_credit_memo_lines:\n")
        pprint(api_response)
    except Exception as e:
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
 **expand** | [**List[str]**](str.md)| (v1.0) Entities to expand | [optional] 
 **select** | [**List[str]**](str.md)| (v1.0) Selected properties to be retrieved | [optional] 

### Return type

[**ListSalesCreditMemoLinesForSalesCreditMemo200Response**](ListSalesCreditMemoLinesForSalesCreditMemo200Response.md)

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
> ListSalesCreditMemoLinesForSalesCreditMemo200Response list_sales_credit_memo_lines_for_sales_credit_memo(company_id, sales_credit_memo_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)

Returns a list of salesCreditMemoLines

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.list_sales_credit_memo_lines_for_sales_credit_memo200_response import ListSalesCreditMemoLinesForSalesCreditMemo200Response
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
    api_instance = pybusinesscentral.SalesCreditMemoLineApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    sales_credit_memo_id = 'sales_credit_memo_id_example' # str | (v1.0) id for salesCreditMemo
    top = 56 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 56 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 56 # int | (v1.0) Number of items to return from the list (optional)
    filter = 'filter_example' # str | (v1.0) Filtering expression (optional)
    expand = ['expand_example'] # List[str] | (v1.0) Entities to expand (optional)
    select = ['select_example'] # List[str] | (v1.0) Selected properties to be retrieved (optional)

    try:
        # Returns a list of salesCreditMemoLines
        api_response = api_instance.list_sales_credit_memo_lines_for_sales_credit_memo(company_id, sales_credit_memo_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        print("The response of SalesCreditMemoLineApi->list_sales_credit_memo_lines_for_sales_credit_memo:\n")
        pprint(api_response)
    except Exception as e:
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
 **expand** | [**List[str]**](str.md)| (v1.0) Entities to expand | [optional] 
 **select** | [**List[str]**](str.md)| (v1.0) Selected properties to be retrieved | [optional] 

### Return type

[**ListSalesCreditMemoLinesForSalesCreditMemo200Response**](ListSalesCreditMemoLinesForSalesCreditMemo200Response.md)

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

# **patch_sales_credit_memo_line_for_sales_credit_memo**
> SalesCreditMemoLine patch_sales_credit_memo_line_for_sales_credit_memo(company_id, sales_credit_memo_id, sales_credit_memo_line_id, content_type, if_match, post_sales_credit_memo_line_for_sales_credit_memo_request)

Updates an object of type salesCreditMemoLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.post_sales_credit_memo_line_for_sales_credit_memo_request import PostSalesCreditMemoLineForSalesCreditMemoRequest
from pybusinesscentral.model.sales_credit_memo_line import SalesCreditMemoLine
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
    api_instance = pybusinesscentral.SalesCreditMemoLineApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    sales_credit_memo_id = 'sales_credit_memo_id_example' # str | (v1.0) id for salesCreditMemo
    sales_credit_memo_line_id = 'sales_credit_memo_line_id_example' # str | (v1.0) id for salesCreditMemoLine
    content_type = 'content_type_example' # str | (v1.0) application/json
    if_match = 'if_match_example' # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    post_sales_credit_memo_line_for_sales_credit_memo_request = pybusinesscentral.PostSalesCreditMemoLineForSalesCreditMemoRequest() # PostSalesCreditMemoLineForSalesCreditMemoRequest | 

    try:
        # Updates an object of type salesCreditMemoLine in Dynamics 365 Business Central
        api_response = api_instance.patch_sales_credit_memo_line_for_sales_credit_memo(company_id, sales_credit_memo_id, sales_credit_memo_line_id, content_type, if_match, post_sales_credit_memo_line_for_sales_credit_memo_request)
        print("The response of SalesCreditMemoLineApi->patch_sales_credit_memo_line_for_sales_credit_memo:\n")
        pprint(api_response)
    except Exception as e:
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
 **post_sales_credit_memo_line_for_sales_credit_memo_request** | [**PostSalesCreditMemoLineForSalesCreditMemoRequest**](PostSalesCreditMemoLineForSalesCreditMemoRequest.md)|  | 

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
> SalesCreditMemoLine post_sales_credit_memo_line(company_id, content_type, post_sales_credit_memo_line_for_sales_credit_memo_request)

Creates an object of type salesCreditMemoLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.post_sales_credit_memo_line_for_sales_credit_memo_request import PostSalesCreditMemoLineForSalesCreditMemoRequest
from pybusinesscentral.model.sales_credit_memo_line import SalesCreditMemoLine
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
    api_instance = pybusinesscentral.SalesCreditMemoLineApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    content_type = 'content_type_example' # str | (v1.0) application/json
    post_sales_credit_memo_line_for_sales_credit_memo_request = pybusinesscentral.PostSalesCreditMemoLineForSalesCreditMemoRequest() # PostSalesCreditMemoLineForSalesCreditMemoRequest | 

    try:
        # Creates an object of type salesCreditMemoLine in Dynamics 365 Business Central
        api_response = api_instance.post_sales_credit_memo_line(company_id, content_type, post_sales_credit_memo_line_for_sales_credit_memo_request)
        print("The response of SalesCreditMemoLineApi->post_sales_credit_memo_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesCreditMemoLineApi->post_sales_credit_memo_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **content_type** | **str**| (v1.0) application/json | 
 **post_sales_credit_memo_line_for_sales_credit_memo_request** | [**PostSalesCreditMemoLineForSalesCreditMemoRequest**](PostSalesCreditMemoLineForSalesCreditMemoRequest.md)|  | 

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
> SalesCreditMemoLine post_sales_credit_memo_line_for_sales_credit_memo(company_id, sales_credit_memo_id, content_type, post_sales_credit_memo_line_for_sales_credit_memo_request)

Creates an object of type salesCreditMemoLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.post_sales_credit_memo_line_for_sales_credit_memo_request import PostSalesCreditMemoLineForSalesCreditMemoRequest
from pybusinesscentral.model.sales_credit_memo_line import SalesCreditMemoLine
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
    api_instance = pybusinesscentral.SalesCreditMemoLineApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    sales_credit_memo_id = 'sales_credit_memo_id_example' # str | (v1.0) id for salesCreditMemo
    content_type = 'content_type_example' # str | (v1.0) application/json
    post_sales_credit_memo_line_for_sales_credit_memo_request = pybusinesscentral.PostSalesCreditMemoLineForSalesCreditMemoRequest() # PostSalesCreditMemoLineForSalesCreditMemoRequest | 

    try:
        # Creates an object of type salesCreditMemoLine in Dynamics 365 Business Central
        api_response = api_instance.post_sales_credit_memo_line_for_sales_credit_memo(company_id, sales_credit_memo_id, content_type, post_sales_credit_memo_line_for_sales_credit_memo_request)
        print("The response of SalesCreditMemoLineApi->post_sales_credit_memo_line_for_sales_credit_memo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SalesCreditMemoLineApi->post_sales_credit_memo_line_for_sales_credit_memo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **sales_credit_memo_id** | **str**| (v1.0) id for salesCreditMemo | 
 **content_type** | **str**| (v1.0) application/json | 
 **post_sales_credit_memo_line_for_sales_credit_memo_request** | [**PostSalesCreditMemoLineForSalesCreditMemoRequest**](PostSalesCreditMemoLineForSalesCreditMemoRequest.md)|  | 

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

