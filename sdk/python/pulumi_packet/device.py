# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from . import utilities, tables

class Device(pulumi.CustomResource):
    """
    Provides a Packet device resource. This can be used to create,
    modify, and delete devices.
    
    ~> **Note:** All arguments including the root_password and user_data will be stored in
     the raw state as plain-text.
    [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
    
    """
    def __init__(__self__, __name__, __opts__=None, always_pxe=None, billing_cycle=None, description=None, facility=None, hardware_reservation_id=None, hostname=None, ipxe_script_url=None, operating_system=None, plan=None, project_id=None, public_ipv4_subnet_size=None, storage=None, tags=None, user_data=None):
        """Create a Device resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['always_pxe'] = always_pxe

        if not billing_cycle:
            raise TypeError('Missing required property billing_cycle')
        __props__['billing_cycle'] = billing_cycle

        __props__['description'] = description

        if not facility:
            raise TypeError('Missing required property facility')
        __props__['facility'] = facility

        __props__['hardware_reservation_id'] = hardware_reservation_id

        if not hostname:
            raise TypeError('Missing required property hostname')
        __props__['hostname'] = hostname

        __props__['ipxe_script_url'] = ipxe_script_url

        if not operating_system:
            raise TypeError('Missing required property operating_system')
        __props__['operating_system'] = operating_system

        if not plan:
            raise TypeError('Missing required property plan')
        __props__['plan'] = plan

        if not project_id:
            raise TypeError('Missing required property project_id')
        __props__['project_id'] = project_id

        __props__['public_ipv4_subnet_size'] = public_ipv4_subnet_size

        __props__['storage'] = storage

        __props__['tags'] = tags

        __props__['user_data'] = user_data

        __props__['access_private_ipv4'] = None
        __props__['access_public_ipv4'] = None
        __props__['access_public_ipv6'] = None
        __props__['created'] = None
        __props__['locked'] = None
        __props__['networks'] = None
        __props__['root_password'] = None
        __props__['state'] = None
        __props__['updated'] = None

        super(Device, __self__).__init__(
            'packet:index/device:Device',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

