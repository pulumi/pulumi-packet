# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetPrecreatedIpBlockResult:
    """
    A collection of values returned by getPrecreatedIpBlock.
    """
    def __init__(__self__, address=None, address_family=None, cidr=None, cidr_notation=None, facility=None, gateway=None, global_=None, id=None, manageable=None, management=None, netmask=None, network=None, project_id=None, public=None, quantity=None):
        if address and not isinstance(address, str):
            raise TypeError("Expected argument 'address' to be a str")
        __self__.address = address
        if address_family and not isinstance(address_family, float):
            raise TypeError("Expected argument 'address_family' to be a float")
        __self__.address_family = address_family
        if cidr and not isinstance(cidr, float):
            raise TypeError("Expected argument 'cidr' to be a float")
        __self__.cidr = cidr
        if cidr_notation and not isinstance(cidr_notation, str):
            raise TypeError("Expected argument 'cidr_notation' to be a str")
        __self__.cidr_notation = cidr_notation
        """
        CIDR notation of the looked up block.
        """
        if facility and not isinstance(facility, str):
            raise TypeError("Expected argument 'facility' to be a str")
        __self__.facility = facility
        if gateway and not isinstance(gateway, str):
            raise TypeError("Expected argument 'gateway' to be a str")
        __self__.gateway = gateway
        if global_ and not isinstance(global_, bool):
            raise TypeError("Expected argument 'global_' to be a bool")
        __self__.global_ = global_
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if manageable and not isinstance(manageable, bool):
            raise TypeError("Expected argument 'manageable' to be a bool")
        __self__.manageable = manageable
        if management and not isinstance(management, bool):
            raise TypeError("Expected argument 'management' to be a bool")
        __self__.management = management
        if netmask and not isinstance(netmask, str):
            raise TypeError("Expected argument 'netmask' to be a str")
        __self__.netmask = netmask
        if network and not isinstance(network, str):
            raise TypeError("Expected argument 'network' to be a str")
        __self__.network = network
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        __self__.project_id = project_id
        if public and not isinstance(public, bool):
            raise TypeError("Expected argument 'public' to be a bool")
        __self__.public = public
        if quantity and not isinstance(quantity, float):
            raise TypeError("Expected argument 'quantity' to be a float")
        __self__.quantity = quantity
class AwaitableGetPrecreatedIpBlockResult(GetPrecreatedIpBlockResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrecreatedIpBlockResult(
            address=self.address,
            address_family=self.address_family,
            cidr=self.cidr,
            cidr_notation=self.cidr_notation,
            facility=self.facility,
            gateway=self.gateway,
            global_=self.global_,
            id=self.id,
            manageable=self.manageable,
            management=self.management,
            netmask=self.netmask,
            network=self.network,
            project_id=self.project_id,
            public=self.public,
            quantity=self.quantity)

def get_precreated_ip_block(address_family=None,facility=None,global_=None,project_id=None,public=None,opts=None):
    """
    Use this data source to get CIDR expression for precreated IPv6 and IPv4 blocks in Packet.
    You can then use the cidrsubnet TF builtin function to derive subnets.




    :param float address_family: 4 or 6, depending on which block you are looking for.
    :param str facility: Facility of the searched block. (Optional) Only allowed for non-global blocks.
    :param bool global_: Whether to look for global block. Default is false for backward compatibility.
    :param str project_id: ID of the project where the searched block should be.
    :param bool public: Whether to look for public or private block. 
    """
    __args__ = dict()


    __args__['addressFamily'] = address_family
    __args__['facility'] = facility
    __args__['global'] = global_
    __args__['projectId'] = project_id
    __args__['public'] = public
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('packet:index/getPrecreatedIpBlock:getPrecreatedIpBlock', __args__, opts=opts).value

    return AwaitableGetPrecreatedIpBlockResult(
        address=__ret__.get('address'),
        address_family=__ret__.get('addressFamily'),
        cidr=__ret__.get('cidr'),
        cidr_notation=__ret__.get('cidrNotation'),
        facility=__ret__.get('facility'),
        gateway=__ret__.get('gateway'),
        global_=__ret__.get('global'),
        id=__ret__.get('id'),
        manageable=__ret__.get('manageable'),
        management=__ret__.get('management'),
        netmask=__ret__.get('netmask'),
        network=__ret__.get('network'),
        project_id=__ret__.get('projectId'),
        public=__ret__.get('public'),
        quantity=__ret__.get('quantity'))
