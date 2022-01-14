"""
    (v2.0) Dynamics 365 Business Central

    (v2.0) Business Central Standard APIs  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pybusinesscentral.api_client import ApiClient, Endpoint as _Endpoint
from pybusinesscentral.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from pybusinesscentral.model.inline_response2007 import InlineResponse2007
from pybusinesscentral.model.payment_term import PaymentTerm


class PaymentTermApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __delete_payment_term(
            self,
            company_id,
            payment_term_id,
            **kwargs
        ):
            """Deletes an object of type paymentTerm in Dynamics 365 Business Central  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_payment_term(company_id, payment_term_id, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str): (v1.0) id for company
                payment_term_id (str): (v1.0) id for paymentTerm

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['company_id'] = \
                company_id
            kwargs['payment_term_id'] = \
                payment_term_id
            return self.call_with_http_info(**kwargs)

        self.delete_payment_term = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'oAuth'
                ],
                'endpoint_path': '/companies({company_id})/paymentTerms({paymentTerm_id})',
                'operation_id': 'delete_payment_term',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'payment_term_id',
                ],
                'required': [
                    'company_id',
                    'payment_term_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'company_id':
                        (str,),
                    'payment_term_id':
                        (str,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'payment_term_id': 'paymentTerm_id',
                },
                'location_map': {
                    'company_id': 'path',
                    'payment_term_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_payment_term
        )

        def __get_payment_term(
            self,
            company_id,
            payment_term_id,
            **kwargs
        ):
            """Retrieve the properties and relationships of an object of type paymentTerm for Dynamics 365 Business Central.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_payment_term(company_id, payment_term_id, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str): (v1.0) id for company
                payment_term_id (str): (v1.0) id for paymentTerm

            Keyword Args:
                select ([str]): (v1.0) Selected properties to be retrieved. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                PaymentTerm
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['company_id'] = \
                company_id
            kwargs['payment_term_id'] = \
                payment_term_id
            return self.call_with_http_info(**kwargs)

        self.get_payment_term = _Endpoint(
            settings={
                'response_type': (PaymentTerm,),
                'auth': [
                    'oAuth'
                ],
                'endpoint_path': '/companies({company_id})/paymentTerms({paymentTerm_id})',
                'operation_id': 'get_payment_term',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'payment_term_id',
                    'select',
                ],
                'required': [
                    'company_id',
                    'payment_term_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'select',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('select',): {

                        "ID": "id",
                        "CODE": "code",
                        "DISPLAYNAME": "displayName",
                        "DUEDATECALCULATION": "dueDateCalculation",
                        "DISCOUNTDATECALCULATION": "discountDateCalculation",
                        "DISCOUNTPERCENT": "discountPercent",
                        "CALCULATEDISCOUNTONCREDITMEMOS": "calculateDiscountOnCreditMemos",
                        "LASTMODIFIEDDATETIME": "lastModifiedDateTime"
                    },
                },
                'openapi_types': {
                    'company_id':
                        (str,),
                    'payment_term_id':
                        (str,),
                    'select':
                        ([str],),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'payment_term_id': 'paymentTerm_id',
                    'select': '$select',
                },
                'location_map': {
                    'company_id': 'path',
                    'payment_term_id': 'path',
                    'select': 'query',
                },
                'collection_format_map': {
                    'select': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__get_payment_term
        )

        def __list_payment_terms(
            self,
            company_id,
            **kwargs
        ):
            """Returns a list of paymentTerms  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_payment_terms(company_id, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str): (v1.0) id for company

            Keyword Args:
                top (int): (v1.0) Number of items to return from the top of the list. [optional]
                skip (int): (v1.0) Number of items to skip from the list. [optional]
                limit (int): (v1.0) Number of items to return from the list. [optional]
                filter (str): (v1.0) Filtering expression. [optional]
                select ([str]): (v1.0) Selected properties to be retrieved. [optional]
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                InlineResponse2007
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['company_id'] = \
                company_id
            return self.call_with_http_info(**kwargs)

        self.list_payment_terms = _Endpoint(
            settings={
                'response_type': (InlineResponse2007,),
                'auth': [
                    'oAuth'
                ],
                'endpoint_path': '/companies({company_id})/paymentTerms',
                'operation_id': 'list_payment_terms',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'top',
                    'skip',
                    'limit',
                    'filter',
                    'select',
                ],
                'required': [
                    'company_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'select',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('select',): {

                        "ID": "id",
                        "CODE": "code",
                        "DISPLAYNAME": "displayName",
                        "DUEDATECALCULATION": "dueDateCalculation",
                        "DISCOUNTDATECALCULATION": "discountDateCalculation",
                        "DISCOUNTPERCENT": "discountPercent",
                        "CALCULATEDISCOUNTONCREDITMEMOS": "calculateDiscountOnCreditMemos",
                        "LASTMODIFIEDDATETIME": "lastModifiedDateTime"
                    },
                },
                'openapi_types': {
                    'company_id':
                        (str,),
                    'top':
                        (int,),
                    'skip':
                        (int,),
                    'limit':
                        (int,),
                    'filter':
                        (str,),
                    'select':
                        ([str],),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'top': '$top',
                    'skip': '$skip',
                    'limit': '$limit',
                    'filter': '$filter',
                    'select': '$select',
                },
                'location_map': {
                    'company_id': 'path',
                    'top': 'query',
                    'skip': 'query',
                    'limit': 'query',
                    'filter': 'query',
                    'select': 'query',
                },
                'collection_format_map': {
                    'select': 'csv',
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client,
            callable=__list_payment_terms
        )

        def __patch_payment_term(
            self,
            company_id,
            payment_term_id,
            content_type,
            if_match,
            payment_term,
            **kwargs
        ):
            """Updates an object of type paymentTerm in Dynamics 365 Business Central  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.patch_payment_term(company_id, payment_term_id, content_type, if_match, payment_term, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str): (v1.0) id for company
                payment_term_id (str): (v1.0) id for paymentTerm
                content_type (str): (v1.0) application/json
                if_match (str): (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
                payment_term (PaymentTerm):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                PaymentTerm
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['company_id'] = \
                company_id
            kwargs['payment_term_id'] = \
                payment_term_id
            kwargs['content_type'] = \
                content_type
            kwargs['if_match'] = \
                if_match
            kwargs['payment_term'] = \
                payment_term
            return self.call_with_http_info(**kwargs)

        self.patch_payment_term = _Endpoint(
            settings={
                'response_type': (PaymentTerm,),
                'auth': [
                    'oAuth'
                ],
                'endpoint_path': '/companies({company_id})/paymentTerms({paymentTerm_id})',
                'operation_id': 'patch_payment_term',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'payment_term_id',
                    'content_type',
                    'if_match',
                    'payment_term',
                ],
                'required': [
                    'company_id',
                    'payment_term_id',
                    'content_type',
                    'if_match',
                    'payment_term',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'company_id':
                        (str,),
                    'payment_term_id':
                        (str,),
                    'content_type':
                        (str,),
                    'if_match':
                        (str,),
                    'payment_term':
                        (PaymentTerm,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'payment_term_id': 'paymentTerm_id',
                    'content_type': 'Content-Type',
                    'if_match': 'If-Match',
                },
                'location_map': {
                    'company_id': 'path',
                    'payment_term_id': 'path',
                    'content_type': 'header',
                    'if_match': 'header',
                    'payment_term': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__patch_payment_term
        )

        def __post_payment_term(
            self,
            company_id,
            content_type,
            payment_term,
            **kwargs
        ):
            """Creates an object of type paymentTerm in Dynamics 365 Business Central  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.post_payment_term(company_id, content_type, payment_term, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str): (v1.0) id for company
                content_type (str): (v1.0) application/json
                payment_term (PaymentTerm):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (int/float/tuple): timeout setting for this request. If
                    one number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                PaymentTerm
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['company_id'] = \
                company_id
            kwargs['content_type'] = \
                content_type
            kwargs['payment_term'] = \
                payment_term
            return self.call_with_http_info(**kwargs)

        self.post_payment_term = _Endpoint(
            settings={
                'response_type': (PaymentTerm,),
                'auth': [
                    'oAuth'
                ],
                'endpoint_path': '/companies({company_id})/paymentTerms',
                'operation_id': 'post_payment_term',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'content_type',
                    'payment_term',
                ],
                'required': [
                    'company_id',
                    'content_type',
                    'payment_term',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'company_id':
                        (str,),
                    'content_type':
                        (str,),
                    'payment_term':
                        (PaymentTerm,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'content_type': 'Content-Type',
                },
                'location_map': {
                    'company_id': 'path',
                    'content_type': 'header',
                    'payment_term': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client,
            callable=__post_payment_term
        )
