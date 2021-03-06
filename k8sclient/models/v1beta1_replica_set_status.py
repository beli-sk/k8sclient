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


class V1beta1ReplicaSetStatus(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, replicas=None, fully_labeled_replicas=None, ready_replicas=None, observed_generation=None):
        """
        V1beta1ReplicaSetStatus - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'replicas': 'int',
            'fully_labeled_replicas': 'int',
            'ready_replicas': 'int',
            'observed_generation': 'int'
        }

        self.attribute_map = {
            'replicas': 'replicas',
            'fully_labeled_replicas': 'fullyLabeledReplicas',
            'ready_replicas': 'readyReplicas',
            'observed_generation': 'observedGeneration'
        }

        self._replicas = replicas
        self._fully_labeled_replicas = fully_labeled_replicas
        self._ready_replicas = ready_replicas
        self._observed_generation = observed_generation

    @property
    def replicas(self):
        """
        Gets the replicas of this V1beta1ReplicaSetStatus.
        Replicas is the most recently oberved number of replicas. More info: http://releases.k8s.io/HEAD/docs/user-guide/replication-controller.md#what-is-a-replication-controller

        :return: The replicas of this V1beta1ReplicaSetStatus.
        :rtype: int
        """
        return self._replicas

    @replicas.setter
    def replicas(self, replicas):
        """
        Sets the replicas of this V1beta1ReplicaSetStatus.
        Replicas is the most recently oberved number of replicas. More info: http://releases.k8s.io/HEAD/docs/user-guide/replication-controller.md#what-is-a-replication-controller

        :param replicas: The replicas of this V1beta1ReplicaSetStatus.
        :type: int
        """

        self._replicas = replicas

    @property
    def fully_labeled_replicas(self):
        """
        Gets the fully_labeled_replicas of this V1beta1ReplicaSetStatus.
        The number of pods that have labels matching the labels of the pod template of the replicaset.

        :return: The fully_labeled_replicas of this V1beta1ReplicaSetStatus.
        :rtype: int
        """
        return self._fully_labeled_replicas

    @fully_labeled_replicas.setter
    def fully_labeled_replicas(self, fully_labeled_replicas):
        """
        Sets the fully_labeled_replicas of this V1beta1ReplicaSetStatus.
        The number of pods that have labels matching the labels of the pod template of the replicaset.

        :param fully_labeled_replicas: The fully_labeled_replicas of this V1beta1ReplicaSetStatus.
        :type: int
        """

        self._fully_labeled_replicas = fully_labeled_replicas

    @property
    def ready_replicas(self):
        """
        Gets the ready_replicas of this V1beta1ReplicaSetStatus.
        The number of ready replicas for this replica set.

        :return: The ready_replicas of this V1beta1ReplicaSetStatus.
        :rtype: int
        """
        return self._ready_replicas

    @ready_replicas.setter
    def ready_replicas(self, ready_replicas):
        """
        Sets the ready_replicas of this V1beta1ReplicaSetStatus.
        The number of ready replicas for this replica set.

        :param ready_replicas: The ready_replicas of this V1beta1ReplicaSetStatus.
        :type: int
        """

        self._ready_replicas = ready_replicas

    @property
    def observed_generation(self):
        """
        Gets the observed_generation of this V1beta1ReplicaSetStatus.
        ObservedGeneration reflects the generation of the most recently observed ReplicaSet.

        :return: The observed_generation of this V1beta1ReplicaSetStatus.
        :rtype: int
        """
        return self._observed_generation

    @observed_generation.setter
    def observed_generation(self, observed_generation):
        """
        Sets the observed_generation of this V1beta1ReplicaSetStatus.
        ObservedGeneration reflects the generation of the most recently observed ReplicaSet.

        :param observed_generation: The observed_generation of this V1beta1ReplicaSetStatus.
        :type: int
        """

        self._observed_generation = observed_generation

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
