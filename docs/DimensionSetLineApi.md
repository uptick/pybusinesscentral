# pybusinesscentral.DimensionSetLineApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dimension_set_lines_for_sales_invoice_line**](DimensionSetLineApi.md#get_dimension_set_lines_for_sales_invoice_line) | **GET** /companies({company_id})/salesInvoices({salesInvoice_id})/salesInvoiceLines({salesInvoiceLine_id})/dimensionSetLines | Retrieve the properties and relationships of the list of dimensionSetLines for a salesInvoiceLine.
[**post_dimension_set_line**](DimensionSetLineApi.md#post_dimension_set_line) | **POST** /companies({company_id})/salesInvoices({salesInvoice_id})/salesInvoiceLines({salesInvoiceLine_id})/dimensionSetLines | Creates an object of type dimensionSetLine in Dynamics 365 Business Central


# **get_dimension_set_lines_for_sales_invoice_line**
> DimensionSetLine get_dimension_set_lines_for_sales_invoice_line(company_id, sales_invoice_id, sales_invoice_line_id)

Retrieve the properties and relationships of the list of dimensionSetLines for a salesInvoiceLine.

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.dimension_set_line import DimensionSetLine
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
    api_instance = pybusinesscentral.DimensionSetLineApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    sales_invoice_id = 'sales_invoice_id_example' # str | (v1.0) id for salesInvoice
    sales_invoice_line_id = 'sales_invoice_line_id_example' # str | (v1.0) id for salesInvoiceLine

    try:
        # Retrieve the properties and relationships of the list of dimensionSetLines for a salesInvoiceLine.
        api_response = api_instance.get_dimension_set_lines_for_sales_invoice_line(company_id, sales_invoice_id, sales_invoice_line_id)
        print("The response of DimensionSetLineApi->get_dimension_set_lines_for_sales_invoice_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DimensionSetLineApi->get_dimension_set_lines_for_sales_invoice_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **sales_invoice_id** | **str**| (v1.0) id for salesInvoice | 
 **sales_invoice_line_id** | **str**| (v1.0) id for salesInvoiceLine | 

### Return type

[**DimensionSetLine**](DimensionSetLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested dimensionSetLines |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_dimension_set_line**
> DimensionSetLine post_dimension_set_line(company_id, sales_invoice_id, sales_invoice_line_id, content_type, post_dimension_set_line_request)

Creates an object of type dimensionSetLine in Dynamics 365 Business Central

### Example

* OAuth Authentication (oAuth):

```python
import pybusinesscentral
from pybusinesscentral.model.dimension_set_line import DimensionSetLine
from pybusinesscentral.model.post_dimension_set_line_request import PostDimensionSetLineRequest
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
    api_instance = pybusinesscentral.DimensionSetLineApi(api_client)
    company_id = 'company_id_example' # str | (v1.0) id for company
    sales_invoice_id = 'sales_invoice_id_example' # str | (v1.0) id for salesInvoice
    sales_invoice_line_id = 'sales_invoice_line_id_example' # str | (v1.0) id for salesInvoiceLine
    content_type = 'content_type_example' # str | (v1.0) application/json
    post_dimension_set_line_request = pybusinesscentral.PostDimensionSetLineRequest() # PostDimensionSetLineRequest | 

    try:
        # Creates an object of type dimensionSetLine in Dynamics 365 Business Central
        api_response = api_instance.post_dimension_set_line(company_id, sales_invoice_id, sales_invoice_line_id, content_type, post_dimension_set_line_request)
        print("The response of DimensionSetLineApi->post_dimension_set_line:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DimensionSetLineApi->post_dimension_set_line: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company | 
 **sales_invoice_id** | **str**| (v1.0) id for salesInvoice | 
 **sales_invoice_line_id** | **str**| (v1.0) id for salesInvoiceLine | 
 **content_type** | **str**| (v1.0) application/json | 
 **post_dimension_set_line_request** | [**PostDimensionSetLineRequest**](PostDimensionSetLineRequest.md)|  | 

### Return type

[**DimensionSetLine**](DimensionSetLine.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | (v1.0) A new dimensionSetLine has been succesfully created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

