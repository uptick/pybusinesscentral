# pybusinesscentral.SalesInvoiceApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_action_sales_invoices**](SalesInvoiceApi.md#cancel_action_sales_invoices) | **POST** /companies({company_id})/salesInvoices({salesInvoice_id})/Microsoft.NAV.cancel | Performs the cancel action for salesInvoices entity
[**cancel_and_send_action_sales_invoices**](SalesInvoiceApi.md#cancel_and_send_action_sales_invoices) | **POST** /companies({company_id})/salesInvoices({salesInvoice_id})/Microsoft.NAV.cancelAndSend | Performs the cancelAndSend action for salesInvoices entity
[**delete_sales_invoice**](SalesInvoiceApi.md#delete_sales_invoice) | **DELETE** /companies({company_id})/salesInvoices({salesInvoice_id}) | Deletes an object of type salesInvoice in Dynamics 365 Business Central
[**get_sales_invoice**](SalesInvoiceApi.md#get_sales_invoice) | **GET** /companies({company_id})/salesInvoices({salesInvoice_id}) | Retrieve the properties and relationships of an object of type salesInvoice for Dynamics 365 Business Central.
[**list_sales_invoices**](SalesInvoiceApi.md#list_sales_invoices) | **GET** /companies({company_id})/salesInvoices | Returns a list of salesInvoices
[**make_corrective_credit_memo_action_sales_invoices**](SalesInvoiceApi.md#make_corrective_credit_memo_action_sales_invoices) | **POST** /companies({company_id})/salesInvoices({salesInvoice_id})/Microsoft.NAV.makeCorrectiveCreditMemo | Performs the makeCorrectiveCreditMemo action for salesInvoices entity
[**patch_sales_invoice**](SalesInvoiceApi.md#patch_sales_invoice) | **PATCH** /companies({company_id})/salesInvoices({salesInvoice_id}) | Updates an object of type salesInvoice in Dynamics 365 Business Central
[**post_action_sales_invoices**](SalesInvoiceApi.md#post_action_sales_invoices) | **POST** /companies({company_id})/salesInvoices({salesInvoice_id})/Microsoft.NAV.post | Performs the post action for salesInvoices entity
[**post_and_send_action_sales_invoices**](SalesInvoiceApi.md#post_and_send_action_sales_invoices) | **POST** /companies({company_id})/salesInvoices({salesInvoice_id})/Microsoft.NAV.postAndSend | Performs the postAndSend action for salesInvoices entity
[**post_sales_invoice**](SalesInvoiceApi.md#post_sales_invoice) | **POST** /companies({company_id})/salesInvoices | Creates an object of type salesInvoice in Dynamics 365 Business Central
[**send_action_sales_invoices**](SalesInvoiceApi.md#send_action_sales_invoices) | **POST** /companies({company_id})/salesInvoices({salesInvoice_id})/Microsoft.NAV.send | Performs the send action for salesInvoices entity


# **cancel_action_sales_invoices**
> cancel_action_sales_invoices(company_id, sales_invoice_id)

Performs the cancel action for salesInvoices entity

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_invoice_api
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
    api_instance = sales_invoice_api.SalesInvoiceApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_invoice_id = "salesInvoice_id_example" # str | (v1.0) id for salesInvoice

    # example passing only required values which don't have defaults set
    try:
        # Performs the cancel action for salesInvoices entity
        api_instance.cancel_action_sales_invoices(company_id, sales_invoice_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesInvoiceApi->cancel_action_sales_invoices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_invoice_id** | **str**| (v1.0) id for salesInvoice |

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
**204** | (v1.0) Succesfully performed a cancel action on the Dynamic 365 Business Central salesInvoices entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_and_send_action_sales_invoices**
> cancel_and_send_action_sales_invoices(company_id, sales_invoice_id)

Performs the cancelAndSend action for salesInvoices entity

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_invoice_api
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
    api_instance = sales_invoice_api.SalesInvoiceApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_invoice_id = "salesInvoice_id_example" # str | (v1.0) id for salesInvoice

    # example passing only required values which don't have defaults set
    try:
        # Performs the cancelAndSend action for salesInvoices entity
        api_instance.cancel_and_send_action_sales_invoices(company_id, sales_invoice_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesInvoiceApi->cancel_and_send_action_sales_invoices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_invoice_id** | **str**| (v1.0) id for salesInvoice |

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
**204** | (v1.0) Succesfully performed a cancelAndSend action on the Dynamic 365 Business Central salesInvoices entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sales_invoice**
> delete_sales_invoice(company_id, sales_invoice_id)

Deletes an object of type salesInvoice in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_invoice_api
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
    api_instance = sales_invoice_api.SalesInvoiceApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_invoice_id = "salesInvoice_id_example" # str | (v1.0) id for salesInvoice

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type salesInvoice in Dynamics 365 Business Central
        api_instance.delete_sales_invoice(company_id, sales_invoice_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesInvoiceApi->delete_sales_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_invoice_id** | **str**| (v1.0) id for salesInvoice |

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
**204** | (v1.0) Succesfully deleted the specified salesInvoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_invoice**
> SalesInvoice get_sales_invoice(company_id, sales_invoice_id)

Retrieve the properties and relationships of an object of type salesInvoice for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_invoice_api
from pybusinesscentral.model.sales_invoice import SalesInvoice
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
    api_instance = sales_invoice_api.SalesInvoiceApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_invoice_id = "salesInvoice_id_example" # str | (v1.0) id for salesInvoice
    expand = [
        "salesInvoiceLines",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type salesInvoice for Dynamics 365 Business Central.
        api_response = api_instance.get_sales_invoice(company_id, sales_invoice_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesInvoiceApi->get_sales_invoice: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type salesInvoice for Dynamics 365 Business Central.
        api_response = api_instance.get_sales_invoice(company_id, sales_invoice_id, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesInvoiceApi->get_sales_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_invoice_id** | **str**| (v1.0) id for salesInvoice |
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**SalesInvoice**](SalesInvoice.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested salesInvoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sales_invoices**
> InlineResponse2008 list_sales_invoices(company_id)

Returns a list of salesInvoices

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_invoice_api
from pybusinesscentral.model.inline_response2008 import InlineResponse2008
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
    api_instance = sales_invoice_api.SalesInvoiceApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    expand = [
        "salesInvoiceLines",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of salesInvoices
        api_response = api_instance.list_sales_invoices(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesInvoiceApi->list_sales_invoices: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of salesInvoices
        api_response = api_instance.list_sales_invoices(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesInvoiceApi->list_sales_invoices: %s\n" % e)
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

[**InlineResponse2008**](InlineResponse2008.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of salesInvoices |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **make_corrective_credit_memo_action_sales_invoices**
> make_corrective_credit_memo_action_sales_invoices(company_id, sales_invoice_id)

Performs the makeCorrectiveCreditMemo action for salesInvoices entity

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_invoice_api
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
    api_instance = sales_invoice_api.SalesInvoiceApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_invoice_id = "salesInvoice_id_example" # str | (v1.0) id for salesInvoice

    # example passing only required values which don't have defaults set
    try:
        # Performs the makeCorrectiveCreditMemo action for salesInvoices entity
        api_instance.make_corrective_credit_memo_action_sales_invoices(company_id, sales_invoice_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesInvoiceApi->make_corrective_credit_memo_action_sales_invoices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_invoice_id** | **str**| (v1.0) id for salesInvoice |

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
**204** | (v1.0) Succesfully performed a makeCorrectiveCreditMemo action on the Dynamic 365 Business Central salesInvoices entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sales_invoice**
> SalesInvoice patch_sales_invoice(company_id, sales_invoice_id, content_type, if_match, unknown_base_type)

Updates an object of type salesInvoice in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_invoice_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.sales_invoice import SalesInvoice
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
    api_instance = sales_invoice_api.SalesInvoiceApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_invoice_id = "salesInvoice_id_example" # str | (v1.0) id for salesInvoice
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        id="id_example",
        number="number_example",
        external_document_number="external_document_number_example",
        invoice_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        customer_purchase_order_reference="customer_purchase_order_reference_example",
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
        order_id="order_id_example",
        order_number="order_number_example",
        payment_terms_id="payment_terms_id_example",
        shipment_method_id="shipment_method_id_example",
        salesperson="salesperson_example",
        prices_include_tax=True,
        remaining_amount=3.14,
        discount_amount=3.14,
        discount_applied_before_tax=True,
        total_amount_excluding_tax=3.14,
        total_tax_amount=3.14,
        total_amount_including_tax=3.14,
        status="status_example",
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        phone_number="phone_number_example",
        email="email_example",
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type salesInvoice in Dynamics 365 Business Central
        api_response = api_instance.patch_sales_invoice(company_id, sales_invoice_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesInvoiceApi->patch_sales_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_invoice_id** | **str**| (v1.0) id for salesInvoice |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**SalesInvoice**](SalesInvoice.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedsalesInvoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_action_sales_invoices**
> post_action_sales_invoices(company_id, sales_invoice_id)

Performs the post action for salesInvoices entity

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_invoice_api
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
    api_instance = sales_invoice_api.SalesInvoiceApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_invoice_id = "salesInvoice_id_example" # str | (v1.0) id for salesInvoice

    # example passing only required values which don't have defaults set
    try:
        # Performs the post action for salesInvoices entity
        api_instance.post_action_sales_invoices(company_id, sales_invoice_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesInvoiceApi->post_action_sales_invoices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_invoice_id** | **str**| (v1.0) id for salesInvoice |

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
**204** | (v1.0) Succesfully performed a post action on the Dynamic 365 Business Central salesInvoices entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_and_send_action_sales_invoices**
> post_and_send_action_sales_invoices(company_id, sales_invoice_id)

Performs the postAndSend action for salesInvoices entity

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_invoice_api
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
    api_instance = sales_invoice_api.SalesInvoiceApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_invoice_id = "salesInvoice_id_example" # str | (v1.0) id for salesInvoice

    # example passing only required values which don't have defaults set
    try:
        # Performs the postAndSend action for salesInvoices entity
        api_instance.post_and_send_action_sales_invoices(company_id, sales_invoice_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesInvoiceApi->post_and_send_action_sales_invoices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_invoice_id** | **str**| (v1.0) id for salesInvoice |

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
**204** | (v1.0) Succesfully performed a postAndSend action on the Dynamic 365 Business Central salesInvoices entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_invoice**
> SalesInvoice post_sales_invoice(company_id, content_type, unknown_base_type)

Creates an object of type salesInvoice in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_invoice_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.sales_invoice import SalesInvoice
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
    api_instance = sales_invoice_api.SalesInvoiceApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    content_type = "Content-Type_example" # str | (v1.0) application/json
    unknown_base_type = {
        id="id_example",
        number="number_example",
        external_document_number="external_document_number_example",
        invoice_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        customer_purchase_order_reference="customer_purchase_order_reference_example",
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
        order_id="order_id_example",
        order_number="order_number_example",
        payment_terms_id="payment_terms_id_example",
        shipment_method_id="shipment_method_id_example",
        salesperson="salesperson_example",
        prices_include_tax=True,
        remaining_amount=3.14,
        discount_amount=3.14,
        discount_applied_before_tax=True,
        total_amount_excluding_tax=3.14,
        total_tax_amount=3.14,
        total_amount_including_tax=3.14,
        status="status_example",
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        phone_number="phone_number_example",
        email="email_example",
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type salesInvoice in Dynamics 365 Business Central
        api_response = api_instance.post_sales_invoice(company_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesInvoiceApi->post_sales_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**SalesInvoice**](SalesInvoice.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new salesInvoice has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_action_sales_invoices**
> send_action_sales_invoices(company_id, sales_invoice_id)

Performs the send action for salesInvoices entity

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_invoice_api
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
    api_instance = sales_invoice_api.SalesInvoiceApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_invoice_id = "salesInvoice_id_example" # str | (v1.0) id for salesInvoice

    # example passing only required values which don't have defaults set
    try:
        # Performs the send action for salesInvoices entity
        api_instance.send_action_sales_invoices(company_id, sales_invoice_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesInvoiceApi->send_action_sales_invoices: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_invoice_id** | **str**| (v1.0) id for salesInvoice |

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
**204** | (v1.0) Succesfully performed a send action on the Dynamic 365 Business Central salesInvoices entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

