# coding: utf-8

"""
    ClickSend v3 REST API

     This is the official [ClickSend](https://clicksend.com) SDK.  *You'll need to create a free account to use the API. You can register [here](https://www.clicksend.com/signup).*  You can use our API documentation along with the SDK. Our API docs can be found [here](https://developers.clicksend.com).   # noqa: E501

    OpenAPI spec version: 3.1.0
    Contact: support@clicksend.com
    Generated by: https://github.com/clicksend-api/clicksend-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from clicksend_client.api_client import ApiClient


class ContactApi(object):
    """NOTE: This class is auto generated by the clicksend code generator program.

    Do not edit the class manually.
    Ref: https://github.com/clicksend-api/clicksend-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def lists_contacts_by_list_id_and_contact_id_delete(self, list_id, contact_id, **kwargs):  # noqa: E501
        """Delete a contact  # noqa: E501

        Delete a contact  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_contacts_by_list_id_and_contact_id_delete(list_id, contact_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: List ID (required)
        :param int contact_id: Contact ID (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lists_contacts_by_list_id_and_contact_id_delete_with_http_info(list_id, contact_id, **kwargs)  # noqa: E501
        else:
            (data) = self.lists_contacts_by_list_id_and_contact_id_delete_with_http_info(list_id, contact_id, **kwargs)  # noqa: E501
            return data

    def lists_contacts_by_list_id_and_contact_id_delete_with_http_info(self, list_id, contact_id, **kwargs):  # noqa: E501
        """Delete a contact  # noqa: E501

        Delete a contact  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_contacts_by_list_id_and_contact_id_delete_with_http_info(list_id, contact_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: List ID (required)
        :param int contact_id: Contact ID (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'contact_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lists_contacts_by_list_id_and_contact_id_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `lists_contacts_by_list_id_and_contact_id_delete`")  # noqa: E501
        # verify the required parameter 'contact_id' is set
        if ('contact_id' not in params or
                params['contact_id'] is None):
            raise ValueError("Missing the required parameter `contact_id` when calling `lists_contacts_by_list_id_and_contact_id_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']  # noqa: E501
        if 'contact_id' in params:
            path_params['contact_id'] = params['contact_id']  # noqa: E501

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
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/lists/{list_id}/contacts/{contact_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lists_contacts_by_list_id_and_contact_id_get(self, list_id, contact_id, **kwargs):  # noqa: E501
        """Get a specific contact  # noqa: E501

        Get a specific contact  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_contacts_by_list_id_and_contact_id_get(list_id, contact_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: Your contact list id you want to access. (required)
        :param int contact_id: Your contact id you want to access. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lists_contacts_by_list_id_and_contact_id_get_with_http_info(list_id, contact_id, **kwargs)  # noqa: E501
        else:
            (data) = self.lists_contacts_by_list_id_and_contact_id_get_with_http_info(list_id, contact_id, **kwargs)  # noqa: E501
            return data

    def lists_contacts_by_list_id_and_contact_id_get_with_http_info(self, list_id, contact_id, **kwargs):  # noqa: E501
        """Get a specific contact  # noqa: E501

        Get a specific contact  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_contacts_by_list_id_and_contact_id_get_with_http_info(list_id, contact_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: Your contact list id you want to access. (required)
        :param int contact_id: Your contact id you want to access. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'contact_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lists_contacts_by_list_id_and_contact_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `lists_contacts_by_list_id_and_contact_id_get`")  # noqa: E501
        # verify the required parameter 'contact_id' is set
        if ('contact_id' not in params or
                params['contact_id'] is None):
            raise ValueError("Missing the required parameter `contact_id` when calling `lists_contacts_by_list_id_and_contact_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']  # noqa: E501
        if 'contact_id' in params:
            path_params['contact_id'] = params['contact_id']  # noqa: E501

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
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/lists/{list_id}/contacts/{contact_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lists_contacts_by_list_id_and_contact_id_put(self, list_id, contact_id, contact, **kwargs):  # noqa: E501
        """Update specific contact  # noqa: E501

        Update specific contact  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_contacts_by_list_id_and_contact_id_put(list_id, contact_id, contact, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: Contact list id (required)
        :param int contact_id: Contact ID (required)
        :param Contact contact: Contact model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lists_contacts_by_list_id_and_contact_id_put_with_http_info(list_id, contact_id, contact, **kwargs)  # noqa: E501
        else:
            (data) = self.lists_contacts_by_list_id_and_contact_id_put_with_http_info(list_id, contact_id, contact, **kwargs)  # noqa: E501
            return data

    def lists_contacts_by_list_id_and_contact_id_put_with_http_info(self, list_id, contact_id, contact, **kwargs):  # noqa: E501
        """Update specific contact  # noqa: E501

        Update specific contact  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_contacts_by_list_id_and_contact_id_put_with_http_info(list_id, contact_id, contact, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: Contact list id (required)
        :param int contact_id: Contact ID (required)
        :param Contact contact: Contact model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'contact_id', 'contact']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lists_contacts_by_list_id_and_contact_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `lists_contacts_by_list_id_and_contact_id_put`")  # noqa: E501
        # verify the required parameter 'contact_id' is set
        if ('contact_id' not in params or
                params['contact_id'] is None):
            raise ValueError("Missing the required parameter `contact_id` when calling `lists_contacts_by_list_id_and_contact_id_put`")  # noqa: E501
        # verify the required parameter 'contact' is set
        if ('contact' not in params or
                params['contact'] is None):
            raise ValueError("Missing the required parameter `contact` when calling `lists_contacts_by_list_id_and_contact_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']  # noqa: E501
        if 'contact_id' in params:
            path_params['contact_id'] = params['contact_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'contact' in params:
            body_params = params['contact']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/lists/{list_id}/contacts/{contact_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lists_contacts_by_list_id_get(self, list_id, **kwargs):  # noqa: E501
        """Get all contacts in a list  # noqa: E501

        Get all contacts in a list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_contacts_by_list_id_get(list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: Contact list ID (required)
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lists_contacts_by_list_id_get_with_http_info(list_id, **kwargs)  # noqa: E501
        else:
            (data) = self.lists_contacts_by_list_id_get_with_http_info(list_id, **kwargs)  # noqa: E501
            return data

    def lists_contacts_by_list_id_get_with_http_info(self, list_id, **kwargs):  # noqa: E501
        """Get all contacts in a list  # noqa: E501

        Get all contacts in a list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_contacts_by_list_id_get_with_http_info(list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: Contact list ID (required)
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lists_contacts_by_list_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `lists_contacts_by_list_id_get`")  # noqa: E501

        if 'page' in params and params['page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `lists_contacts_by_list_id_get`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `lists_contacts_by_list_id_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/lists/{list_id}/contacts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lists_contacts_by_list_id_post(self, contact, list_id, **kwargs):  # noqa: E501
        """Create new contact  # noqa: E501

        Create new contact  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_contacts_by_list_id_post(contact, list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Contact contact: Contact model (required)
        :param int list_id: List id (required)
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lists_contacts_by_list_id_post_with_http_info(contact, list_id, **kwargs)  # noqa: E501
        else:
            (data) = self.lists_contacts_by_list_id_post_with_http_info(contact, list_id, **kwargs)  # noqa: E501
            return data

    def lists_contacts_by_list_id_post_with_http_info(self, contact, list_id, **kwargs):  # noqa: E501
        """Create new contact  # noqa: E501

        Create new contact  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_contacts_by_list_id_post_with_http_info(contact, list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Contact contact: Contact model (required)
        :param int list_id: List id (required)
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['contact', 'list_id', 'page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lists_contacts_by_list_id_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'contact' is set
        if ('contact' not in params or
                params['contact'] is None):
            raise ValueError("Missing the required parameter `contact` when calling `lists_contacts_by_list_id_post`")  # noqa: E501
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `lists_contacts_by_list_id_post`")  # noqa: E501

        if 'page' in params and params['page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `lists_contacts_by_list_id_post`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `lists_contacts_by_list_id_post`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']  # noqa: E501

        query_params = []
        if 'page' in params:
            query_params.append(('page', params['page']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'contact' in params:
            body_params = params['contact']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/lists/{list_id}/contacts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lists_remove_opted_out_contacts_by_list_id_and_opt_out_list_id_put(self, list_id, opt_out_list_id, **kwargs):  # noqa: E501
        """Remove all opted out contacts  # noqa: E501

        Remove all opted out contacts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_remove_opted_out_contacts_by_list_id_and_opt_out_list_id_put(list_id, opt_out_list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: Your list id (required)
        :param int opt_out_list_id: Your opt out list id (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lists_remove_opted_out_contacts_by_list_id_and_opt_out_list_id_put_with_http_info(list_id, opt_out_list_id, **kwargs)  # noqa: E501
        else:
            (data) = self.lists_remove_opted_out_contacts_by_list_id_and_opt_out_list_id_put_with_http_info(list_id, opt_out_list_id, **kwargs)  # noqa: E501
            return data

    def lists_remove_opted_out_contacts_by_list_id_and_opt_out_list_id_put_with_http_info(self, list_id, opt_out_list_id, **kwargs):  # noqa: E501
        """Remove all opted out contacts  # noqa: E501

        Remove all opted out contacts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_remove_opted_out_contacts_by_list_id_and_opt_out_list_id_put_with_http_info(list_id, opt_out_list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int list_id: Your list id (required)
        :param int opt_out_list_id: Your opt out list id (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['list_id', 'opt_out_list_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lists_remove_opted_out_contacts_by_list_id_and_opt_out_list_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'list_id' is set
        if ('list_id' not in params or
                params['list_id'] is None):
            raise ValueError("Missing the required parameter `list_id` when calling `lists_remove_opted_out_contacts_by_list_id_and_opt_out_list_id_put`")  # noqa: E501
        # verify the required parameter 'opt_out_list_id' is set
        if ('opt_out_list_id' not in params or
                params['opt_out_list_id'] is None):
            raise ValueError("Missing the required parameter `opt_out_list_id` when calling `lists_remove_opted_out_contacts_by_list_id_and_opt_out_list_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'list_id' in params:
            path_params['list_id'] = params['list_id']  # noqa: E501
        if 'opt_out_list_id' in params:
            path_params['opt_out_list_id'] = params['opt_out_list_id']  # noqa: E501

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
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/lists/{list_id}/remove-opted-out-contacts/{opt_out_list_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def lists_transfer_contact_put(self, from_list_id, contact_id, to_list_id, **kwargs):  # noqa: E501
        """Transfer contact to another list  # noqa: E501

        Transfer contact to another list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_transfer_contact_put(from_list_id, contact_id, to_list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int from_list_id: List ID for list that contains contact. (required)
        :param int contact_id: Contact ID (required)
        :param int to_list_id: List ID for list you want to transfer contact to. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lists_transfer_contact_put_with_http_info(from_list_id, contact_id, to_list_id, **kwargs)  # noqa: E501
        else:
            (data) = self.lists_transfer_contact_put_with_http_info(from_list_id, contact_id, to_list_id, **kwargs)  # noqa: E501
            return data

    def lists_transfer_contact_put_with_http_info(self, from_list_id, contact_id, to_list_id, **kwargs):  # noqa: E501
        """Transfer contact to another list  # noqa: E501

        Transfer contact to another list  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lists_transfer_contact_put_with_http_info(from_list_id, contact_id, to_list_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int from_list_id: List ID for list that contains contact. (required)
        :param int contact_id: Contact ID (required)
        :param int to_list_id: List ID for list you want to transfer contact to. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['from_list_id', 'contact_id', 'to_list_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lists_transfer_contact_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'from_list_id' is set
        if ('from_list_id' not in params or
                params['from_list_id'] is None):
            raise ValueError("Missing the required parameter `from_list_id` when calling `lists_transfer_contact_put`")  # noqa: E501
        # verify the required parameter 'contact_id' is set
        if ('contact_id' not in params or
                params['contact_id'] is None):
            raise ValueError("Missing the required parameter `contact_id` when calling `lists_transfer_contact_put`")  # noqa: E501
        # verify the required parameter 'to_list_id' is set
        if ('to_list_id' not in params or
                params['to_list_id'] is None):
            raise ValueError("Missing the required parameter `to_list_id` when calling `lists_transfer_contact_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'from_list_id' in params:
            path_params['from_list_id'] = params['from_list_id']  # noqa: E501
        if 'contact_id' in params:
            path_params['contact_id'] = params['contact_id']  # noqa: E501
        if 'to_list_id' in params:
            path_params['to_list_id'] = params['to_list_id']  # noqa: E501

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
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/lists/{from_list_id}/contacts/{contact_id}/transfer/{to_list_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
