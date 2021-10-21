# pybusinesscentral.TimeRegistrationEntryApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_time_registration_entry**](TimeRegistrationEntryApi.md#delete_time_registration_entry) | **DELETE** /companies({company_id})/timeRegistrationEntries({timeRegistrationEntry_id}) | Deletes an object of type timeRegistrationEntry in Dynamics 365 Business Central
[**delete_time_registration_entry_for_employee**](TimeRegistrationEntryApi.md#delete_time_registration_entry_for_employee) | **DELETE** /companies({company_id})/employees({employee_id})/timeRegistrationEntries({timeRegistrationEntry_id}) | Deletes an object of type timeRegistrationEntry in Dynamics 365 Business Central
[**get_time_registration_entry**](TimeRegistrationEntryApi.md#get_time_registration_entry) | **GET** /companies({company_id})/timeRegistrationEntries({timeRegistrationEntry_id}) | Retrieve the properties and relationships of an object of type timeRegistrationEntry for Dynamics 365 Business Central.
[**get_time_registration_entry_for_employee**](TimeRegistrationEntryApi.md#get_time_registration_entry_for_employee) | **GET** /companies({company_id})/employees({employee_id})/timeRegistrationEntries({timeRegistrationEntry_id}) | Retrieve the properties and relationships of an object of type timeRegistrationEntry for Dynamics 365 Business Central.
[**list_time_registration_entries**](TimeRegistrationEntryApi.md#list_time_registration_entries) | **GET** /companies({company_id})/timeRegistrationEntries | Returns a list of timeRegistrationEntries
[**list_time_registration_entries_for_employee**](TimeRegistrationEntryApi.md#list_time_registration_entries_for_employee) | **GET** /companies({company_id})/employees({employee_id})/timeRegistrationEntries | Returns a list of timeRegistrationEntries
[**patch_time_registration_entry**](TimeRegistrationEntryApi.md#patch_time_registration_entry) | **PATCH** /companies({company_id})/timeRegistrationEntries({timeRegistrationEntry_id}) | Updates an object of type timeRegistrationEntry in Dynamics 365 Business Central
[**patch_time_registration_entry_for_employee**](TimeRegistrationEntryApi.md#patch_time_registration_entry_for_employee) | **PATCH** /companies({company_id})/employees({employee_id})/timeRegistrationEntries({timeRegistrationEntry_id}) | Updates an object of type timeRegistrationEntry in Dynamics 365 Business Central
[**post_time_registration_entry**](TimeRegistrationEntryApi.md#post_time_registration_entry) | **POST** /companies({company_id})/timeRegistrationEntries | Creates an object of type timeRegistrationEntry in Dynamics 365 Business Central
[**post_time_registration_entry_for_employee**](TimeRegistrationEntryApi.md#post_time_registration_entry_for_employee) | **POST** /companies({company_id})/employees({employee_id})/timeRegistrationEntries | Creates an object of type timeRegistrationEntry in Dynamics 365 Business Central


# **delete_time_registration_entry**
> delete_time_registration_entry(company_id, time_registration_entry_id)

Deletes an object of type timeRegistrationEntry in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import time_registration_entry_api
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
    api_instance = time_registration_entry_api.TimeRegistrationEntryApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    time_registration_entry_id = "timeRegistrationEntry_id_example" # str | (v1.0) id for timeRegistrationEntry

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type timeRegistrationEntry in Dynamics 365 Business Central
        api_instance.delete_time_registration_entry(company_id, time_registration_entry_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling TimeRegistrationEntryApi->delete_time_registration_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **time_registration_entry_id** | **str**| (v1.0) id for timeRegistrationEntry |

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
**204** | (v1.0) Succesfully deleted the specified timeRegistrationEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_time_registration_entry_for_employee**
> delete_time_registration_entry_for_employee(company_id, employee_id, time_registration_entry_id)

Deletes an object of type timeRegistrationEntry in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import time_registration_entry_api
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
    api_instance = time_registration_entry_api.TimeRegistrationEntryApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    employee_id = "employee_id_example" # str | (v1.0) id for employee
    time_registration_entry_id = "timeRegistrationEntry_id_example" # str | (v1.0) id for timeRegistrationEntry

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type timeRegistrationEntry in Dynamics 365 Business Central
        api_instance.delete_time_registration_entry_for_employee(company_id, employee_id, time_registration_entry_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling TimeRegistrationEntryApi->delete_time_registration_entry_for_employee: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **employee_id** | **str**| (v1.0) id for employee |
 **time_registration_entry_id** | **str**| (v1.0) id for timeRegistrationEntry |

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
**204** | (v1.0) Succesfully deleted the specified timeRegistrationEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_registration_entry**
> TimeRegistrationEntry get_time_registration_entry(company_id, time_registration_entry_id)

Retrieve the properties and relationships of an object of type timeRegistrationEntry for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import time_registration_entry_api
from pybusinesscentral.model.time_registration_entry import TimeRegistrationEntry
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
    api_instance = time_registration_entry_api.TimeRegistrationEntryApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    time_registration_entry_id = "timeRegistrationEntry_id_example" # str | (v1.0) id for timeRegistrationEntry
    expand = [
        "project",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type timeRegistrationEntry for Dynamics 365 Business Central.
        api_response = api_instance.get_time_registration_entry(company_id, time_registration_entry_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling TimeRegistrationEntryApi->get_time_registration_entry: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type timeRegistrationEntry for Dynamics 365 Business Central.
        api_response = api_instance.get_time_registration_entry(company_id, time_registration_entry_id, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling TimeRegistrationEntryApi->get_time_registration_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **time_registration_entry_id** | **str**| (v1.0) id for timeRegistrationEntry |
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**TimeRegistrationEntry**](TimeRegistrationEntry.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested timeRegistrationEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_registration_entry_for_employee**
> TimeRegistrationEntry get_time_registration_entry_for_employee(company_id, employee_id, time_registration_entry_id)

Retrieve the properties and relationships of an object of type timeRegistrationEntry for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import time_registration_entry_api
from pybusinesscentral.model.time_registration_entry import TimeRegistrationEntry
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
    api_instance = time_registration_entry_api.TimeRegistrationEntryApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    employee_id = "employee_id_example" # str | (v1.0) id for employee
    time_registration_entry_id = "timeRegistrationEntry_id_example" # str | (v1.0) id for timeRegistrationEntry
    expand = [
        "project",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type timeRegistrationEntry for Dynamics 365 Business Central.
        api_response = api_instance.get_time_registration_entry_for_employee(company_id, employee_id, time_registration_entry_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling TimeRegistrationEntryApi->get_time_registration_entry_for_employee: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type timeRegistrationEntry for Dynamics 365 Business Central.
        api_response = api_instance.get_time_registration_entry_for_employee(company_id, employee_id, time_registration_entry_id, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling TimeRegistrationEntryApi->get_time_registration_entry_for_employee: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **employee_id** | **str**| (v1.0) id for employee |
 **time_registration_entry_id** | **str**| (v1.0) id for timeRegistrationEntry |
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**TimeRegistrationEntry**](TimeRegistrationEntry.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested timeRegistrationEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_time_registration_entries**
> InlineResponse20019 list_time_registration_entries(company_id)

Returns a list of timeRegistrationEntries

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import time_registration_entry_api
from pybusinesscentral.model.inline_response20019 import InlineResponse20019
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
    api_instance = time_registration_entry_api.TimeRegistrationEntryApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    expand = [
        "project",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of timeRegistrationEntries
        api_response = api_instance.list_time_registration_entries(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling TimeRegistrationEntryApi->list_time_registration_entries: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of timeRegistrationEntries
        api_response = api_instance.list_time_registration_entries(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling TimeRegistrationEntryApi->list_time_registration_entries: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional]
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional]
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional]
 **filter** | **str**| (v1.0) Filtering expression | [optional]
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of timeRegistrationEntries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_time_registration_entries_for_employee**
> InlineResponse20019 list_time_registration_entries_for_employee(company_id, employee_id)

Returns a list of timeRegistrationEntries

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import time_registration_entry_api
from pybusinesscentral.model.inline_response20019 import InlineResponse20019
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
    api_instance = time_registration_entry_api.TimeRegistrationEntryApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    employee_id = "employee_id_example" # str | (v1.0) id for employee
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    expand = [
        "project",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of timeRegistrationEntries
        api_response = api_instance.list_time_registration_entries_for_employee(company_id, employee_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling TimeRegistrationEntryApi->list_time_registration_entries_for_employee: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of timeRegistrationEntries
        api_response = api_instance.list_time_registration_entries_for_employee(company_id, employee_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling TimeRegistrationEntryApi->list_time_registration_entries_for_employee: %s\n" % e)
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
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse20019**](InlineResponse20019.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of timeRegistrationEntries |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_time_registration_entry**
> TimeRegistrationEntry patch_time_registration_entry(company_id, time_registration_entry_id, content_type, if_match, unknown_base_type)

Updates an object of type timeRegistrationEntry in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import time_registration_entry_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.time_registration_entry import TimeRegistrationEntry
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
    api_instance = time_registration_entry_api.TimeRegistrationEntryApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    time_registration_entry_id = "timeRegistrationEntry_id_example" # str | (v1.0) id for timeRegistrationEntry
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        id="id_example",
        employee_id="employee_id_example",
        employee_number="employee_number_example",
        job_id="job_id_example",
        job_number="job_number_example",
        absence="absence_example",
        line_number=1,
        date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        quantity=3.14,
        status="status_example",
        unit_of_measure_id="unit_of_measure_id_example",
        unit_of_measure=,
        dimensions=[
            ,
        ],
        last_modfied_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type timeRegistrationEntry in Dynamics 365 Business Central
        api_response = api_instance.patch_time_registration_entry(company_id, time_registration_entry_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling TimeRegistrationEntryApi->patch_time_registration_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **time_registration_entry_id** | **str**| (v1.0) id for timeRegistrationEntry |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**TimeRegistrationEntry**](TimeRegistrationEntry.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedtimeRegistrationEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_time_registration_entry_for_employee**
> TimeRegistrationEntry patch_time_registration_entry_for_employee(company_id, employee_id, time_registration_entry_id, content_type, if_match, unknown_base_type)

Updates an object of type timeRegistrationEntry in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import time_registration_entry_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.time_registration_entry import TimeRegistrationEntry
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
    api_instance = time_registration_entry_api.TimeRegistrationEntryApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    employee_id = "employee_id_example" # str | (v1.0) id for employee
    time_registration_entry_id = "timeRegistrationEntry_id_example" # str | (v1.0) id for timeRegistrationEntry
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        id="id_example",
        employee_id="employee_id_example",
        employee_number="employee_number_example",
        job_id="job_id_example",
        job_number="job_number_example",
        absence="absence_example",
        line_number=1,
        date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        quantity=3.14,
        status="status_example",
        unit_of_measure_id="unit_of_measure_id_example",
        unit_of_measure=,
        dimensions=[
            ,
        ],
        last_modfied_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type timeRegistrationEntry in Dynamics 365 Business Central
        api_response = api_instance.patch_time_registration_entry_for_employee(company_id, employee_id, time_registration_entry_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling TimeRegistrationEntryApi->patch_time_registration_entry_for_employee: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **employee_id** | **str**| (v1.0) id for employee |
 **time_registration_entry_id** | **str**| (v1.0) id for timeRegistrationEntry |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**TimeRegistrationEntry**](TimeRegistrationEntry.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedtimeRegistrationEntry |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_time_registration_entry**
> TimeRegistrationEntry post_time_registration_entry(company_id, content_type, unknown_base_type)

Creates an object of type timeRegistrationEntry in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import time_registration_entry_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.time_registration_entry import TimeRegistrationEntry
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
    api_instance = time_registration_entry_api.TimeRegistrationEntryApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    content_type = "Content-Type_example" # str | (v1.0) application/json
    unknown_base_type = {
        id="id_example",
        employee_id="employee_id_example",
        employee_number="employee_number_example",
        job_id="job_id_example",
        job_number="job_number_example",
        absence="absence_example",
        line_number=1,
        date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        quantity=3.14,
        status="status_example",
        unit_of_measure_id="unit_of_measure_id_example",
        unit_of_measure=,
        dimensions=[
            ,
        ],
        last_modfied_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type timeRegistrationEntry in Dynamics 365 Business Central
        api_response = api_instance.post_time_registration_entry(company_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling TimeRegistrationEntryApi->post_time_registration_entry: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**TimeRegistrationEntry**](TimeRegistrationEntry.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new timeRegistrationEntry has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_time_registration_entry_for_employee**
> TimeRegistrationEntry post_time_registration_entry_for_employee(company_id, employee_id, content_type, unknown_base_type)

Creates an object of type timeRegistrationEntry in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import time_registration_entry_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.time_registration_entry import TimeRegistrationEntry
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
    api_instance = time_registration_entry_api.TimeRegistrationEntryApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    employee_id = "employee_id_example" # str | (v1.0) id for employee
    content_type = "Content-Type_example" # str | (v1.0) application/json
    unknown_base_type = {
        id="id_example",
        employee_id="employee_id_example",
        employee_number="employee_number_example",
        job_id="job_id_example",
        job_number="job_number_example",
        absence="absence_example",
        line_number=1,
        date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        quantity=3.14,
        status="status_example",
        unit_of_measure_id="unit_of_measure_id_example",
        unit_of_measure=,
        dimensions=[
            ,
        ],
        last_modfied_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type timeRegistrationEntry in Dynamics 365 Business Central
        api_response = api_instance.post_time_registration_entry_for_employee(company_id, employee_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling TimeRegistrationEntryApi->post_time_registration_entry_for_employee: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **employee_id** | **str**| (v1.0) id for employee |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**TimeRegistrationEntry**](TimeRegistrationEntry.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new timeRegistrationEntry has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

