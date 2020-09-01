# coding: utf-8

"""
    ClickSend v3 API

     This is an official SDK for [ClickSend](https://clicksend.com)  Below you will find a current list of the available methods for clicksend.  *NOTE: You will need to create a free account to use the API. You can register [here](https://dashboard.clicksend.com/#/signup/step1/)..*   # noqa: E501

    OpenAPI spec version: 3.1
    Contact: support@clicksend.com
    Generated by: https://github.com/clicksend-api/clicksend-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class InboundSMSRule(object):
    """NOTE: This class is auto generated by the clicksend code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      clicksend_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    clicksend_types = {
        'dedicated_number': 'str',
        'rule_name': 'str',
        'message_search_type': 'float',
        'message_search_term': 'str',
        'action': 'str',
        'action_address': 'str',
        'enabled': 'float',
        'webhook_type': 'str'
    }

    attribute_map = {
        'dedicated_number': 'dedicated_number',
        'rule_name': 'rule_name',
        'message_search_type': 'message_search_type',
        'message_search_term': 'message_search_term',
        'action': 'action',
        'action_address': 'action_address',
        'enabled': 'enabled',
        'webhook_type': 'webhook_type'
    }

    discriminator_value_class_map = {
        
    }

    def __init__(self, dedicated_number=None, rule_name=None, message_search_type=None, message_search_term=None, action=None, action_address=None, enabled=None, webhook_type=None):  # noqa: E501
        """InboundSMSRule - a model defined in Swagger"""  # noqa: E501

        self._dedicated_number = None
        self._rule_name = None
        self._message_search_type = None
        self._message_search_term = None
        self._action = None
        self._action_address = None
        self._enabled = None
        self._webhook_type = None
        self.discriminator = 'classType'

        self.dedicated_number = dedicated_number
        self.rule_name = rule_name
        self.message_search_type = message_search_type
        self.message_search_term = message_search_term
        self.action = action
        self.action_address = action_address
        self.enabled = enabled
        if webhook_type is not None:
            self.webhook_type = webhook_type

    @property
    def dedicated_number(self):
        """Gets the dedicated_number of this InboundSMSRule.  # noqa: E501

        Dedicated Number. Can be '*' to apply to all numbers.  # noqa: E501

        :return: The dedicated_number of this InboundSMSRule.  # noqa: E501
        :rtype: str
        """
        return self._dedicated_number

    @dedicated_number.setter
    def dedicated_number(self, dedicated_number):
        """Sets the dedicated_number of this InboundSMSRule.

        Dedicated Number. Can be '*' to apply to all numbers.  # noqa: E501

        :param dedicated_number: The dedicated_number of this InboundSMSRule.  # noqa: E501
        :type: str
        """
        if dedicated_number is None:
            raise ValueError("Invalid value for `dedicated_number`, must not be `None`")  # noqa: E501

        self._dedicated_number = dedicated_number

    @property
    def rule_name(self):
        """Gets the rule_name of this InboundSMSRule.  # noqa: E501

        Rule Name.  # noqa: E501

        :return: The rule_name of this InboundSMSRule.  # noqa: E501
        :rtype: str
        """
        return self._rule_name

    @rule_name.setter
    def rule_name(self, rule_name):
        """Sets the rule_name of this InboundSMSRule.

        Rule Name.  # noqa: E501

        :param rule_name: The rule_name of this InboundSMSRule.  # noqa: E501
        :type: str
        """
        if rule_name is None:
            raise ValueError("Invalid value for `rule_name`, must not be `None`")  # noqa: E501

        self._rule_name = rule_name

    @property
    def message_search_type(self):
        """Gets the message_search_type of this InboundSMSRule.  # noqa: E501

        Message Search Type: 0=Any message, 1=starts with, 2=contains, 3=does not contain.  # noqa: E501

        :return: The message_search_type of this InboundSMSRule.  # noqa: E501
        :rtype: float
        """
        return self._message_search_type

    @message_search_type.setter
    def message_search_type(self, message_search_type):
        """Sets the message_search_type of this InboundSMSRule.

        Message Search Type: 0=Any message, 1=starts with, 2=contains, 3=does not contain.  # noqa: E501

        :param message_search_type: The message_search_type of this InboundSMSRule.  # noqa: E501
        :type: float
        """
        if message_search_type is None:
            raise ValueError("Invalid value for `message_search_type`, must not be `None`")  # noqa: E501

        self._message_search_type = message_search_type

    @property
    def message_search_term(self):
        """Gets the message_search_term of this InboundSMSRule.  # noqa: E501

        Message search term.  # noqa: E501

        :return: The message_search_term of this InboundSMSRule.  # noqa: E501
        :rtype: str
        """
        return self._message_search_term

    @message_search_term.setter
    def message_search_term(self, message_search_term):
        """Sets the message_search_term of this InboundSMSRule.

        Message search term.  # noqa: E501

        :param message_search_term: The message_search_term of this InboundSMSRule.  # noqa: E501
        :type: str
        """
        if message_search_term is None:
            raise ValueError("Invalid value for `message_search_term`, must not be `None`")  # noqa: E501

        self._message_search_term = message_search_term

    @property
    def action(self):
        """Gets the action of this InboundSMSRule.  # noqa: E501

        Action to be taken (AUTO_REPLY, EMAIL_USER, EMAIL_FIXED, URL, SMS, POLL, GROUP_SMS, MOVE_CONTACT, CREATE_CONTACT, CREATE_CONTACT_PLUS_EMAIL, CREATE_CONTACT_PLUS_NAME_EMAIL CREATE_CONTACT_PLUS_NAME, SMPP, NONE).  # noqa: E501

        :return: The action of this InboundSMSRule.  # noqa: E501
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this InboundSMSRule.

        Action to be taken (AUTO_REPLY, EMAIL_USER, EMAIL_FIXED, URL, SMS, POLL, GROUP_SMS, MOVE_CONTACT, CREATE_CONTACT, CREATE_CONTACT_PLUS_EMAIL, CREATE_CONTACT_PLUS_NAME_EMAIL CREATE_CONTACT_PLUS_NAME, SMPP, NONE).  # noqa: E501

        :param action: The action of this InboundSMSRule.  # noqa: E501
        :type: str
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def action_address(self):
        """Gets the action_address of this InboundSMSRule.  # noqa: E501

        Action address.  # noqa: E501

        :return: The action_address of this InboundSMSRule.  # noqa: E501
        :rtype: str
        """
        return self._action_address

    @action_address.setter
    def action_address(self, action_address):
        """Sets the action_address of this InboundSMSRule.

        Action address.  # noqa: E501

        :param action_address: The action_address of this InboundSMSRule.  # noqa: E501
        :type: str
        """
        if action_address is None:
            raise ValueError("Invalid value for `action_address`, must not be `None`")  # noqa: E501

        self._action_address = action_address

    @property
    def enabled(self):
        """Gets the enabled of this InboundSMSRule.  # noqa: E501

        Enabled: Disabled=0 or Enabled=1.  # noqa: E501

        :return: The enabled of this InboundSMSRule.  # noqa: E501
        :rtype: float
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this InboundSMSRule.

        Enabled: Disabled=0 or Enabled=1.  # noqa: E501

        :param enabled: The enabled of this InboundSMSRule.  # noqa: E501
        :type: float
        """
        if enabled is None:
            raise ValueError("Invalid value for `enabled`, must not be `None`")  # noqa: E501

        self._enabled = enabled

    @property
    def webhook_type(self):
        """Gets the webhook_type of this InboundSMSRule.  # noqa: E501

        post, get, or json. post by default  # noqa: E501

        :return: The webhook_type of this InboundSMSRule.  # noqa: E501
        :rtype: str
        """
        return self._webhook_type

    @webhook_type.setter
    def webhook_type(self, webhook_type):
        """Sets the webhook_type of this InboundSMSRule.

        post, get, or json. post by default  # noqa: E501

        :param webhook_type: The webhook_type of this InboundSMSRule.  # noqa: E501
        :type: str
        """

        self._webhook_type = webhook_type

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_value = data[self.discriminator].lower()
        return self.discriminator_value_class_map.get(discriminator_value)

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.clicksend_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(InboundSMSRule, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InboundSMSRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
