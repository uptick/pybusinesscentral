"""
    (v1.0) Dynamics 365 Business Central

    (v1.0) Business Central Standard APIs  # noqa: E501

    The version of the OpenAPI document: 1.0.0
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
from pybusinesscentral.model.income_statement import IncomeStatement
from pybusinesscentral.model.inline_response20039 import InlineResponse20039


class IncomeStatementApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_income_statement(
            self,
            company_id,
            income_statement_line_number,
            **kwargs
        ):
            """Retrieve the properties and relationships of an object of type incomeStatement for Dynamics 365 Business Central.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_income_statement(company_id, income_statement_line_number, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str): (v1.0) id for company
                income_statement_line_number (int): (v1.0) lineNumber for incomeStatement

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
                IncomeStatement
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
            kwargs['income_statement_line_number'] = \
                income_statement_line_number
            return self.call_with_http_info(**kwargs)

        self.get_income_statement = _Endpoint(
            settings={
                'response_type': (IncomeStatement,),
                'auth': [
                    'oAuth'
                ],
                'endpoint_path': '/companies({company_id})/incomeStatement({incomeStatement_lineNumber})',
                'operation_id': 'get_income_statement',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'income_statement_line_number',
                    'select',
                ],
                'required': [
                    'company_id',
                    'income_statement_line_number',
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

                        "LINENUMBER": "lineNumber",
                        "DISPLAY": "display",
                        "NETCHANGE": "netChange",
                        "LINETYPE": "lineType",
                        "INDENTATION": "indentation",
                        "DATEFILTER": "dateFilter"
                    },
                },
                'openapi_types': {
                    'company_id':
                        (str,),
                    'income_statement_line_number':
                        (int,),
                    'select':
                        ([str],),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'income_statement_line_number': 'incomeStatement_lineNumber',
                    'select': '$select',
                },
                'location_map': {
                    'company_id': 'path',
                    'income_statement_line_number': 'path',
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
            callable=__get_income_statement
        )

        def __list_income_statement(
            self,
            company_id,
            **kwargs
        ):
            """Returns a list of incomeStatement  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_income_statement(company_id, async_req=True)
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
                InlineResponse20039
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

        self.list_income_statement = _Endpoint(
            settings={
                'response_type': (InlineResponse20039,),
                'auth': [
                    'oAuth'
                ],
                'endpoint_path': '/companies({company_id})/incomeStatement',
                'operation_id': 'list_income_statement',
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

                        "LINENUMBER": "lineNumber",
                        "DISPLAY": "display",
                        "NETCHANGE": "netChange",
                        "LINETYPE": "lineType",
                        "INDENTATION": "indentation",
                        "DATEFILTER": "dateFilter"
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
            callable=__list_income_statement
        )
