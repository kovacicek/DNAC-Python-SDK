# coding: utf-8

"""
    Swagger

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from python_client.api_client import ApiClient


class TopologyApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_topology_l2_by_vlan_id(self, vlan_id, **kwargs):  # noqa: E501
        """getL2Topology  # noqa: E501

        This method is used to obtain the Layer 2 topology by Vlan ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_topology_l2_by_vlan_id(vlan_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str vlan_id: Vlan Name for e.g Vlan1, Vlan23 etc (required)
        :return: TopologyResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_topology_l2_by_vlan_id_with_http_info(vlan_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_topology_l2_by_vlan_id_with_http_info(vlan_id, **kwargs)  # noqa: E501
            return data

    def get_topology_l2_by_vlan_id_with_http_info(self, vlan_id, **kwargs):  # noqa: E501
        """getL2Topology  # noqa: E501

        This method is used to obtain the Layer 2 topology by Vlan ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_topology_l2_by_vlan_id_with_http_info(vlan_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str vlan_id: Vlan Name for e.g Vlan1, Vlan23 etc (required)
        :return: TopologyResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['vlan_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_topology_l2_by_vlan_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'vlan_id' is set
        if ('vlan_id' not in params or
                params['vlan_id'] is None):
            raise ValueError("Missing the required parameter `vlan_id` when calling `get_topology_l2_by_vlan_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'vlan_id' in params:
            path_params['vlanID'] = params['vlan_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/topology/l2/${vlanID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TopologyResult',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_topology_l3_by_topology_type(self, topology_type, **kwargs):  # noqa: E501
        """getL3Topology  # noqa: E501

        This method is used to obtain Layer 3 device topology by routing protocol type  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_topology_l3_by_topology_type(topology_type, async=True)
        >>> result = thread.get()

        :param async bool
        :param str topology_type: Type of topology(OSPF,ISIS,etc) (required)
        :return: TopologyResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_topology_l3_by_topology_type_with_http_info(topology_type, **kwargs)  # noqa: E501
        else:
            (data) = self.get_topology_l3_by_topology_type_with_http_info(topology_type, **kwargs)  # noqa: E501
            return data

    def get_topology_l3_by_topology_type_with_http_info(self, topology_type, **kwargs):  # noqa: E501
        """getL3Topology  # noqa: E501

        This method is used to obtain Layer 3 device topology by routing protocol type  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_topology_l3_by_topology_type_with_http_info(topology_type, async=True)
        >>> result = thread.get()

        :param async bool
        :param str topology_type: Type of topology(OSPF,ISIS,etc) (required)
        :return: TopologyResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['topology_type']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_topology_l3_by_topology_type" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'topology_type' is set
        if ('topology_type' not in params or
                params['topology_type'] is None):
            raise ValueError("Missing the required parameter `topology_type` when calling `get_topology_l3_by_topology_type`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'topology_type' in params:
            path_params['topologyType'] = params['topology_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/topology/l3/${topologyType}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TopologyResult',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_topology_physical_topology(self, **kwargs):  # noqa: E501
        """getPhysicalTopology  # noqa: E501

        This method is used to obtain the raw physical topology and filter based on nodeType  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_topology_physical_topology(async=True)
        >>> result = thread.get()

        :param async bool
        :param str node_type: nodeType
        :return: TopologyResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_topology_physical_topology_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_topology_physical_topology_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_topology_physical_topology_with_http_info(self, **kwargs):  # noqa: E501
        """getPhysicalTopology  # noqa: E501

        This method is used to obtain the raw physical topology and filter based on nodeType  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_topology_physical_topology_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param str node_type: nodeType
        :return: TopologyResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['node_type']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_topology_physical_topology" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'node_type' in params:
            query_params.append(('nodeType', params['node_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/topology/physical-topology', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TopologyResult',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_topology_site_topology(self, **kwargs):  # noqa: E501
        """getSiteTopology  # noqa: E501

        This method is used to obtain the site topology  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_topology_site_topology(async=True)
        >>> result = thread.get()

        :param async bool
        :return: SiteResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_topology_site_topology_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_topology_site_topology_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_topology_site_topology_with_http_info(self, **kwargs):  # noqa: E501
        """getSiteTopology  # noqa: E501

        This method is used to obtain the site topology  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_topology_site_topology_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: SiteResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_topology_site_topology" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/topology/site-topology', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SiteResult',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_topology_vlan_vlan_names(self, **kwargs):  # noqa: E501
        """getVlanNames  # noqa: E501

        This method is used to obtain the list of vlan names  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_topology_vlan_vlan_names(async=True)
        >>> result = thread.get()

        :param async bool
        :return: VlanNamesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.get_topology_vlan_vlan_names_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_topology_vlan_vlan_names_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_topology_vlan_vlan_names_with_http_info(self, **kwargs):  # noqa: E501
        """getVlanNames  # noqa: E501

        This method is used to obtain the list of vlan names  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_topology_vlan_vlan_names_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :return: VlanNamesResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_topology_vlan_vlan_names" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/topology/vlan/vlan-names', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='VlanNamesResult',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
