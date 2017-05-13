# coding: utf-8

"""
    Postmark API

    Postmark makes sending and receiving email incredibly easy. 

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class InlineResponse2005(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, desktop=None, web_mail=None, mobile=None, unknown=None, days=None):
        """
        InlineResponse2005 - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'desktop': 'int',
            'web_mail': 'int',
            'mobile': 'int',
            'unknown': 'int',
            'days': 'list[DynamicResponse]'
        }

        self.attribute_map = {
            'desktop': 'Desktop',
            'web_mail': 'WebMail',
            'mobile': 'Mobile',
            'unknown': 'Unknown',
            'days': 'Days'
        }

        self._desktop = None
        self._web_mail = None
        self._mobile = None
        self._unknown = None
        self._days = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if desktop is not None:
          self.desktop = desktop
        if web_mail is not None:
          self.web_mail = web_mail
        if mobile is not None:
          self.mobile = mobile
        if unknown is not None:
          self.unknown = unknown
        if days is not None:
          self.days = days

    @property
    def desktop(self):
        """
        Gets the desktop of this InlineResponse2005.

        :return: The desktop of this InlineResponse2005.
        :rtype: int
        """
        return self._desktop

    @desktop.setter
    def desktop(self, desktop):
        """
        Sets the desktop of this InlineResponse2005.

        :param desktop: The desktop of this InlineResponse2005.
        :type: int
        """

        self._desktop = desktop

    @property
    def web_mail(self):
        """
        Gets the web_mail of this InlineResponse2005.

        :return: The web_mail of this InlineResponse2005.
        :rtype: int
        """
        return self._web_mail

    @web_mail.setter
    def web_mail(self, web_mail):
        """
        Sets the web_mail of this InlineResponse2005.

        :param web_mail: The web_mail of this InlineResponse2005.
        :type: int
        """

        self._web_mail = web_mail

    @property
    def mobile(self):
        """
        Gets the mobile of this InlineResponse2005.

        :return: The mobile of this InlineResponse2005.
        :rtype: int
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        """
        Sets the mobile of this InlineResponse2005.

        :param mobile: The mobile of this InlineResponse2005.
        :type: int
        """

        self._mobile = mobile

    @property
    def unknown(self):
        """
        Gets the unknown of this InlineResponse2005.

        :return: The unknown of this InlineResponse2005.
        :rtype: int
        """
        return self._unknown

    @unknown.setter
    def unknown(self, unknown):
        """
        Sets the unknown of this InlineResponse2005.

        :param unknown: The unknown of this InlineResponse2005.
        :type: int
        """

        self._unknown = unknown

    @property
    def days(self):
        """
        Gets the days of this InlineResponse2005.

        :return: The days of this InlineResponse2005.
        :rtype: list[DynamicResponse]
        """
        return self._days

    @days.setter
    def days(self, days):
        """
        Sets the days of this InlineResponse2005.

        :param days: The days of this InlineResponse2005.
        :type: list[DynamicResponse]
        """

        self._days = days

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, InlineResponse2005):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
