# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from . import utilities, tables

class Device(pulumi.CustomResource):
    access_private_ipv4: pulumi.Output[str]
    """
    The ipv4 private IP assigned to the device
    """
    access_public_ipv4: pulumi.Output[str]
    """
    The ipv4 maintenance IP assigned to the device
    """
    access_public_ipv6: pulumi.Output[str]
    """
    The ipv6 maintenance IP assigned to the device
    """
    always_pxe: pulumi.Output[bool]
    """
    If true, a device with OS `custom_ipxe` will
    continue to boot via iPXE on reboots.
    """
    billing_cycle: pulumi.Output[str]
    """
    monthly or hourly
    """
    created: pulumi.Output[str]
    """
    The timestamp for when the device was created
    """
    description: pulumi.Output[str]
    """
    Description string for the device
    """
    facility: pulumi.Output[str]
    """
    The facility in which to create the device. To find the facility code, visit [Facilities API docs](https://www.packet.net/developers/api/#facilities), set your API auth token in the top of the page and see JSON from the API response.
    """
    hardware_reservation_id: pulumi.Output[str]
    """
    The id of hardware reservation where you want this device deployed, or `next-available` if you want to pick your next available reservation automatically.
    """
    hostname: pulumi.Output[str]
    """
    The device name
    """
    ipxe_script_url: pulumi.Output[str]
    """
    URL pointing to a hosted iPXE script. More
    information is in the
    [Custom iPXE](https://help.packet.net/article/26-custom-ipxe)
    doc.
    """
    locked: pulumi.Output[bool]
    """
    Whether the device is locked
    """
    networks: pulumi.Output[list]
    """
    The device's private and public IP (v4 and v6) network details
    """
    operating_system: pulumi.Output[str]
    """
    The operating system slug. To find the slug, or visit [Operating Systems API docs](https://www.packet.net/developers/api/#operatingsystems), set your API auth token in the top of the page and see JSON from the API response.
    """
    plan: pulumi.Output[str]
    """
    The device plan slug. To find the plan slug, visit [Device plans API docs](https://www.packet.net/developers/api/#plans), set your auth token in the top of the page and see JSON from the API response.
    """
    project_id: pulumi.Output[str]
    """
    The id of the project in which to create the device
    """
    public_ipv4_subnet_size: pulumi.Output[int]
    """
    Size of allocated subnet, more
    information is in the
    [Custom Subnet Size](https://help.packet.net/article/55-custom-subnet-size) doc.
    """
    root_password: pulumi.Output[str]
    """
    Root password to the server (disabled after 24 hours)
    """
    state: pulumi.Output[str]
    """
    The status of the device
    """
    storage: pulumi.Output[str]
    """
    JSON for custom partitioning. Only usable on reserved hardware. More information in in the [Custom Partitioning and RAID](https://help.packet.net/article/61-custom-partitioning-raid) doc.
    """
    tags: pulumi.Output[list]
    """
    Tags attached to the device
    """
    updated: pulumi.Output[str]
    """
    The timestamp for the last time the device was updated
    """
    user_data: pulumi.Output[str]
    """
    A string of the desired User Data for the device.
    """
    def __init__(__self__, __name__, __opts__=None, always_pxe=None, billing_cycle=None, description=None, facility=None, hardware_reservation_id=None, hostname=None, ipxe_script_url=None, operating_system=None, plan=None, project_id=None, public_ipv4_subnet_size=None, storage=None, tags=None, user_data=None):
        """
        Provides a Packet device resource. This can be used to create,
        modify, and delete devices.
        
        > **Note:** All arguments including the root_password and user_data will be stored in
         the raw state as plain-text.
        [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
        
        
        
        :param str __name__: The name of the resource.
        :param pulumi.ResourceOptions __opts__: Options for the resource.
        :param pulumi.Input[bool] always_pxe: If true, a device with OS `custom_ipxe` will
               continue to boot via iPXE on reboots.
        :param pulumi.Input[str] billing_cycle: monthly or hourly
        :param pulumi.Input[str] description: Description string for the device
        :param pulumi.Input[str] facility: The facility in which to create the device. To find the facility code, visit [Facilities API docs](https://www.packet.net/developers/api/#facilities), set your API auth token in the top of the page and see JSON from the API response.
        :param pulumi.Input[str] hardware_reservation_id: The id of hardware reservation where you want this device deployed, or `next-available` if you want to pick your next available reservation automatically.
        :param pulumi.Input[str] hostname: The device name
        :param pulumi.Input[str] ipxe_script_url: URL pointing to a hosted iPXE script. More
               information is in the
               [Custom iPXE](https://help.packet.net/article/26-custom-ipxe)
               doc.
        :param pulumi.Input[str] operating_system: The operating system slug. To find the slug, or visit [Operating Systems API docs](https://www.packet.net/developers/api/#operatingsystems), set your API auth token in the top of the page and see JSON from the API response.
        :param pulumi.Input[str] plan: The device plan slug. To find the plan slug, visit [Device plans API docs](https://www.packet.net/developers/api/#plans), set your auth token in the top of the page and see JSON from the API response.
        :param pulumi.Input[str] project_id: The id of the project in which to create the device
        :param pulumi.Input[int] public_ipv4_subnet_size: Size of allocated subnet, more
               information is in the
               [Custom Subnet Size](https://help.packet.net/article/55-custom-subnet-size) doc.
        :param pulumi.Input[str] storage: JSON for custom partitioning. Only usable on reserved hardware. More information in in the [Custom Partitioning and RAID](https://help.packet.net/article/61-custom-partitioning-raid) doc.
        :param pulumi.Input[list] tags: Tags attached to the device
        :param pulumi.Input[str] user_data: A string of the desired User Data for the device.
        """
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

