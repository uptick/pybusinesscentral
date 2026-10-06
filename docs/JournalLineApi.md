# pybusinesscentral.JournalLineApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_journal_line_for_journal**](JournalLineApi.md#delete_journal_line_for_journal) | **DELETE** /companies({company_id})/journals({journal_id})/journalLines({journalLine_id}) | Deletes an object of type journalLine in Dynamics 365 Business Central
[**list_journal_lines_for_journal**](JournalLineApi.md#list_journal_lines_for_journal) | **GET** /companies({company_id})/journals({journal_id})/journalLines | Returns a list of journalLines
[**patch_journal_line_for_journal**](JournalLineApi.md#patch_journal_line_for_journal) | **PATCH** /companies({company_id})/journals({journal_id})/journalLines({journalLine_id}) | Updates an object of type journalLine in Dynamics 365 Business Central
[**post_journal_line_for_journal**](JournalLineApi.md#post_journal_line_for_journal) | **POST** /companies({company_id})/journals({journal_id})/journalLines | Creates an object of type journalLine in Dynamics 365 Business Central


# **delete_journal_line_for_journal**
> delete_journal_line_for_journal(company_id, journal_id, journal_line_id, if_match)

Deletes an object of type journalLine in Dynamics 365 Business Central

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
    api_instance = pybusinesscentral.JournalLineApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    journal_id = 'journal_id_example' # str | (v1.0) id for journal
    journal_line_id = 'journal_line_id_example' # str | (v1.0) id for journalLine
    if_match = 'if_match_example' # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.

    try:
        # Deletes an object of type journalLine in Dynamics 365 Business Central
        api_instance.delete_journal_line_for_journal(company_id, journal_id, journal_line_id, if_match)
    except Exception as e:
        print("Exception when calling JournalLineApi->delete_journal_line_for_journal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **journal_id** | **str**| (v1.0) id for journal | 
 **journal_line_id** | **str**| (v1.0) id for journalLine | 
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. | 

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
**204** | (v1.0) Succesfully deleted the specified journalLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_journal_lines_for_journal**
> ListJournalLinesForJournal200Response list_journal_lines_for_journal(company_id, journal_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)

Returns a list of journalLines

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.list_journal_lines_for_journal200_response import ListJournalLinesForJournal200Response
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
    api_instance = pybusinesscentral.JournalLineApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    journal_id = 'journal_id_example' # str | (v1.0) id for journal
    top = 56 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 56 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 56 # int | (v1.0) Number of items to return from the list (optional)
    filter = 'filter_example' # str | (v1.0) Filtering expression (optional)
    expand = ['expand_example'] # List[str] | (v1.0) Entities to expand (optional)
    select = ['select_example'] # List[str] | (v1.0) Selected properties to be retrieved (optional)

    try:
        # Returns a list of journalLines
        api_response = api_instance.list_journal_lines_for_journal(company_id, journal_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        print("The response of JournalLineApi->list_journal_lines_for_journal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalLineApi->list_journal_lines_for_journal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **journal_id** | **str**| (v1.0) id for journal | 
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional] 
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional] 
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional] 
 **filter** | **str**| (v1.0) Filtering expression | [optional] 
 **expand** | [**List[str]**](str.md)| (v1.0) Entities to expand | [optional] 
 **select** | [**List[str]**](str.md)| (v1.0) Selected properties to be retrieved | [optional] 

### Return type

[**ListJournalLinesForJournal200Response**](ListJournalLinesForJournal200Response.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of journalLines |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_journal_line_for_journal**
> JournalLine patch_journal_line_for_journal(company_id, journal_id, journal_line_id, content_type, if_match, post_journal_line_for_journal_request)

Updates an object of type journalLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.journal_line import JournalLine
from pybusinesscentral.model.post_journal_line_for_journal_request import PostJournalLineForJournalRequest
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
    api_instance = pybusinesscentral.JournalLineApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    journal_id = 'journal_id_example' # str | (v1.0) id for journal
    journal_line_id = 'journal_line_id_example' # str | (v1.0) id for journalLine
    content_type = 'content_type_example' # str | (v1.0) application/json
    if_match = 'if_match_example' # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    post_journal_line_for_journal_request = pybusinesscentral.PostJournalLineForJournalRequest() # PostJournalLineForJournalRequest | 

    try:
        # Updates an object of type journalLine in Dynamics 365 Business Central
        api_response = api_instance.patch_journal_line_for_journal(company_id, journal_id, journal_line_id, content_type, if_match, post_journal_line_for_journal_request)
        print("The response of JournalLineApi->patch_journal_line_for_journal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalLineApi->patch_journal_line_for_journal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **journal_id** | **str**| (v1.0) id for journal | 
 **journal_line_id** | **str**| (v1.0) id for journalLine | 
 **content_type** | **str**| (v1.0) application/json | 
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. | 
 **post_journal_line_for_journal_request** | [**PostJournalLineForJournalRequest**](PostJournalLineForJournalRequest.md)|  | 

### Return type

[**JournalLine**](JournalLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specified journalLine |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_journal_line_for_journal**
> JournalLine post_journal_line_for_journal(company_id, journal_id, content_type, post_journal_line_for_journal_request)

Creates an object of type journalLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.journal_line import JournalLine
from pybusinesscentral.model.post_journal_line_for_journal_request import PostJournalLineForJournalRequest
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
    api_instance = pybusinesscentral.JournalLineApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    journal_id = 'journal_id_example' # str | (v1.0) id for journal
    content_type = 'content_type_example' # str | (v1.0) application/json
    post_journal_line_for_journal_request = pybusinesscentral.PostJournalLineForJournalRequest() # PostJournalLineForJournalRequest | 

    try:
        # Creates an object of type journalLine in Dynamics 365 Business Central
        api_response = api_instance.post_journal_line_for_journal(company_id, journal_id, content_type, post_journal_line_for_journal_request)
        print("The response of JournalLineApi->post_journal_line_for_journal:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JournalLineApi->post_journal_line_for_journal: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **journal_id** | **str**| (v1.0) id for journal | 
 **content_type** | **str**| (v1.0) application/json | 
 **post_journal_line_for_journal_request** | [**PostJournalLineForJournalRequest**](PostJournalLineForJournalRequest.md)|  | 

### Return type

[**JournalLine**](JournalLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new journalLine has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

