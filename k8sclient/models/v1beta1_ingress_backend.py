# coding: utf-8

"""
    

    No descripton provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: extensions/v1beta1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems
import re


class V1beta1IngressBackend(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, service_name=None, service_port=None):
        """
        V1beta1IngressBackend - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'service_name': 'str',
            'service_port': 'str'
        }

        self.attribute_map = {
            'service_name': 'serviceName',
            'service_port': 'servicePort'
        }

        self._service_name = service_name
        self._service_port = service_port

    @property
    def service_name(self):
        """
        Gets the service_name of this V1beta1IngressBackend.
        Specifies the name of the referenced service.

        :return: The service_name of this V1beta1IngressBackend.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        """
        Sets the service_name of this V1beta1IngressBackend.
        Specifies the name of the referenced service.

        :param service_name: The service_name of this V1beta1IngressBackend.
        :type: str
        """

        self._service_name = service_name

    @property
    def service_port(self):
        """
        Gets the service_port of this V1beta1IngressBackend.
        Specifies the port of the referenced service.

        :return: The service_port of this V1beta1IngressBackend.
        :rtype: str
        """
        return self._service_port

    @service_port.setter
    def service_port(self, service_port):
        """
        Sets the service_port of this V1beta1IngressBackend.
        Specifies the port of the referenced service.

        :param service_port: The service_port of this V1beta1IngressBackend.
        :type: str
        """

        self._service_port = service_port

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other