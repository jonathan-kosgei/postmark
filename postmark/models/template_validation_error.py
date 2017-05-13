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


class TemplateValidationError(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, message=None, line=None, character_position=None):
        """
        TemplateValidationError - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'message': 'str',
            'line': 'int',
            'character_position': 'int'
        }

        self.attribute_map = {
            'message': 'Message',
            'line': 'Line',
            'character_position': 'CharacterPosition'
        }

        self._message = None
        self._line = None
        self._character_position = None

        # TODO: let required properties as mandatory parameter in the constructor.
        #       - to check if required property is not None (e.g. by calling setter)
        #       - ApiClient.__deserialize_model has to be adapted as well
        if message is not None:
          self.message = message
        if line is not None:
          self.line = line
        if character_position is not None:
          self.character_position = character_position

    @property
    def message(self):
        """
        Gets the message of this TemplateValidationError.

        :return: The message of this TemplateValidationError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this TemplateValidationError.

        :param message: The message of this TemplateValidationError.
        :type: str
        """

        self._message = message

    @property
    def line(self):
        """
        Gets the line of this TemplateValidationError.

        :return: The line of this TemplateValidationError.
        :rtype: int
        """
        return self._line

    @line.setter
    def line(self, line):
        """
        Sets the line of this TemplateValidationError.

        :param line: The line of this TemplateValidationError.
        :type: int
        """

        self._line = line

    @property
    def character_position(self):
        """
        Gets the character_position of this TemplateValidationError.

        :return: The character_position of this TemplateValidationError.
        :rtype: int
        """
        return self._character_position

    @character_position.setter
    def character_position(self, character_position):
        """
        Sets the character_position of this TemplateValidationError.

        :param character_position: The character_position of this TemplateValidationError.
        :type: int
        """

        self._character_position = character_position

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
        if not isinstance(other, TemplateValidationError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
