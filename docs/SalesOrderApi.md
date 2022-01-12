# pybusinesscentral.SalesOrderApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_sales_order**](SalesOrderApi.md#delete_sales_order) | **DELETE** /companies({company_id})/salesOrders({salesOrder_id}) | Deletes an object of type salesOrder in Dynamics 365 Business Central
[**get_sales_order**](SalesOrderApi.md#get_sales_order) | **GET** /companies({company_id})/salesOrders({salesOrder_id}) | Retrieve the properties and relationships of an object of type salesOrder for Dynamics 365 Business Central.
[**list_sales_orders**](SalesOrderApi.md#list_sales_orders) | **GET** /companies({company_id})/salesOrders | Returns a list of salesOrders
[**patch_sales_order**](SalesOrderApi.md#patch_sales_order) | **PATCH** /companies({company_id})/salesOrders({salesOrder_id}) | Updates an object of type salesOrder in Dynamics 365 Business Central
[**post_sales_order**](SalesOrderApi.md#post_sales_order) | **POST** /companies({company_id})/salesOrders | Creates an object of type salesOrder in Dynamics 365 Business Central
[**ship_and_invoice_action_sales_orders**](SalesOrderApi.md#ship_and_invoice_action_sales_orders) | **POST** /companies({company_id})/salesOrders({salesOrder_id})/Microsoft.NAV.shipAndInvoice | Performs the shipAndInvoice action for salesOrders entity


# **delete_sales_order**
> delete_sales_order(company_id, sales_order_id)

Deletes an object of type salesOrder in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_order_api
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
    api_instance = sales_order_api.SalesOrderApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_order_id = "salesOrder_id_example" # str | (v1.0) id for salesOrder

    # example passing only required values which don't have defaults set
    try:
        # Deletes an object of type salesOrder in Dynamics 365 Business Central
        api_instance.delete_sales_order(company_id, sales_order_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesOrderApi->delete_sales_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_order_id** | **str**| (v1.0) id for salesOrder |

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
**204** | (v1.0) Succesfully deleted the specified salesOrder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sales_order**
> SalesOrder get_sales_order(company_id, sales_order_id)

Retrieve the properties and relationships of an object of type salesOrder for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_order_api
from pybusinesscentral.model.sales_order import SalesOrder
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
    api_instance = sales_order_api.SalesOrderApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_order_id = "salesOrder_id_example" # str | (v1.0) id for salesOrder
    expand = [
        "salesOrderLines",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type salesOrder for Dynamics 365 Business Central.
        api_response = api_instance.get_sales_order(company_id, sales_order_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesOrderApi->get_sales_order: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type salesOrder for Dynamics 365 Business Central.
        api_response = api_instance.get_sales_order(company_id, sales_order_id, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesOrderApi->get_sales_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_order_id** | **str**| (v1.0) id for salesOrder |
 **expand** | **[str]**| (v1.0) Entities to expand | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**SalesOrder**](SalesOrder.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested salesOrder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sales_orders**
> InlineResponse20031 list_sales_orders(company_id)

Returns a list of salesOrders

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_order_api
from pybusinesscentral.model.inline_response20031 import InlineResponse20031
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
    api_instance = sales_order_api.SalesOrderApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    expand = [
        "salesOrderLines",
    ] # [str] | (v1.0) Entities to expand (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of salesOrders
        api_response = api_instance.list_sales_orders(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesOrderApi->list_sales_orders: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of salesOrders
        api_response = api_instance.list_sales_orders(company_id, top=top, skip=skip, limit=limit, filter=filter, expand=expand, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesOrderApi->list_sales_orders: %s\n" % e)
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

[**InlineResponse20031**](InlineResponse20031.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of salesOrders |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_sales_order**
> SalesOrder patch_sales_order(company_id, sales_order_id, content_type, if_match, unknown_base_type)

Updates an object of type salesOrder in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_order_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.sales_order import SalesOrder
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
    api_instance = sales_order_api.SalesOrderApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_order_id = "salesOrder_id_example" # str | (v1.0) id for salesOrder
    content_type = "Content-Type_example" # str | (v1.0) application/json
    if_match = "If-Match_example" # str | (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
    unknown_base_type = {
        id="id_example",
        number="number_example",
        external_document_number="external_document_number_example",
        order_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
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
        prices_include_tax=True,
        payment_terms_id="payment_terms_id_example",
        shipment_method_id="shipment_method_id_example",
        salesperson="salesperson_example",
        partial_shipping=True,
        requested_delivery_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        discount_amount=3.14,
        discount_applied_before_tax=True,
        total_amount_excluding_tax=3.14,
        total_tax_amount=3.14,
        total_amount_including_tax=3.14,
        fully_shipped=True,
        status="status_example",
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        phone_number="phone_number_example",
        email="email_example",
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Updates an object of type salesOrder in Dynamics 365 Business Central
        api_response = api_instance.patch_sales_order(company_id, sales_order_id, content_type, if_match, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesOrderApi->patch_sales_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_order_id** | **str**| (v1.0) id for salesOrder |
 **content_type** | **str**| (v1.0) application/json |
 **if_match** | **str**| (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated. |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**SalesOrder**](SalesOrder.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully updated the specifiedsalesOrder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_sales_order**
> SalesOrder post_sales_order(company_id, content_type, unknown_base_type)

Creates an object of type salesOrder in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_order_api
from pybusinesscentral.model.unknownbasetype import UNKNOWNBASETYPE
from pybusinesscentral.model.sales_order import SalesOrder
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
    api_instance = sales_order_api.SalesOrderApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    content_type = "Content-Type_example" # str | (v1.0) application/json
    unknown_base_type = {
        id="id_example",
        number="number_example",
        external_document_number="external_document_number_example",
        order_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
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
        prices_include_tax=True,
        payment_terms_id="payment_terms_id_example",
        shipment_method_id="shipment_method_id_example",
        salesperson="salesperson_example",
        partial_shipping=True,
        requested_delivery_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
        discount_amount=3.14,
        discount_applied_before_tax=True,
        total_amount_excluding_tax=3.14,
        total_tax_amount=3.14,
        total_amount_including_tax=3.14,
        fully_shipped=True,
        status="status_example",
        last_modified_date_time=dateutil_parser('1970-01-01T00:00:00.00Z'),
        phone_number="phone_number_example",
        email="email_example",
    } # UNKNOWN_BASE_TYPE | 

    # example passing only required values which don't have defaults set
    try:
        # Creates an object of type salesOrder in Dynamics 365 Business Central
        api_response = api_instance.post_sales_order(company_id, content_type, unknown_base_type)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesOrderApi->post_sales_order: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **content_type** | **str**| (v1.0) application/json |
 **unknown_base_type** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)|  |

### Return type

[**SalesOrder**](SalesOrder.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new salesOrder has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ship_and_invoice_action_sales_orders**
> ship_and_invoice_action_sales_orders(company_id, sales_order_id)

Performs the shipAndInvoice action for salesOrders entity

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import sales_order_api
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
    api_instance = sales_order_api.SalesOrderApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_order_id = "salesOrder_id_example" # str | (v1.0) id for salesOrder

    # example passing only required values which don't have defaults set
    try:
        # Performs the shipAndInvoice action for salesOrders entity
        api_instance.ship_and_invoice_action_sales_orders(company_id, sales_order_id)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling SalesOrderApi->ship_and_invoice_action_sales_orders: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_order_id** | **str**| (v1.0) id for salesOrder |

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
**204** | (v1.0) Succesfully performed a shipAndInvoice action on the Dynamic 365 Business Central salesOrders entity |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

