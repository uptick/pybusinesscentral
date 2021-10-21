# pybusinesscentral.VendorPurchaseApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_vendor_purchase**](VendorPurchaseApi.md#get_vendor_purchase) | **GET** /companies({company_id})/vendorPurchases({vendorPurchase_vendorId},&#39;{vendorPurchase_vendorNumber}&#39;,&#39;{vendorPurchase_name}&#39;) | Retrieve the properties and relationships of an object of type vendorPurchase for Dynamics 365 Business Central.
[**list_vendor_purchases**](VendorPurchaseApi.md#list_vendor_purchases) | **GET** /companies({company_id})/vendorPurchases | Returns a list of vendorPurchases


# **get_vendor_purchase**
> VendorPurchase get_vendor_purchase(company_id, vendor_purchase_vendor_id, vendor_purchase_vendor_number, vendor_purchase_name)

Retrieve the properties and relationships of an object of type vendorPurchase for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import vendor_purchase_api
from pybusinesscentral.model.vendor_purchase import VendorPurchase
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
    api_instance = vendor_purchase_api.VendorPurchaseApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    vendor_purchase_vendor_id = "vendorPurchase_vendorId_example" # str | (v1.0) vendorId for vendorPurchase
    vendor_purchase_vendor_number = "vendorPurchase_vendorNumber_example" # str | (v1.0) vendorNumber for vendorPurchase
    vendor_purchase_name = "vendorPurchase_name_example" # str | (v1.0) name for vendorPurchase
    select = [
        "vendorId",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type vendorPurchase for Dynamics 365 Business Central.
        api_response = api_instance.get_vendor_purchase(company_id, vendor_purchase_vendor_id, vendor_purchase_vendor_number, vendor_purchase_name)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling VendorPurchaseApi->get_vendor_purchase: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type vendorPurchase for Dynamics 365 Business Central.
        api_response = api_instance.get_vendor_purchase(company_id, vendor_purchase_vendor_id, vendor_purchase_vendor_number, vendor_purchase_name, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling VendorPurchaseApi->get_vendor_purchase: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **vendor_purchase_vendor_id** | **str**| (v1.0) vendorId for vendorPurchase |
 **vendor_purchase_vendor_number** | **str**| (v1.0) vendorNumber for vendorPurchase |
 **vendor_purchase_name** | **str**| (v1.0) name for vendorPurchase |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**VendorPurchase**](VendorPurchase.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested vendorPurchase |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_vendor_purchases**
> InlineResponse20051 list_vendor_purchases(company_id)

Returns a list of vendorPurchases

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import vendor_purchase_api
from pybusinesscentral.model.inline_response20051 import InlineResponse20051
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
    api_instance = vendor_purchase_api.VendorPurchaseApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "vendorId",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of vendorPurchases
        api_response = api_instance.list_vendor_purchases(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling VendorPurchaseApi->list_vendor_purchases: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of vendorPurchases
        api_response = api_instance.list_vendor_purchases(company_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling VendorPurchaseApi->list_vendor_purchases: %s\n" % e)
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

[**InlineResponse20051**](InlineResponse20051.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of vendorPurchases |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

