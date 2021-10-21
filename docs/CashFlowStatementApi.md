# pybusinesscentral.CashFlowStatementApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_cash_flow_statement**](CashFlowStatementApi.md#get_cash_flow_statement) | **GET** /companies({company_id})/cashFlowStatement({cashFlowStatement_lineNumber}) | Retrieve the properties and relationships of an object of type cashFlowStatement for Dynamics 365 Business Central.
[**list_cash_flow_statement**](CashFlowStatementApi.md#list_cash_flow_statement) | **GET** /companies({company_id})/cashFlowStatement | Returns a list of cashFlowStatement


# **get_cash_flow_statement**
> CashFlowStatement get_cash_flow_statement(company_id, cash_flow_statement_line_number)

Retrieve the properties and relationships of an object of type cashFlowStatement for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import cash_flow_statement_api
from pybusinesscentral.model.cash_flow_statement import CashFlowStatement
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
    api_instance = cash_flow_statement_api.CashFlowStatementApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    cash_flow_statement_line_number = 1 # int | (v1.0) lineNumber for cashFlowStatement
    select = [
        "lineNumber",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type cashFlowStatement for Dynamics 365 Business Central.
        api_response = api_instance.get_cash_flow_statement(company_id, cash_flow_statement_line_number)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CashFlowStatementApi->get_cash_flow_statement: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type cashFlowStatement for Dynamics 365 Business Central.
        api_response = api_instance.get_cash_flow_statement(company_id, cash_flow_statement_line_number, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CashFlowStatementApi->get_cash_flow_statement: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **cash_flow_statement_line_number** | **int**| (v1.0) lineNumber for cashFlowStatement |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**CashFlowStatement**](CashFlowStatement.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested cashFlowStatement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_cash_flow_statement**
> InlineResponse20029 list_cash_flow_statement(company_id)

Returns a list of cashFlowStatement

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import cash_flow_statement_api
from pybusinesscentral.model.inline_response20029 import InlineResponse20029
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
    api_instance = cash_flow_statement_api.CashFlowStatementApi(api_client)
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
        # Returns a list of cashFlowStatement
        api_response = api_instance.list_cash_flow_statement(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CashFlowStatementApi->list_cash_flow_statement: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of cashFlowStatement
        api_response = api_instance.list_cash_flow_statement(company_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CashFlowStatementApi->list_cash_flow_statement: %s\n" % e)
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

[**InlineResponse20029**](InlineResponse20029.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of cashFlowStatement |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

