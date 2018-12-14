# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from . import utilities, tables

class ReservedIpBlock(pulumi.CustomResource):
    """
    Provides a resource to create and manage blocks of reserved IP addresses in a project.
    
    When user provision first device in a facility, Packet automatically allocates IPv6/56 and private IPv4/25 blocks.
    The new device then gets IPv6 and private IPv4 addresses from those block. It also gets a public IPv4/31 address.
    Every new device in the project and facility will automatically get IPv6 and private IPv4 addresses from pre-allocated i
    blocks.
    The IPv6 and private IPv4 blocks can't be created, only imported.
    
    It is only possible to create public IPv4 blocks, with masks from /24 (256 addresses) to /32 (1 address).
    
    Once IP block is allocated or imported, an address from it can be assigned to device with the `packet_ip_attachment` resource.
    """
    def __init__(__self__, __name__, __opts__=None, facility=None, project_id=None, quantity=None):
        """Create a ReservedIpBlock resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not facility:
            raise TypeError('Missing required property facility')
        __props__['facility'] = facility

        if not project_id:
            raise TypeError('Missing required property project_id')
        __props__['project_id'] = project_id

        if not quantity:
            raise TypeError('Missing required property quantity')
        __props__['quantity'] = quantity

        __props__['address'] = None
        __props__['address_family'] = None
        __props__['cidr'] = None
        __props__['cidr_notation'] = None
        __props__['gateway'] = None
        __props__['manageable'] = None
        __props__['management'] = None
        __props__['netmask'] = None
        __props__['network'] = None
        __props__['public'] = None

        super(ReservedIpBlock, __self__).__init__(
            'packet:index/reservedIpBlock:ReservedIpBlock',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
