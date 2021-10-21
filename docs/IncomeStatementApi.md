# pybusinesscentral.IncomeStatementApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_income_statement**](IncomeStatementApi.md#get_income_statement) | **GET** /companies({company_id})/incomeStatement({incomeStatement_lineNumber}) | Retrieve the properties and relationships of an object of type incomeStatement for Dynamics 365 Business Central.
[**list_income_statement**](IncomeStatementApi.md#list_income_statement) | **GET** /companies({company_id})/incomeStatement | Returns a list of incomeStatement


# **get_income_statement**
> IncomeStatement get_income_statement(company_id, income_statement_line_number)

Retrieve the properties and relationships of an object of type incomeStatement for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import income_statement_api
from pybusinesscentral.model.income_statement import IncomeStatement
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
    api_instance = income_statement_api.IncomeStatementApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    income_statement_line_number = 1 # int | (v1.0) lineNumber for incomeStatement
    select = [
        "lineNumber",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type incomeStatement for Dynamics 365 Business Central.
        api_response = api_instance.get_income_statement(company_id, income_statement_line_number)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling IncomeStatementApi->get_income_statement: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type incomeStatement for Dynamics 365 Business Central.
        api_response = api_instance.get_income_statement(company_id, income_statement_line_number, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling IncomeStatementApi->get_income_statement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **income_statement_line_number** | **int**| (v1.0) lineNumber for incomeStatement |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**IncomeStatement**](IncomeStatement.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested incomeStatement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_income_statement**
> InlineResponse20039 list_income_statement(company_id)

Returns a list of incomeStatement

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import income_statement_api
from pybusinesscentral.model.inline_response20039 import InlineResponse20039
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
    api_instance = income_statement_api.IncomeStatementApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "lineNumber",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of incomeStatement
        api_response = api_instance.list_income_statement(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling IncomeStatementApi->list_income_statement: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of incomeStatement
        api_response = api_instance.list_income_statement(company_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling IncomeStatementApi->list_income_statement: %s\n" % e)
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

[**InlineResponse20039**](InlineResponse20039.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of incomeStatement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

