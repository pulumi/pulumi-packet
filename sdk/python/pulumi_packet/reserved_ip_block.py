# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class ReservedIpBlock(pulumi.CustomResource):
    address: pulumi.Output[str]
    address_family: pulumi.Output[float]
    """
    Address family as integer (4 or 6)
    """
    cidr: pulumi.Output[float]
    """
    length of CIDR prefix of the block as integer
    """
    cidr_notation: pulumi.Output[str]
    """
    Address and mask in CIDR notation, e.g. "147.229.15.30/31"
    """
    description: pulumi.Output[str]
    """
    Arbitrary description
    """
    facility: pulumi.Output[str]
    """
    Facility where to allocate the public IP address block, makes sense only for type==public_ipv4, must be empty for type==global_ipv4
    """
    gateway: pulumi.Output[str]
    global_: pulumi.Output[bool]
    """
    boolean flag whether addresses from a block are global (i.e. can be assigned in any facility)
    """
    manageable: pulumi.Output[bool]
    management: pulumi.Output[bool]
    netmask: pulumi.Output[str]
    """
    Mask in decimal notation, e.g. "255.255.255.0"
    """
    network: pulumi.Output[str]
    """
    Network IP address portion of the block specification
    """
    project_id: pulumi.Output[str]
    """
    The packet project ID where to allocate the address block
    """
    public: pulumi.Output[bool]
    """
    boolean flag whether addresses from a block are public
    """
    quantity: pulumi.Output[float]
    """
    The number of allocated /32 addresses, a power of 2
    """
    type: pulumi.Output[str]
    """
    Either "global_ipv4" or "public_ipv4", defaults to "public_ipv4" for backward compatibility
    """
    def __init__(__self__, resource_name, opts=None, description=None, facility=None, project_id=None, quantity=None, type=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a resource to create and manage blocks of reserved IP addresses in a project.
        
        When a user provisions first device in a facility, Packet API automatically allocates IPv6/56 and private IPv4/25 blocks.
        The new device then gets IPv6 and private IPv4 addresses from those block. It also gets a public IPv4/31 address.
        Every new device in the project and facility will automatically get IPv6 and private IPv4 addresses from these pre-allocated blocks.
        The IPv6 and private IPv4 blocks can't be created, only imported. With this resource, it's possible to create either public IPv4 blocks or global IPv4 blocks.
        
        Public blocks are allocated in a facility. Addresses from public blocks can only be assigned to devices in the facility. Public blocks can have mask from /24 (256 addresses) to /32 (1 address). If you create public block with this resource, you must fill the facility argmument.
        
        Addresses from global blocks can be assigned in any facility. Global blocks can have mask from /30 (4 addresses), to /32 (1 address). If you create global block with this resource, you must specify type = "global_ipv4" and you must omit the facility argument.
        
        Once IP block is allocated or imported, an address from it can be assigned to device with the `.IpAttachment` resource.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Arbitrary description
        :param pulumi.Input[str] facility: Facility where to allocate the public IP address block, makes sense only for type==public_ipv4, must be empty for type==global_ipv4
        :param pulumi.Input[str] project_id: The packet project ID where to allocate the address block
        :param pulumi.Input[float] quantity: The number of allocated /32 addresses, a power of 2
        :param pulumi.Input[str] type: Either "global_ipv4" or "public_ipv4", defaults to "public_ipv4" for backward compatibility

        > This content is derived from https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/reserved_ip_block.html.markdown.
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

            __props__['description'] = description
            __props__['facility'] = facility
            if project_id is None:
                raise TypeError("Missing required property 'project_id'")
            __props__['project_id'] = project_id
            if quantity is None:
                raise TypeError("Missing required property 'quantity'")
            __props__['quantity'] = quantity
            __props__['type'] = type
            __props__['address'] = None
            __props__['address_family'] = None
            __props__['cidr'] = None
            __props__['cidr_notation'] = None
            __props__['gateway'] = None
            __props__['global_'] = None
            __props__['manageable'] = None
            __props__['management'] = None
            __props__['netmask'] = None
            __props__['network'] = None
            __props__['public'] = None
        super(ReservedIpBlock, __self__).__init__(
            'packet:index/reservedIpBlock:ReservedIpBlock',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, address=None, address_family=None, cidr=None, cidr_notation=None, description=None, facility=None, gateway=None, global_=None, manageable=None, management=None, netmask=None, network=None, project_id=None, public=None, quantity=None, type=None):
        """
        Get an existing ReservedIpBlock resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] address_family: Address family as integer (4 or 6)
        :param pulumi.Input[float] cidr: length of CIDR prefix of the block as integer
        :param pulumi.Input[str] cidr_notation: Address and mask in CIDR notation, e.g. "147.229.15.30/31"
        :param pulumi.Input[str] description: Arbitrary description
        :param pulumi.Input[str] facility: Facility where to allocate the public IP address block, makes sense only for type==public_ipv4, must be empty for type==global_ipv4
        :param pulumi.Input[bool] global_: boolean flag whether addresses from a block are global (i.e. can be assigned in any facility)
        :param pulumi.Input[str] netmask: Mask in decimal notation, e.g. "255.255.255.0"
        :param pulumi.Input[str] network: Network IP address portion of the block specification
        :param pulumi.Input[str] project_id: The packet project ID where to allocate the address block
        :param pulumi.Input[bool] public: boolean flag whether addresses from a block are public
        :param pulumi.Input[float] quantity: The number of allocated /32 addresses, a power of 2
        :param pulumi.Input[str] type: Either "global_ipv4" or "public_ipv4", defaults to "public_ipv4" for backward compatibility

        > This content is derived from https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/reserved_ip_block.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["address"] = address
        __props__["address_family"] = address_family
        __props__["cidr"] = cidr
        __props__["cidr_notation"] = cidr_notation
        __props__["description"] = description
        __props__["facility"] = facility
        __props__["gateway"] = gateway
        __props__["global_"] = global_
        __props__["manageable"] = manageable
        __props__["management"] = management
        __props__["netmask"] = netmask
        __props__["network"] = network
        __props__["project_id"] = project_id
        __props__["public"] = public
        __props__["quantity"] = quantity
        __props__["type"] = type
        return ReservedIpBlock(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

