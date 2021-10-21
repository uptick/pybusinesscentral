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
from pybusinesscentral.model.aged_accounts_payable import AgedAccountsPayable
from pybusinesscentral.model.inline_response20036 import InlineResponse20036


class AgedAccountsPayableApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __get_aged_accounts_payable(
            self,
            company_id,
            aged_accounts_payable_vendor_id,
            **kwargs
        ):
            """Retrieve the properties and relationships of an object of type agedAccountsPayable for Dynamics 365 Business Central.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_aged_accounts_payable(company_id, aged_accounts_payable_vendor_id, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str): (v1.0) id for company
                aged_accounts_payable_vendor_id (str): (v1.0) vendorId for agedAccountsPayable

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
                AgedAccountsPayable
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
            kwargs['aged_accounts_payable_vendor_id'] = \
                aged_accounts_payable_vendor_id
            return self.call_with_http_info(**kwargs)

        self.get_aged_accounts_payable = _Endpoint(
            settings={
                'response_type': (AgedAccountsPayable,),
                'auth': [
                    'oAuth'
                ],
                'endpoint_path': '/companies({company_id})/agedAccountsPayable({agedAccountsPayable_vendorId})',
                'operation_id': 'get_aged_accounts_payable',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'aged_accounts_payable_vendor_id',
                    'select',
                ],
                'required': [
                    'company_id',
                    'aged_accounts_payable_vendor_id',
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

                        "VENDORID": "vendorId",
                        "VENDORNUMBER": "vendorNumber",
                        "NAME": "name",
                        "CURRENCYCODE": "currencyCode",
                        "BALANCEDUE": "balanceDue",
                        "CURRENTAMOUNT": "currentAmount",
                        "PERIOD1AMOUNT": "period1Amount",
                        "PERIOD2AMOUNT": "period2Amount",
                        "PERIOD3AMOUNT": "period3Amount",
                        "AGEDASOFDATE": "agedAsOfDate",
                        "PERIODLENGTHFILTER": "periodLengthFilter"
                    },
                },
                'openapi_types': {
                    'company_id':
                        (str,),
                    'aged_accounts_payable_vendor_id':
                        (str,),
                    'select':
                        ([str],),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'aged_accounts_payable_vendor_id': 'agedAccountsPayable_vendorId',
                    'select': '$select',
                },
                'location_map': {
                    'company_id': 'path',
                    'aged_accounts_payable_vendor_id': 'path',
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
            callable=__get_aged_accounts_payable
        )

        def __list_aged_accounts_payable(
            self,
            company_id,
            **kwargs
        ):
            """Returns a list of agedAccountsPayable  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_aged_accounts_payable(company_id, async_req=True)
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
                InlineResponse20036
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

        self.list_aged_accounts_payable = _Endpoint(
            settings={
                'response_type': (InlineResponse20036,),
                'auth': [
                    'oAuth'
                ],
                'endpoint_path': '/companies({company_id})/agedAccountsPayable',
                'operation_id': 'list_aged_accounts_payable',
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

                        "VENDORID": "vendorId",
                        "VENDORNUMBER": "vendorNumber",
                        "NAME": "name",
                        "CURRENCYCODE": "currencyCode",
                        "BALANCEDUE": "balanceDue",
                        "CURRENTAMOUNT": "currentAmount",
                        "PERIOD1AMOUNT": "period1Amount",
                        "PERIOD2AMOUNT": "period2Amount",
                        "PERIOD3AMOUNT": "period3Amount",
                        "AGEDASOFDATE": "agedAsOfDate",
                        "PERIODLENGTHFILTER": "periodLengthFilter"
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
            callable=__list_aged_accounts_payable
        )
