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


class SmsCampaignApi(object):
    """NOTE: This class is auto generated by the clicksend code generator program.

    Do not edit the class manually.
    Ref: https://github.com/clicksend-api/clicksend-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def sms_campaign_by_sms_campaign_id_get(self, sms_campaign_id, **kwargs):  # noqa: E501
        """Get specific sms campaign  # noqa: E501

        Get specific sms campaign  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.sms_campaign_by_sms_campaign_id_get(sms_campaign_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int sms_campaign_id: ID of SMS campaign to retrieve (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.sms_campaign_by_sms_campaign_id_get_with_http_info(sms_campaign_id, **kwargs)  # noqa: E501
        else:
            (data) = self.sms_campaign_by_sms_campaign_id_get_with_http_info(sms_campaign_id, **kwargs)  # noqa: E501
            return data

    def sms_campaign_by_sms_campaign_id_get_with_http_info(self, sms_campaign_id, **kwargs):  # noqa: E501
        """Get specific sms campaign  # noqa: E501

        Get specific sms campaign  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.sms_campaign_by_sms_campaign_id_get_with_http_info(sms_campaign_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int sms_campaign_id: ID of SMS campaign to retrieve (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sms_campaign_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sms_campaign_by_sms_campaign_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sms_campaign_id' is set
        if ('sms_campaign_id' not in params or
                params['sms_campaign_id'] is None):
            raise ValueError("Missing the required parameter `sms_campaign_id` when calling `sms_campaign_by_sms_campaign_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sms_campaign_id' in params:
            path_params['sms_campaign_id'] = params['sms_campaign_id']  # noqa: E501

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
            '/sms-campaign/{sms_campaign_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sms_campaigns_by_sms_campaign_id_put(self, sms_campaign_id, campaign, **kwargs):  # noqa: E501
        """Update sms campaign  # noqa: E501

        Update sms campaign  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.sms_campaigns_by_sms_campaign_id_put(sms_campaign_id, campaign, async=True)
        >>> result = thread.get()

        :param async bool
        :param int sms_campaign_id: ID of SMS campaign to update (required)
        :param SmsCampaign campaign: SmsCampaign model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.sms_campaigns_by_sms_campaign_id_put_with_http_info(sms_campaign_id, campaign, **kwargs)  # noqa: E501
        else:
            (data) = self.sms_campaigns_by_sms_campaign_id_put_with_http_info(sms_campaign_id, campaign, **kwargs)  # noqa: E501
            return data

    def sms_campaigns_by_sms_campaign_id_put_with_http_info(self, sms_campaign_id, campaign, **kwargs):  # noqa: E501
        """Update sms campaign  # noqa: E501

        Update sms campaign  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.sms_campaigns_by_sms_campaign_id_put_with_http_info(sms_campaign_id, campaign, async=True)
        >>> result = thread.get()

        :param async bool
        :param int sms_campaign_id: ID of SMS campaign to update (required)
        :param SmsCampaign campaign: SmsCampaign model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sms_campaign_id', 'campaign']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sms_campaigns_by_sms_campaign_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sms_campaign_id' is set
        if ('sms_campaign_id' not in params or
                params['sms_campaign_id'] is None):
            raise ValueError("Missing the required parameter `sms_campaign_id` when calling `sms_campaigns_by_sms_campaign_id_put`")  # noqa: E501
        # verify the required parameter 'campaign' is set
        if ('campaign' not in params or
                params['campaign'] is None):
            raise ValueError("Missing the required parameter `campaign` when calling `sms_campaigns_by_sms_campaign_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sms_campaign_id' in params:
            path_params['sms_campaign_id'] = params['sms_campaign_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'campaign' in params:
            body_params = params['campaign']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/sms-campaigns/{sms_campaign_id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sms_campaigns_cancel_by_sms_campaign_id_put(self, sms_campaign_id, **kwargs):  # noqa: E501
        """Cancel sms campaign  # noqa: E501

        Cancel sms campaign  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.sms_campaigns_cancel_by_sms_campaign_id_put(sms_campaign_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int sms_campaign_id: ID of SMS Campaign to cancel (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.sms_campaigns_cancel_by_sms_campaign_id_put_with_http_info(sms_campaign_id, **kwargs)  # noqa: E501
        else:
            (data) = self.sms_campaigns_cancel_by_sms_campaign_id_put_with_http_info(sms_campaign_id, **kwargs)  # noqa: E501
            return data

    def sms_campaigns_cancel_by_sms_campaign_id_put_with_http_info(self, sms_campaign_id, **kwargs):  # noqa: E501
        """Cancel sms campaign  # noqa: E501

        Cancel sms campaign  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.sms_campaigns_cancel_by_sms_campaign_id_put_with_http_info(sms_campaign_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param int sms_campaign_id: ID of SMS Campaign to cancel (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['sms_campaign_id']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sms_campaigns_cancel_by_sms_campaign_id_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'sms_campaign_id' is set
        if ('sms_campaign_id' not in params or
                params['sms_campaign_id'] is None):
            raise ValueError("Missing the required parameter `sms_campaign_id` when calling `sms_campaigns_cancel_by_sms_campaign_id_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'sms_campaign_id' in params:
            path_params['sms_campaign_id'] = params['sms_campaign_id']  # noqa: E501

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
            '/sms-campaigns/{sms_campaign_id}/cancel', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sms_campaigns_get(self, **kwargs):  # noqa: E501
        """Get list of sms campaigns  # noqa: E501

        Get list of sms campaigns  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.sms_campaigns_get(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.sms_campaigns_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.sms_campaigns_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def sms_campaigns_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get list of sms campaigns  # noqa: E501

        Get list of sms campaigns  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.sms_campaigns_get_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: Page number
        :param int limit: Number of records per page
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'limit']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sms_campaigns_get" % key
                )
            params[key] = val
        del params['kwargs']

        if 'page' in params and params['page'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `page` when calling `sms_campaigns_get`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'limit' in params and params['limit'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `sms_campaigns_get`, must be a value greater than or equal to `1`")  # noqa: E501
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
            '/sms-campaigns', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sms_campaigns_price_post(self, campaign, **kwargs):  # noqa: E501
        """Calculate price for sms campaign  # noqa: E501

        Calculate price for sms campaign  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.sms_campaigns_price_post(campaign, async=True)
        >>> result = thread.get()

        :param async bool
        :param SmsCampaign campaign: SmsCampaign model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.sms_campaigns_price_post_with_http_info(campaign, **kwargs)  # noqa: E501
        else:
            (data) = self.sms_campaigns_price_post_with_http_info(campaign, **kwargs)  # noqa: E501
            return data

    def sms_campaigns_price_post_with_http_info(self, campaign, **kwargs):  # noqa: E501
        """Calculate price for sms campaign  # noqa: E501

        Calculate price for sms campaign  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.sms_campaigns_price_post_with_http_info(campaign, async=True)
        >>> result = thread.get()

        :param async bool
        :param SmsCampaign campaign: SmsCampaign model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sms_campaigns_price_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign' is set
        if ('campaign' not in params or
                params['campaign'] is None):
            raise ValueError("Missing the required parameter `campaign` when calling `sms_campaigns_price_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'campaign' in params:
            body_params = params['campaign']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/sms-campaigns/price', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def sms_campaigns_send_post(self, campaign, **kwargs):  # noqa: E501
        """Create sms campaign  # noqa: E501

        Create sms campaign  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.sms_campaigns_send_post(campaign, async=True)
        >>> result = thread.get()

        :param async bool
        :param SmsCampaign campaign: SmsCampaign model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.sms_campaigns_send_post_with_http_info(campaign, **kwargs)  # noqa: E501
        else:
            (data) = self.sms_campaigns_send_post_with_http_info(campaign, **kwargs)  # noqa: E501
            return data

    def sms_campaigns_send_post_with_http_info(self, campaign, **kwargs):  # noqa: E501
        """Create sms campaign  # noqa: E501

        Create sms campaign  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.sms_campaigns_send_post_with_http_info(campaign, async=True)
        >>> result = thread.get()

        :param async bool
        :param SmsCampaign campaign: SmsCampaign model (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['campaign']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method sms_campaigns_send_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'campaign' is set
        if ('campaign' not in params or
                params['campaign'] is None):
            raise ValueError("Missing the required parameter `campaign` when calling `sms_campaigns_send_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'campaign' in params:
            body_params = params['campaign']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['BasicAuth']  # noqa: E501

        return self.api_client.call_api(
            '/sms-campaigns/send', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)