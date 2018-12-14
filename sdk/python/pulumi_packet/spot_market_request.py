# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from . import utilities, tables

class SpotMarketRequest(pulumi.CustomResource):
    """
    Provides a Packet Spot Market Request resource to allow you to
    manage spot market requests on your account. https://help.packet.net/en-us/article/20-spot-market 
    """
    def __init__(__self__, __name__, __opts__=None, devices_max=None, devices_min=None, facilities=None, instance_parameters=None, max_bid_price=None, project_id=None, wait_for_devices=None):
        """Create a SpotMarketRequest resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not devices_max:
            raise TypeError('Missing required property devices_max')
        __props__['devices_max'] = devices_max

        if not devices_min:
            raise TypeError('Missing required property devices_min')
        __props__['devices_min'] = devices_min

        if not facilities:
            raise TypeError('Missing required property facilities')
        __props__['facilities'] = facilities

        if not instance_parameters:
            raise TypeError('Missing required property instance_parameters')
        __props__['instance_parameters'] = instance_parameters

        if not max_bid_price:
            raise TypeError('Missing required property max_bid_price')
        __props__['max_bid_price'] = max_bid_price

        if not project_id:
            raise TypeError('Missing required property project_id')
        __props__['project_id'] = project_id

        __props__['wait_for_devices'] = wait_for_devices

        super(SpotMarketRequest, __self__).__init__(
            'packet:index/spotMarketRequest:SpotMarketRequest',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

