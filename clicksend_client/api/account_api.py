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


class AccountApi(object):
    """NOTE: This class is auto generated by the clicksend code generator program.

    Do not edit the class manually.
    Ref: https://github.com/clicksend-api/clicksend-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def account_get(self, **kwargs):  # noqa: E501
        """Get account information  # noqa: E501

        Get account details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.account_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.account_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def account_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get account information  # noqa: E501

        Get account details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_get_with_http_info(async_req=True)
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
                    " to method account_get" % key
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
            '/account', 'GET',
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

    def account_post(self, account, **kwargs):  # noqa: E501
        """Create a new account  # noqa: E501

        Create An Account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_post(account, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Account account: Account model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.account_post_with_http_info(account, **kwargs)  # noqa: E501
        else:
            (data) = self.account_post_with_http_info(account, **kwargs)  # noqa: E501
            return data

    def account_post_with_http_info(self, account, **kwargs):  # noqa: E501
        """Create a new account  # noqa: E501

        Create An Account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_post_with_http_info(account, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Account account: Account model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account' is set
        if ('account' not in params or
                params['account'] is None):
            raise ValueError("Missing the required parameter `account` when calling `account_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'account' in params:
            body_params = params['account']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/account', 'POST',
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

    def account_verify_send_put(self, account_verify, **kwargs):  # noqa: E501
        """Send account activation token  # noqa: E501

        Send account activation token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_verify_send_put(account_verify, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountVerify account_verify: Account details (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.account_verify_send_put_with_http_info(account_verify, **kwargs)  # noqa: E501
        else:
            (data) = self.account_verify_send_put_with_http_info(account_verify, **kwargs)  # noqa: E501
            return data

    def account_verify_send_put_with_http_info(self, account_verify, **kwargs):  # noqa: E501
        """Send account activation token  # noqa: E501

        Send account activation token  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_verify_send_put_with_http_info(account_verify, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountVerify account_verify: Account details (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['account_verify']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_verify_send_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'account_verify' is set
        if ('account_verify' not in params or
                params['account_verify'] is None):
            raise ValueError("Missing the required parameter `account_verify` when calling `account_verify_send_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'account_verify' in params:
            body_params = params['account_verify']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/account-verify/send', 'PUT',
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

    def account_verify_verify_by_activation_token_put(self, activation_token, **kwargs):  # noqa: E501
        """Verify new account  # noqa: E501

        Verify new account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_verify_verify_by_activation_token_put(activation_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int activation_token:  (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.account_verify_verify_by_activation_token_put_with_http_info(activation_token, **kwargs)  # noqa: E501
        else:
            (data) = self.account_verify_verify_by_activation_token_put_with_http_info(activation_token, **kwargs)  # noqa: E501
            return data

    def account_verify_verify_by_activation_token_put_with_http_info(self, activation_token, **kwargs):  # noqa: E501
        """Verify new account  # noqa: E501

        Verify new account  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_verify_verify_by_activation_token_put_with_http_info(activation_token, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int activation_token:  (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['activation_token']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_verify_verify_by_activation_token_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'activation_token' is set
        if ('activation_token' not in params or
                params['activation_token'] is None):
            raise ValueError("Missing the required parameter `activation_token` when calling `account_verify_verify_by_activation_token_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'activation_token' in params:
            path_params['activation_token'] = params['activation_token']  # noqa: E501

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
            '/account-verify/verify/{activation_token}', 'PUT',
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

    def forgot_password_put(self, username, **kwargs):  # noqa: E501
        """Forgot password  # noqa: E501

        Forgot password  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.forgot_password_put(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: Username belonging to account (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.forgot_password_put_with_http_info(username, **kwargs)  # noqa: E501
        else:
            (data) = self.forgot_password_put_with_http_info(username, **kwargs)  # noqa: E501
            return data

    def forgot_password_put_with_http_info(self, username, **kwargs):  # noqa: E501
        """Forgot password  # noqa: E501

        Forgot password  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.forgot_password_put_with_http_info(username, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str username: Username belonging to account (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['username']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method forgot_password_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'username' is set
        if ('username' not in params or
                params['username'] is None):
            raise ValueError("Missing the required parameter `username` when calling `forgot_password_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'username' in params:
            body_params = params['username']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/forgot-password', 'PUT',
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

    def forgot_password_verify_put(self, verify_password, **kwargs):  # noqa: E501
        """Verify forgot password  # noqa: E501

        Verify forgot password  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.forgot_password_verify_put(verify_password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountForgotPasswordVerify verify_password: verifyPassword data (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.forgot_password_verify_put_with_http_info(verify_password, **kwargs)  # noqa: E501
        else:
            (data) = self.forgot_password_verify_put_with_http_info(verify_password, **kwargs)  # noqa: E501
            return data

    def forgot_password_verify_put_with_http_info(self, verify_password, **kwargs):  # noqa: E501
        """Verify forgot password  # noqa: E501

        Verify forgot password  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.forgot_password_verify_put_with_http_info(verify_password, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AccountForgotPasswordVerify verify_password: verifyPassword data (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['verify_password']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method forgot_password_verify_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'verify_password' is set
        if ('verify_password' not in params or
                params['verify_password'] is None):
            raise ValueError("Missing the required parameter `verify_password` when calling `forgot_password_verify_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'verify_password' in params:
            body_params = params['verify_password']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/forgot-password/verify', 'PUT',
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

    def forgot_username_put(self, email, **kwargs):  # noqa: E501
        """Forgot username  # noqa: E501

        Forgot username  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.forgot_username_put(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str email: Email belonging to account (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.forgot_username_put_with_http_info(email, **kwargs)  # noqa: E501
        else:
            (data) = self.forgot_username_put_with_http_info(email, **kwargs)  # noqa: E501
            return data

    def forgot_username_put_with_http_info(self, email, **kwargs):  # noqa: E501
        """Forgot username  # noqa: E501

        Forgot username  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.forgot_username_put_with_http_info(email, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str email: Email belonging to account (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['email']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method forgot_username_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'email' is set
        if ('email' not in params or
                params['email'] is None):
            raise ValueError("Missing the required parameter `email` when calling `forgot_username_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'email' in params:
            body_params = params['email']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/forgot-username', 'PUT',
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
