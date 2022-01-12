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
from pybusinesscentral.model.account import Account
from pybusinesscentral.model.inline_response2005 import InlineResponse2005


class AccountApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_account(
            self,
            company_id,
            account_id,
            **kwargs
        ):
            """Retrieve the properties and relationships of an object of type account for Dynamics 365 Business Central.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_account(company_id, account_id, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str): (v1.0) id for company
                account_id (str): (v1.0) id for account

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
                Account
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
            kwargs['account_id'] = \
                account_id
            return self.call_with_http_info(**kwargs)

        self.get_account = _Endpoint(
            settings={
                'response_type': (Account,),
                'auth': [
                    'oAuth'
                ],
                'endpoint_path': '/companies({company_id})/accounts({account_id})',
                'operation_id': 'get_account',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'account_id',
                    'select',
                ],
                'required': [
                    'company_id',
                    'account_id',
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
                        "NUMBER": "number",
                        "DISPLAYNAME": "displayName",
                        "CATEGORY": "category",
                        "SUBCATEGORY": "subCategory",
                        "BLOCKED": "blocked",
                        "LASTMODIFIEDDATETIME": "lastModifiedDateTime"
                    },
                },
                'openapi_types': {
                    'company_id':
                        (str,),
                    'account_id':
                        (str,),
                    'select':
                        ([str],),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'account_id': 'account_id',
                    'select': '$select',
                },
                'location_map': {
                    'company_id': 'path',
                    'account_id': 'path',
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
            callable=__get_account
        )

        def __list_accounts(
            self,
            company_id,
            **kwargs
        ):
            """Returns a list of accounts  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_accounts(company_id, async_req=True)
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
                InlineResponse2005
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

        self.list_accounts = _Endpoint(
            settings={
                'response_type': (InlineResponse2005,),
                'auth': [
                    'oAuth'
                ],
                'endpoint_path': '/companies({company_id})/accounts',
                'operation_id': 'list_accounts',
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
                        "NUMBER": "number",
                        "DISPLAYNAME": "displayName",
                        "CATEGORY": "category",
                        "SUBCATEGORY": "subCategory",
                        "BLOCKED": "blocked",
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
            callable=__list_accounts
        )
