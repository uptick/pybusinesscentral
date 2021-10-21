# pybusinesscentral.ShipmentMethodApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_shipment_method**](ShipmentMethodApi.md#delete_shipment_method) | **DELETE** /companies({company_id})/shipmentMethods({shipmentMethod_id}) | Deletes an object of type shipmentMethod in Dynamics 365 Business Central
[**get_shipment_method**](ShipmentMethodApi.md#get_shipment_method) | **GET** /companies({company_id})/shipmentMethods({shipmentMethod_id}) | Retrieve the properties and relationships of an object of type shipmentMethod for Dynamics 365 Business Central.
[**list_shipment_methods**](ShipmentMethodApi.md#list_shipment_methods) | **GET** /companies({company_id})/shipmentMethods | Returns a list of shipmentMethods
[**patch_shipment_method**](ShipmentMethodApi.md#patch_shipment_method) | **PATCH** /companies({company_id})/shipmentMethods({shipmentMethod_id}) | Updates an object of type shipmentMethod in Dynamics 365 Business Central
[**post_shipment_method**](ShipmentMethodApi.md#post_shipment_method) | **POST** /companies({company_id})/shipmentMethods | Creates an object of type shipmentMethod in Dynamics 365 Business Central


# **delete_shipment_method**
> delete_shipment_method(company_id, shipment_method_id)

Deletes an object of type shipmentMethod in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import shipment_method_api
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
    api_instance = shipment_method_api.ShipmentMethodApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    shipment_method_id = "shipmentMethod_id_example" # str | (v1.0) id for shipmentMethod

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type shipmentMethod in Dynamics 365 Business Central
        api_instance.delete_shipment_method(company_id, shipment_method_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling ShipmentMethodApi->delete_shipment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **shipment_method_id** | **str**| (v1.0) id for shipmentMethod |

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
**204** | (v1.0) Succesfully deleted the specified shipmentMethod |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shipment_method**
> ShipmentMethod get_shipment_method(company_id, shipment_method_id)

Retrieve the properties and relationships of an object of type shipmentMethod for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import shipment_method_api
from pybusinesscentral.model.shipment_method import ShipmentMethod
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
    api_instance = shipment_method_api.ShipmentMethodApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    shipment_method_id = "shipmentMethod_id_example" # str | (v1.0) id for shipmentMethod
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type shipmentMethod for Dynamics 365 Business Central.
        api_response = api_instance.get_shipment_method(company_id, shipment_method_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling ShipmentMethodApi->get_shipment_method: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type shipmentMethod for Dynamics 365 Business Central.
        api_response = api_instance.get_shipment_method(company_id, shipment_method_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling ShipmentMethodApi->get_shipment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **shipment_method_id** | **str**| (v1.0) id for shipmentMethod |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**ShipmentMethod**](ShipmentMethod.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested shipmentMethod |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_shipment_methods**
> InlineResponse20027 list_shipment_methods(company_id)

Returns a list of shipmentMethods

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import shipment_method_api
from pybusinesscentral.model.inline_response20027 import InlineResponse20027
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
    api_instance = shipment_method_api.ShipmentMethodApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of shipmentMethods
        api_response = api_instance.list_shipment_methods(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling ShipmentMethodApi->list_shipment_methods: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of shipmentMethods
        api_response = api_instance.list_shipment_methods(company_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling ShipmentMethodApi->list_shipment_methods: %s\n" % e)
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

[**InlineResponse20027**](InlineResponse20027.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of shipmentMethods |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_shipment_method**
> ShipmentMethod patch_shipment_method(company_id, shipment_method_id, content_type, if_match, unknown_base_type)

Updates an object of type shipmentMethod in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import shipment_method_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.shipment_method import ShipmentMethod
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
    api_instance = shipment_method_api.ShipmentMethodApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    shipment_method_id = "shipmentMethod_id_example" # str | (v1.0) id for shipmentMethod
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        id="id_example",
        code="code_example",
        display_name="display_name_example",
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type shipmentMethod in Dynamics 365 Business Central
        api_response = api_instance.patch_shipment_method(company_id, shipment_method_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling ShipmentMethodApi->patch_shipment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **shipment_method_id** | **str**| (v1.0) id for shipmentMethod |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**ShipmentMethod**](ShipmentMethod.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedshipmentMethod |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_shipment_method**
> ShipmentMethod post_shipment_method(company_id, content_type, unknown_base_type)

Creates an object of type shipmentMethod in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import shipment_method_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.shipment_method import ShipmentMethod
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
    api_instance = shipment_method_api.ShipmentMethodApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    content_type = "Content-Type_example" # str | (v1.0) application/json
    unknown_base_type = {
        id="id_example",
        code="code_example",
        display_name="display_name_example",
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type shipmentMethod in Dynamics 365 Business Central
        api_response = api_instance.post_shipment_method(company_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling ShipmentMethodApi->post_shipment_method: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**ShipmentMethod**](ShipmentMethod.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new shipmentMethod has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

