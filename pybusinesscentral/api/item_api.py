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
from pybusinesscentral.model.inline_response2001 import InlineResponse2001
from pybusinesscentral.model.item import Item


class ItemApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __delete_item(
            self,
            company_id,
            item_id,
            **kwargs
        ):
            """Deletes an object of type item in Dynamics 365 Business Central  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.delete_item(company_id, item_id, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str): (v1.0) id for company
                item_id (str): (v1.0) id for item

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
            kwargs['item_id'] = \
                item_id
            return self.call_with_http_info(**kwargs)

        self.delete_item = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'oAuth'
                ],
                'endpoint_path': '/companies({company_id})/items({item_id})',
                'operation_id': 'delete_item',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'item_id',
                ],
                'required': [
                    'company_id',
                    'item_id',
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
                    'item_id':
                        (str,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'item_id': 'item_id',
                },
                'location_map': {
                    'company_id': 'path',
                    'item_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client,
            callable=__delete_item
        )

        def __get_item(
            self,
            company_id,
            item_id,
            **kwargs
        ):
            """Retrieve the properties and relationships of an object of type item for Dynamics 365 Business Central.  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.get_item(company_id, item_id, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str): (v1.0) id for company
                item_id (str): (v1.0) id for item

            Keyword Args:
                expand ([str]): (v1.0) Entities to expand. [optional]
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
                Item
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
            kwargs['item_id'] = \
                item_id
            return self.call_with_http_info(**kwargs)

        self.get_item = _Endpoint(
            settings={
                'response_type': (Item,),
                'auth': [
                    'oAuth'
                ],
                'endpoint_path': '/companies({company_id})/items({item_id})',
                'operation_id': 'get_item',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'item_id',
                    'expand',
                    'select',
                ],
                'required': [
                    'company_id',
                    'item_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'expand',
                    'select',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('expand',): {

                        "PICTURE": "picture",
                        "DEFAULTDIMENSIONS": "defaultDimensions",
                        "ITEMCATEGORY": "itemCategory"
                    },
                    ('select',): {

                        "ID": "id",
                        "NUMBER": "number",
                        "DISPLAYNAME": "displayName",
                        "TYPE": "type",
                        "ITEMCATEGORYID": "itemCategoryId",
                        "ITEMCATEGORYCODE": "itemCategoryCode",
                        "BLOCKED": "blocked",
                        "BASEUNITOFMEASUREID": "baseUnitOfMeasureId",
                        "BASEUNITOFMEASURE": "baseUnitOfMeasure",
                        "GTIN": "gtin",
                        "INVENTORY": "inventory",
                        "UNITPRICE": "unitPrice",
                        "PRICEINCLUDESTAX": "priceIncludesTax",
                        "UNITCOST": "unitCost",
                        "TAXGROUPID": "taxGroupId",
                        "TAXGROUPCODE": "taxGroupCode",
                        "LASTMODIFIEDDATETIME": "lastModifiedDateTime"
                    },
                },
                'openapi_types': {
                    'company_id':
                        (str,),
                    'item_id':
                        (str,),
                    'expand':
                        ([str],),
                    'select':
                        ([str],),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'item_id': 'item_id',
                    'expand': '$expand',
                    'select': '$select',
                },
                'location_map': {
                    'company_id': 'path',
                    'item_id': 'path',
                    'expand': 'query',
                    'select': 'query',
                },
                'collection_format_map': {
                    'expand': 'csv',
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
            callable=__get_item
        )

        def __list_items(
            self,
            company_id,
            **kwargs
        ):
            """Returns a list of items  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.list_items(company_id, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str): (v1.0) id for company

            Keyword Args:
                top (int): (v1.0) Number of items to return from the top of the list. [optional]
                skip (int): (v1.0) Number of items to skip from the list. [optional]
                limit (int): (v1.0) Number of items to return from the list. [optional]
                filter (str): (v1.0) Filtering expression. [optional]
                expand ([str]): (v1.0) Entities to expand. [optional]
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
                InlineResponse2001
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

        self.list_items = _Endpoint(
            settings={
                'response_type': (InlineResponse2001,),
                'auth': [
                    'oAuth'
                ],
                'endpoint_path': '/companies({company_id})/items',
                'operation_id': 'list_items',
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
                    'expand',
                    'select',
                ],
                'required': [
                    'company_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'expand',
                    'select',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('expand',): {

                        "PICTURE": "picture",
                        "DEFAULTDIMENSIONS": "defaultDimensions",
                        "ITEMCATEGORY": "itemCategory"
                    },
                    ('select',): {

                        "ID": "id",
                        "NUMBER": "number",
                        "DISPLAYNAME": "displayName",
                        "TYPE": "type",
                        "ITEMCATEGORYID": "itemCategoryId",
                        "ITEMCATEGORYCODE": "itemCategoryCode",
                        "BLOCKED": "blocked",
                        "BASEUNITOFMEASUREID": "baseUnitOfMeasureId",
                        "BASEUNITOFMEASURE": "baseUnitOfMeasure",
                        "GTIN": "gtin",
                        "INVENTORY": "inventory",
                        "UNITPRICE": "unitPrice",
                        "PRICEINCLUDESTAX": "priceIncludesTax",
                        "UNITCOST": "unitCost",
                        "TAXGROUPID": "taxGroupId",
                        "TAXGROUPCODE": "taxGroupCode",
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
                    'expand':
                        ([str],),
                    'select':
                        ([str],),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'top': '$top',
                    'skip': '$skip',
                    'limit': '$limit',
                    'filter': '$filter',
                    'expand': '$expand',
                    'select': '$select',
                },
                'location_map': {
                    'company_id': 'path',
                    'top': 'query',
                    'skip': 'query',
                    'limit': 'query',
                    'filter': 'query',
                    'expand': 'query',
                    'select': 'query',
                },
                'collection_format_map': {
                    'expand': 'csv',
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
            callable=__list_items
        )

        def __patch_item(
            self,
            company_id,
            item_id,
            content_type,
            if_match,
            item,
            **kwargs
        ):
            """Updates an object of type item in Dynamics 365 Business Central  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.patch_item(company_id, item_id, content_type, if_match, item, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str): (v1.0) id for company
                item_id (str): (v1.0) id for item
                content_type (str): (v1.0) application/json
                if_match (str): (v1.0) Required. When this request header is included and the eTag provided does not match the current tag on the entity, this will not be updated.
                item (Item):

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
                Item
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
            kwargs['item_id'] = \
                item_id
            kwargs['content_type'] = \
                content_type
            kwargs['if_match'] = \
                if_match
            kwargs['item'] = \
                item
            return self.call_with_http_info(**kwargs)

        self.patch_item = _Endpoint(
            settings={
                'response_type': (Item,),
                'auth': [
                    'oAuth'
                ],
                'endpoint_path': '/companies({company_id})/items({item_id})',
                'operation_id': 'patch_item',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'item_id',
                    'content_type',
                    'if_match',
                    'item',
                ],
                'required': [
                    'company_id',
                    'item_id',
                    'content_type',
                    'if_match',
                    'item',
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
                    'item_id':
                        (str,),
                    'content_type':
                        (str,),
                    'if_match':
                        (str,),
                    'item':
                        (Item,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'item_id': 'item_id',
                    'content_type': 'Content-Type',
                    'if_match': 'If-Match',
                },
                'location_map': {
                    'company_id': 'path',
                    'item_id': 'path',
                    'content_type': 'header',
                    'if_match': 'header',
                    'item': 'body',
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
            callable=__patch_item
        )

        def __post_item(
            self,
            company_id,
            content_type,
            item,
            **kwargs
        ):
            """Creates an object of type item in Dynamics 365 Business Central  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.post_item(company_id, content_type, item, async_req=True)
            >>> result = thread.get()

            Args:
                company_id (str): (v1.0) id for company
                content_type (str): (v1.0) application/json
                item (Item):

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
                Item
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
            kwargs['item'] = \
                item
            return self.call_with_http_info(**kwargs)

        self.post_item = _Endpoint(
            settings={
                'response_type': (Item,),
                'auth': [
                    'oAuth'
                ],
                'endpoint_path': '/companies({company_id})/items',
                'operation_id': 'post_item',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'company_id',
                    'content_type',
                    'item',
                ],
                'required': [
                    'company_id',
                    'content_type',
                    'item',
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
                    'item':
                        (Item,),
                },
                'attribute_map': {
                    'company_id': 'company_id',
                    'content_type': 'Content-Type',
                },
                'location_map': {
                    'company_id': 'path',
                    'content_type': 'header',
                    'item': 'body',
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
            callable=__post_item
        )
