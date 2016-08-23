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

from __future__ import absolute_import

import os
import sys
import unittest

import k8sclient
from k8sclient.rest import ApiException
from k8sclient.apis.apisextensionsvbeta_api import ApisextensionsvbetaApi


class TestApisextensionsvbetaApi(unittest.TestCase):
    """ ApisextensionsvbetaApi unit test stubs """

    def setUp(self):
        self.api = k8sclient.apis.apisextensionsvbeta_api.ApisextensionsvbetaApi()

    def tearDown(self):
        pass

    def test_create_namespaced_daemon_set(self):
        """
        Test case for create_namespaced_daemon_set

        create a DaemonSet
        """
        pass

    def test_create_namespaced_deployment(self):
        """
        Test case for create_namespaced_deployment

        create a Deployment
        """
        pass

    def test_create_namespaced_deployment_rollback_rollback(self):
        """
        Test case for create_namespaced_deployment_rollback_rollback

        create rollback of a DeploymentRollback
        """
        pass

    def test_create_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for create_namespaced_horizontal_pod_autoscaler

        create a HorizontalPodAutoscaler
        """
        pass

    def test_create_namespaced_ingress(self):
        """
        Test case for create_namespaced_ingress

        create a Ingress
        """
        pass

    def test_create_namespaced_job(self):
        """
        Test case for create_namespaced_job

        create a Job
        """
        pass

    def test_create_namespaced_network_policy(self):
        """
        Test case for create_namespaced_network_policy

        create a NetworkPolicy
        """
        pass

    def test_create_namespaced_replica_set(self):
        """
        Test case for create_namespaced_replica_set

        create a ReplicaSet
        """
        pass

    def test_create_storage_class(self):
        """
        Test case for create_storage_class

        create a StorageClass
        """
        pass

    def test_create_third_party_resource(self):
        """
        Test case for create_third_party_resource

        create a ThirdPartyResource
        """
        pass

    def test_delete_namespaced_daemon_set(self):
        """
        Test case for delete_namespaced_daemon_set

        delete a DaemonSet
        """
        pass

    def test_delete_namespaced_deployment(self):
        """
        Test case for delete_namespaced_deployment

        delete a Deployment
        """
        pass

    def test_delete_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for delete_namespaced_horizontal_pod_autoscaler

        delete a HorizontalPodAutoscaler
        """
        pass

    def test_delete_namespaced_ingress(self):
        """
        Test case for delete_namespaced_ingress

        delete a Ingress
        """
        pass

    def test_delete_namespaced_job(self):
        """
        Test case for delete_namespaced_job

        delete a Job
        """
        pass

    def test_delete_namespaced_network_policy(self):
        """
        Test case for delete_namespaced_network_policy

        delete a NetworkPolicy
        """
        pass

    def test_delete_namespaced_replica_set(self):
        """
        Test case for delete_namespaced_replica_set

        delete a ReplicaSet
        """
        pass

    def test_delete_storage_class(self):
        """
        Test case for delete_storage_class

        delete a StorageClass
        """
        pass

    def test_delete_third_party_resource(self):
        """
        Test case for delete_third_party_resource

        delete a ThirdPartyResource
        """
        pass

    def test_deletecollection_namespaced_daemon_set(self):
        """
        Test case for deletecollection_namespaced_daemon_set

        delete collection of DaemonSet
        """
        pass

    def test_deletecollection_namespaced_deployment(self):
        """
        Test case for deletecollection_namespaced_deployment

        delete collection of Deployment
        """
        pass

    def test_deletecollection_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for deletecollection_namespaced_horizontal_pod_autoscaler

        delete collection of HorizontalPodAutoscaler
        """
        pass

    def test_deletecollection_namespaced_ingress(self):
        """
        Test case for deletecollection_namespaced_ingress

        delete collection of Ingress
        """
        pass

    def test_deletecollection_namespaced_job(self):
        """
        Test case for deletecollection_namespaced_job

        delete collection of Job
        """
        pass

    def test_deletecollection_namespaced_network_policy(self):
        """
        Test case for deletecollection_namespaced_network_policy

        delete collection of NetworkPolicy
        """
        pass

    def test_deletecollection_namespaced_replica_set(self):
        """
        Test case for deletecollection_namespaced_replica_set

        delete collection of ReplicaSet
        """
        pass

    def test_deletecollection_storage_class(self):
        """
        Test case for deletecollection_storage_class

        delete collection of StorageClass
        """
        pass

    def test_deletecollection_third_party_resource(self):
        """
        Test case for deletecollection_third_party_resource

        delete collection of ThirdPartyResource
        """
        pass

    def test_get_api_resources(self):
        """
        Test case for get_api_resources

        get available resources
        """
        pass

    def test_list_namespaced_daemon_set(self):
        """
        Test case for list_namespaced_daemon_set

        list or watch objects of kind DaemonSet
        """
        pass

    def test_list_namespaced_daemon_set_0(self):
        """
        Test case for list_namespaced_daemon_set_0

        list or watch objects of kind DaemonSet
        """
        pass

    def test_list_namespaced_deployment(self):
        """
        Test case for list_namespaced_deployment

        list or watch objects of kind Deployment
        """
        pass

    def test_list_namespaced_deployment_0(self):
        """
        Test case for list_namespaced_deployment_0

        list or watch objects of kind Deployment
        """
        pass

    def test_list_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for list_namespaced_horizontal_pod_autoscaler

        list or watch objects of kind HorizontalPodAutoscaler
        """
        pass

    def test_list_namespaced_horizontal_pod_autoscaler_0(self):
        """
        Test case for list_namespaced_horizontal_pod_autoscaler_0

        list or watch objects of kind HorizontalPodAutoscaler
        """
        pass

    def test_list_namespaced_ingress(self):
        """
        Test case for list_namespaced_ingress

        list or watch objects of kind Ingress
        """
        pass

    def test_list_namespaced_ingress_0(self):
        """
        Test case for list_namespaced_ingress_0

        list or watch objects of kind Ingress
        """
        pass

    def test_list_namespaced_job(self):
        """
        Test case for list_namespaced_job

        list or watch objects of kind Job
        """
        pass

    def test_list_namespaced_job_0(self):
        """
        Test case for list_namespaced_job_0

        list or watch objects of kind Job
        """
        pass

    def test_list_namespaced_network_policy(self):
        """
        Test case for list_namespaced_network_policy

        list or watch objects of kind NetworkPolicy
        """
        pass

    def test_list_namespaced_network_policy_0(self):
        """
        Test case for list_namespaced_network_policy_0

        list or watch objects of kind NetworkPolicy
        """
        pass

    def test_list_namespaced_replica_set(self):
        """
        Test case for list_namespaced_replica_set

        list or watch objects of kind ReplicaSet
        """
        pass

    def test_list_namespaced_replica_set_0(self):
        """
        Test case for list_namespaced_replica_set_0

        list or watch objects of kind ReplicaSet
        """
        pass

    def test_list_storage_class(self):
        """
        Test case for list_storage_class

        list or watch objects of kind StorageClass
        """
        pass

    def test_list_third_party_resource(self):
        """
        Test case for list_third_party_resource

        list or watch objects of kind ThirdPartyResource
        """
        pass

    def test_patch_namespaced_daemon_set(self):
        """
        Test case for patch_namespaced_daemon_set

        partially update the specified DaemonSet
        """
        pass

    def test_patch_namespaced_daemon_set_status(self):
        """
        Test case for patch_namespaced_daemon_set_status

        partially update status of the specified DaemonSet
        """
        pass

    def test_patch_namespaced_deployment(self):
        """
        Test case for patch_namespaced_deployment

        partially update the specified Deployment
        """
        pass

    def test_patch_namespaced_deployment_status(self):
        """
        Test case for patch_namespaced_deployment_status

        partially update status of the specified Deployment
        """
        pass

    def test_patch_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for patch_namespaced_horizontal_pod_autoscaler

        partially update the specified HorizontalPodAutoscaler
        """
        pass

    def test_patch_namespaced_horizontal_pod_autoscaler_status(self):
        """
        Test case for patch_namespaced_horizontal_pod_autoscaler_status

        partially update status of the specified HorizontalPodAutoscaler
        """
        pass

    def test_patch_namespaced_ingress(self):
        """
        Test case for patch_namespaced_ingress

        partially update the specified Ingress
        """
        pass

    def test_patch_namespaced_ingress_status(self):
        """
        Test case for patch_namespaced_ingress_status

        partially update status of the specified Ingress
        """
        pass

    def test_patch_namespaced_job(self):
        """
        Test case for patch_namespaced_job

        partially update the specified Job
        """
        pass

    def test_patch_namespaced_job_status(self):
        """
        Test case for patch_namespaced_job_status

        partially update status of the specified Job
        """
        pass

    def test_patch_namespaced_network_policy(self):
        """
        Test case for patch_namespaced_network_policy

        partially update the specified NetworkPolicy
        """
        pass

    def test_patch_namespaced_replica_set(self):
        """
        Test case for patch_namespaced_replica_set

        partially update the specified ReplicaSet
        """
        pass

    def test_patch_namespaced_replica_set_status(self):
        """
        Test case for patch_namespaced_replica_set_status

        partially update status of the specified ReplicaSet
        """
        pass

    def test_patch_namespaced_scale_scale(self):
        """
        Test case for patch_namespaced_scale_scale

        partially update scale of the specified Scale
        """
        pass

    def test_patch_namespaced_scale_scale_0(self):
        """
        Test case for patch_namespaced_scale_scale_0

        partially update scale of the specified Scale
        """
        pass

    def test_patch_namespaced_scale_scale_1(self):
        """
        Test case for patch_namespaced_scale_scale_1

        partially update scale of the specified Scale
        """
        pass

    def test_patch_storage_class(self):
        """
        Test case for patch_storage_class

        partially update the specified StorageClass
        """
        pass

    def test_patch_third_party_resource(self):
        """
        Test case for patch_third_party_resource

        partially update the specified ThirdPartyResource
        """
        pass

    def test_read_namespaced_daemon_set(self):
        """
        Test case for read_namespaced_daemon_set

        read the specified DaemonSet
        """
        pass

    def test_read_namespaced_daemon_set_status(self):
        """
        Test case for read_namespaced_daemon_set_status

        read status of the specified DaemonSet
        """
        pass

    def test_read_namespaced_deployment(self):
        """
        Test case for read_namespaced_deployment

        read the specified Deployment
        """
        pass

    def test_read_namespaced_deployment_status(self):
        """
        Test case for read_namespaced_deployment_status

        read status of the specified Deployment
        """
        pass

    def test_read_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for read_namespaced_horizontal_pod_autoscaler

        read the specified HorizontalPodAutoscaler
        """
        pass

    def test_read_namespaced_horizontal_pod_autoscaler_status(self):
        """
        Test case for read_namespaced_horizontal_pod_autoscaler_status

        read status of the specified HorizontalPodAutoscaler
        """
        pass

    def test_read_namespaced_ingress(self):
        """
        Test case for read_namespaced_ingress

        read the specified Ingress
        """
        pass

    def test_read_namespaced_ingress_status(self):
        """
        Test case for read_namespaced_ingress_status

        read status of the specified Ingress
        """
        pass

    def test_read_namespaced_job(self):
        """
        Test case for read_namespaced_job

        read the specified Job
        """
        pass

    def test_read_namespaced_job_status(self):
        """
        Test case for read_namespaced_job_status

        read status of the specified Job
        """
        pass

    def test_read_namespaced_network_policy(self):
        """
        Test case for read_namespaced_network_policy

        read the specified NetworkPolicy
        """
        pass

    def test_read_namespaced_replica_set(self):
        """
        Test case for read_namespaced_replica_set

        read the specified ReplicaSet
        """
        pass

    def test_read_namespaced_replica_set_status(self):
        """
        Test case for read_namespaced_replica_set_status

        read status of the specified ReplicaSet
        """
        pass

    def test_read_namespaced_scale_scale(self):
        """
        Test case for read_namespaced_scale_scale

        read scale of the specified Scale
        """
        pass

    def test_read_namespaced_scale_scale_0(self):
        """
        Test case for read_namespaced_scale_scale_0

        read scale of the specified Scale
        """
        pass

    def test_read_namespaced_scale_scale_1(self):
        """
        Test case for read_namespaced_scale_scale_1

        read scale of the specified Scale
        """
        pass

    def test_read_storage_class(self):
        """
        Test case for read_storage_class

        read the specified StorageClass
        """
        pass

    def test_read_third_party_resource(self):
        """
        Test case for read_third_party_resource

        read the specified ThirdPartyResource
        """
        pass

    def test_replace_namespaced_daemon_set(self):
        """
        Test case for replace_namespaced_daemon_set

        replace the specified DaemonSet
        """
        pass

    def test_replace_namespaced_daemon_set_status(self):
        """
        Test case for replace_namespaced_daemon_set_status

        replace status of the specified DaemonSet
        """
        pass

    def test_replace_namespaced_deployment(self):
        """
        Test case for replace_namespaced_deployment

        replace the specified Deployment
        """
        pass

    def test_replace_namespaced_deployment_status(self):
        """
        Test case for replace_namespaced_deployment_status

        replace status of the specified Deployment
        """
        pass

    def test_replace_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for replace_namespaced_horizontal_pod_autoscaler

        replace the specified HorizontalPodAutoscaler
        """
        pass

    def test_replace_namespaced_horizontal_pod_autoscaler_status(self):
        """
        Test case for replace_namespaced_horizontal_pod_autoscaler_status

        replace status of the specified HorizontalPodAutoscaler
        """
        pass

    def test_replace_namespaced_ingress(self):
        """
        Test case for replace_namespaced_ingress

        replace the specified Ingress
        """
        pass

    def test_replace_namespaced_ingress_status(self):
        """
        Test case for replace_namespaced_ingress_status

        replace status of the specified Ingress
        """
        pass

    def test_replace_namespaced_job(self):
        """
        Test case for replace_namespaced_job

        replace the specified Job
        """
        pass

    def test_replace_namespaced_job_status(self):
        """
        Test case for replace_namespaced_job_status

        replace status of the specified Job
        """
        pass

    def test_replace_namespaced_network_policy(self):
        """
        Test case for replace_namespaced_network_policy

        replace the specified NetworkPolicy
        """
        pass

    def test_replace_namespaced_replica_set(self):
        """
        Test case for replace_namespaced_replica_set

        replace the specified ReplicaSet
        """
        pass

    def test_replace_namespaced_replica_set_status(self):
        """
        Test case for replace_namespaced_replica_set_status

        replace status of the specified ReplicaSet
        """
        pass

    def test_replace_namespaced_scale_scale(self):
        """
        Test case for replace_namespaced_scale_scale

        replace scale of the specified Scale
        """
        pass

    def test_replace_namespaced_scale_scale_0(self):
        """
        Test case for replace_namespaced_scale_scale_0

        replace scale of the specified Scale
        """
        pass

    def test_replace_namespaced_scale_scale_1(self):
        """
        Test case for replace_namespaced_scale_scale_1

        replace scale of the specified Scale
        """
        pass

    def test_replace_storage_class(self):
        """
        Test case for replace_storage_class

        replace the specified StorageClass
        """
        pass

    def test_replace_third_party_resource(self):
        """
        Test case for replace_third_party_resource

        replace the specified ThirdPartyResource
        """
        pass

    def test_watch_namespaced_daemon_set(self):
        """
        Test case for watch_namespaced_daemon_set

        watch changes to an object of kind DaemonSet
        """
        pass

    def test_watch_namespaced_daemon_set_list(self):
        """
        Test case for watch_namespaced_daemon_set_list

        watch individual changes to a list of DaemonSet
        """
        pass

    def test_watch_namespaced_daemon_set_list_0(self):
        """
        Test case for watch_namespaced_daemon_set_list_0

        watch individual changes to a list of DaemonSet
        """
        pass

    def test_watch_namespaced_deployment(self):
        """
        Test case for watch_namespaced_deployment

        watch changes to an object of kind Deployment
        """
        pass

    def test_watch_namespaced_deployment_list(self):
        """
        Test case for watch_namespaced_deployment_list

        watch individual changes to a list of Deployment
        """
        pass

    def test_watch_namespaced_deployment_list_0(self):
        """
        Test case for watch_namespaced_deployment_list_0

        watch individual changes to a list of Deployment
        """
        pass

    def test_watch_namespaced_horizontal_pod_autoscaler(self):
        """
        Test case for watch_namespaced_horizontal_pod_autoscaler

        watch changes to an object of kind HorizontalPodAutoscaler
        """
        pass

    def test_watch_namespaced_horizontal_pod_autoscaler_list(self):
        """
        Test case for watch_namespaced_horizontal_pod_autoscaler_list

        watch individual changes to a list of HorizontalPodAutoscaler
        """
        pass

    def test_watch_namespaced_horizontal_pod_autoscaler_list_0(self):
        """
        Test case for watch_namespaced_horizontal_pod_autoscaler_list_0

        watch individual changes to a list of HorizontalPodAutoscaler
        """
        pass

    def test_watch_namespaced_ingress(self):
        """
        Test case for watch_namespaced_ingress

        watch changes to an object of kind Ingress
        """
        pass

    def test_watch_namespaced_ingress_list(self):
        """
        Test case for watch_namespaced_ingress_list

        watch individual changes to a list of Ingress
        """
        pass

    def test_watch_namespaced_ingress_list_0(self):
        """
        Test case for watch_namespaced_ingress_list_0

        watch individual changes to a list of Ingress
        """
        pass

    def test_watch_namespaced_job(self):
        """
        Test case for watch_namespaced_job

        watch changes to an object of kind Job
        """
        pass

    def test_watch_namespaced_job_list(self):
        """
        Test case for watch_namespaced_job_list

        watch individual changes to a list of Job
        """
        pass

    def test_watch_namespaced_job_list_0(self):
        """
        Test case for watch_namespaced_job_list_0

        watch individual changes to a list of Job
        """
        pass

    def test_watch_namespaced_network_policy(self):
        """
        Test case for watch_namespaced_network_policy

        watch changes to an object of kind NetworkPolicy
        """
        pass

    def test_watch_namespaced_network_policy_list(self):
        """
        Test case for watch_namespaced_network_policy_list

        watch individual changes to a list of NetworkPolicy
        """
        pass

    def test_watch_namespaced_network_policy_list_0(self):
        """
        Test case for watch_namespaced_network_policy_list_0

        watch individual changes to a list of NetworkPolicy
        """
        pass

    def test_watch_namespaced_replica_set(self):
        """
        Test case for watch_namespaced_replica_set

        watch changes to an object of kind ReplicaSet
        """
        pass

    def test_watch_namespaced_replica_set_list(self):
        """
        Test case for watch_namespaced_replica_set_list

        watch individual changes to a list of ReplicaSet
        """
        pass

    def test_watch_namespaced_replica_set_list_0(self):
        """
        Test case for watch_namespaced_replica_set_list_0

        watch individual changes to a list of ReplicaSet
        """
        pass

    def test_watch_storage_class(self):
        """
        Test case for watch_storage_class

        watch changes to an object of kind StorageClass
        """
        pass

    def test_watch_storage_class_list(self):
        """
        Test case for watch_storage_class_list

        watch individual changes to a list of StorageClass
        """
        pass

    def test_watch_third_party_resource(self):
        """
        Test case for watch_third_party_resource

        watch changes to an object of kind ThirdPartyResource
        """
        pass

    def test_watch_third_party_resource_list(self):
        """
        Test case for watch_third_party_resource_list

        watch individual changes to a list of ThirdPartyResource
        """
        pass


if __name__ == '__main__':
    unittest.main()
