# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class SshKey(pulumi.CustomResource):
    created: pulumi.Output[str]
    """
    The timestamp for when the SSH key was created
    """
    fingerprint: pulumi.Output[str]
    """
    The fingerprint of the SSH key
    """
    name: pulumi.Output[str]
    """
    The name of the SSH key for identification
    """
    owner_id: pulumi.Output[str]
    """
    The UUID of the Packet API User who owns this key
    """
    public_key: pulumi.Output[str]
    """
    The public key. If this is a file, it
    can be read using the file interpolation function
    """
    updated: pulumi.Output[str]
    """
    The timestamp for the last time the SSH key was updated
    """
    def __init__(__self__, resource_name, opts=None, name=None, public_key=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a resource to manage User SSH keys on your Packet user account. If you create a new device in a project, all the keys of the project's collaborators will be injected to the device.

        The link between User SSH key and device is implicit. If you want to make sure that a key will be copied to a device, you must ensure that the device resource `depends_on` the key resource.



        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] name: The name of the SSH key for identification
        :param pulumi.Input[str] public_key: The public key. If this is a file, it
               can be read using the file interpolation function
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

            if name is None:
                raise TypeError("Missing required property 'name'")
            __props__['name'] = name
            if public_key is None:
                raise TypeError("Missing required property 'public_key'")
            __props__['public_key'] = public_key
            __props__['created'] = None
            __props__['fingerprint'] = None
            __props__['owner_id'] = None
            __props__['updated'] = None
        super(SshKey, __self__).__init__(
            'packet:index/sshKey:SshKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, created=None, fingerprint=None, name=None, owner_id=None, public_key=None, updated=None):
        """
        Get an existing SshKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created: The timestamp for when the SSH key was created
        :param pulumi.Input[str] fingerprint: The fingerprint of the SSH key
        :param pulumi.Input[str] name: The name of the SSH key for identification
        :param pulumi.Input[str] owner_id: The UUID of the Packet API User who owns this key
        :param pulumi.Input[str] public_key: The public key. If this is a file, it
               can be read using the file interpolation function
        :param pulumi.Input[str] updated: The timestamp for the last time the SSH key was updated
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["created"] = created
        __props__["fingerprint"] = fingerprint
        __props__["name"] = name
        __props__["owner_id"] = owner_id
        __props__["public_key"] = public_key
        __props__["updated"] = updated
        return SshKey(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

