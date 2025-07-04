# coding: utf-8

"""
    (v2.0) Dynamics 365 Business Central

    (v2.0) Business Central Standard APIs

    The version of the OpenAPI document: 2.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from pybusinesscentral.model.account import Account
from pybusinesscentral.model.list_accounts200_response import ListAccounts200Response

from pybusinesscentral.api_client import ApiClient, RequestSerialized
from pybusinesscentral.api_response import ApiResponse
from pybusinesscentral.rest import RESTResponseType


class AccountApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_account(
        self,
        company_id: Annotated[StrictStr, Field(description="(v1.0) id for company")],
        account_id: Annotated[StrictStr, Field(description="(v1.0) id for account")],
        select: Annotated[Optional[List[StrictStr]], Field(description="(v1.0) Selected properties to be retrieved")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Account:
        """Retrieve the properties and relationships of an object of type account for Dynamics 365 Business Central.


        :param company_id: (v1.0) id for company (required)
        :type company_id: str
        :param account_id: (v1.0) id for account (required)
        :type account_id: str
        :param select: (v1.0) Selected properties to be retrieved
        :type select: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_account_serialize(
            company_id=company_id,
            account_id=account_id,
            select=select,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Account",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_account_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="(v1.0) id for company")],
        account_id: Annotated[StrictStr, Field(description="(v1.0) id for account")],
        select: Annotated[Optional[List[StrictStr]], Field(description="(v1.0) Selected properties to be retrieved")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Account]:
        """Retrieve the properties and relationships of an object of type account for Dynamics 365 Business Central.


        :param company_id: (v1.0) id for company (required)
        :type company_id: str
        :param account_id: (v1.0) id for account (required)
        :type account_id: str
        :param select: (v1.0) Selected properties to be retrieved
        :type select: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_account_serialize(
            company_id=company_id,
            account_id=account_id,
            select=select,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Account",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_account_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="(v1.0) id for company")],
        account_id: Annotated[StrictStr, Field(description="(v1.0) id for account")],
        select: Annotated[Optional[List[StrictStr]], Field(description="(v1.0) Selected properties to be retrieved")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve the properties and relationships of an object of type account for Dynamics 365 Business Central.


        :param company_id: (v1.0) id for company (required)
        :type company_id: str
        :param account_id: (v1.0) id for account (required)
        :type account_id: str
        :param select: (v1.0) Selected properties to be retrieved
        :type select: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_account_serialize(
            company_id=company_id,
            account_id=account_id,
            select=select,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Account",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_account_serialize(
        self,
        company_id,
        account_id,
        select,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            '$select': 'csv',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['company_id'] = company_id
        if account_id is not None:
            _path_params['account_id'] = account_id
        # process the query parameters
        if select is not None:
            
            _query_params.append(('$select', select))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/companies({company_id})/accounts({account_id})',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )




    @validate_call
    def list_accounts(
        self,
        company_id: Annotated[StrictStr, Field(description="(v1.0) id for company")],
        top: Annotated[Optional[StrictInt], Field(description="(v1.0) Number of items to return from the top of the list")] = None,
        skip: Annotated[Optional[StrictInt], Field(description="(v1.0) Number of items to skip from the list")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="(v1.0) Number of items to return from the list")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="(v1.0) Filtering expression")] = None,
        select: Annotated[Optional[List[StrictStr]], Field(description="(v1.0) Selected properties to be retrieved")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ListAccounts200Response:
        """Returns a list of accounts


        :param company_id: (v1.0) id for company (required)
        :type company_id: str
        :param top: (v1.0) Number of items to return from the top of the list
        :type top: int
        :param skip: (v1.0) Number of items to skip from the list
        :type skip: int
        :param limit: (v1.0) Number of items to return from the list
        :type limit: int
        :param filter: (v1.0) Filtering expression
        :type filter: str
        :param select: (v1.0) Selected properties to be retrieved
        :type select: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_accounts_serialize(
            company_id=company_id,
            top=top,
            skip=skip,
            limit=limit,
            filter=filter,
            select=select,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListAccounts200Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def list_accounts_with_http_info(
        self,
        company_id: Annotated[StrictStr, Field(description="(v1.0) id for company")],
        top: Annotated[Optional[StrictInt], Field(description="(v1.0) Number of items to return from the top of the list")] = None,
        skip: Annotated[Optional[StrictInt], Field(description="(v1.0) Number of items to skip from the list")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="(v1.0) Number of items to return from the list")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="(v1.0) Filtering expression")] = None,
        select: Annotated[Optional[List[StrictStr]], Field(description="(v1.0) Selected properties to be retrieved")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[ListAccounts200Response]:
        """Returns a list of accounts


        :param company_id: (v1.0) id for company (required)
        :type company_id: str
        :param top: (v1.0) Number of items to return from the top of the list
        :type top: int
        :param skip: (v1.0) Number of items to skip from the list
        :type skip: int
        :param limit: (v1.0) Number of items to return from the list
        :type limit: int
        :param filter: (v1.0) Filtering expression
        :type filter: str
        :param select: (v1.0) Selected properties to be retrieved
        :type select: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_accounts_serialize(
            company_id=company_id,
            top=top,
            skip=skip,
            limit=limit,
            filter=filter,
            select=select,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListAccounts200Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def list_accounts_without_preload_content(
        self,
        company_id: Annotated[StrictStr, Field(description="(v1.0) id for company")],
        top: Annotated[Optional[StrictInt], Field(description="(v1.0) Number of items to return from the top of the list")] = None,
        skip: Annotated[Optional[StrictInt], Field(description="(v1.0) Number of items to skip from the list")] = None,
        limit: Annotated[Optional[StrictInt], Field(description="(v1.0) Number of items to return from the list")] = None,
        filter: Annotated[Optional[StrictStr], Field(description="(v1.0) Filtering expression")] = None,
        select: Annotated[Optional[List[StrictStr]], Field(description="(v1.0) Selected properties to be retrieved")] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Returns a list of accounts


        :param company_id: (v1.0) id for company (required)
        :type company_id: str
        :param top: (v1.0) Number of items to return from the top of the list
        :type top: int
        :param skip: (v1.0) Number of items to skip from the list
        :type skip: int
        :param limit: (v1.0) Number of items to return from the list
        :type limit: int
        :param filter: (v1.0) Filtering expression
        :type filter: str
        :param select: (v1.0) Selected properties to be retrieved
        :type select: List[str]
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._list_accounts_serialize(
            company_id=company_id,
            top=top,
            skip=skip,
            limit=limit,
            filter=filter,
            select=select,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "ListAccounts200Response",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _list_accounts_serialize(
        self,
        company_id,
        top,
        skip,
        limit,
        filter,
        select,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            '$select': 'csv',
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if company_id is not None:
            _path_params['company_id'] = company_id
        # process the query parameters
        if top is not None:
            
            _query_params.append(('$top', top))
            
        if skip is not None:
            
            _query_params.append(('$skip', skip))
            
        if limit is not None:
            
            _query_params.append(('$limit', limit))
            
        if filter is not None:
            
            _query_params.append(('$filter', filter))
            
        if select is not None:
            
            _query_params.append(('$select', select))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        # authentication setting
        _auth_settings: List[str] = [
            'oAuth'
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/companies({company_id})/accounts',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


