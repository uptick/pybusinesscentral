# pybusinesscentral.PictureApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_picture**](PictureApi.md#delete_picture) | **DELETE** /companies({company_id})/picture({picture_id}) | Deletes an object of type picture in Dynamics 365 Business Central
[**delete_picture_for_customer**](PictureApi.md#delete_picture_for_customer) | **DELETE** /companies({company_id})/customers({customer_id})/picture({picture_id}) | Deletes an object of type picture in Dynamics 365 Business Central
[**delete_picture_for_employee**](PictureApi.md#delete_picture_for_employee) | **DELETE** /companies({company_id})/employees({employee_id})/picture({picture_id}) | Deletes an object of type picture in Dynamics 365 Business Central
[**delete_picture_for_item**](PictureApi.md#delete_picture_for_item) | **DELETE** /companies({company_id})/items({item_id})/picture({picture_id}) | Deletes an object of type picture in Dynamics 365 Business Central
[**delete_picture_for_vendor**](PictureApi.md#delete_picture_for_vendor) | **DELETE** /companies({company_id})/vendors({vendor_id})/picture({picture_id}) | Deletes an object of type picture in Dynamics 365 Business Central
[**get_picture**](PictureApi.md#get_picture) | **GET** /companies({company_id})/picture({picture_id}) | Retrieve the properties and relationships of an object of type picture for Dynamics 365 Business Central.
[**get_picture_for_customer**](PictureApi.md#get_picture_for_customer) | **GET** /companies({company_id})/customers({customer_id})/picture({picture_id}) | Retrieve the properties and relationships of an object of type picture for Dynamics 365 Business Central.
[**get_picture_for_employee**](PictureApi.md#get_picture_for_employee) | **GET** /companies({company_id})/employees({employee_id})/picture({picture_id}) | Retrieve the properties and relationships of an object of type picture for Dynamics 365 Business Central.
[**get_picture_for_item**](PictureApi.md#get_picture_for_item) | **GET** /companies({company_id})/items({item_id})/picture({picture_id}) | Retrieve the properties and relationships of an object of type picture for Dynamics 365 Business Central.
[**get_picture_for_vendor**](PictureApi.md#get_picture_for_vendor) | **GET** /companies({company_id})/vendors({vendor_id})/picture({picture_id}) | Retrieve the properties and relationships of an object of type picture for Dynamics 365 Business Central.
[**list_picture**](PictureApi.md#list_picture) | **GET** /companies({company_id})/picture | Returns a list of picture
[**list_picture_for_customer**](PictureApi.md#list_picture_for_customer) | **GET** /companies({company_id})/customers({customer_id})/picture | Returns a list of picture
[**list_picture_for_employee**](PictureApi.md#list_picture_for_employee) | **GET** /companies({company_id})/employees({employee_id})/picture | Returns a list of picture
[**list_picture_for_item**](PictureApi.md#list_picture_for_item) | **GET** /companies({company_id})/items({item_id})/picture | Returns a list of picture
[**list_picture_for_vendor**](PictureApi.md#list_picture_for_vendor) | **GET** /companies({company_id})/vendors({vendor_id})/picture | Returns a list of picture
[**patch_picture**](PictureApi.md#patch_picture) | **PATCH** /companies({company_id})/picture({picture_id}) | Updates an object of type picture in Dynamics 365 Business Central
[**patch_picture_for_customer**](PictureApi.md#patch_picture_for_customer) | **PATCH** /companies({company_id})/customers({customer_id})/picture({picture_id}) | Updates an object of type picture in Dynamics 365 Business Central
[**patch_picture_for_employee**](PictureApi.md#patch_picture_for_employee) | **PATCH** /companies({company_id})/employees({employee_id})/picture({picture_id}) | Updates an object of type picture in Dynamics 365 Business Central
[**patch_picture_for_item**](PictureApi.md#patch_picture_for_item) | **PATCH** /companies({company_id})/items({item_id})/picture({picture_id}) | Updates an object of type picture in Dynamics 365 Business Central
[**patch_picture_for_vendor**](PictureApi.md#patch_picture_for_vendor) | **PATCH** /companies({company_id})/vendors({vendor_id})/picture({picture_id}) | Updates an object of type picture in Dynamics 365 Business Central


# **delete_picture**
> delete_picture(company_id, picture_id)

Deletes an object of type picture in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import picture_api
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
    api_instance = picture_api.PictureApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    picture_id = "picture_id_example" # str | (v1.0) id for picture

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type picture in Dynamics 365 Business Central
        api_instance.delete_picture(company_id, picture_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->delete_picture: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **picture_id** | **str**| (v1.0) id for picture |

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
**204** | (v1.0) Succesfully deleted the specified picture |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_picture_for_customer**
> delete_picture_for_customer(company_id, customer_id, picture_id)

Deletes an object of type picture in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import picture_api
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
    api_instance = picture_api.PictureApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    customer_id = "customer_id_example" # str | (v1.0) id for customer
    picture_id = "picture_id_example" # str | (v1.0) id for picture

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type picture in Dynamics 365 Business Central
        api_instance.delete_picture_for_customer(company_id, customer_id, picture_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->delete_picture_for_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **customer_id** | **str**| (v1.0) id for customer |
 **picture_id** | **str**| (v1.0) id for picture |

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
**204** | (v1.0) Succesfully deleted the specified picture |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_picture_for_employee**
> delete_picture_for_employee(company_id, employee_id, picture_id)

Deletes an object of type picture in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import picture_api
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
    api_instance = picture_api.PictureApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    employee_id = "employee_id_example" # str | (v1.0) id for employee
    picture_id = "picture_id_example" # str | (v1.0) id for picture

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type picture in Dynamics 365 Business Central
        api_instance.delete_picture_for_employee(company_id, employee_id, picture_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->delete_picture_for_employee: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **employee_id** | **str**| (v1.0) id for employee |
 **picture_id** | **str**| (v1.0) id for picture |

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
**204** | (v1.0) Succesfully deleted the specified picture |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_picture_for_item**
> delete_picture_for_item(company_id, item_id, picture_id)

Deletes an object of type picture in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import picture_api
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
    api_instance = picture_api.PictureApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    item_id = "item_id_example" # str | (v1.0) id for item
    picture_id = "picture_id_example" # str | (v1.0) id for picture

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type picture in Dynamics 365 Business Central
        api_instance.delete_picture_for_item(company_id, item_id, picture_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->delete_picture_for_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **item_id** | **str**| (v1.0) id for item |
 **picture_id** | **str**| (v1.0) id for picture |

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
**204** | (v1.0) Succesfully deleted the specified picture |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_picture_for_vendor**
> delete_picture_for_vendor(company_id, vendor_id, picture_id)

Deletes an object of type picture in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import picture_api
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
    api_instance = picture_api.PictureApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    vendor_id = "vendor_id_example" # str | (v1.0) id for vendor
    picture_id = "picture_id_example" # str | (v1.0) id for picture

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type picture in Dynamics 365 Business Central
        api_instance.delete_picture_for_vendor(company_id, vendor_id, picture_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->delete_picture_for_vendor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **vendor_id** | **str**| (v1.0) id for vendor |
 **picture_id** | **str**| (v1.0) id for picture |

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
**204** | (v1.0) Succesfully deleted the specified picture |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_picture**
> Picture get_picture(company_id, picture_id)

Retrieve the properties and relationships of an object of type picture for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import picture_api
from pybusinesscentral.model.picture import Picture
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
    api_instance = picture_api.PictureApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    picture_id = "picture_id_example" # str | (v1.0) id for picture
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type picture for Dynamics 365 Business Central.
        api_response = api_instance.get_picture(company_id, picture_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->get_picture: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type picture for Dynamics 365 Business Central.
        api_response = api_instance.get_picture(company_id, picture_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->get_picture: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **picture_id** | **str**| (v1.0) id for picture |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**Picture**](Picture.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested picture |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_picture_for_customer**
> Picture get_picture_for_customer(company_id, customer_id, picture_id)

Retrieve the properties and relationships of an object of type picture for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import picture_api
from pybusinesscentral.model.picture import Picture
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
    api_instance = picture_api.PictureApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    customer_id = "customer_id_example" # str | (v1.0) id for customer
    picture_id = "picture_id_example" # str | (v1.0) id for picture
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type picture for Dynamics 365 Business Central.
        api_response = api_instance.get_picture_for_customer(company_id, customer_id, picture_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->get_picture_for_customer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type picture for Dynamics 365 Business Central.
        api_response = api_instance.get_picture_for_customer(company_id, customer_id, picture_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->get_picture_for_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **customer_id** | **str**| (v1.0) id for customer |
 **picture_id** | **str**| (v1.0) id for picture |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**Picture**](Picture.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested picture |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_picture_for_employee**
> Picture get_picture_for_employee(company_id, employee_id, picture_id)

Retrieve the properties and relationships of an object of type picture for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import picture_api
from pybusinesscentral.model.picture import Picture
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
    api_instance = picture_api.PictureApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    employee_id = "employee_id_example" # str | (v1.0) id for employee
    picture_id = "picture_id_example" # str | (v1.0) id for picture
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type picture for Dynamics 365 Business Central.
        api_response = api_instance.get_picture_for_employee(company_id, employee_id, picture_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->get_picture_for_employee: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type picture for Dynamics 365 Business Central.
        api_response = api_instance.get_picture_for_employee(company_id, employee_id, picture_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->get_picture_for_employee: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **employee_id** | **str**| (v1.0) id for employee |
 **picture_id** | **str**| (v1.0) id for picture |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**Picture**](Picture.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested picture |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_picture_for_item**
> Picture get_picture_for_item(company_id, item_id, picture_id)

Retrieve the properties and relationships of an object of type picture for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import picture_api
from pybusinesscentral.model.picture import Picture
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
    api_instance = picture_api.PictureApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    item_id = "item_id_example" # str | (v1.0) id for item
    picture_id = "picture_id_example" # str | (v1.0) id for picture
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type picture for Dynamics 365 Business Central.
        api_response = api_instance.get_picture_for_item(company_id, item_id, picture_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->get_picture_for_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type picture for Dynamics 365 Business Central.
        api_response = api_instance.get_picture_for_item(company_id, item_id, picture_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->get_picture_for_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **item_id** | **str**| (v1.0) id for item |
 **picture_id** | **str**| (v1.0) id for picture |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**Picture**](Picture.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested picture |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_picture_for_vendor**
> Picture get_picture_for_vendor(company_id, vendor_id, picture_id)

Retrieve the properties and relationships of an object of type picture for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import picture_api
from pybusinesscentral.model.picture import Picture
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
    api_instance = picture_api.PictureApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    vendor_id = "vendor_id_example" # str | (v1.0) id for vendor
    picture_id = "picture_id_example" # str | (v1.0) id for picture
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type picture for Dynamics 365 Business Central.
        api_response = api_instance.get_picture_for_vendor(company_id, vendor_id, picture_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->get_picture_for_vendor: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type picture for Dynamics 365 Business Central.
        api_response = api_instance.get_picture_for_vendor(company_id, vendor_id, picture_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->get_picture_for_vendor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **vendor_id** | **str**| (v1.0) id for vendor |
 **picture_id** | **str**| (v1.0) id for picture |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**Picture**](Picture.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested picture |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_picture**
> InlineResponse2002 list_picture(company_id)

Returns a list of picture

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import picture_api
from pybusinesscentral.model.inline_response2002 import InlineResponse2002
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
    api_instance = picture_api.PictureApi(api_client)
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
        # Returns a list of picture
        api_response = api_instance.list_picture(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->list_picture: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of picture
        api_response = api_instance.list_picture(company_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->list_picture: %s\n" % e)
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

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of picture |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_picture_for_customer**
> InlineResponse2002 list_picture_for_customer(company_id, customer_id)

Returns a list of picture

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import picture_api
from pybusinesscentral.model.inline_response2002 import InlineResponse2002
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
    api_instance = picture_api.PictureApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    customer_id = "customer_id_example" # str | (v1.0) id for customer
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of picture
        api_response = api_instance.list_picture_for_customer(company_id, customer_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->list_picture_for_customer: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of picture
        api_response = api_instance.list_picture_for_customer(company_id, customer_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->list_picture_for_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **customer_id** | **str**| (v1.0) id for customer |
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional]
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional]
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional]
 **filter** | **str**| (v1.0) Filtering expression | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of picture |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_picture_for_employee**
> InlineResponse2002 list_picture_for_employee(company_id, employee_id)

Returns a list of picture

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import picture_api
from pybusinesscentral.model.inline_response2002 import InlineResponse2002
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
    api_instance = picture_api.PictureApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    employee_id = "employee_id_example" # str | (v1.0) id for employee
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of picture
        api_response = api_instance.list_picture_for_employee(company_id, employee_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->list_picture_for_employee: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of picture
        api_response = api_instance.list_picture_for_employee(company_id, employee_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->list_picture_for_employee: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **employee_id** | **str**| (v1.0) id for employee |
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional]
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional]
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional]
 **filter** | **str**| (v1.0) Filtering expression | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of picture |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_picture_for_item**
> InlineResponse2002 list_picture_for_item(company_id, item_id)

Returns a list of picture

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import picture_api
from pybusinesscentral.model.inline_response2002 import InlineResponse2002
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
    api_instance = picture_api.PictureApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    item_id = "item_id_example" # str | (v1.0) id for item
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of picture
        api_response = api_instance.list_picture_for_item(company_id, item_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->list_picture_for_item: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of picture
        api_response = api_instance.list_picture_for_item(company_id, item_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->list_picture_for_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **item_id** | **str**| (v1.0) id for item |
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional]
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional]
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional]
 **filter** | **str**| (v1.0) Filtering expression | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of picture |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_picture_for_vendor**
> InlineResponse2002 list_picture_for_vendor(company_id, vendor_id)

Returns a list of picture

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import picture_api
from pybusinesscentral.model.inline_response2002 import InlineResponse2002
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
    api_instance = picture_api.PictureApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    vendor_id = "vendor_id_example" # str | (v1.0) id for vendor
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of picture
        api_response = api_instance.list_picture_for_vendor(company_id, vendor_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->list_picture_for_vendor: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of picture
        api_response = api_instance.list_picture_for_vendor(company_id, vendor_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->list_picture_for_vendor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **vendor_id** | **str**| (v1.0) id for vendor |
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional]
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional]
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional]
 **filter** | **str**| (v1.0) Filtering expression | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse2002**](InlineResponse2002.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of picture |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_picture**
> Picture patch_picture(company_id, picture_id, content_type, if_match, unknown_base_type)

Updates an object of type picture in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import picture_api
from pybusinesscentral.model.picture import Picture
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
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
    api_instance = picture_api.PictureApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    picture_id = "picture_id_example" # str | (v1.0) id for picture
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        id="id_example",
        width=1,
        height=1,
        content_type="content_type_example",
        content=open('/path/to/file', 'rb'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type picture in Dynamics 365 Business Central
        api_response = api_instance.patch_picture(company_id, picture_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->patch_picture: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **picture_id** | **str**| (v1.0) id for picture |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**Picture**](Picture.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedpicture |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_picture_for_customer**
> Picture patch_picture_for_customer(company_id, customer_id, picture_id, content_type, if_match, unknown_base_type)

Updates an object of type picture in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import picture_api
from pybusinesscentral.model.picture import Picture
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
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
    api_instance = picture_api.PictureApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    customer_id = "customer_id_example" # str | (v1.0) id for customer
    picture_id = "picture_id_example" # str | (v1.0) id for picture
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        id="id_example",
        width=1,
        height=1,
        content_type="content_type_example",
        content=open('/path/to/file', 'rb'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type picture in Dynamics 365 Business Central
        api_response = api_instance.patch_picture_for_customer(company_id, customer_id, picture_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->patch_picture_for_customer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **customer_id** | **str**| (v1.0) id for customer |
 **picture_id** | **str**| (v1.0) id for picture |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**Picture**](Picture.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedpicture |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_picture_for_employee**
> Picture patch_picture_for_employee(company_id, employee_id, picture_id, content_type, if_match, unknown_base_type)

Updates an object of type picture in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import picture_api
from pybusinesscentral.model.picture import Picture
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
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
    api_instance = picture_api.PictureApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    employee_id = "employee_id_example" # str | (v1.0) id for employee
    picture_id = "picture_id_example" # str | (v1.0) id for picture
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        id="id_example",
        width=1,
        height=1,
        content_type="content_type_example",
        content=open('/path/to/file', 'rb'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type picture in Dynamics 365 Business Central
        api_response = api_instance.patch_picture_for_employee(company_id, employee_id, picture_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->patch_picture_for_employee: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **employee_id** | **str**| (v1.0) id for employee |
 **picture_id** | **str**| (v1.0) id for picture |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**Picture**](Picture.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedpicture |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_picture_for_item**
> Picture patch_picture_for_item(company_id, item_id, picture_id, content_type, if_match, unknown_base_type)

Updates an object of type picture in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import picture_api
from pybusinesscentral.model.picture import Picture
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
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
    api_instance = picture_api.PictureApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    item_id = "item_id_example" # str | (v1.0) id for item
    picture_id = "picture_id_example" # str | (v1.0) id for picture
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        id="id_example",
        width=1,
        height=1,
        content_type="content_type_example",
        content=open('/path/to/file', 'rb'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type picture in Dynamics 365 Business Central
        api_response = api_instance.patch_picture_for_item(company_id, item_id, picture_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->patch_picture_for_item: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **item_id** | **str**| (v1.0) id for item |
 **picture_id** | **str**| (v1.0) id for picture |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**Picture**](Picture.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedpicture |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_picture_for_vendor**
> Picture patch_picture_for_vendor(company_id, vendor_id, picture_id, content_type, if_match, unknown_base_type)

Updates an object of type picture in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import picture_api
from pybusinesscentral.model.picture import Picture
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
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
    api_instance = picture_api.PictureApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    vendor_id = "vendor_id_example" # str | (v1.0) id for vendor
    picture_id = "picture_id_example" # str | (v1.0) id for picture
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        id="id_example",
        width=1,
        height=1,
        content_type="content_type_example",
        content=open('/path/to/file', 'rb'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type picture in Dynamics 365 Business Central
        api_response = api_instance.patch_picture_for_vendor(company_id, vendor_id, picture_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PictureApi->patch_picture_for_vendor: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **vendor_id** | **str**| (v1.0) id for vendor |
 **picture_id** | **str**| (v1.0) id for picture |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**Picture**](Picture.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedpicture |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

