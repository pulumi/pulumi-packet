# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
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
    List of facility codes with deployment preferences. Packet API will go through the list and will deploy your device to first facility with free capacity. List items must be facility codes or `any` (a wildcard). To find the facility code, visit [Facilities API docs](https://www.packet.com/developers/api/facilities), set your API auth token in the top of the page and see JSON from the API response.
    """
    force_detach_volumes: pulumi.Output[bool]
    """
    Delete device even if it has volumes attached. Only applies for destroy action.
    """
    hardware_reservation_id: pulumi.Output[str]
    """
    The ID of hardware reservation which this device occupies
    * `hostname`- The hostname of the device
    """
    hostname: pulumi.Output[str]
    """
    The device name
    """
    ip_addresses: pulumi.Output[list]
    """
    A list of IP address types for the device (structure is documented below).

      * `cidr` (`float`) - CIDR suffix for IP address block to be assigned, i.e. amount of addresses.
      * `reservationIds` (`list`)
      * `type` (`str`) - One of [`private_ipv4`, `public_ipv4`, `public_ipv6`]
    """
    ipxe_script_url: pulumi.Output[str]
    """
    URL pointing to a hosted iPXE script. More
    information is in the
    [Custom iPXE](https://www.packet.com/developers/docs/servers/operating-systems/custom-ipxe/)
    doc.
    """
    locked: pulumi.Output[bool]
    """
    Whether the device is locked
    """
    network_type: pulumi.Output[str]
    networks: pulumi.Output[list]
    """
    The device's private and public IP (v4 and v6) network details. When a device is run without any special network configuration, it will have 3 networks: 
    * Public IPv4 at `packet_device.name.network.0`
    * IPv6 at `packet_device.name.network.1`
    * Private IPv4 at `packet_device.name.network.2`
    Elastic addresses then stack by type - an assigned public IPv4 will go after the management public IPv4 (to index 1), and will then shift the indices of the IPv6 and private IPv4. Assigned private IPv4 will go after the management private IPv4 (to the end of the network list).
    The fields of the network attributes are:

      * `address` (`str`) - IPv4 or IPv6 address string
      * `cidr` (`float`) - CIDR suffix for IP address block to be assigned, i.e. amount of addresses.
      * `family` (`float`) - IP version - "4" or "6"
      * `gateway` (`str`) - address of router
      * `public` (`bool`) - whether the address is routable from the Internet
    """
    operating_system: pulumi.Output[str]
    """
    The operating system slug. To find the slug, or visit [Operating Systems API docs](https://www.packet.com/developers/api/operatingsystems), set your API auth token in the top of the page and see JSON from the API response.
    """
    plan: pulumi.Output[str]
    """
    The device plan slug. To find the plan slug, visit [Device plans API docs](https://www.packet.com/developers/api/plans), set your auth token in the top of the page and see JSON from the API response.
    """
    ports: pulumi.Output[list]
    """
    Ports assigned to the device

      * `bonded` (`bool`) - Whether this port is part of a bond in bonded network setup
        * `project_id`- The ID of the project the device belongs to
      * `id` (`str`) - ID of the port
      * `mac` (`str`) - MAC address assigned to the port
      * `name` (`str`) - Name of the port (e.g. `eth0`, or `bond0`)
      * `type` (`str`) - One of [`private_ipv4`, `public_ipv4`, `public_ipv6`]
    """
    project_id: pulumi.Output[str]
    """
    The ID of the project in which to create the device
    """
    project_ssh_key_ids: pulumi.Output[list]
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
    JSON for custom partitioning. Only usable on reserved hardware. More information in in the [Custom Partitioning and RAID](https://www.packet.com/developers/docs/servers/key-features/cpr/) doc.
    * Please note that the disks.partitions.size attribute must be a string, not an integer. It can be a number string, or size notation string, e.g. "4G" or "8M" (for gigabytes and megabytes).
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
    def __init__(__self__, resource_name, opts=None, always_pxe=None, billing_cycle=None, description=None, facilities=None, force_detach_volumes=None, hardware_reservation_id=None, hostname=None, ip_addresses=None, ipxe_script_url=None, network_type=None, operating_system=None, plan=None, project_id=None, project_ssh_key_ids=None, storage=None, tags=None, user_data=None, wait_for_reservation_deprovision=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a Packet device resource. This can be used to create,
        modify, and delete devices.

        > **Note:** All arguments including the `root_password` and `user_data` will be stored in
         the raw state as plain-text.
        [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).

        ## Example Usage

        Create a device and add it to cool_project

        ```python
        import pulumi
        import pulumi_packet as packet

        web1 = packet.Device("web1",
            hostname="tf.coreos2",
            plan="t1.small.x86",
            facilities=["ewr1"],
            operating_system="coreos_stable",
            billing_cycle="hourly",
            project_id=local["project_id"])
        ```

        Same as above, but boot via iPXE initially, using the Ignition Provider for provisioning

        ```python
        import pulumi
        import pulumi_packet as packet

        pxe1 = packet.Device("pxe1",
            hostname="tf.coreos2-pxe",
            plan="t1.small.x86",
            facilities=["ewr1"],
            operating_system="custom_ipxe",
            billing_cycle="hourly",
            project_id=local["project_id"],
            ipxe_script_url="https://rawgit.com/cloudnativelabs/pxe/master/packet/coreos-stable-packet.ipxe",
            always_pxe="false",
            user_data=data["ignition_config"]["example"]["rendered"])
        ```

        Create a device without a public IP address, with only a /30 private IPv4 subnet (4 IP addresses)

        ```python
        import pulumi
        import pulumi_packet as packet

        web1 = packet.Device("web1",
            hostname="tf.coreos2",
            plan="t1.small.x86",
            facilities=["ewr1"],
            operating_system="coreos_stable",
            billing_cycle="hourly",
            project_id=local["project_id"],
            ip_addresses=[{
                "type": "private_ipv4",
                "cidr": 30,
            }])
        ```

        Deploy device on next-available reserved hardware and do custom partitioning.

        ```python
        import pulumi
        import pulumi_packet as packet

        web1 = packet.Device("web1",
            hostname="tftest",
            plan="t1.small.x86",
            facilities=["sjc1"],
            operating_system="ubuntu_16_04",
            billing_cycle="hourly",
            project_id=local["project_id"],
            hardware_reservation_id="next-available",
            storage=\"\"\"{
          "disks": [
            {
              "device": "/dev/sda",
              "wipeTable": true,
              "partitions": [
                {
                  "label": "BIOS",
                  "number": 1,
                  "size": "4096"
                },
                {
                  "label": "SWAP",
                  "number": 2,
                  "size": "3993600"
                },
                {
                  "label": "ROOT",
                  "number": 3,
                  "size": "0"
                }
              ]
            }
          ],
          "filesystems": [
            {
              "mount": {
                "device": "/dev/sda3",
                "format": "ext4",
                "point": "/",
                "create": {
                  "options": [
                    "-L",
                    "ROOT"
                  ]
                }
              }
            },
            {
              "mount": {
                "device": "/dev/sda2",
                "format": "swap",
                "point": "none",
                "create": {
                  "options": [
                    "-L",
                    "SWAP"
                  ]
                }
              }
            }
          ]
        }
        \"\"\")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] always_pxe: If true, a device with OS `custom_ipxe` will
               continue to boot via iPXE on reboots.
        :param pulumi.Input[str] billing_cycle: monthly or hourly
        :param pulumi.Input[str] description: Description string for the device
        :param pulumi.Input[list] facilities: List of facility codes with deployment preferences. Packet API will go through the list and will deploy your device to first facility with free capacity. List items must be facility codes or `any` (a wildcard). To find the facility code, visit [Facilities API docs](https://www.packet.com/developers/api/facilities), set your API auth token in the top of the page and see JSON from the API response.
        :param pulumi.Input[bool] force_detach_volumes: Delete device even if it has volumes attached. Only applies for destroy action.
        :param pulumi.Input[str] hardware_reservation_id: The ID of hardware reservation which this device occupies
               * `hostname`- The hostname of the device
        :param pulumi.Input[str] hostname: The device name
        :param pulumi.Input[list] ip_addresses: A list of IP address types for the device (structure is documented below).
        :param pulumi.Input[str] ipxe_script_url: URL pointing to a hosted iPXE script. More
               information is in the
               [Custom iPXE](https://www.packet.com/developers/docs/servers/operating-systems/custom-ipxe/)
               doc.
        :param pulumi.Input[str] operating_system: The operating system slug. To find the slug, or visit [Operating Systems API docs](https://www.packet.com/developers/api/operatingsystems), set your API auth token in the top of the page and see JSON from the API response.
        :param pulumi.Input[str] plan: The device plan slug. To find the plan slug, visit [Device plans API docs](https://www.packet.com/developers/api/plans), set your auth token in the top of the page and see JSON from the API response.
        :param pulumi.Input[str] project_id: The ID of the project in which to create the device
        :param pulumi.Input[str] storage: JSON for custom partitioning. Only usable on reserved hardware. More information in in the [Custom Partitioning and RAID](https://www.packet.com/developers/docs/servers/key-features/cpr/) doc.
               * Please note that the disks.partitions.size attribute must be a string, not an integer. It can be a number string, or size notation string, e.g. "4G" or "8M" (for gigabytes and megabytes).
        :param pulumi.Input[list] tags: Tags attached to the device
        :param pulumi.Input[str] user_data: A string of the desired User Data for the device.
        :param pulumi.Input[bool] wait_for_reservation_deprovision: Only used for devices in reserved hardware. If set, the deletion of this device will block until the hardware reservation is marked provisionable (about 4 minutes in August 2019).

        The **ip_addresses** object supports the following:

          * `cidr` (`pulumi.Input[float]`) - CIDR suffix for IP address block to be assigned, i.e. amount of addresses.
          * `reservationIds` (`pulumi.Input[list]`)
          * `type` (`pulumi.Input[str]`) - One of [`private_ipv4`, `public_ipv4`, `public_ipv6`]
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

            __props__['always_pxe'] = always_pxe
            if billing_cycle is None:
                raise TypeError("Missing required property 'billing_cycle'")
            __props__['billing_cycle'] = billing_cycle
            __props__['description'] = description
            if facilities is None:
                raise TypeError("Missing required property 'facilities'")
            __props__['facilities'] = facilities
            __props__['force_detach_volumes'] = force_detach_volumes
            __props__['hardware_reservation_id'] = hardware_reservation_id
            if hostname is None:
                raise TypeError("Missing required property 'hostname'")
            __props__['hostname'] = hostname
            __props__['ip_addresses'] = ip_addresses
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
        super(Device, __self__).__init__(
            'packet:index/device:Device',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, access_private_ipv4=None, access_public_ipv4=None, access_public_ipv6=None, always_pxe=None, billing_cycle=None, created=None, deployed_facility=None, description=None, facilities=None, force_detach_volumes=None, hardware_reservation_id=None, hostname=None, ip_addresses=None, ipxe_script_url=None, locked=None, network_type=None, networks=None, operating_system=None, plan=None, ports=None, project_id=None, project_ssh_key_ids=None, root_password=None, ssh_key_ids=None, state=None, storage=None, tags=None, updated=None, user_data=None, wait_for_reservation_deprovision=None):
        """
        Get an existing Device resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_private_ipv4: The ipv4 private IP assigned to the device
        :param pulumi.Input[str] access_public_ipv4: The ipv4 maintenance IP assigned to the device
        :param pulumi.Input[str] access_public_ipv6: The ipv6 maintenance IP assigned to the device
        :param pulumi.Input[bool] always_pxe: If true, a device with OS `custom_ipxe` will
               continue to boot via iPXE on reboots.
        :param pulumi.Input[str] billing_cycle: monthly or hourly
        :param pulumi.Input[str] created: The timestamp for when the device was created
        :param pulumi.Input[str] deployed_facility: The facility where the device is deployed.
        :param pulumi.Input[str] description: Description string for the device
        :param pulumi.Input[list] facilities: List of facility codes with deployment preferences. Packet API will go through the list and will deploy your device to first facility with free capacity. List items must be facility codes or `any` (a wildcard). To find the facility code, visit [Facilities API docs](https://www.packet.com/developers/api/facilities), set your API auth token in the top of the page and see JSON from the API response.
        :param pulumi.Input[bool] force_detach_volumes: Delete device even if it has volumes attached. Only applies for destroy action.
        :param pulumi.Input[str] hardware_reservation_id: The ID of hardware reservation which this device occupies
               * `hostname`- The hostname of the device
        :param pulumi.Input[str] hostname: The device name
        :param pulumi.Input[list] ip_addresses: A list of IP address types for the device (structure is documented below).
        :param pulumi.Input[str] ipxe_script_url: URL pointing to a hosted iPXE script. More
               information is in the
               [Custom iPXE](https://www.packet.com/developers/docs/servers/operating-systems/custom-ipxe/)
               doc.
        :param pulumi.Input[bool] locked: Whether the device is locked
        :param pulumi.Input[list] networks: The device's private and public IP (v4 and v6) network details. When a device is run without any special network configuration, it will have 3 networks: 
               * Public IPv4 at `packet_device.name.network.0`
               * IPv6 at `packet_device.name.network.1`
               * Private IPv4 at `packet_device.name.network.2`
               Elastic addresses then stack by type - an assigned public IPv4 will go after the management public IPv4 (to index 1), and will then shift the indices of the IPv6 and private IPv4. Assigned private IPv4 will go after the management private IPv4 (to the end of the network list).
               The fields of the network attributes are:
        :param pulumi.Input[str] operating_system: The operating system slug. To find the slug, or visit [Operating Systems API docs](https://www.packet.com/developers/api/operatingsystems), set your API auth token in the top of the page and see JSON from the API response.
        :param pulumi.Input[str] plan: The device plan slug. To find the plan slug, visit [Device plans API docs](https://www.packet.com/developers/api/plans), set your auth token in the top of the page and see JSON from the API response.
        :param pulumi.Input[list] ports: Ports assigned to the device
        :param pulumi.Input[str] project_id: The ID of the project in which to create the device
        :param pulumi.Input[str] root_password: Root password to the server (disabled after 24 hours)
        :param pulumi.Input[list] ssh_key_ids: List of IDs of SSH keys deployed in the device, can be both user and project SSH keys
        :param pulumi.Input[str] state: The status of the device
        :param pulumi.Input[str] storage: JSON for custom partitioning. Only usable on reserved hardware. More information in in the [Custom Partitioning and RAID](https://www.packet.com/developers/docs/servers/key-features/cpr/) doc.
               * Please note that the disks.partitions.size attribute must be a string, not an integer. It can be a number string, or size notation string, e.g. "4G" or "8M" (for gigabytes and megabytes).
        :param pulumi.Input[list] tags: Tags attached to the device
        :param pulumi.Input[str] updated: The timestamp for the last time the device was updated
        :param pulumi.Input[str] user_data: A string of the desired User Data for the device.
        :param pulumi.Input[bool] wait_for_reservation_deprovision: Only used for devices in reserved hardware. If set, the deletion of this device will block until the hardware reservation is marked provisionable (about 4 minutes in August 2019).

        The **ip_addresses** object supports the following:

          * `cidr` (`pulumi.Input[float]`) - CIDR suffix for IP address block to be assigned, i.e. amount of addresses.
          * `reservationIds` (`pulumi.Input[list]`)
          * `type` (`pulumi.Input[str]`) - One of [`private_ipv4`, `public_ipv4`, `public_ipv6`]

        The **networks** object supports the following:

          * `address` (`pulumi.Input[str]`) - IPv4 or IPv6 address string
          * `cidr` (`pulumi.Input[float]`) - CIDR suffix for IP address block to be assigned, i.e. amount of addresses.
          * `family` (`pulumi.Input[float]`) - IP version - "4" or "6"
          * `gateway` (`pulumi.Input[str]`) - address of router
          * `public` (`pulumi.Input[bool]`) - whether the address is routable from the Internet

        The **ports** object supports the following:

          * `bonded` (`pulumi.Input[bool]`) - Whether this port is part of a bond in bonded network setup
            * `project_id`- The ID of the project the device belongs to
          * `id` (`pulumi.Input[str]`) - ID of the port
          * `mac` (`pulumi.Input[str]`) - MAC address assigned to the port
          * `name` (`pulumi.Input[str]`) - Name of the port (e.g. `eth0`, or `bond0`)
          * `type` (`pulumi.Input[str]`) - One of [`private_ipv4`, `public_ipv4`, `public_ipv6`]
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access_private_ipv4"] = access_private_ipv4
        __props__["access_public_ipv4"] = access_public_ipv4
        __props__["access_public_ipv6"] = access_public_ipv6
        __props__["always_pxe"] = always_pxe
        __props__["billing_cycle"] = billing_cycle
        __props__["created"] = created
        __props__["deployed_facility"] = deployed_facility
        __props__["description"] = description
        __props__["facilities"] = facilities
        __props__["force_detach_volumes"] = force_detach_volumes
        __props__["hardware_reservation_id"] = hardware_reservation_id
        __props__["hostname"] = hostname
        __props__["ip_addresses"] = ip_addresses
        __props__["ipxe_script_url"] = ipxe_script_url
        __props__["locked"] = locked
        __props__["network_type"] = network_type
        __props__["networks"] = networks
        __props__["operating_system"] = operating_system
        __props__["plan"] = plan
        __props__["ports"] = ports
        __props__["project_id"] = project_id
        __props__["project_ssh_key_ids"] = project_ssh_key_ids
        __props__["root_password"] = root_password
        __props__["ssh_key_ids"] = ssh_key_ids
        __props__["state"] = state
        __props__["storage"] = storage
        __props__["tags"] = tags
        __props__["updated"] = updated
        __props__["user_data"] = user_data
        __props__["wait_for_reservation_deprovision"] = wait_for_reservation_deprovision
        return Device(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
