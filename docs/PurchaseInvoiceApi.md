# pybusinesscentral.PurchaseInvoiceApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_purchase_invoice**](PurchaseInvoiceApi.md#delete_purchase_invoice) | **DELETE** /companies({company_id})/purchaseInvoices({purchaseInvoice_id}) | Deletes an object of type purchaseInvoice in Dynamics 365 Business Central
[**get_purchase_invoice**](PurchaseInvoiceApi.md#get_purchase_invoice) | **GET** /companies({company_id})/purchaseInvoices({purchaseInvoice_id}) | Retrieve the properties and relationships of an object of type purchaseInvoice for Dynamics 365 Business Central.
[**list_purchase_invoices**](PurchaseInvoiceApi.md#list_purchase_invoices) | **GET** /companies({company_id})/purchaseInvoices | Returns a list of purchaseInvoices
[**patch_purchase_invoice**](PurchaseInvoiceApi.md#patch_purchase_invoice) | **PATCH** /companies({company_id})/purchaseInvoices({purchaseInvoice_id}) | Updates an object of type purchaseInvoice in Dynamics 365 Business Central
[**post_purchase_invoice**](PurchaseInvoiceApi.md#post_purchase_invoice) | **POST** /companies({company_id})/purchaseInvoices | Creates an object of type purchaseInvoice in Dynamics 365 Business Central


# **delete_purchase_invoice**
> delete_purchase_invoice(company_id, purchase_invoice_id)

Deletes an object of type purchaseInvoice in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import purchase_invoice_api
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
    api_instance = purchase_invoice_api.PurchaseInvoiceApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    purchase_invoice_id = "purchaseInvoice_id_example" # str | (v1.0) id for purchaseInvoice

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type purchaseInvoice in Dynamics 365 Business Central
        api_instance.delete_purchase_invoice(company_id, purchase_invoice_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceApi->delete_purchase_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **purchase_invoice_id** | **str**| (v1.0) id for purchaseInvoice |

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
**204** | (v1.0) Succesfully deleted the specified purchaseInvoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_purchase_invoice**
> PurchaseInvoice get_purchase_invoice(company_id, purchase_invoice_id)

Retrieve the properties and relationships of an object of type purchaseInvoice for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import purchase_invoice_api
from pybusinesscentral.model.purchase_invoice import PurchaseInvoice
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
    api_instance = purchase_invoice_api.PurchaseInvoiceApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    purchase_invoice_id = "purchaseInvoice_id_example" # str | (v1.0) id for purchaseInvoice
    expand = [
        "purchaseInvoiceLines",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type purchaseInvoice for Dynamics 365 Business Central.
        api_response = api_instance.get_purchase_invoice(company_id, purchase_invoice_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceApi->get_purchase_invoice: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type purchaseInvoice for Dynamics 365 Business Central.
        api_response = api_instance.get_purchase_invoice(company_id, purchase_invoice_id, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceApi->get_purchase_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **purchase_invoice_id** | **str**| (v1.0) id for purchaseInvoice |
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**PurchaseInvoice**](PurchaseInvoice.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested purchaseInvoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_purchase_invoices**
> InlineResponse2008 list_purchase_invoices(company_id)

Returns a list of purchaseInvoices

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import purchase_invoice_api
from pybusinesscentral.model.inline_response2008 import InlineResponse2008
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
    api_instance = purchase_invoice_api.PurchaseInvoiceApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    expand = [
        "purchaseInvoiceLines",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of purchaseInvoices
        api_response = api_instance.list_purchase_invoices(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceApi->list_purchase_invoices: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of purchaseInvoices
        api_response = api_instance.list_purchase_invoices(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceApi->list_purchase_invoices: %s\n" % e)
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
**200** | (v1.0) Succesfully returned a list of purchaseInvoices |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_purchase_invoice**
> PurchaseInvoice patch_purchase_invoice(company_id, purchase_invoice_id, content_type, if_match, unknown_base_type)

Updates an object of type purchaseInvoice in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import purchase_invoice_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.purchase_invoice import PurchaseInvoice
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
    api_instance = purchase_invoice_api.PurchaseInvoiceApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    purchase_invoice_id = "purchaseInvoice_id_example" # str | (v1.0) id for purchaseInvoice
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        id="id_example",
        number="number_example",
        invoice_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        vendor_invoice_number="vendor_invoice_number_example",
        vendor_id="vendor_id_example",
        vendor_number="vendor_number_example",
        vendor_name="vendor_name_example",
        pay_to_name="pay_to_name_example",
        pay_to_contact="pay_to_contact_example",
        pay_to_vendor_id="pay_to_vendor_id_example",
        pay_to_vendor_number="pay_to_vendor_number_example",
        ship_to_name="ship_to_name_example",
        ship_to_contact="ship_to_contact_example",
        buy_from_address=,
        pay_to_address=,
        ship_to_address=,
        currency_id="currency_id_example",
        currency_code="currency_code_example",
        prices_include_tax=True,
        discount_amount=3.14,
        discount_applied_before_tax=True,
        total_amount_excluding_tax=3.14,
        total_tax_amount=3.14,
        total_amount_including_tax=3.14,
        status="status_example",
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type purchaseInvoice in Dynamics 365 Business Central
        api_response = api_instance.patch_purchase_invoice(company_id, purchase_invoice_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceApi->patch_purchase_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **purchase_invoice_id** | **str**| (v1.0) id for purchaseInvoice |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**PurchaseInvoice**](PurchaseInvoice.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedpurchaseInvoice |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_purchase_invoice**
> PurchaseInvoice post_purchase_invoice(company_id, content_type, unknown_base_type)

Creates an object of type purchaseInvoice in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import purchase_invoice_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.purchase_invoice import PurchaseInvoice
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
    api_instance = purchase_invoice_api.PurchaseInvoiceApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    content_type = "Content-Type_example" # str | (v1.0) application/json
    unknown_base_type = {
        id="id_example",
        number="number_example",
        invoice_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        due_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        vendor_invoice_number="vendor_invoice_number_example",
        vendor_id="vendor_id_example",
        vendor_number="vendor_number_example",
        vendor_name="vendor_name_example",
        pay_to_name="pay_to_name_example",
        pay_to_contact="pay_to_contact_example",
        pay_to_vendor_id="pay_to_vendor_id_example",
        pay_to_vendor_number="pay_to_vendor_number_example",
        ship_to_name="ship_to_name_example",
        ship_to_contact="ship_to_contact_example",
        buy_from_address=,
        pay_to_address=,
        ship_to_address=,
        currency_id="currency_id_example",
        currency_code="currency_code_example",
        prices_include_tax=True,
        discount_amount=3.14,
        discount_applied_before_tax=True,
        total_amount_excluding_tax=3.14,
        total_tax_amount=3.14,
        total_amount_including_tax=3.14,
        status="status_example",
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
    } # UNKNOWN_BASE_TYPE | 
    expand = [
        "purchaseInvoiceLines",
    ] # [str] | (v1.0) Entities to expand (optional)

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type purchaseInvoice in Dynamics 365 Business Central
        api_response = api_instance.post_purchase_invoice(company_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceApi->post_purchase_invoice: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Creates an object of type purchaseInvoice in Dynamics 365 Business Central
        api_response = api_instance.post_purchase_invoice(company_id, content_type, unknown_base_type, expand=expand)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PurchaseInvoiceApi->post_purchase_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]

### Return type

[**PurchaseInvoice**](PurchaseInvoice.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new purchaseInvoice has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

