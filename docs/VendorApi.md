# pybusinesscentral.VendorApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_vendor**](VendorApi.md#delete_vendor) | **DELETE** /companies({company_id})/vendors({vendor_id}) | Deletes an object of type vendor in Dynamics 365 Business Central
[**get_vendor**](VendorApi.md#get_vendor) | **GET** /companies({company_id})/vendors({vendor_id}) | Retrieve the properties and relationships of an object of type vendor for Dynamics 365 Business Central.
[**list_vendors**](VendorApi.md#list_vendors) | **GET** /companies({company_id})/vendors | Returns a list of vendors
[**patch_vendor**](VendorApi.md#patch_vendor) | **PATCH** /companies({company_id})/vendors({vendor_id}) | Updates an object of type vendor in Dynamics 365 Business Central
[**post_vendor**](VendorApi.md#post_vendor) | **POST** /companies({company_id})/vendors | Creates an object of type vendor in Dynamics 365 Business Central


# **delete_vendor**
> delete_vendor(company_id, vendor_id)

Deletes an object of type vendor in Dynamics 365 Business Central

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
    api_instance = pybusinesscentral.VendorApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    vendor_id = 'vendor_id_example' # str | (v1.0) id for vendor

    try:
        # Deletes an object of type vendor in Dynamics 365 Business Central
        api_instance.delete_vendor(company_id, vendor_id)
    except Exception as e:
        print("Exception when calling VendorApi->delete_vendor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **vendor_id** | **str**| (v1.0) id for vendor | 

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
**204** | (v1.0) Succesfully deleted the specified vendor |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vendor**
> Vendor get_vendor(company_id, vendor_id, expand=expand, select=select)

Retrieve the properties and relationships of an object of type vendor for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.vendor import Vendor
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
    api_instance = pybusinesscentral.VendorApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    vendor_id = 'vendor_id_example' # str | (v1.0) id for vendor
    expand = ['expand_example'] # List[str] | (v1.0) Entities to expand (optional)
    select = ['select_example'] # List[str] | (v1.0) Selected properties to be retrieved (optional)

    try:
        # Retrieve the properties and relationships of an object of type vendor for Dynamics 365 Business Central.
        api_response = api_instance.get_vendor(company_id, vendor_id, expand=expand, select=select)
        print("The response of VendorApi->get_vendor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorApi->get_vendor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **vendor_id** | **str**| (v1.0) id for vendor | 
 **expand** | [**List[str]**](str.md)| (v1.0) Entities to expand | [optional] 
 **select** | [**List[str]**](str.md)| (v1.0) Selected properties to be retrieved | [optional] 

### Return type

[**Vendor**](Vendor.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested vendor |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vendors**
> ListVendors200Response list_vendors(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)

Returns a list of vendors

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.list_vendors200_response import ListVendors200Response
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
    api_instance = pybusinesscentral.VendorApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    top = 56 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 56 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 56 # int | (v1.0) Number of items to return from the list (optional)
    filter = 'filter_example' # str | (v1.0) Filtering expression (optional)
    expand = ['expand_example'] # List[str] | (v1.0) Entities to expand (optional)
    select = ['select_example'] # List[str] | (v1.0) Selected properties to be retrieved (optional)

    try:
        # Returns a list of vendors
        api_response = api_instance.list_vendors(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        print("The response of VendorApi->list_vendors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorApi->list_vendors: %s\n" % e)
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

[**ListVendors200Response**](ListVendors200Response.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of vendors |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_vendor**
> Vendor patch_vendor(company_id, vendor_id, content_type, if_match, post_vendor_request)

Updates an object of type vendor in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.post_vendor_request import PostVendorRequest
from pybusinesscentral.model.vendor import Vendor
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
    api_instance = pybusinesscentral.VendorApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    vendor_id = 'vendor_id_example' # str | (v1.0) id for vendor
    content_type = 'content_type_example' # str | (v1.0) application/json
    if_match = 'if_match_example' # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    post_vendor_request = pybusinesscentral.PostVendorRequest() # PostVendorRequest | 

    try:
        # Updates an object of type vendor in Dynamics 365 Business Central
        api_response = api_instance.patch_vendor(company_id, vendor_id, content_type, if_match, post_vendor_request)
        print("The response of VendorApi->patch_vendor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorApi->patch_vendor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **vendor_id** | **str**| (v1.0) id for vendor | 
 **content_type** | **str**| (v1.0) application/json | 
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. | 
 **post_vendor_request** | [**PostVendorRequest**](PostVendorRequest.md)|  | 

### Return type

[**Vendor**](Vendor.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedvendor |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_vendor**
> Vendor post_vendor(company_id, content_type, post_vendor_request, expand=expand)

Creates an object of type vendor in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.post_vendor_request import PostVendorRequest
from pybusinesscentral.model.vendor import Vendor
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
    api_instance = pybusinesscentral.VendorApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    content_type = 'content_type_example' # str | (v1.0) application/json
    post_vendor_request = pybusinesscentral.PostVendorRequest() # PostVendorRequest | 
    expand = ['expand_example'] # List[str] | (v1.0) Entities to expand (optional)

    try:
        # Creates an object of type vendor in Dynamics 365 Business Central
        api_response = api_instance.post_vendor(company_id, content_type, post_vendor_request, expand=expand)
        print("The response of VendorApi->post_vendor:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VendorApi->post_vendor: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **content_type** | **str**| (v1.0) application/json | 
 **post_vendor_request** | [**PostVendorRequest**](PostVendorRequest.md)|  | 
 **expand** | [**List[str]**](str.md)| (v1.0) Entities to expand | [optional] 

### Return type

[**Vendor**](Vendor.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new vendor has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

