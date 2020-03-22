# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetProjectResult:
    """
    A collection of values returned by getProject.
    """
    def __init__(__self__, backend_transfer=None, bgp_config=None, created=None, id=None, name=None, organization_id=None, payment_method_id=None, project_id=None, updated=None, user_ids=None):
        if backend_transfer and not isinstance(backend_transfer, bool):
            raise TypeError("Expected argument 'backend_transfer' to be a bool")
        __self__.backend_transfer = backend_transfer
        """
        Whether Backend Transfer is enabled for this project
        """
        if bgp_config and not isinstance(bgp_config, dict):
            raise TypeError("Expected argument 'bgp_config' to be a dict")
        __self__.bgp_config = bgp_config
        """
        Optional BGP settings. Refer to [Packet guide for BGP](https://www.packet.com/developers/docs/network/advanced/local-and-global-bgp/).
        """
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        __self__.created = created
        """
        The timestamp for when the project was created
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        __self__.organization_id = organization_id
        """
        The UUID of this project's parent organization
        """
        if payment_method_id and not isinstance(payment_method_id, str):
            raise TypeError("Expected argument 'payment_method_id' to be a str")
        __self__.payment_method_id = payment_method_id
        """
        The UUID of payment method for this project
        """
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        __self__.project_id = project_id
        if updated and not isinstance(updated, str):
            raise TypeError("Expected argument 'updated' to be a str")
        __self__.updated = updated
        """
        The timestamp for the last time the project was updated
        """
        if user_ids and not isinstance(user_ids, list):
            raise TypeError("Expected argument 'user_ids' to be a list")
        __self__.user_ids = user_ids
        """
        List of UUIDs of user accounts which beling to this project
        """
class AwaitableGetProjectResult(GetProjectResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProjectResult(
            backend_transfer=self.backend_transfer,
            bgp_config=self.bgp_config,
            created=self.created,
            id=self.id,
            name=self.name,
            organization_id=self.organization_id,
            payment_method_id=self.payment_method_id,
            project_id=self.project_id,
            updated=self.updated,
            user_ids=self.user_ids)

def get_project(name=None,project_id=None,opts=None):
    """
    Use this datasource to retrieve attributes of the Project API resource.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/d/project.html.markdown.


    :param str name: The name which is used to look up the project
    :param str project_id: The UUID by which to look up the project
    """
    __args__ = dict()


    __args__['name'] = name
    __args__['projectId'] = project_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('packet:index/getProject:getProject', __args__, opts=opts).value

    return AwaitableGetProjectResult(
        backend_transfer=__ret__.get('backendTransfer'),
        bgp_config=__ret__.get('bgpConfig'),
        created=__ret__.get('created'),
        id=__ret__.get('id'),
        name=__ret__.get('name'),
        organization_id=__ret__.get('organizationId'),
        payment_method_id=__ret__.get('paymentMethodId'),
        project_id=__ret__.get('projectId'),
        updated=__ret__.get('updated'),
        user_ids=__ret__.get('userIds'))
