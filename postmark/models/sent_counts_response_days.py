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


class SentCountsResponseDays(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, date=None, sent=None):
        """
        SentCountsResponseDays - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'date': 'str',
            'sent': 'int'
        }

        self.attribute_map = {
            'date': 'Date',
            'sent': 'Sent'
        }

        self._date = None
        self._sent = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if date is not None:
          self.date = date
        if sent is not None:
          self.sent = sent

    @property
    def date(self):
        """
        Gets the date of this SentCountsResponseDays.

        :return: The date of this SentCountsResponseDays.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this SentCountsResponseDays.

        :param date: The date of this SentCountsResponseDays.
        :type: str
        """

        self._date = date

    @property
    def sent(self):
        """
        Gets the sent of this SentCountsResponseDays.

        :return: The sent of this SentCountsResponseDays.
        :rtype: int
        """
        return self._sent

    @sent.setter
    def sent(self, sent):
        """
        Sets the sent of this SentCountsResponseDays.

        :param sent: The sent of this SentCountsResponseDays.
        :type: int
        """

        self._sent = sent

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
        if not isinstance(other, SentCountsResponseDays):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
