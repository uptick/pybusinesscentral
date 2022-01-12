# pybusinesscentral.CustomerPaymentApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_customer_payment**](CustomerPaymentApi.md#delete_customer_payment) | **DELETE** /companies({company_id})/customerPayments({customerPayment_id}) | Deletes an object of type customerPayment in Dynamics 365 Business Central
[**delete_customer_payment_for_customer_payment_journal**](CustomerPaymentApi.md#delete_customer_payment_for_customer_payment_journal) | **DELETE** /companies({company_id})/customerPaymentJournals({customerPaymentJournal_id})/customerPayments({customerPayment_id}) | Deletes an object of type customerPayment in Dynamics 365 Business Central
[**get_customer_payment**](CustomerPaymentApi.md#get_customer_payment) | **GET** /companies({company_id})/customerPayments({customerPayment_id}) | Retrieve the properties and relationships of an object of type customerPayment for Dynamics 365 Business Central.
[**get_customer_payment_for_customer_payment_journal**](CustomerPaymentApi.md#get_customer_payment_for_customer_payment_journal) | **GET** /companies({company_id})/customerPaymentJournals({customerPaymentJournal_id})/customerPayments({customerPayment_id}) | Retrieve the properties and relationships of an object of type customerPayment for Dynamics 365 Business Central.
[**list_customer_payments**](CustomerPaymentApi.md#list_customer_payments) | **GET** /companies({company_id})/customerPayments | Returns a list of customerPayments
[**list_customer_payments_for_customer_payment_journal**](CustomerPaymentApi.md#list_customer_payments_for_customer_payment_journal) | **GET** /companies({company_id})/customerPaymentJournals({customerPaymentJournal_id})/customerPayments | Returns a list of customerPayments
[**patch_customer_payment**](CustomerPaymentApi.md#patch_customer_payment) | **PATCH** /companies({company_id})/customerPayments({customerPayment_id}) | Updates an object of type customerPayment in Dynamics 365 Business Central
[**patch_customer_payment_for_customer_payment_journal**](CustomerPaymentApi.md#patch_customer_payment_for_customer_payment_journal) | **PATCH** /companies({company_id})/customerPaymentJournals({customerPaymentJournal_id})/customerPayments({customerPayment_id}) | Updates an object of type customerPayment in Dynamics 365 Business Central
[**post_customer_payment**](CustomerPaymentApi.md#post_customer_payment) | **POST** /companies({company_id})/customerPayments | Creates an object of type customerPayment in Dynamics 365 Business Central
[**post_customer_payment_for_customer_payment_journal**](CustomerPaymentApi.md#post_customer_payment_for_customer_payment_journal) | **POST** /companies({company_id})/customerPaymentJournals({customerPaymentJournal_id})/customerPayments | Creates an object of type customerPayment in Dynamics 365 Business Central


# **delete_customer_payment**
> delete_customer_payment(company_id, customer_payment_id)

Deletes an object of type customerPayment in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import customer_payment_api
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
    api_instance = customer_payment_api.CustomerPaymentApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    customer_payment_id = "customerPayment_id_example" # str | (v1.0) id for customerPayment

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type customerPayment in Dynamics 365 Business Central
        api_instance.delete_customer_payment(company_id, customer_payment_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerPaymentApi->delete_customer_payment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **customer_payment_id** | **str**| (v1.0) id for customerPayment |

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
**204** | (v1.0) Succesfully deleted the specified customerPayment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_customer_payment_for_customer_payment_journal**
> delete_customer_payment_for_customer_payment_journal(company_id, customer_payment_journal_id, customer_payment_id)

Deletes an object of type customerPayment in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import customer_payment_api
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
    api_instance = customer_payment_api.CustomerPaymentApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    customer_payment_journal_id = "customerPaymentJournal_id_example" # str | (v1.0) id for customerPaymentJournal
    customer_payment_id = "customerPayment_id_example" # str | (v1.0) id for customerPayment

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type customerPayment in Dynamics 365 Business Central
        api_instance.delete_customer_payment_for_customer_payment_journal(company_id, customer_payment_journal_id, customer_payment_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerPaymentApi->delete_customer_payment_for_customer_payment_journal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **customer_payment_journal_id** | **str**| (v1.0) id for customerPaymentJournal |
 **customer_payment_id** | **str**| (v1.0) id for customerPayment |

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
**204** | (v1.0) Succesfully deleted the specified customerPayment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_payment**
> CustomerPayment get_customer_payment(company_id, customer_payment_id)

Retrieve the properties and relationships of an object of type customerPayment for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import customer_payment_api
from pybusinesscentral.model.customer_payment import CustomerPayment
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
    api_instance = customer_payment_api.CustomerPaymentApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    customer_payment_id = "customerPayment_id_example" # str | (v1.0) id for customerPayment
    expand = [
        "customer",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type customerPayment for Dynamics 365 Business Central.
        api_response = api_instance.get_customer_payment(company_id, customer_payment_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerPaymentApi->get_customer_payment: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type customerPayment for Dynamics 365 Business Central.
        api_response = api_instance.get_customer_payment(company_id, customer_payment_id, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerPaymentApi->get_customer_payment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **customer_payment_id** | **str**| (v1.0) id for customerPayment |
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**CustomerPayment**](CustomerPayment.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested customerPayment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_payment_for_customer_payment_journal**
> CustomerPayment get_customer_payment_for_customer_payment_journal(company_id, customer_payment_journal_id, customer_payment_id)

Retrieve the properties and relationships of an object of type customerPayment for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import customer_payment_api
from pybusinesscentral.model.customer_payment import CustomerPayment
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
    api_instance = customer_payment_api.CustomerPaymentApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    customer_payment_journal_id = "customerPaymentJournal_id_example" # str | (v1.0) id for customerPaymentJournal
    customer_payment_id = "customerPayment_id_example" # str | (v1.0) id for customerPayment
    expand = [
        "customer",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type customerPayment for Dynamics 365 Business Central.
        api_response = api_instance.get_customer_payment_for_customer_payment_journal(company_id, customer_payment_journal_id, customer_payment_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerPaymentApi->get_customer_payment_for_customer_payment_journal: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type customerPayment for Dynamics 365 Business Central.
        api_response = api_instance.get_customer_payment_for_customer_payment_journal(company_id, customer_payment_journal_id, customer_payment_id, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerPaymentApi->get_customer_payment_for_customer_payment_journal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **customer_payment_journal_id** | **str**| (v1.0) id for customerPaymentJournal |
 **customer_payment_id** | **str**| (v1.0) id for customerPayment |
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**CustomerPayment**](CustomerPayment.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested customerPayment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_payments**
> InlineResponse20012 list_customer_payments(company_id)

Returns a list of customerPayments

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import customer_payment_api
from pybusinesscentral.model.inline_response20012 import InlineResponse20012
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
    api_instance = customer_payment_api.CustomerPaymentApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    expand = [
        "customer",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of customerPayments
        api_response = api_instance.list_customer_payments(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerPaymentApi->list_customer_payments: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of customerPayments
        api_response = api_instance.list_customer_payments(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerPaymentApi->list_customer_payments: %s\n" % e)
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

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of customerPayments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_customer_payments_for_customer_payment_journal**
> InlineResponse20012 list_customer_payments_for_customer_payment_journal(company_id, customer_payment_journal_id)

Returns a list of customerPayments

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import customer_payment_api
from pybusinesscentral.model.inline_response20012 import InlineResponse20012
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
    api_instance = customer_payment_api.CustomerPaymentApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    customer_payment_journal_id = "customerPaymentJournal_id_example" # str | (v1.0) id for customerPaymentJournal
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    expand = [
        "customer",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of customerPayments
        api_response = api_instance.list_customer_payments_for_customer_payment_journal(company_id, customer_payment_journal_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerPaymentApi->list_customer_payments_for_customer_payment_journal: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of customerPayments
        api_response = api_instance.list_customer_payments_for_customer_payment_journal(company_id, customer_payment_journal_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerPaymentApi->list_customer_payments_for_customer_payment_journal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **customer_payment_journal_id** | **str**| (v1.0) id for customerPaymentJournal |
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional]
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional]
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional]
 **filter** | **str**| (v1.0) Filtering expression | [optional]
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse20012**](InlineResponse20012.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of customerPayments |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_customer_payment**
> CustomerPayment patch_customer_payment(company_id, customer_payment_id, content_type, if_match, unknown_base_type)

Updates an object of type customerPayment in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import customer_payment_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.customer_payment import CustomerPayment
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
    api_instance = customer_payment_api.CustomerPaymentApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    customer_payment_id = "customerPayment_id_example" # str | (v1.0) id for customerPayment
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        id="id_example",
        journal_display_name="journal_display_name_example",
        line_number=1,
        customer_id="customer_id_example",
        customer_number="customer_number_example",
        contact_id="contact_id_example",
        posting_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        document_number="document_number_example",
        external_document_number="external_document_number_example",
        amount=3.14,
        applies_to_invoice_id="applies_to_invoice_id_example",
        applies_to_invoice_number="applies_to_invoice_number_example",
        description="description_example",
        comment="comment_example",
        dimensions=[
            ,
        ],
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type customerPayment in Dynamics 365 Business Central
        api_response = api_instance.patch_customer_payment(company_id, customer_payment_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerPaymentApi->patch_customer_payment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **customer_payment_id** | **str**| (v1.0) id for customerPayment |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**CustomerPayment**](CustomerPayment.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedcustomerPayment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_customer_payment_for_customer_payment_journal**
> CustomerPayment patch_customer_payment_for_customer_payment_journal(company_id, customer_payment_journal_id, customer_payment_id, content_type, if_match, unknown_base_type)

Updates an object of type customerPayment in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import customer_payment_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.customer_payment import CustomerPayment
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
    api_instance = customer_payment_api.CustomerPaymentApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    customer_payment_journal_id = "customerPaymentJournal_id_example" # str | (v1.0) id for customerPaymentJournal
    customer_payment_id = "customerPayment_id_example" # str | (v1.0) id for customerPayment
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        id="id_example",
        journal_display_name="journal_display_name_example",
        line_number=1,
        customer_id="customer_id_example",
        customer_number="customer_number_example",
        contact_id="contact_id_example",
        posting_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        document_number="document_number_example",
        external_document_number="external_document_number_example",
        amount=3.14,
        applies_to_invoice_id="applies_to_invoice_id_example",
        applies_to_invoice_number="applies_to_invoice_number_example",
        description="description_example",
        comment="comment_example",
        dimensions=[
            ,
        ],
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type customerPayment in Dynamics 365 Business Central
        api_response = api_instance.patch_customer_payment_for_customer_payment_journal(company_id, customer_payment_journal_id, customer_payment_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerPaymentApi->patch_customer_payment_for_customer_payment_journal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **customer_payment_journal_id** | **str**| (v1.0) id for customerPaymentJournal |
 **customer_payment_id** | **str**| (v1.0) id for customerPayment |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**CustomerPayment**](CustomerPayment.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedcustomerPayment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_customer_payment**
> CustomerPayment post_customer_payment(company_id, content_type, unknown_base_type)

Creates an object of type customerPayment in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import customer_payment_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.customer_payment import CustomerPayment
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
    api_instance = customer_payment_api.CustomerPaymentApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    content_type = "Content-Type_example" # str | (v1.0) application/json
    unknown_base_type = {
        id="id_example",
        journal_display_name="journal_display_name_example",
        line_number=1,
        customer_id="customer_id_example",
        customer_number="customer_number_example",
        contact_id="contact_id_example",
        posting_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        document_number="document_number_example",
        external_document_number="external_document_number_example",
        amount=3.14,
        applies_to_invoice_id="applies_to_invoice_id_example",
        applies_to_invoice_number="applies_to_invoice_number_example",
        description="description_example",
        comment="comment_example",
        dimensions=[
            ,
        ],
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type customerPayment in Dynamics 365 Business Central
        api_response = api_instance.post_customer_payment(company_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerPaymentApi->post_customer_payment: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**CustomerPayment**](CustomerPayment.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new customerPayment has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_customer_payment_for_customer_payment_journal**
> CustomerPayment post_customer_payment_for_customer_payment_journal(company_id, customer_payment_journal_id, content_type, unknown_base_type)

Creates an object of type customerPayment in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import customer_payment_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.customer_payment import CustomerPayment
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
    api_instance = customer_payment_api.CustomerPaymentApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    customer_payment_journal_id = "customerPaymentJournal_id_example" # str | (v1.0) id for customerPaymentJournal
    content_type = "Content-Type_example" # str | (v1.0) application/json
    unknown_base_type = {
        id="id_example",
        journal_display_name="journal_display_name_example",
        line_number=1,
        customer_id="customer_id_example",
        customer_number="customer_number_example",
        contact_id="contact_id_example",
        posting_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        document_number="document_number_example",
        external_document_number="external_document_number_example",
        amount=3.14,
        applies_to_invoice_id="applies_to_invoice_id_example",
        applies_to_invoice_number="applies_to_invoice_number_example",
        description="description_example",
        comment="comment_example",
        dimensions=[
            ,
        ],
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type customerPayment in Dynamics 365 Business Central
        api_response = api_instance.post_customer_payment_for_customer_payment_journal(company_id, customer_payment_journal_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling CustomerPaymentApi->post_customer_payment_for_customer_payment_journal: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **customer_payment_journal_id** | **str**| (v1.0) id for customerPaymentJournal |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**CustomerPayment**](CustomerPayment.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new customerPayment has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

