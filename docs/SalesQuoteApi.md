# pybusinesscentral.SalesQuoteApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_quote**](SalesQuoteApi.md#delete_sales_quote) | **DELETE** /companies({company_id})/salesQuotes({salesQuote_id}) | Deletes an object of type salesQuote in Dynamics 365 Business Central
[**get_sales_quote**](SalesQuoteApi.md#get_sales_quote) | **GET** /companies({company_id})/salesQuotes({salesQuote_id}) | Retrieve the properties and relationships of an object of type salesQuote for Dynamics 365 Business Central.
[**list_sales_quotes**](SalesQuoteApi.md#list_sales_quotes) | **GET** /companies({company_id})/salesQuotes | Returns a list of salesQuotes
[**make_invoice_action_sales_quotes**](SalesQuoteApi.md#make_invoice_action_sales_quotes) | **POST** /companies({company_id})/salesQuotes({salesQuote_id})/Microsoft.NAV.makeInvoice | Performs the makeInvoice action for salesQuotes entity
[**make_order_action_sales_quotes**](SalesQuoteApi.md#make_order_action_sales_quotes) | **POST** /companies({company_id})/salesQuotes({salesQuote_id})/Microsoft.NAV.makeOrder | Performs the makeOrder action for salesQuotes entity
[**patch_sales_quote**](SalesQuoteApi.md#patch_sales_quote) | **PATCH** /companies({company_id})/salesQuotes({salesQuote_id}) | Updates an object of type salesQuote in Dynamics 365 Business Central
[**post_sales_quote**](SalesQuoteApi.md#post_sales_quote) | **POST** /companies({company_id})/salesQuotes | Creates an object of type salesQuote in Dynamics 365 Business Central
[**send_action_sales_quotes**](SalesQuoteApi.md#send_action_sales_quotes) | **POST** /companies({company_id})/salesQuotes({salesQuote_id})/Microsoft.NAV.send | Performs the send action for salesQuotes entity


# **delete_sales_quote**
> delete_sales_quote(company_id, sales_quote_id)

Deletes an object of type salesQuote in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_quote_api
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
    api_instance = sales_quote_api.SalesQuoteApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_quote_id = "salesQuote_id_example" # str | (v1.0) id for salesQuote

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type salesQuote in Dynamics 365 Business Central
        api_instance.delete_sales_quote(company_id, sales_quote_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteApi->delete_sales_quote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_quote_id** | **str**| (v1.0) id for salesQuote |

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
**204** | (v1.0) Succesfully deleted the specified salesQuote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_quote**
> SalesQuote get_sales_quote(company_id, sales_quote_id)

Retrieve the properties and relationships of an object of type salesQuote for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_quote_api
from pybusinesscentral.model.sales_quote import SalesQuote
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
    api_instance = sales_quote_api.SalesQuoteApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_quote_id = "salesQuote_id_example" # str | (v1.0) id for salesQuote
    expand = [
        "salesQuoteLines",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type salesQuote for Dynamics 365 Business Central.
        api_response = api_instance.get_sales_quote(company_id, sales_quote_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteApi->get_sales_quote: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type salesQuote for Dynamics 365 Business Central.
        api_response = api_instance.get_sales_quote(company_id, sales_quote_id, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteApi->get_sales_quote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_quote_id** | **str**| (v1.0) id for salesQuote |
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**SalesQuote**](SalesQuote.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested salesQuote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sales_quotes**
> InlineResponse20041 list_sales_quotes(company_id)

Returns a list of salesQuotes

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_quote_api
from pybusinesscentral.model.inline_response20041 import InlineResponse20041
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
    api_instance = sales_quote_api.SalesQuoteApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    expand = [
        "salesQuoteLines",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of salesQuotes
        api_response = api_instance.list_sales_quotes(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteApi->list_sales_quotes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of salesQuotes
        api_response = api_instance.list_sales_quotes(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteApi->list_sales_quotes: %s\n" % e)
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

[**InlineResponse20041**](InlineResponse20041.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of salesQuotes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **make_invoice_action_sales_quotes**
> make_invoice_action_sales_quotes(company_id, sales_quote_id)

Performs the makeInvoice action for salesQuotes entity

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_quote_api
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
    api_instance = sales_quote_api.SalesQuoteApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_quote_id = "salesQuote_id_example" # str | (v1.0) id for salesQuote

    # example passing only required values which don't have defaults set
    try:
        # Performs the makeInvoice action for salesQuotes entity
        api_instance.make_invoice_action_sales_quotes(company_id, sales_quote_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteApi->make_invoice_action_sales_quotes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_quote_id** | **str**| (v1.0) id for salesQuote |

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
**204** | (v1.0) Succesfully performed a makeInvoice action on the Dynamic 365 Business Central salesQuotes entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **make_order_action_sales_quotes**
> make_order_action_sales_quotes(company_id, sales_quote_id)

Performs the makeOrder action for salesQuotes entity

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_quote_api
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
    api_instance = sales_quote_api.SalesQuoteApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_quote_id = "salesQuote_id_example" # str | (v1.0) id for salesQuote

    # example passing only required values which don't have defaults set
    try:
        # Performs the makeOrder action for salesQuotes entity
        api_instance.make_order_action_sales_quotes(company_id, sales_quote_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteApi->make_order_action_sales_quotes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_quote_id** | **str**| (v1.0) id for salesQuote |

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
**204** | (v1.0) Succesfully performed a makeOrder action on the Dynamic 365 Business Central salesQuotes entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sales_quote**
> SalesQuote patch_sales_quote(company_id, sales_quote_id, content_type, if_match, unknown_base_type)

Updates an object of type salesQuote in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_quote_api
from pybusinesscentral.model.sales_quote import SalesQuote
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
    api_instance = sales_quote_api.SalesQuoteApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_quote_id = "salesQuote_id_example" # str | (v1.0) id for salesQuote
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        id="id_example",
        number="number_example",
        external_document_number="external_document_number_example",
        document_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        customer_id="customer_id_example",
        contact_id="contact_id_example",
        customer_number="customer_number_example",
        customer_name="customer_name_example",
        bill_to_name="bill_to_name_example",
        bill_to_customer_id="bill_to_customer_id_example",
        bill_to_customer_number="bill_to_customer_number_example",
        ship_to_name="ship_to_name_example",
        ship_to_contact="ship_to_contact_example",
        selling_postal_address=,
        billing_postal_address=,
        shipping_postal_address=,
        currency_id="currency_id_example",
        currency_code="currency_code_example",
        payment_terms_id="payment_terms_id_example",
        shipment_method_id="shipment_method_id_example",
        salesperson="salesperson_example",
        discount_amount=3.14,
        total_amount_excluding_tax=3.14,
        total_tax_amount=3.14,
        total_amount_including_tax=3.14,
        status="status_example",
        sent_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        valid_until_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        accepted_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        phone_number="phone_number_example",
        email="email_example",
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type salesQuote in Dynamics 365 Business Central
        api_response = api_instance.patch_sales_quote(company_id, sales_quote_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteApi->patch_sales_quote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_quote_id** | **str**| (v1.0) id for salesQuote |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**SalesQuote**](SalesQuote.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedsalesQuote |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_quote**
> SalesQuote post_sales_quote(company_id, content_type, unknown_base_type)

Creates an object of type salesQuote in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_quote_api
from pybusinesscentral.model.sales_quote import SalesQuote
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
    api_instance = sales_quote_api.SalesQuoteApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    content_type = "Content-Type_example" # str | (v1.0) application/json
    unknown_base_type = {
        id="id_example",
        number="number_example",
        external_document_number="external_document_number_example",
        document_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        customer_id="customer_id_example",
        contact_id="contact_id_example",
        customer_number="customer_number_example",
        customer_name="customer_name_example",
        bill_to_name="bill_to_name_example",
        bill_to_customer_id="bill_to_customer_id_example",
        bill_to_customer_number="bill_to_customer_number_example",
        ship_to_name="ship_to_name_example",
        ship_to_contact="ship_to_contact_example",
        selling_postal_address=,
        billing_postal_address=,
        shipping_postal_address=,
        currency_id="currency_id_example",
        currency_code="currency_code_example",
        payment_terms_id="payment_terms_id_example",
        shipment_method_id="shipment_method_id_example",
        salesperson="salesperson_example",
        discount_amount=3.14,
        total_amount_excluding_tax=3.14,
        total_tax_amount=3.14,
        total_amount_including_tax=3.14,
        status="status_example",
        sent_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        valid_until_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        accepted_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        phone_number="phone_number_example",
        email="email_example",
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type salesQuote in Dynamics 365 Business Central
        api_response = api_instance.post_sales_quote(company_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteApi->post_sales_quote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**SalesQuote**](SalesQuote.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new salesQuote has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_action_sales_quotes**
> send_action_sales_quotes(company_id, sales_quote_id)

Performs the send action for salesQuotes entity

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_quote_api
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
    api_instance = sales_quote_api.SalesQuoteApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_quote_id = "salesQuote_id_example" # str | (v1.0) id for salesQuote

    # example passing only required values which don't have defaults set
    try:
        # Performs the send action for salesQuotes entity
        api_instance.send_action_sales_quotes(company_id, sales_quote_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesQuoteApi->send_action_sales_quotes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_quote_id** | **str**| (v1.0) id for salesQuote |

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
**204** | (v1.0) Succesfully performed a send action on the Dynamic 365 Business Central salesQuotes entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

