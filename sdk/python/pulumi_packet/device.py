# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
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
    deployed_facility: pulumi.Output[str]
    """
    The facility where the device is deployed.
    """
    description: pulumi.Output[str]
    """
    Description string for the device
    """
    facilities: pulumi.Output[list]
    """
    List of facility codes with deployment preferences. Packet API will go through the list and will deploy your device to first facility with free capacity. List items must be facility codes or `any` (a wildcard). To find the facility code, visit [Facilities API docs](https://www.packet.com/developers/api/#facilities), set your API auth token in the top of the page and see JSON from the API response.
    """
    hardware_reservation_id: pulumi.Output[str]
    """
    The id of hardware reservation where you want this device deployed, or `next-available` if you want to pick your next available reservation automatically.
    """
    hostname: pulumi.Output[str]
    """
    The device name
    """
    ip_address_types: pulumi.Output[list]
    """
    A set containing one or more of [`private_ipv4`, `public_ipv4`, `public_ipv6`]. It specifies which IP address types a new device should obtain. If omitted, a created device will obtain all 3 addresses. If you only want private IPv4 address for the new device, pass [`private_ipv4`].
    """
    ipxe_script_url: pulumi.Output[str]
    """
    URL pointing to a hosted iPXE script. More
    information is in the
    [Custom iPXE](https://support.packet.com/kb/articles/custom-ipxe)
    doc.
    """
    locked: pulumi.Output[bool]
    """
    Whether the device is locked
    """
    networks: pulumi.Output[list]
    """
    The device's private and public IP (v4 and v6) network details. When a device is run without any special network configuration, it will have 3 networks: 
    * Public IPv4 at `packet_device.name.network.0`
    * IPv6 at `packet_device.name.network.1`
    * Private IPv4 at `packet_device.name.network.2`
    Elastic addresses then stack by type - an assigned public IPv4 will go after the management public IPv4 (to index 1), and will then shift the indices of the IPv6 and private IPv4. Assigned private IPv4 will go after the management private IPv4 (to the end of the network list).
    The fields of the network attributes are:
    """
    network_type: pulumi.Output[str]
    operating_system: pulumi.Output[str]
    """
    The operating system slug. To find the slug, or visit [Operating Systems API docs](https://www.packet.com/developers/api/#operatingsystems), set your API auth token in the top of the page and see JSON from the API response.
    """
    plan: pulumi.Output[str]
    """
    The device plan slug. To find the plan slug, visit [Device plans API docs](https://www.packet.com/developers/api/#plans), set your auth token in the top of the page and see JSON from the API response.
    """
    ports: pulumi.Output[list]
    """
    Ports assigned to the device
    """
    project_id: pulumi.Output[str]
    """
    The id of the project in which to create the device
    """
    project_ssh_key_ids: pulumi.Output[list]
    """
    Array of IDs of the project SSH keys which should be added to the device. If you omit this, SSH keys of all the members of the parent project will be added to the device. If you specify this array, only the listed project SSH keys will be added. Project SSH keys can be created with the [packet_project_ssh_key][packet_project_ssh_key.html] resource.
    """
    public_ipv4_subnet_size: pulumi.Output[float]
    """
    Size of allocated subnet, more
    information is in the
    [Custom Subnet Size](https://support.packet.com/kb/articles/custom-subnet-size) doc.
    """
    root_password: pulumi.Output[str]
    """
    Root password to the server (disabled after 24 hours)
    """
    ssh_key_ids: pulumi.Output[list]
    """
    List of IDs of SSH keys deployed in the device, can be both user and project SSH keys
    """
    state: pulumi.Output[str]
    """
    The status of the device
    """
    storage: pulumi.Output[str]
    """
    JSON for custom partitioning. Only usable on reserved hardware. More information in in the [Custom Partitioning and RAID](https://support.packet.com/kb/articles/custom-partitioning-raid) doc.
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
    wait_for_reservation_deprovision: pulumi.Output[bool]
    """
    Only used for devices in reserved hardware. If set, the deletion of this device will block until the hardware reservation is marked provisionable (about 4 minutes in August 2019).
    """
    def __init__(__self__, resource_name, opts=None, always_pxe=None, billing_cycle=None, description=None, facilities=None, hardware_reservation_id=None, hostname=None, ip_address_types=None, ipxe_script_url=None, network_type=None, operating_system=None, plan=None, project_id=None, project_ssh_key_ids=None, public_ipv4_subnet_size=None, storage=None, tags=None, user_data=None, wait_for_reservation_deprovision=None, __name__=None, __opts__=None):
        """
        Provides a Packet device resource. This can be used to create,
        modify, and delete devices.
        
        > **Note:** All arguments including the `root_password` and `user_data` will be stored in
         the raw state as plain-text.
        [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] always_pxe: If true, a device with OS `custom_ipxe` will
               continue to boot via iPXE on reboots.
        :param pulumi.Input[str] billing_cycle: monthly or hourly
        :param pulumi.Input[str] description: Description string for the device
        :param pulumi.Input[list] facilities: List of facility codes with deployment preferences. Packet API will go through the list and will deploy your device to first facility with free capacity. List items must be facility codes or `any` (a wildcard). To find the facility code, visit [Facilities API docs](https://www.packet.com/developers/api/#facilities), set your API auth token in the top of the page and see JSON from the API response.
        :param pulumi.Input[str] hardware_reservation_id: The id of hardware reservation where you want this device deployed, or `next-available` if you want to pick your next available reservation automatically.
        :param pulumi.Input[str] hostname: The device name
        :param pulumi.Input[list] ip_address_types: A set containing one or more of [`private_ipv4`, `public_ipv4`, `public_ipv6`]. It specifies which IP address types a new device should obtain. If omitted, a created device will obtain all 3 addresses. If you only want private IPv4 address for the new device, pass [`private_ipv4`].
        :param pulumi.Input[str] ipxe_script_url: URL pointing to a hosted iPXE script. More
               information is in the
               [Custom iPXE](https://support.packet.com/kb/articles/custom-ipxe)
               doc.
        :param pulumi.Input[str] operating_system: The operating system slug. To find the slug, or visit [Operating Systems API docs](https://www.packet.com/developers/api/#operatingsystems), set your API auth token in the top of the page and see JSON from the API response.
        :param pulumi.Input[str] plan: The device plan slug. To find the plan slug, visit [Device plans API docs](https://www.packet.com/developers/api/#plans), set your auth token in the top of the page and see JSON from the API response.
        :param pulumi.Input[str] project_id: The id of the project in which to create the device
        :param pulumi.Input[list] project_ssh_key_ids: Array of IDs of the project SSH keys which should be added to the device. If you omit this, SSH keys of all the members of the parent project will be added to the device. If you specify this array, only the listed project SSH keys will be added. Project SSH keys can be created with the [packet_project_ssh_key][packet_project_ssh_key.html] resource.
        :param pulumi.Input[float] public_ipv4_subnet_size: Size of allocated subnet, more
               information is in the
               [Custom Subnet Size](https://support.packet.com/kb/articles/custom-subnet-size) doc.
        :param pulumi.Input[str] storage: JSON for custom partitioning. Only usable on reserved hardware. More information in in the [Custom Partitioning and RAID](https://support.packet.com/kb/articles/custom-partitioning-raid) doc.
        :param pulumi.Input[list] tags: Tags attached to the device
        :param pulumi.Input[str] user_data: A string of the desired User Data for the device.
        :param pulumi.Input[bool] wait_for_reservation_deprovision: Only used for devices in reserved hardware. If set, the deletion of this device will block until the hardware reservation is marked provisionable (about 4 minutes in August 2019).

        > This content is derived from https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/device.html.markdown.
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

        __props__['always_pxe'] = always_pxe

        if billing_cycle is None:
            raise TypeError("Missing required property 'billing_cycle'")
        __props__['billing_cycle'] = billing_cycle

        __props__['description'] = description

        if facilities is None:
            raise TypeError("Missing required property 'facilities'")
        __props__['facilities'] = facilities

        __props__['hardware_reservation_id'] = hardware_reservation_id

        if hostname is None:
            raise TypeError("Missing required property 'hostname'")
        __props__['hostname'] = hostname

        __props__['ip_address_types'] = ip_address_types

        __props__['ipxe_script_url'] = ipxe_script_url

        __props__['network_type'] = network_type

        if operating_system is None:
            raise TypeError("Missing required property 'operating_system'")
        __props__['operating_system'] = operating_system

        if plan is None:
            raise TypeError("Missing required property 'plan'")
        __props__['plan'] = plan

        if project_id is None:
            raise TypeError("Missing required property 'project_id'")
        __props__['project_id'] = project_id

        __props__['project_ssh_key_ids'] = project_ssh_key_ids

        __props__['public_ipv4_subnet_size'] = public_ipv4_subnet_size

        __props__['storage'] = storage

        __props__['tags'] = tags

        __props__['user_data'] = user_data

        __props__['wait_for_reservation_deprovision'] = wait_for_reservation_deprovision

        __props__['access_private_ipv4'] = None
        __props__['access_public_ipv4'] = None
        __props__['access_public_ipv6'] = None
        __props__['created'] = None
        __props__['deployed_facility'] = None
        __props__['locked'] = None
        __props__['networks'] = None
        __props__['ports'] = None
        __props__['root_password'] = None
        __props__['ssh_key_ids'] = None
        __props__['state'] = None
        __props__['updated'] = None

        if opts is None:
            opts = pulumi.ResourceOptions()
        if opts.version is None:
            opts.version = utilities.get_version()
        super(Device, __self__).__init__(
            'packet:index/device:Device',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

