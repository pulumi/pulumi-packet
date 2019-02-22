# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class BgpSession(pulumi.CustomResource):
    address_family: pulumi.Output[str]
    """
    `ipv4` or `ipv6`
    """
    device_id: pulumi.Output[str]
    """
    ID of device 
    """
    status: pulumi.Output[str]
    def __init__(__self__, resource_name, opts=None, address_family=None, device_id=None, __name__=None, __opts__=None):
        """
        Provides a resource to manage BGP sessions in Packet Host. Refer to [Packet BGP documentation](https://support.packet.com/kb/articles/bgp) for more details.
        
        You need to have BGP config enabled in your project.
        
        BGP session must be linked to a device running [BIRD](https://bird.network.cz) or other BGP routing daemon which will control route advertisements via the session to Packet's upstream routers. 
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address_family: `ipv4` or `ipv6`
        :param pulumi.Input[str] device_id: ID of device 
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if address_family is None:
            raise TypeError('Missing required property address_family')
        __props__['address_family'] = address_family

        if device_id is None:
            raise TypeError('Missing required property device_id')
        __props__['device_id'] = device_id

        __props__['status'] = None

        super(BgpSession, __self__).__init__(
            'packet:index/bgpSession:BgpSession',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
