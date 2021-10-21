# pybusinesscentral.PaymentTermApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_payment_term**](PaymentTermApi.md#delete_payment_term) | **DELETE** /companies({company_id})/paymentTerms({paymentTerm_id}) | Deletes an object of type paymentTerm in Dynamics 365 Business Central
[**get_payment_term**](PaymentTermApi.md#get_payment_term) | **GET** /companies({company_id})/paymentTerms({paymentTerm_id}) | Retrieve the properties and relationships of an object of type paymentTerm for Dynamics 365 Business Central.
[**list_payment_terms**](PaymentTermApi.md#list_payment_terms) | **GET** /companies({company_id})/paymentTerms | Returns a list of paymentTerms
[**patch_payment_term**](PaymentTermApi.md#patch_payment_term) | **PATCH** /companies({company_id})/paymentTerms({paymentTerm_id}) | Updates an object of type paymentTerm in Dynamics 365 Business Central
[**post_payment_term**](PaymentTermApi.md#post_payment_term) | **POST** /companies({company_id})/paymentTerms | Creates an object of type paymentTerm in Dynamics 365 Business Central


# **delete_payment_term**
> delete_payment_term(company_id, payment_term_id)

Deletes an object of type paymentTerm in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import payment_term_api
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
    api_instance = payment_term_api.PaymentTermApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    payment_term_id = "paymentTerm_id_example" # str | (v1.0) id for paymentTerm

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type paymentTerm in Dynamics 365 Business Central
        api_instance.delete_payment_term(company_id, payment_term_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PaymentTermApi->delete_payment_term: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **payment_term_id** | **str**| (v1.0) id for paymentTerm |

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
**204** | (v1.0) Succesfully deleted the specified paymentTerm |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_term**
> PaymentTerm get_payment_term(company_id, payment_term_id)

Retrieve the properties and relationships of an object of type paymentTerm for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import payment_term_api
from pybusinesscentral.model.payment_term import PaymentTerm
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
    api_instance = payment_term_api.PaymentTermApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    payment_term_id = "paymentTerm_id_example" # str | (v1.0) id for paymentTerm
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type paymentTerm for Dynamics 365 Business Central.
        api_response = api_instance.get_payment_term(company_id, payment_term_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PaymentTermApi->get_payment_term: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type paymentTerm for Dynamics 365 Business Central.
        api_response = api_instance.get_payment_term(company_id, payment_term_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PaymentTermApi->get_payment_term: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **payment_term_id** | **str**| (v1.0) id for paymentTerm |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**PaymentTerm**](PaymentTerm.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested paymentTerm |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_payment_terms**
> InlineResponse20026 list_payment_terms(company_id)

Returns a list of paymentTerms

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import payment_term_api
from pybusinesscentral.model.inline_response20026 import InlineResponse20026
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
    api_instance = payment_term_api.PaymentTermApi(api_client)
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
        # Returns a list of paymentTerms
        api_response = api_instance.list_payment_terms(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PaymentTermApi->list_payment_terms: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of paymentTerms
        api_response = api_instance.list_payment_terms(company_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PaymentTermApi->list_payment_terms: %s\n" % e)
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

[**InlineResponse20026**](InlineResponse20026.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of paymentTerms |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_payment_term**
> PaymentTerm patch_payment_term(company_id, payment_term_id, content_type, if_match, unknown_base_type)

Updates an object of type paymentTerm in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import payment_term_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.payment_term import PaymentTerm
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
    api_instance = payment_term_api.PaymentTermApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    payment_term_id = "paymentTerm_id_example" # str | (v1.0) id for paymentTerm
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        id="id_example",
        code="code_example",
        display_name="display_name_example",
        due_date_calculation="due_date_calculation_example",
        discount_date_calculation="discount_date_calculation_example",
        discount_percent=3.14,
        calculate_discount_on_credit_memos=True,
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type paymentTerm in Dynamics 365 Business Central
        api_response = api_instance.patch_payment_term(company_id, payment_term_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PaymentTermApi->patch_payment_term: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **payment_term_id** | **str**| (v1.0) id for paymentTerm |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**PaymentTerm**](PaymentTerm.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedpaymentTerm |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_payment_term**
> PaymentTerm post_payment_term(company_id, content_type, unknown_base_type)

Creates an object of type paymentTerm in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import payment_term_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.payment_term import PaymentTerm
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
    api_instance = payment_term_api.PaymentTermApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    content_type = "Content-Type_example" # str | (v1.0) application/json
    unknown_base_type = {
        id="id_example",
        code="code_example",
        display_name="display_name_example",
        due_date_calculation="due_date_calculation_example",
        discount_date_calculation="discount_date_calculation_example",
        discount_percent=3.14,
        calculate_discount_on_credit_memos=True,
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type paymentTerm in Dynamics 365 Business Central
        api_response = api_instance.post_payment_term(company_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PaymentTermApi->post_payment_term: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**PaymentTerm**](PaymentTerm.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new paymentTerm has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

