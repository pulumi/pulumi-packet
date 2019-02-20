# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class SpotMarketRequest(pulumi.CustomResource):
    devices_max: pulumi.Output[int]
    """
    Maximum number devices to be created
    """
    devices_min: pulumi.Output[int]
    """
    Miniumum number devices to be created
    """
    facilities: pulumi.Output[list]
    """
    Facility IDs where devices should be created
    """
    instance_parameters: pulumi.Output[dict]
    """
    Device parameters. See device resource for details
    """
    max_bid_price: pulumi.Output[float]
    """
    Maximum price user is willing to pay per hour per device
    """
    project_id: pulumi.Output[str]
    """
    Project ID
    """
    wait_for_devices: pulumi.Output[bool]
    """
    On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed
    """
    def __init__(__self__, resource_name, opts=None, devices_max=None, devices_min=None, facilities=None, instance_parameters=None, max_bid_price=None, project_id=None, wait_for_devices=None, __name__=None, __opts__=None):
        """
        Provides a Packet Spot Market Request resource to allow you to
        manage spot market requests on your account. https://help.packet.net/en-us/article/20-spot-market 
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] devices_max: Maximum number devices to be created
        :param pulumi.Input[int] devices_min: Miniumum number devices to be created
        :param pulumi.Input[list] facilities: Facility IDs where devices should be created
        :param pulumi.Input[dict] instance_parameters: Device parameters. See device resource for details
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
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if devices_max is None:
            raise TypeError('Missing required property devices_max')
        __props__['devices_max'] = devices_max

        if devices_min is None:
            raise TypeError('Missing required property devices_min')
        __props__['devices_min'] = devices_min

        if facilities is None:
            raise TypeError('Missing required property facilities')
        __props__['facilities'] = facilities

        if instance_parameters is None:
            raise TypeError('Missing required property instance_parameters')
        __props__['instance_parameters'] = instance_parameters

        if max_bid_price is None:
            raise TypeError('Missing required property max_bid_price')
        __props__['max_bid_price'] = max_bid_price

        if project_id is None:
            raise TypeError('Missing required property project_id')
        __props__['project_id'] = project_id

        __props__['wait_for_devices'] = wait_for_devices

        super(SpotMarketRequest, __self__).__init__(
            'packet:index/spotMarketRequest:SpotMarketRequest',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

