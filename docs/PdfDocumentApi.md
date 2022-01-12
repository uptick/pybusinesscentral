# pybusinesscentral.PdfDocumentApi

All URIs are relative to *https://api.businesscentral.dynamics.com/v2.0/sandbox/api/v2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_pdf_document**](PdfDocumentApi.md#get_pdf_document) | **GET** /companies({company_id})/pdfDocument({pdfDocument_id}) | Retrieve the properties and relationships of an object of type pdfDocument for Dynamics 365 Business Central.
[**get_pdf_document_for_purchase_invoice**](PdfDocumentApi.md#get_pdf_document_for_purchase_invoice) | **GET** /companies({company_id})/purchaseInvoices({purchaseInvoice_id})/pdfDocument({pdfDocument_id}) | Retrieve the properties and relationships of an object of type pdfDocument for Dynamics 365 Business Central.
[**get_pdf_document_for_sales_credit_memo**](PdfDocumentApi.md#get_pdf_document_for_sales_credit_memo) | **GET** /companies({company_id})/salesCreditMemos({salesCreditMemo_id})/pdfDocument({pdfDocument_id}) | Retrieve the properties and relationships of an object of type pdfDocument for Dynamics 365 Business Central.
[**get_pdf_document_for_sales_invoice**](PdfDocumentApi.md#get_pdf_document_for_sales_invoice) | **GET** /companies({company_id})/salesInvoices({salesInvoice_id})/pdfDocument({pdfDocument_id}) | Retrieve the properties and relationships of an object of type pdfDocument for Dynamics 365 Business Central.
[**get_pdf_document_for_sales_quote**](PdfDocumentApi.md#get_pdf_document_for_sales_quote) | **GET** /companies({company_id})/salesQuotes({salesQuote_id})/pdfDocument({pdfDocument_id}) | Retrieve the properties and relationships of an object of type pdfDocument for Dynamics 365 Business Central.
[**list_pdf_document**](PdfDocumentApi.md#list_pdf_document) | **GET** /companies({company_id})/pdfDocument | Returns a list of pdfDocument
[**list_pdf_document_for_purchase_invoice**](PdfDocumentApi.md#list_pdf_document_for_purchase_invoice) | **GET** /companies({company_id})/purchaseInvoices({purchaseInvoice_id})/pdfDocument | Returns a list of pdfDocument
[**list_pdf_document_for_sales_credit_memo**](PdfDocumentApi.md#list_pdf_document_for_sales_credit_memo) | **GET** /companies({company_id})/salesCreditMemos({salesCreditMemo_id})/pdfDocument | Returns a list of pdfDocument
[**list_pdf_document_for_sales_invoice**](PdfDocumentApi.md#list_pdf_document_for_sales_invoice) | **GET** /companies({company_id})/salesInvoices({salesInvoice_id})/pdfDocument | Returns a list of pdfDocument
[**list_pdf_document_for_sales_quote**](PdfDocumentApi.md#list_pdf_document_for_sales_quote) | **GET** /companies({company_id})/salesQuotes({salesQuote_id})/pdfDocument | Returns a list of pdfDocument


# **get_pdf_document**
> PdfDocument get_pdf_document(company_id, pdf_document_id)

Retrieve the properties and relationships of an object of type pdfDocument for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import pdf_document_api
from pybusinesscentral.model.pdf_document import PdfDocument
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
    api_instance = pdf_document_api.PdfDocumentApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    pdf_document_id = "pdfDocument_id_example" # str | (v1.0) id for pdfDocument
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type pdfDocument for Dynamics 365 Business Central.
        api_response = api_instance.get_pdf_document(company_id, pdf_document_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PdfDocumentApi->get_pdf_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type pdfDocument for Dynamics 365 Business Central.
        api_response = api_instance.get_pdf_document(company_id, pdf_document_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PdfDocumentApi->get_pdf_document: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **pdf_document_id** | **str**| (v1.0) id for pdfDocument |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**PdfDocument**](PdfDocument.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested pdfDocument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_document_for_purchase_invoice**
> PdfDocument get_pdf_document_for_purchase_invoice(company_id, purchase_invoice_id, pdf_document_id)

Retrieve the properties and relationships of an object of type pdfDocument for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import pdf_document_api
from pybusinesscentral.model.pdf_document import PdfDocument
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
    api_instance = pdf_document_api.PdfDocumentApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    purchase_invoice_id = "purchaseInvoice_id_example" # str | (v1.0) id for purchaseInvoice
    pdf_document_id = "pdfDocument_id_example" # str | (v1.0) id for pdfDocument
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type pdfDocument for Dynamics 365 Business Central.
        api_response = api_instance.get_pdf_document_for_purchase_invoice(company_id, purchase_invoice_id, pdf_document_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PdfDocumentApi->get_pdf_document_for_purchase_invoice: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type pdfDocument for Dynamics 365 Business Central.
        api_response = api_instance.get_pdf_document_for_purchase_invoice(company_id, purchase_invoice_id, pdf_document_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PdfDocumentApi->get_pdf_document_for_purchase_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **purchase_invoice_id** | **str**| (v1.0) id for purchaseInvoice |
 **pdf_document_id** | **str**| (v1.0) id for pdfDocument |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**PdfDocument**](PdfDocument.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested pdfDocument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_document_for_sales_credit_memo**
> PdfDocument get_pdf_document_for_sales_credit_memo(company_id, sales_credit_memo_id, pdf_document_id)

Retrieve the properties and relationships of an object of type pdfDocument for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import pdf_document_api
from pybusinesscentral.model.pdf_document import PdfDocument
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
    api_instance = pdf_document_api.PdfDocumentApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_credit_memo_id = "salesCreditMemo_id_example" # str | (v1.0) id for salesCreditMemo
    pdf_document_id = "pdfDocument_id_example" # str | (v1.0) id for pdfDocument
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type pdfDocument for Dynamics 365 Business Central.
        api_response = api_instance.get_pdf_document_for_sales_credit_memo(company_id, sales_credit_memo_id, pdf_document_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PdfDocumentApi->get_pdf_document_for_sales_credit_memo: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type pdfDocument for Dynamics 365 Business Central.
        api_response = api_instance.get_pdf_document_for_sales_credit_memo(company_id, sales_credit_memo_id, pdf_document_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PdfDocumentApi->get_pdf_document_for_sales_credit_memo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_credit_memo_id** | **str**| (v1.0) id for salesCreditMemo |
 **pdf_document_id** | **str**| (v1.0) id for pdfDocument |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**PdfDocument**](PdfDocument.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested pdfDocument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_document_for_sales_invoice**
> PdfDocument get_pdf_document_for_sales_invoice(company_id, sales_invoice_id, pdf_document_id)

Retrieve the properties and relationships of an object of type pdfDocument for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import pdf_document_api
from pybusinesscentral.model.pdf_document import PdfDocument
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
    api_instance = pdf_document_api.PdfDocumentApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_invoice_id = "salesInvoice_id_example" # str | (v1.0) id for salesInvoice
    pdf_document_id = "pdfDocument_id_example" # str | (v1.0) id for pdfDocument
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type pdfDocument for Dynamics 365 Business Central.
        api_response = api_instance.get_pdf_document_for_sales_invoice(company_id, sales_invoice_id, pdf_document_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PdfDocumentApi->get_pdf_document_for_sales_invoice: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type pdfDocument for Dynamics 365 Business Central.
        api_response = api_instance.get_pdf_document_for_sales_invoice(company_id, sales_invoice_id, pdf_document_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PdfDocumentApi->get_pdf_document_for_sales_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_invoice_id** | **str**| (v1.0) id for salesInvoice |
 **pdf_document_id** | **str**| (v1.0) id for pdfDocument |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**PdfDocument**](PdfDocument.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested pdfDocument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pdf_document_for_sales_quote**
> PdfDocument get_pdf_document_for_sales_quote(company_id, sales_quote_id, pdf_document_id)

Retrieve the properties and relationships of an object of type pdfDocument for Dynamics 365 Business Central.

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import pdf_document_api
from pybusinesscentral.model.pdf_document import PdfDocument
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
    api_instance = pdf_document_api.PdfDocumentApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_quote_id = "salesQuote_id_example" # str | (v1.0) id for salesQuote
    pdf_document_id = "pdfDocument_id_example" # str | (v1.0) id for pdfDocument
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Retrieve the properties and relationships of an object of type pdfDocument for Dynamics 365 Business Central.
        api_response = api_instance.get_pdf_document_for_sales_quote(company_id, sales_quote_id, pdf_document_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PdfDocumentApi->get_pdf_document_for_sales_quote: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Retrieve the properties and relationships of an object of type pdfDocument for Dynamics 365 Business Central.
        api_response = api_instance.get_pdf_document_for_sales_quote(company_id, sales_quote_id, pdf_document_id, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PdfDocumentApi->get_pdf_document_for_sales_quote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_quote_id** | **str**| (v1.0) id for salesQuote |
 **pdf_document_id** | **str**| (v1.0) id for pdfDocument |
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**PdfDocument**](PdfDocument.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned the requested pdfDocument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pdf_document**
> InlineResponse20010 list_pdf_document(company_id)

Returns a list of pdfDocument

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import pdf_document_api
from pybusinesscentral.model.inline_response20010 import InlineResponse20010
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
    api_instance = pdf_document_api.PdfDocumentApi(api_client)
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
        # Returns a list of pdfDocument
        api_response = api_instance.list_pdf_document(company_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PdfDocumentApi->list_pdf_document: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of pdfDocument
        api_response = api_instance.list_pdf_document(company_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PdfDocumentApi->list_pdf_document: %s\n" % e)
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

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of pdfDocument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pdf_document_for_purchase_invoice**
> InlineResponse20010 list_pdf_document_for_purchase_invoice(company_id, purchase_invoice_id)

Returns a list of pdfDocument

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import pdf_document_api
from pybusinesscentral.model.inline_response20010 import InlineResponse20010
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
    api_instance = pdf_document_api.PdfDocumentApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    purchase_invoice_id = "purchaseInvoice_id_example" # str | (v1.0) id for purchaseInvoice
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of pdfDocument
        api_response = api_instance.list_pdf_document_for_purchase_invoice(company_id, purchase_invoice_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PdfDocumentApi->list_pdf_document_for_purchase_invoice: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of pdfDocument
        api_response = api_instance.list_pdf_document_for_purchase_invoice(company_id, purchase_invoice_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PdfDocumentApi->list_pdf_document_for_purchase_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **purchase_invoice_id** | **str**| (v1.0) id for purchaseInvoice |
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional]
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional]
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional]
 **filter** | **str**| (v1.0) Filtering expression | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of pdfDocument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pdf_document_for_sales_credit_memo**
> InlineResponse20010 list_pdf_document_for_sales_credit_memo(company_id, sales_credit_memo_id)

Returns a list of pdfDocument

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import pdf_document_api
from pybusinesscentral.model.inline_response20010 import InlineResponse20010
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
    api_instance = pdf_document_api.PdfDocumentApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_credit_memo_id = "salesCreditMemo_id_example" # str | (v1.0) id for salesCreditMemo
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of pdfDocument
        api_response = api_instance.list_pdf_document_for_sales_credit_memo(company_id, sales_credit_memo_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PdfDocumentApi->list_pdf_document_for_sales_credit_memo: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of pdfDocument
        api_response = api_instance.list_pdf_document_for_sales_credit_memo(company_id, sales_credit_memo_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PdfDocumentApi->list_pdf_document_for_sales_credit_memo: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_credit_memo_id** | **str**| (v1.0) id for salesCreditMemo |
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional]
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional]
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional]
 **filter** | **str**| (v1.0) Filtering expression | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of pdfDocument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pdf_document_for_sales_invoice**
> InlineResponse20010 list_pdf_document_for_sales_invoice(company_id, sales_invoice_id)

Returns a list of pdfDocument

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import pdf_document_api
from pybusinesscentral.model.inline_response20010 import InlineResponse20010
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
    api_instance = pdf_document_api.PdfDocumentApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_invoice_id = "salesInvoice_id_example" # str | (v1.0) id for salesInvoice
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of pdfDocument
        api_response = api_instance.list_pdf_document_for_sales_invoice(company_id, sales_invoice_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PdfDocumentApi->list_pdf_document_for_sales_invoice: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of pdfDocument
        api_response = api_instance.list_pdf_document_for_sales_invoice(company_id, sales_invoice_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PdfDocumentApi->list_pdf_document_for_sales_invoice: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_invoice_id** | **str**| (v1.0) id for salesInvoice |
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional]
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional]
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional]
 **filter** | **str**| (v1.0) Filtering expression | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of pdfDocument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_pdf_document_for_sales_quote**
> InlineResponse20010 list_pdf_document_for_sales_quote(company_id, sales_quote_id)

Returns a list of pdfDocument

### Example

* OAuth Authentication (oAuth):
```python
import time
import pybusinesscentral
from pybusinesscentral.api import pdf_document_api
from pybusinesscentral.model.inline_response20010 import InlineResponse20010
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
    api_instance = pdf_document_api.PdfDocumentApi(api_client)
    company_id = "company_id_example" # str | (v1.0) id for company
    sales_quote_id = "salesQuote_id_example" # str | (v1.0) id for salesQuote
    top = 1 # int | (v1.0) Number of items to return from the top of the list (optional)
    skip = 1 # int | (v1.0) Number of items to skip from the list (optional)
    limit = 1 # int | (v1.0) Number of items to return from the list (optional)
    filter = "$filter_example" # str | (v1.0) Filtering expression (optional)
    select = [
        "id",
    ] # [str] | (v1.0) Selected properties to be retrieved (optional)

    # example passing only required values which don't have defaults set
    try:
        # Returns a list of pdfDocument
        api_response = api_instance.list_pdf_document_for_sales_quote(company_id, sales_quote_id)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PdfDocumentApi->list_pdf_document_for_sales_quote: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Returns a list of pdfDocument
        api_response = api_instance.list_pdf_document_for_sales_quote(company_id, sales_quote_id, top=top, skip=skip, limit=limit, filter=filter, select=select)
        pprint(api_response)
    except pybusinesscentral.ApiException as e:
        print("Exception when calling PdfDocumentApi->list_pdf_document_for_sales_quote: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_id** | **str**| (v1.0) id for company |
 **sales_quote_id** | **str**| (v1.0) id for salesQuote |
 **top** | **int**| (v1.0) Number of items to return from the top of the list | [optional]
 **skip** | **int**| (v1.0) Number of items to skip from the list | [optional]
 **limit** | **int**| (v1.0) Number of items to return from the list | [optional]
 **filter** | **str**| (v1.0) Filtering expression | [optional]
 **select** | **[str]**| (v1.0) Selected properties to be retrieved | [optional]

### Return type

[**InlineResponse20010**](InlineResponse20010.md)

### Authorization

[oAuth](../README.md#oAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | (v1.0) Succesfully returned a list of pdfDocument |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

