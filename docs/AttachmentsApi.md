# pybusinesscentral.AttachmentsApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_attachments**](AttachmentsApi.md#delete_attachments) | **DELETE** /companies({company_id})/attachments({attachments_parentId},{attachments_id}) | Deletes an object of type attachments in Dynamics 365 Business Central
[**delete_attachments_for_journal_line**](AttachmentsApi.md#delete_attachments_for_journal_line) | **DELETE** /companies({company_id})/journalLines({journalLine_id})/attachments({attachments_parentId},{attachments_id}) | Deletes an object of type attachments in Dynamics 365 Business Central
[**delete_attachments_for_journal_line_for_journal**](AttachmentsApi.md#delete_attachments_for_journal_line_for_journal) | **DELETE** /companies({company_id})/journals({journal_id})/journalLines({journalLine_id})/attachments({attachments_parentId},{attachments_id}) | Deletes an object of type attachments in Dynamics 365 Business Central
[**get_attachments**](AttachmentsApi.md#get_attachments) | **GET** /companies({company_id})/attachments({attachments_parentId},{attachments_id}) | Retrieve the properties and relationships of an object of type attachments for Dynamics 365 Business Central.
[**get_attachments_for_journal_line**](AttachmentsApi.md#get_attachments_for_journal_line) | **GET** /companies({company_id})/journalLines({journalLine_id})/attachments({attachments_parentId},{attachments_id}) | Retrieve the properties and relationships of an object of type attachments for Dynamics 365 Business Central.
[**get_attachments_for_journal_line_for_journal**](AttachmentsApi.md#get_attachments_for_journal_line_for_journal) | **GET** /companies({company_id})/journals({journal_id})/journalLines({journalLine_id})/attachments({attachments_parentId},{attachments_id}) | Retrieve the properties and relationships of an object of type attachments for Dynamics 365 Business Central.
[**list_attachments**](AttachmentsApi.md#list_attachments) | **GET** /companies({company_id})/attachments | Returns a list of attachments
[**list_attachments_for_journal_line**](AttachmentsApi.md#list_attachments_for_journal_line) | **GET** /companies({company_id})/journalLines({journalLine_id})/attachments | Returns a list of attachments
[**list_attachments_for_journal_line_for_journal**](AttachmentsApi.md#list_attachments_for_journal_line_for_journal) | **GET** /companies({company_id})/journals({journal_id})/journalLines({journalLine_id})/attachments | Returns a list of attachments
[**patch_attachments**](AttachmentsApi.md#patch_attachments) | **PATCH** /companies({company_id})/attachments({attachments_parentId},{attachments_id}) | Updates an object of type attachments in Dynamics 365 Business Central
[**patch_attachments_for_journal_line**](AttachmentsApi.md#patch_attachments_for_journal_line) | **PATCH** /companies({company_id})/journalLines({journalLine_id})/attachments({attachments_parentId},{attachments_id}) | Updates an object of type attachments in Dynamics 365 Business Central
[**patch_attachments_for_journal_line_for_journal**](AttachmentsApi.md#patch_attachments_for_journal_line_for_journal) | **PATCH** /companies({company_id})/journals({journal_id})/journalLines({journalLine_id})/attachments({attachments_parentId},{attachments_id}) | Updates an object of type attachments in Dynamics 365 Business Central
[**post_attachments**](AttachmentsApi.md#post_attachments) | **POST** /companies({company_id})/attachments | Creates an object of type attachments in Dynamics 365 Business Central
[**post_attachments_for_journal_line**](AttachmentsApi.md#post_attachments_for_journal_line) | **POST** /companies({company_id})/journalLines({journalLine_id})/attachments | Creates an object of type attachments in Dynamics 365 Business Central
[**post_attachments_for_journal_line_for_journal**](AttachmentsApi.md#post_attachments_for_journal_line_for_journal) | **POST** /companies({company_id})/journals({journal_id})/journalLines({journalLine_id})/attachments | Creates an object of type attachments in Dynamics 365 Business Central


# **delete_attachments**
> delete_attachments(company_id, attachments_parent_id, attachments_id)

Deletes an object of type attachments in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import attachments_api
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    attachments_parent_id = "attachments_parentId_example" # str | (v1.0) parentId for attachments
    attachments_id = "attachments_id_example" # str | (v1.0) id for attachments

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type attachments in Dynamics 365 Business Central
        api_instance.delete_attachments(company_id, attachments_parent_id, attachments_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->delete_attachments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **attachments_parent_id** | **str**| (v1.0) parentId for attachments |
 **attachments_id** | **str**| (v1.0) id for attachments |

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
**204** | (v1.0) Succesfully deleted the specified attachments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attachments_for_journal_line**
> delete_attachments_for_journal_line(company_id, journal_line_id, attachments_parent_id, attachments_id)

Deletes an object of type attachments in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import attachments_api
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    journal_line_id = "journalLine_id_example" # str | (v1.0) id for journalLine
    attachments_parent_id = "attachments_parentId_example" # str | (v1.0) parentId for attachments
    attachments_id = "attachments_id_example" # str | (v1.0) id for attachments

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type attachments in Dynamics 365 Business Central
        api_instance.delete_attachments_for_journal_line(company_id, journal_line_id, attachments_parent_id, attachments_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->delete_attachments_for_journal_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **journal_line_id** | **str**| (v1.0) id for journalLine |
 **attachments_parent_id** | **str**| (v1.0) parentId for attachments |
 **attachments_id** | **str**| (v1.0) id for attachments |

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
**204** | (v1.0) Succesfully deleted the specified attachments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_attachments_for_journal_line_for_journal**
> delete_attachments_for_journal_line_for_journal(company_id, journal_id, journal_line_id, attachments_parent_id, attachments_id)

Deletes an object of type attachments in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import attachments_api
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    journal_id = "journal_id_example" # str | (v1.0) id for journal
    journal_line_id = "journalLine_id_example" # str | (v1.0) id for journalLine
    attachments_parent_id = "attachments_parentId_example" # str | (v1.0) parentId for attachments
    attachments_id = "attachments_id_example" # str | (v1.0) id for attachments

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type attachments in Dynamics 365 Business Central
        api_instance.delete_attachments_for_journal_line_for_journal(company_id, journal_id, journal_line_id, attachments_parent_id, attachments_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->delete_attachments_for_journal_line_for_journal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **journal_id** | **str**| (v1.0) id for journal |
 **journal_line_id** | **str**| (v1.0) id for journalLine |
 **attachments_parent_id** | **str**| (v1.0) parentId for attachments |
 **attachments_id** | **str**| (v1.0) id for attachments |

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
**204** | (v1.0) Succesfully deleted the specified attachments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachments**
> Attachments get_attachments(company_id, attachments_parent_id, attachments_id)

Retrieve the properties and relationships of an object of type attachments for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import attachments_api
from pybusinesscentral.model.attachments import Attachments
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    attachments_parent_id = "attachments_parentId_example" # str | (v1.0) parentId for attachments
    attachments_id = "attachments_id_example" # str | (v1.0) id for attachments
    select = [
        "parentId",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type attachments for Dynamics 365 Business Central.
        api_response = api_instance.get_attachments(company_id, attachments_parent_id, attachments_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type attachments for Dynamics 365 Business Central.
        api_response = api_instance.get_attachments(company_id, attachments_parent_id, attachments_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **attachments_parent_id** | **str**| (v1.0) parentId for attachments |
 **attachments_id** | **str**| (v1.0) id for attachments |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**Attachments**](Attachments.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested attachments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachments_for_journal_line**
> Attachments get_attachments_for_journal_line(company_id, journal_line_id, attachments_parent_id, attachments_id)

Retrieve the properties and relationships of an object of type attachments for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import attachments_api
from pybusinesscentral.model.attachments import Attachments
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    journal_line_id = "journalLine_id_example" # str | (v1.0) id for journalLine
    attachments_parent_id = "attachments_parentId_example" # str | (v1.0) parentId for attachments
    attachments_id = "attachments_id_example" # str | (v1.0) id for attachments
    select = [
        "parentId",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type attachments for Dynamics 365 Business Central.
        api_response = api_instance.get_attachments_for_journal_line(company_id, journal_line_id, attachments_parent_id, attachments_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachments_for_journal_line: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type attachments for Dynamics 365 Business Central.
        api_response = api_instance.get_attachments_for_journal_line(company_id, journal_line_id, attachments_parent_id, attachments_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachments_for_journal_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **journal_line_id** | **str**| (v1.0) id for journalLine |
 **attachments_parent_id** | **str**| (v1.0) parentId for attachments |
 **attachments_id** | **str**| (v1.0) id for attachments |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**Attachments**](Attachments.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested attachments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attachments_for_journal_line_for_journal**
> Attachments get_attachments_for_journal_line_for_journal(company_id, journal_id, journal_line_id, attachments_parent_id, attachments_id)

Retrieve the properties and relationships of an object of type attachments for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import attachments_api
from pybusinesscentral.model.attachments import Attachments
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    journal_id = "journal_id_example" # str | (v1.0) id for journal
    journal_line_id = "journalLine_id_example" # str | (v1.0) id for journalLine
    attachments_parent_id = "attachments_parentId_example" # str | (v1.0) parentId for attachments
    attachments_id = "attachments_id_example" # str | (v1.0) id for attachments
    select = [
        "parentId",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type attachments for Dynamics 365 Business Central.
        api_response = api_instance.get_attachments_for_journal_line_for_journal(company_id, journal_id, journal_line_id, attachments_parent_id, attachments_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachments_for_journal_line_for_journal: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type attachments for Dynamics 365 Business Central.
        api_response = api_instance.get_attachments_for_journal_line_for_journal(company_id, journal_id, journal_line_id, attachments_parent_id, attachments_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->get_attachments_for_journal_line_for_journal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **journal_id** | **str**| (v1.0) id for journal |
 **journal_line_id** | **str**| (v1.0) id for journalLine |
 **attachments_parent_id** | **str**| (v1.0) parentId for attachments |
 **attachments_id** | **str**| (v1.0) id for attachments |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**Attachments**](Attachments.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested attachments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_attachments**
> InlineResponse20017 list_attachments(company_id)

Returns a list of attachments

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import attachments_api
from pybusinesscentral.model.inline_response20017 import InlineResponse20017
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "parentId",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of attachments
        api_response = api_instance.list_attachments(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->list_attachments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of attachments
        api_response = api_instance.list_attachments(company_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->list_attachments: %s\n" % e)
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

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of attachments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_attachments_for_journal_line**
> InlineResponse20017 list_attachments_for_journal_line(company_id, journal_line_id)

Returns a list of attachments

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import attachments_api
from pybusinesscentral.model.inline_response20017 import InlineResponse20017
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    journal_line_id = "journalLine_id_example" # str | (v1.0) id for journalLine
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "parentId",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of attachments
        api_response = api_instance.list_attachments_for_journal_line(company_id, journal_line_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->list_attachments_for_journal_line: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of attachments
        api_response = api_instance.list_attachments_for_journal_line(company_id, journal_line_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->list_attachments_for_journal_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **journal_line_id** | **str**| (v1.0) id for journalLine |
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional]
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional]
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional]
 **filter** | **str**| (v1.0) Filtering expression | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of attachments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_attachments_for_journal_line_for_journal**
> InlineResponse20017 list_attachments_for_journal_line_for_journal(company_id, journal_id, journal_line_id)

Returns a list of attachments

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import attachments_api
from pybusinesscentral.model.inline_response20017 import InlineResponse20017
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    journal_id = "journal_id_example" # str | (v1.0) id for journal
    journal_line_id = "journalLine_id_example" # str | (v1.0) id for journalLine
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "parentId",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of attachments
        api_response = api_instance.list_attachments_for_journal_line_for_journal(company_id, journal_id, journal_line_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->list_attachments_for_journal_line_for_journal: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of attachments
        api_response = api_instance.list_attachments_for_journal_line_for_journal(company_id, journal_id, journal_line_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->list_attachments_for_journal_line_for_journal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **journal_id** | **str**| (v1.0) id for journal |
 **journal_line_id** | **str**| (v1.0) id for journalLine |
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional]
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional]
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional]
 **filter** | **str**| (v1.0) Filtering expression | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse20017**](InlineResponse20017.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of attachments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_attachments**
> Attachments patch_attachments(company_id, attachments_parent_id, attachments_id, content_type, if_match, unknown_base_type)

Updates an object of type attachments in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import attachments_api
from pybusinesscentral.model.attachments import Attachments
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    attachments_parent_id = "attachments_parentId_example" # str | (v1.0) parentId for attachments
    attachments_id = "attachments_id_example" # str | (v1.0) id for attachments
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        parent_id="parent_id_example",
        id="id_example",
        file_name="file_name_example",
        byte_size=1,
        content=open('/path/to/file', 'rb'),
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type attachments in Dynamics 365 Business Central
        api_response = api_instance.patch_attachments(company_id, attachments_parent_id, attachments_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->patch_attachments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **attachments_parent_id** | **str**| (v1.0) parentId for attachments |
 **attachments_id** | **str**| (v1.0) id for attachments |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedattachments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_attachments_for_journal_line**
> Attachments patch_attachments_for_journal_line(company_id, journal_line_id, attachments_parent_id, attachments_id, content_type, if_match, unknown_base_type)

Updates an object of type attachments in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import attachments_api
from pybusinesscentral.model.attachments import Attachments
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    journal_line_id = "journalLine_id_example" # str | (v1.0) id for journalLine
    attachments_parent_id = "attachments_parentId_example" # str | (v1.0) parentId for attachments
    attachments_id = "attachments_id_example" # str | (v1.0) id for attachments
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        parent_id="parent_id_example",
        id="id_example",
        file_name="file_name_example",
        byte_size=1,
        content=open('/path/to/file', 'rb'),
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type attachments in Dynamics 365 Business Central
        api_response = api_instance.patch_attachments_for_journal_line(company_id, journal_line_id, attachments_parent_id, attachments_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->patch_attachments_for_journal_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **journal_line_id** | **str**| (v1.0) id for journalLine |
 **attachments_parent_id** | **str**| (v1.0) parentId for attachments |
 **attachments_id** | **str**| (v1.0) id for attachments |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedattachments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_attachments_for_journal_line_for_journal**
> Attachments patch_attachments_for_journal_line_for_journal(company_id, journal_id, journal_line_id, attachments_parent_id, attachments_id, content_type, if_match, unknown_base_type)

Updates an object of type attachments in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import attachments_api
from pybusinesscentral.model.attachments import Attachments
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    journal_id = "journal_id_example" # str | (v1.0) id for journal
    journal_line_id = "journalLine_id_example" # str | (v1.0) id for journalLine
    attachments_parent_id = "attachments_parentId_example" # str | (v1.0) parentId for attachments
    attachments_id = "attachments_id_example" # str | (v1.0) id for attachments
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        parent_id="parent_id_example",
        id="id_example",
        file_name="file_name_example",
        byte_size=1,
        content=open('/path/to/file', 'rb'),
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type attachments in Dynamics 365 Business Central
        api_response = api_instance.patch_attachments_for_journal_line_for_journal(company_id, journal_id, journal_line_id, attachments_parent_id, attachments_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->patch_attachments_for_journal_line_for_journal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **journal_id** | **str**| (v1.0) id for journal |
 **journal_line_id** | **str**| (v1.0) id for journalLine |
 **attachments_parent_id** | **str**| (v1.0) parentId for attachments |
 **attachments_id** | **str**| (v1.0) id for attachments |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedattachments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_attachments**
> Attachments post_attachments(company_id, content_type, unknown_base_type)

Creates an object of type attachments in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import attachments_api
from pybusinesscentral.model.attachments import Attachments
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    content_type = "Content-Type_example" # str | (v1.0) application/json
    unknown_base_type = {
        parent_id="parent_id_example",
        id="id_example",
        file_name="file_name_example",
        byte_size=1,
        content=open('/path/to/file', 'rb'),
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type attachments in Dynamics 365 Business Central
        api_response = api_instance.post_attachments(company_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->post_attachments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new attachments has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_attachments_for_journal_line**
> Attachments post_attachments_for_journal_line(company_id, journal_line_id, content_type, unknown_base_type)

Creates an object of type attachments in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import attachments_api
from pybusinesscentral.model.attachments import Attachments
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    journal_line_id = "journalLine_id_example" # str | (v1.0) id for journalLine
    content_type = "Content-Type_example" # str | (v1.0) application/json
    unknown_base_type = {
        parent_id="parent_id_example",
        id="id_example",
        file_name="file_name_example",
        byte_size=1,
        content=open('/path/to/file', 'rb'),
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type attachments in Dynamics 365 Business Central
        api_response = api_instance.post_attachments_for_journal_line(company_id, journal_line_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->post_attachments_for_journal_line: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **journal_line_id** | **str**| (v1.0) id for journalLine |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new attachments has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_attachments_for_journal_line_for_journal**
> Attachments post_attachments_for_journal_line_for_journal(company_id, journal_id, journal_line_id, content_type, unknown_base_type)

Creates an object of type attachments in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import attachments_api
from pybusinesscentral.model.attachments import Attachments
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
    api_instance = attachments_api.AttachmentsApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    journal_id = "journal_id_example" # str | (v1.0) id for journal
    journal_line_id = "journalLine_id_example" # str | (v1.0) id for journalLine
    content_type = "Content-Type_example" # str | (v1.0) application/json
    unknown_base_type = {
        parent_id="parent_id_example",
        id="id_example",
        file_name="file_name_example",
        byte_size=1,
        content=open('/path/to/file', 'rb'),
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type attachments in Dynamics 365 Business Central
        api_response = api_instance.post_attachments_for_journal_line_for_journal(company_id, journal_id, journal_line_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling AttachmentsApi->post_attachments_for_journal_line_for_journal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **journal_id** | **str**| (v1.0) id for journal |
 **journal_line_id** | **str**| (v1.0) id for journalLine |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**Attachments**](Attachments.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new attachments has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

