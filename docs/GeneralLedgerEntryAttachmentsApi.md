# pybusinesscentral.GeneralLedgerEntryAttachmentsApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_general_ledger_entry_attachments**](GeneralLedgerEntryAttachmentsApi.md#delete_general_ledger_entry_attachments) | **DELETE** /companies({company_id})/generalLedgerEntryAttachments({generalLedgerEntryAttachments_generalLedgerEntryNumber},{generalLedgerEntryAttachments_id}) | Deletes an object of type generalLedgerEntryAttachments in Dynamics 365 Business Central
[**get_general_ledger_entry_attachments**](GeneralLedgerEntryAttachmentsApi.md#get_general_ledger_entry_attachments) | **GET** /companies({company_id})/generalLedgerEntryAttachments({generalLedgerEntryAttachments_generalLedgerEntryNumber},{generalLedgerEntryAttachments_id}) | Retrieve the properties and relationships of an object of type generalLedgerEntryAttachments for Dynamics 365 Business Central.
[**list_general_ledger_entry_attachments**](GeneralLedgerEntryAttachmentsApi.md#list_general_ledger_entry_attachments) | **GET** /companies({company_id})/generalLedgerEntryAttachments | Returns a list of generalLedgerEntryAttachments
[**patch_general_ledger_entry_attachments**](GeneralLedgerEntryAttachmentsApi.md#patch_general_ledger_entry_attachments) | **PATCH** /companies({company_id})/generalLedgerEntryAttachments({generalLedgerEntryAttachments_generalLedgerEntryNumber},{generalLedgerEntryAttachments_id}) | Updates an object of type generalLedgerEntryAttachments in Dynamics 365 Business Central
[**post_general_ledger_entry_attachments**](GeneralLedgerEntryAttachmentsApi.md#post_general_ledger_entry_attachments) | **POST** /companies({company_id})/generalLedgerEntryAttachments | Creates an object of type generalLedgerEntryAttachments in Dynamics 365 Business Central


# **delete_general_ledger_entry_attachments**
> delete_general_ledger_entry_attachments(company_id, general_ledger_entry_attachments_general_ledger_entry_number, general_ledger_entry_attachments_id)

Deletes an object of type generalLedgerEntryAttachments in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import general_ledger_entry_attachments_api
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

# Configure OAuth2 access token for authorization: oAuth
configuration = pybusinesscentral.Configuration(
    host = "https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pybusinesscentral.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = general_ledger_entry_attachments_api.GeneralLedgerEntryAttachmentsApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    general_ledger_entry_attachments_general_ledger_entry_number = 1 # int | (v1.0) generalLedgerEntryNumber for generalLedgerEntryAttachments
    general_ledger_entry_attachments_id = "generalLedgerEntryAttachments_id_example" # str | (v1.0) id for generalLedgerEntryAttachments

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type generalLedgerEntryAttachments in Dynamics 365 Business Central
        api_instance.delete_general_ledger_entry_attachments(company_id, general_ledger_entry_attachments_general_ledger_entry_number, general_ledger_entry_attachments_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling GeneralLedgerEntryAttachmentsApi->delete_general_ledger_entry_attachments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **general_ledger_entry_attachments_general_ledger_entry_number** | **int**| (v1.0) generalLedgerEntryNumber for generalLedgerEntryAttachments |
 **general_ledger_entry_attachments_id** | **str**| (v1.0) id for generalLedgerEntryAttachments |

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
**204** | (v1.0) Succesfully deleted the specified generalLedgerEntryAttachments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_general_ledger_entry_attachments**
> GeneralLedgerEntryAttachments get_general_ledger_entry_attachments(company_id, general_ledger_entry_attachments_general_ledger_entry_number, general_ledger_entry_attachments_id)

Retrieve the properties and relationships of an object of type generalLedgerEntryAttachments for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import general_ledger_entry_attachments_api
from pybusinesscentral.model.general_ledger_entry_attachments import GeneralLedgerEntryAttachments
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

# Configure OAuth2 access token for authorization: oAuth
configuration = pybusinesscentral.Configuration(
    host = "https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pybusinesscentral.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = general_ledger_entry_attachments_api.GeneralLedgerEntryAttachmentsApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    general_ledger_entry_attachments_general_ledger_entry_number = 1 # int | (v1.0) generalLedgerEntryNumber for generalLedgerEntryAttachments
    general_ledger_entry_attachments_id = "generalLedgerEntryAttachments_id_example" # str | (v1.0) id for generalLedgerEntryAttachments
    expand = [
        "generalLedgerEntry",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "generalLedgerEntryNumber",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type generalLedgerEntryAttachments for Dynamics 365 Business Central.
        api_response = api_instance.get_general_ledger_entry_attachments(company_id, general_ledger_entry_attachments_general_ledger_entry_number, general_ledger_entry_attachments_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling GeneralLedgerEntryAttachmentsApi->get_general_ledger_entry_attachments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type generalLedgerEntryAttachments for Dynamics 365 Business Central.
        api_response = api_instance.get_general_ledger_entry_attachments(company_id, general_ledger_entry_attachments_general_ledger_entry_number, general_ledger_entry_attachments_id, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling GeneralLedgerEntryAttachmentsApi->get_general_ledger_entry_attachments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **general_ledger_entry_attachments_general_ledger_entry_number** | **int**| (v1.0) generalLedgerEntryNumber for generalLedgerEntryAttachments |
 **general_ledger_entry_attachments_id** | **str**| (v1.0) id for generalLedgerEntryAttachments |
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**GeneralLedgerEntryAttachments**](GeneralLedgerEntryAttachments.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested generalLedgerEntryAttachments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_general_ledger_entry_attachments**
> InlineResponse20045 list_general_ledger_entry_attachments(company_id)

Returns a list of generalLedgerEntryAttachments

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import general_ledger_entry_attachments_api
from pybusinesscentral.model.inline_response20045 import InlineResponse20045
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

# Configure OAuth2 access token for authorization: oAuth
configuration = pybusinesscentral.Configuration(
    host = "https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pybusinesscentral.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = general_ledger_entry_attachments_api.GeneralLedgerEntryAttachmentsApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    expand = [
        "generalLedgerEntry",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "generalLedgerEntryNumber",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of generalLedgerEntryAttachments
        api_response = api_instance.list_general_ledger_entry_attachments(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling GeneralLedgerEntryAttachmentsApi->list_general_ledger_entry_attachments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of generalLedgerEntryAttachments
        api_response = api_instance.list_general_ledger_entry_attachments(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling GeneralLedgerEntryAttachmentsApi->list_general_ledger_entry_attachments: %s\n" % e)
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

[**InlineResponse20045**](InlineResponse20045.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of generalLedgerEntryAttachments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_general_ledger_entry_attachments**
> GeneralLedgerEntryAttachments patch_general_ledger_entry_attachments(company_id, general_ledger_entry_attachments_general_ledger_entry_number, general_ledger_entry_attachments_id, content_type, if_match, unknown_base_type)

Updates an object of type generalLedgerEntryAttachments in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import general_ledger_entry_attachments_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.general_ledger_entry_attachments import GeneralLedgerEntryAttachments
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

# Configure OAuth2 access token for authorization: oAuth
configuration = pybusinesscentral.Configuration(
    host = "https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pybusinesscentral.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = general_ledger_entry_attachments_api.GeneralLedgerEntryAttachmentsApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    general_ledger_entry_attachments_general_ledger_entry_number = 1 # int | (v1.0) generalLedgerEntryNumber for generalLedgerEntryAttachments
    general_ledger_entry_attachments_id = "generalLedgerEntryAttachments_id_example" # str | (v1.0) id for generalLedgerEntryAttachments
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        general_ledger_entry_number=1,
        id="id_example",
        file_name="file_name_example",
        byte_size=1,
        content=open('/path/to/file', 'rb'),
        created_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type generalLedgerEntryAttachments in Dynamics 365 Business Central
        api_response = api_instance.patch_general_ledger_entry_attachments(company_id, general_ledger_entry_attachments_general_ledger_entry_number, general_ledger_entry_attachments_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling GeneralLedgerEntryAttachmentsApi->patch_general_ledger_entry_attachments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **general_ledger_entry_attachments_general_ledger_entry_number** | **int**| (v1.0) generalLedgerEntryNumber for generalLedgerEntryAttachments |
 **general_ledger_entry_attachments_id** | **str**| (v1.0) id for generalLedgerEntryAttachments |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**GeneralLedgerEntryAttachments**](GeneralLedgerEntryAttachments.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedgeneralLedgerEntryAttachments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_general_ledger_entry_attachments**
> GeneralLedgerEntryAttachments post_general_ledger_entry_attachments(company_id, content_type, unknown_base_type)

Creates an object of type generalLedgerEntryAttachments in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import general_ledger_entry_attachments_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.general_ledger_entry_attachments import GeneralLedgerEntryAttachments
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

# Configure OAuth2 access token for authorization: oAuth
configuration = pybusinesscentral.Configuration(
    host = "https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0"
)
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# Enter a context with an instance of the API client
with pybusinesscentral.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = general_ledger_entry_attachments_api.GeneralLedgerEntryAttachmentsApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    content_type = "Content-Type_example" # str | (v1.0) application/json
    unknown_base_type = {
        general_ledger_entry_number=1,
        id="id_example",
        file_name="file_name_example",
        byte_size=1,
        content=open('/path/to/file', 'rb'),
        created_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type generalLedgerEntryAttachments in Dynamics 365 Business Central
        api_response = api_instance.post_general_ledger_entry_attachments(company_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling GeneralLedgerEntryAttachmentsApi->post_general_ledger_entry_attachments: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**GeneralLedgerEntryAttachments**](GeneralLedgerEntryAttachments.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new generalLedgerEntryAttachments has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

