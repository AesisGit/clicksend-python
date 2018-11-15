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


class VoiceApi(object):
    """NOTE: This class is auto generated by the clicksend code generator program.

    Do not edit the class manually.
    Ref: https://github.com/clicksend-api/clicksend-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def voice_cancel_all_put(self, **kwargs):  # noqa: E501
        """Update all voice messages as cancelled  # noqa: E501

        Update all voice messages as cancelled  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_cancel_all_put(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.voice_cancel_all_put_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.voice_cancel_all_put_with_http_info(**kwargs)  # noqa: E501
            return data

    def voice_cancel_all_put_with_http_info(self, **kwargs):  # noqa: E501
        """Update all voice messages as cancelled  # noqa: E501

        Update all voice messages as cancelled  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_cancel_all_put_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method voice_cancel_all_put" % key
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
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/voice/cancel-all', 'PUT',
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

    def voice_cancel_by_message_id_put(self, message_id, **kwargs):  # noqa: E501
        """Update voice message status as cancelled  # noqa: E501

        Update voice message status as cancelled  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_cancel_by_message_id_put(message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str message_id: Your voice message id (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.voice_cancel_by_message_id_put_with_http_info(message_id, **kwargs)  # noqa: E501
        else:
            (data) = self.voice_cancel_by_message_id_put_with_http_info(message_id, **kwargs)  # noqa: E501
            return data

    def voice_cancel_by_message_id_put_with_http_info(self, message_id, **kwargs):  # noqa: E501
        """Update voice message status as cancelled  # noqa: E501

        Update voice message status as cancelled  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_cancel_by_message_id_put_with_http_info(message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str message_id: Your voice message id (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['message_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method voice_cancel_by_message_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'message_id' is set
        if ('message_id' not in params or
                params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `voice_cancel_by_message_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'message_id' in params:
            path_params['message_id'] = params['message_id']  # noqa: E501

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
            '/voice/{message_id}/cancel', 'PUT',
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

    def voice_history_export_get(self, filename, **kwargs):  # noqa: E501
        """Export voice history  # noqa: E501

        Export voice history  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_history_export_get(filename, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filename: Filename to export to (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.voice_history_export_get_with_http_info(filename, **kwargs)  # noqa: E501
        else:
            (data) = self.voice_history_export_get_with_http_info(filename, **kwargs)  # noqa: E501
            return data

    def voice_history_export_get_with_http_info(self, filename, **kwargs):  # noqa: E501
        """Export voice history  # noqa: E501

        Export voice history  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_history_export_get_with_http_info(filename, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str filename: Filename to export to (required)
        :return: file
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['filename']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method voice_history_export_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'filename' is set
        if ('filename' not in params or
                params['filename'] is None):
            raise ValueError("Missing the required parameter `filename` when calling `voice_history_export_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'filename' in params:
            query_params.append(('filename', params['filename']))  # noqa: E501

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
            '/voice/history/export', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='file',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def voice_history_get(self, **kwargs):  # noqa: E501
        """Get all voice history  # noqa: E501

        Get all voice history  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_history_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int date_from: Timestamp (from) used to show records by date.
        :param int date_to: Timestamp (to) used to show records by date
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.voice_history_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.voice_history_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def voice_history_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all voice history  # noqa: E501

        Get all voice history  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_history_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int date_from: Timestamp (from) used to show records by date.
        :param int date_to: Timestamp (to) used to show records by date
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['date_from', 'date_to', 'page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method voice_history_get" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page' in params and params['page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `voice_history_get`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `voice_history_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'date_from' in params:
            query_params.append(('date_from', params['date_from']))  # noqa: E501
        if 'date_to' in params:
            query_params.append(('date_to', params['date_to']))  # noqa: E501
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
            '/voice/history', 'GET',
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

    def voice_lang_get(self, **kwargs):  # noqa: E501
        """Get all voice languages  # noqa: E501

        Get all voice languages  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_lang_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.voice_lang_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.voice_lang_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def voice_lang_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all voice languages  # noqa: E501

        Get all voice languages  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_lang_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method voice_lang_get" % key
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
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/voice/lang', 'GET',
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

    def voice_price_post(self, voice_messages, **kwargs):  # noqa: E501
        """Calculate voice price  # noqa: E501

        Calculate voice price  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_price_post(voice_messages, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VoiceMessageCollection voice_messages: VoiceMessageCollection model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.voice_price_post_with_http_info(voice_messages, **kwargs)  # noqa: E501
        else:
            (data) = self.voice_price_post_with_http_info(voice_messages, **kwargs)  # noqa: E501
            return data

    def voice_price_post_with_http_info(self, voice_messages, **kwargs):  # noqa: E501
        """Calculate voice price  # noqa: E501

        Calculate voice price  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_price_post_with_http_info(voice_messages, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VoiceMessageCollection voice_messages: VoiceMessageCollection model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['voice_messages']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method voice_price_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'voice_messages' is set
        if ('voice_messages' not in params or
                params['voice_messages'] is None):
            raise ValueError("Missing the required parameter `voice_messages` when calling `voice_price_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'voice_messages' in params:
            body_params = params['voice_messages']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/voice/price', 'POST',
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

    def voice_receipts_get(self, **kwargs):  # noqa: E501
        """Get all voice receipts  # noqa: E501

        Get all voice receipts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_receipts_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.voice_receipts_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.voice_receipts_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def voice_receipts_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all voice receipts  # noqa: E501

        Get all voice receipts  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_receipts_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method voice_receipts_get" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page' in params and params['page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `voice_receipts_get`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `voice_receipts_get`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

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
            '/voice/receipts', 'GET',
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

    def voice_send_post(self, voice_messages, **kwargs):  # noqa: E501
        """Send voice message(s)  # noqa: E501

        Send a voice call  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_send_post(voice_messages, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VoiceMessageCollection voice_messages: VoiceMessageCollection model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.voice_send_post_with_http_info(voice_messages, **kwargs)  # noqa: E501
        else:
            (data) = self.voice_send_post_with_http_info(voice_messages, **kwargs)  # noqa: E501
            return data

    def voice_send_post_with_http_info(self, voice_messages, **kwargs):  # noqa: E501
        """Send voice message(s)  # noqa: E501

        Send a voice call  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.voice_send_post_with_http_info(voice_messages, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param VoiceMessageCollection voice_messages: VoiceMessageCollection model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['voice_messages']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method voice_send_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'voice_messages' is set
        if ('voice_messages' not in params or
                params['voice_messages'] is None):
            raise ValueError("Missing the required parameter `voice_messages` when calling `voice_send_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'voice_messages' in params:
            body_params = params['voice_messages']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/voice/send', 'POST',
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
