# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['SpotMarketRequest']


class SpotMarketRequest(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 devices_max: Optional[pulumi.Input[int]] = None,
                 devices_min: Optional[pulumi.Input[int]] = None,
                 facilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 instance_parameters: Optional[pulumi.Input[pulumi.InputType['SpotMarketRequestInstanceParametersArgs']]] = None,
                 max_bid_price: Optional[pulumi.Input[float]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 wait_for_devices: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Packet Spot Market Request resource to allow you to
        manage spot market requests on your account. For more detail on Spot Market, see [this article in Packet documentaion](https://www.packet.com/developers/docs/getting-started/deployment-options/spot-market/).

        ## Example Usage

        ```python
        import pulumi
        import pulumi_packet as packet

        # Create a spot market request
        req = packet.SpotMarketRequest("req",
            project_id=local["project_id"],
            max_bid_price=0.03,
            facilities=["ewr1"],
            devices_min=1,
            devices_max=1,
            instance_parameters=packet.SpotMarketRequestInstanceParametersArgs(
                hostname="testspot",
                billing_cycle="hourly",
                operating_system="coreos_stable",
                plan="t1.small.x86",
            ))
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] devices_max: Maximum number devices to be created
        :param pulumi.Input[int] devices_min: Miniumum number devices to be created
        :param pulumi.Input[Sequence[pulumi.Input[str]]] facilities: Facility IDs where devices should be created
        :param pulumi.Input[pulumi.InputType['SpotMarketRequestInstanceParametersArgs']] instance_parameters: Device parameters. See device resource for details
        :param pulumi.Input[float] max_bid_price: Maximum price user is willing to pay per hour per device
        :param pulumi.Input[str] project_id: Project ID
        :param pulumi.Input[bool] wait_for_devices: On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed
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
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if devices_max is None:
                raise TypeError("Missing required property 'devices_max'")
            __props__['devices_max'] = devices_max
            if devices_min is None:
                raise TypeError("Missing required property 'devices_min'")
            __props__['devices_min'] = devices_min
            if facilities is None:
                raise TypeError("Missing required property 'facilities'")
            __props__['facilities'] = facilities
            if instance_parameters is None:
                raise TypeError("Missing required property 'instance_parameters'")
            __props__['instance_parameters'] = instance_parameters
            if max_bid_price is None:
                raise TypeError("Missing required property 'max_bid_price'")
            __props__['max_bid_price'] = max_bid_price
            if project_id is None:
                raise TypeError("Missing required property 'project_id'")
            __props__['project_id'] = project_id
            __props__['wait_for_devices'] = wait_for_devices
        super(SpotMarketRequest, __self__).__init__(
            'packet:index/spotMarketRequest:SpotMarketRequest',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            devices_max: Optional[pulumi.Input[int]] = None,
            devices_min: Optional[pulumi.Input[int]] = None,
            facilities: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            instance_parameters: Optional[pulumi.Input[pulumi.InputType['SpotMarketRequestInstanceParametersArgs']]] = None,
            max_bid_price: Optional[pulumi.Input[float]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            wait_for_devices: Optional[pulumi.Input[bool]] = None) -> 'SpotMarketRequest':
        """
        Get an existing SpotMarketRequest resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] devices_max: Maximum number devices to be created
        :param pulumi.Input[int] devices_min: Miniumum number devices to be created
        :param pulumi.Input[Sequence[pulumi.Input[str]]] facilities: Facility IDs where devices should be created
        :param pulumi.Input[pulumi.InputType['SpotMarketRequestInstanceParametersArgs']] instance_parameters: Device parameters. See device resource for details
        :param pulumi.Input[float] max_bid_price: Maximum price user is willing to pay per hour per device
        :param pulumi.Input[str] project_id: Project ID
        :param pulumi.Input[bool] wait_for_devices: On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["devices_max"] = devices_max
        __props__["devices_min"] = devices_min
        __props__["facilities"] = facilities
        __props__["instance_parameters"] = instance_parameters
        __props__["max_bid_price"] = max_bid_price
        __props__["project_id"] = project_id
        __props__["wait_for_devices"] = wait_for_devices
        return SpotMarketRequest(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="devicesMax")
    def devices_max(self) -> pulumi.Output[int]:
        """
        Maximum number devices to be created
        """
        return pulumi.get(self, "devices_max")

    @property
    @pulumi.getter(name="devicesMin")
    def devices_min(self) -> pulumi.Output[int]:
        """
        Miniumum number devices to be created
        """
        return pulumi.get(self, "devices_min")

    @property
    @pulumi.getter
    def facilities(self) -> pulumi.Output[Sequence[str]]:
        """
        Facility IDs where devices should be created
        """
        return pulumi.get(self, "facilities")

    @property
    @pulumi.getter(name="instanceParameters")
    def instance_parameters(self) -> pulumi.Output['outputs.SpotMarketRequestInstanceParameters']:
        """
        Device parameters. See device resource for details
        """
        return pulumi.get(self, "instance_parameters")

    @property
    @pulumi.getter(name="maxBidPrice")
    def max_bid_price(self) -> pulumi.Output[float]:
        """
        Maximum price user is willing to pay per hour per device
        """
        return pulumi.get(self, "max_bid_price")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        Project ID
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="waitForDevices")
    def wait_for_devices(self) -> pulumi.Output[Optional[bool]]:
        """
        On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed
        """
        return pulumi.get(self, "wait_for_devices")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

