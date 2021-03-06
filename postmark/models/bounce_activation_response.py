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


class BounceActivationResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, message=None, bounce=None):
        """
        BounceActivationResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'message': 'str',
            'bounce': 'BounceInfoResponse'
        }

        self.attribute_map = {
            'message': 'Message',
            'bounce': 'Bounce'
        }

        self._message = None
        self._bounce = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if message is not None:
          self.message = message
        if bounce is not None:
          self.bounce = bounce

    @property
    def message(self):
        """
        Gets the message of this BounceActivationResponse.

        :return: The message of this BounceActivationResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this BounceActivationResponse.

        :param message: The message of this BounceActivationResponse.
        :type: str
        """

        self._message = message

    @property
    def bounce(self):
        """
        Gets the bounce of this BounceActivationResponse.

        :return: The bounce of this BounceActivationResponse.
        :rtype: BounceInfoResponse
        """
        return self._bounce

    @bounce.setter
    def bounce(self, bounce):
        """
        Sets the bounce of this BounceActivationResponse.

        :param bounce: The bounce of this BounceActivationResponse.
        :type: BounceInfoResponse
        """

        self._bounce = bounce

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
        if not isinstance(other, BounceActivationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
