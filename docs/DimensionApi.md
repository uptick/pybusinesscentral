# pybusinesscentral.DimensionApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dimension**](DimensionApi.md#get_dimension) | **GET** /companies({company_id})/dimensions({dimension_id}) | Retrieve the properties and relationships of an object of type dimension for Dynamics 365 Business Central.
[**list_dimensions**](DimensionApi.md#list_dimensions) | **GET** /companies({company_id})/dimensions | Returns a list of dimensions


# **get_dimension**
> Dimension get_dimension(company_id, dimension_id, expand=expand, select=select)

Retrieve the properties and relationships of an object of type dimension for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.dimension import Dimension
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
    api_instance = pybusinesscentral.DimensionApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    dimension_id = 'dimension_id_example' # str | (v1.0) id for dimension
    expand = ['expand_example'] # List[str] | (v1.0) Entities to expand (optional)
    select = ['select_example'] # List[str] | (v1.0) Selected properties to be retrieved (optional)

    try:
        # Retrieve the properties and relationships of an object of type dimension for Dynamics 365 Business Central.
        api_response = api_instance.get_dimension(company_id, dimension_id, expand=expand, select=select)
        print("The response of DimensionApi->get_dimension:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DimensionApi->get_dimension: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **dimension_id** | **str**| (v1.0) id for dimension | 
 **expand** | [**List[str]**](str.md)| (v1.0) Entities to expand | [optional] 
 **select** | [**List[str]**](str.md)| (v1.0) Selected properties to be retrieved | [optional] 

### Return type

[**Dimension**](Dimension.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested dimension |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_dimensions**
> ListDimensions200Response list_dimensions(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)

Returns a list of dimensions

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.list_dimensions200_response import ListDimensions200Response
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
    api_instance = pybusinesscentral.DimensionApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    top = 56 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 56 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 56 # int | (v1.0) Number of items to return from the list (optional)
    filter = 'filter_example' # str | (v1.0) Filtering expression (optional)
    expand = ['expand_example'] # List[str] | (v1.0) Entities to expand (optional)
    select = ['select_example'] # List[str] | (v1.0) Selected properties to be retrieved (optional)

    try:
        # Returns a list of dimensions
        api_response = api_instance.list_dimensions(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        print("The response of DimensionApi->list_dimensions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DimensionApi->list_dimensions: %s\n" % e)
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

[**ListDimensions200Response**](ListDimensions200Response.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of dimensions |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

