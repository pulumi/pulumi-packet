# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class BgpSession(pulumi.CustomResource):
    address_family: pulumi.Output[str]
    """
    `ipv4` or `ipv6`
    """
    default_route: pulumi.Output[bool]
    """
    Boolean flag to set the default route policy. False by default.
    """
    device_id: pulumi.Output[str]
    """
    ID of device 
    """
    status: pulumi.Output[str]
    def __init__(__self__, resource_name, opts=None, address_family=None, default_route=None, device_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a resource to manage BGP sessions in Packet Host. Refer to [Packet BGP documentation](https://www.packet.com/developers/docs/network/advanced/local-and-global-bgp/) for more details.

        You need to have BGP config enabled in your project.

        BGP session must be linked to a device running [BIRD](https://bird.network.cz) or other BGP routing daemon which will control route advertisements via the session to Packet's upstream routers. 



        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address_family: `ipv4` or `ipv6`
        :param pulumi.Input[bool] default_route: Boolean flag to set the default route policy. False by default.
        :param pulumi.Input[str] device_id: ID of device 
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if address_family is None:
                raise TypeError("Missing required property 'address_family'")
            __props__['address_family'] = address_family
            __props__['default_route'] = default_route
            if device_id is None:
                raise TypeError("Missing required property 'device_id'")
            __props__['device_id'] = device_id
            __props__['status'] = None
        super(BgpSession, __self__).__init__(
            'packet:index/bgpSession:BgpSession',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, address_family=None, default_route=None, device_id=None, status=None):
        """
        Get an existing BgpSession resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address_family: `ipv4` or `ipv6`
        :param pulumi.Input[bool] default_route: Boolean flag to set the default route policy. False by default.
        :param pulumi.Input[str] device_id: ID of device 
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["address_family"] = address_family
        __props__["default_route"] = default_route
        __props__["device_id"] = device_id
        __props__["status"] = status
        return BgpSession(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

