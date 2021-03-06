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


class InlineResponse200Days(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, date=None, hard_bounce=None, soft_bounce=None, smtp_api_error=None, transient=None):
        """
        InlineResponse200Days - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'date': 'str',
            'hard_bounce': 'int',
            'soft_bounce': 'int',
            'smtp_api_error': 'int',
            'transient': 'int'
        }

        self.attribute_map = {
            'date': 'Date',
            'hard_bounce': 'HardBounce',
            'soft_bounce': 'SoftBounce',
            'smtp_api_error': 'SMTPApiError',
            'transient': 'Transient'
        }

        self._date = None
        self._hard_bounce = None
        self._soft_bounce = None
        self._smtp_api_error = None
        self._transient = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if date is not None:
          self.date = date
        if hard_bounce is not None:
          self.hard_bounce = hard_bounce
        if soft_bounce is not None:
          self.soft_bounce = soft_bounce
        if smtp_api_error is not None:
          self.smtp_api_error = smtp_api_error
        if transient is not None:
          self.transient = transient

    @property
    def date(self):
        """
        Gets the date of this InlineResponse200Days.

        :return: The date of this InlineResponse200Days.
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """
        Sets the date of this InlineResponse200Days.

        :param date: The date of this InlineResponse200Days.
        :type: str
        """

        self._date = date

    @property
    def hard_bounce(self):
        """
        Gets the hard_bounce of this InlineResponse200Days.

        :return: The hard_bounce of this InlineResponse200Days.
        :rtype: int
        """
        return self._hard_bounce

    @hard_bounce.setter
    def hard_bounce(self, hard_bounce):
        """
        Sets the hard_bounce of this InlineResponse200Days.

        :param hard_bounce: The hard_bounce of this InlineResponse200Days.
        :type: int
        """

        self._hard_bounce = hard_bounce

    @property
    def soft_bounce(self):
        """
        Gets the soft_bounce of this InlineResponse200Days.

        :return: The soft_bounce of this InlineResponse200Days.
        :rtype: int
        """
        return self._soft_bounce

    @soft_bounce.setter
    def soft_bounce(self, soft_bounce):
        """
        Sets the soft_bounce of this InlineResponse200Days.

        :param soft_bounce: The soft_bounce of this InlineResponse200Days.
        :type: int
        """

        self._soft_bounce = soft_bounce

    @property
    def smtp_api_error(self):
        """
        Gets the smtp_api_error of this InlineResponse200Days.

        :return: The smtp_api_error of this InlineResponse200Days.
        :rtype: int
        """
        return self._smtp_api_error

    @smtp_api_error.setter
    def smtp_api_error(self, smtp_api_error):
        """
        Sets the smtp_api_error of this InlineResponse200Days.

        :param smtp_api_error: The smtp_api_error of this InlineResponse200Days.
        :type: int
        """

        self._smtp_api_error = smtp_api_error

    @property
    def transient(self):
        """
        Gets the transient of this InlineResponse200Days.

        :return: The transient of this InlineResponse200Days.
        :rtype: int
        """
        return self._transient

    @transient.setter
    def transient(self, transient):
        """
        Sets the transient of this InlineResponse200Days.

        :param transient: The transient of this InlineResponse200Days.
        :type: int
        """

        self._transient = transient

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
        if not isinstance(other, InlineResponse200Days):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
