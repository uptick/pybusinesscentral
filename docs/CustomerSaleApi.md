# pybusinesscentral.CustomerSaleApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_customer_sale**](CustomerSaleApi.md#get_customer_sale) | **GET** /companies({company_id})/customerSales({customerSale_customerId},&#39;{customerSale_customerNumber}&#39;,&#39;{customerSale_name}&#39;) | Retrieve the properties and relationships of an object of type customerSale for Dynamics 365 Business Central.
[**list_customer_sales**](CustomerSaleApi.md#list_customer_sales) | **GET** /companies({company_id})/customerSales | Returns a list of customerSales


# **get_customer_sale**
> CustomerSale get_customer_sale(company_id, customer_sale_customer_id, customer_sale_customer_number, customer_sale_name)

Retrieve the properties and relationships of an object of type customerSale for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import customer_sale_api
from pybusinesscentral.model.customer_sale import CustomerSale
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
    api_instance = customer_sale_api.CustomerSaleApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    customer_sale_customer_id = "customerSale_customerId_example" # str | (v1.0) customerId for customerSale
    customer_sale_customer_number = "customerSale_customerNumber_example" # str | (v1.0) customerNumber for customerSale
    customer_sale_name = "customerSale_name_example" # str | (v1.0) name for customerSale
    select = [
        "customerId",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type customerSale for Dynamics 365 Business Central.
        api_response = api_instance.get_customer_sale(company_id, customer_sale_customer_id, customer_sale_customer_number, customer_sale_name)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerSaleApi->get_customer_sale: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type customerSale for Dynamics 365 Business Central.
        api_response = api_instance.get_customer_sale(company_id, customer_sale_customer_id, customer_sale_customer_number, customer_sale_name, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerSaleApi->get_customer_sale: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **customer_sale_customer_id** | **str**| (v1.0) customerId for customerSale |
 **customer_sale_customer_number** | **str**| (v1.0) customerNumber for customerSale |
 **customer_sale_name** | **str**| (v1.0) name for customerSale |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**CustomerSale**](CustomerSale.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested customerSale |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_sales**
> InlineResponse20050 list_customer_sales(company_id)

Returns a list of customerSales

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import customer_sale_api
from pybusinesscentral.model.inline_response20050 import InlineResponse20050
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
    api_instance = customer_sale_api.CustomerSaleApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "customerId",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of customerSales
        api_response = api_instance.list_customer_sales(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerSaleApi->list_customer_sales: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of customerSales
        api_response = api_instance.list_customer_sales(company_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerSaleApi->list_customer_sales: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional]
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional]
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional]
 **filter** | **str**| (v1.0) Filtering expression | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse20050**](InlineResponse20050.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of customerSales |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

