// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Packet device resource. This can be used to create,
 * modify, and delete devices.
 * 
 * ~> **Note:** All arguments including the root_password and user_data will be stored in
 *  the raw state as plain-text.
 * [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
 * 
 */
export class Device extends pulumi.CustomResource {
    /**
     * Get an existing Device resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DeviceState, opts?: pulumi.CustomResourceOptions): Device {
        return new Device(name, <any>state, { ...opts, id: id });
    }

    /**
     * The ipv4 private IP assigned to the device
     */
    public /*out*/ readonly accessPrivateIpv4: pulumi.Output<string>;
    /**
     * The ipv4 maintenance IP assigned to the device
     */
    public /*out*/ readonly accessPublicIpv4: pulumi.Output<string>;
    /**
     * The ipv6 maintenance IP assigned to the device
     */
    public /*out*/ readonly accessPublicIpv6: pulumi.Output<string>;
    /**
     * If true, a device with OS `custom_ipxe` will
     * continue to boot via iPXE on reboots.
     */
    public readonly alwaysPxe: pulumi.Output<boolean | undefined>;
    /**
     * monthly or hourly
     */
    public readonly billingCycle: pulumi.Output<string>;
    /**
     * The timestamp for when the device was created
     */
    public /*out*/ readonly created: pulumi.Output<string>;
    /**
     * Description string for the device
     */
    public readonly description: pulumi.Output<string | undefined>;
    /**
     * The facility in which to create the device. To find the facility code, visit [Facilities API docs](https://www.packet.net/developers/api/#facilities), set your API auth token in the top of the page and see JSON from the API response.
     */
    public readonly facility: pulumi.Output<string>;
    /**
     * The id of hardware reservation where you want this device deployed, or `next-available` if you want to pick your next available reservation automatically.
     */
    public readonly hardwareReservationId: pulumi.Output<string>;
    /**
     * The device name
     */
    public readonly hostname: pulumi.Output<string>;
    /**
     * URL pointing to a hosted iPXE script. More
     * information is in the
     * [Custom iPXE](https://help.packet.net/article/26-custom-ipxe)
     * doc.
     */
    public readonly ipxeScriptUrl: pulumi.Output<string | undefined>;
    /**
     * Whether the device is locked
     */
    public /*out*/ readonly locked: pulumi.Output<boolean>;
    /**
     * The device's private and public IP (v4 and v6) network details
     */
    public /*out*/ readonly networks: pulumi.Output<{ address: string, cidr: number, family: number, gateway: string, public: boolean }[]>;
    /**
     * The operating system slug. To find the slug, or visit [Operating Systems API docs](https://www.packet.net/developers/api/#operatingsystems), set your API auth token in the top of the page and see JSON from the API response.
     */
    public readonly operatingSystem: pulumi.Output<string>;
    /**
     * The device plan slug. To find the plan slug, visit [Device plans API docs](https://www.packet.net/developers/api/#plans), set your auth token in the top of the page and see JSON from the API response.
     */
    public readonly plan: pulumi.Output<string>;
    /**
     * The id of the project in which to create the device
     */
    public readonly projectId: pulumi.Output<string>;
    /**
     * Size of allocated subnet, more
     * information is in the
     * [Custom Subnet Size](https://help.packet.net/article/55-custom-subnet-size) doc.
     */
    public readonly publicIpv4SubnetSize: pulumi.Output<number>;
    /**
     * Root password to the server (disabled after 24 hours)
     */
    public /*out*/ readonly rootPassword: pulumi.Output<string>;
    /**
     * The status of the device
     */
    public /*out*/ readonly state: pulumi.Output<string>;
    /**
     * JSON for custom partitioning. Only usable on reserved hardware. More information in in the [Custom Partitioning and RAID](https://help.packet.net/article/61-custom-partitioning-raid) doc.
     */
    public readonly storage: pulumi.Output<string | undefined>;
    /**
     * Tags attached to the device
     */
    public readonly tags: pulumi.Output<string[] | undefined>;
    /**
     * The timestamp for the last time the device was updated
     */
    public /*out*/ readonly updated: pulumi.Output<string>;
    /**
     * A string of the desired User Data for the device.
     */
    public readonly userData: pulumi.Output<string | undefined>;

    /**
     * Create a Device resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DeviceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DeviceArgs | DeviceState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: DeviceState = argsOrState as DeviceState | undefined;
            inputs["accessPrivateIpv4"] = state ? state.accessPrivateIpv4 : undefined;
            inputs["accessPublicIpv4"] = state ? state.accessPublicIpv4 : undefined;
            inputs["accessPublicIpv6"] = state ? state.accessPublicIpv6 : undefined;
            inputs["alwaysPxe"] = state ? state.alwaysPxe : undefined;
            inputs["billingCycle"] = state ? state.billingCycle : undefined;
            inputs["created"] = state ? state.created : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["facility"] = state ? state.facility : undefined;
            inputs["hardwareReservationId"] = state ? state.hardwareReservationId : undefined;
            inputs["hostname"] = state ? state.hostname : undefined;
            inputs["ipxeScriptUrl"] = state ? state.ipxeScriptUrl : undefined;
            inputs["locked"] = state ? state.locked : undefined;
            inputs["networks"] = state ? state.networks : undefined;
            inputs["operatingSystem"] = state ? state.operatingSystem : undefined;
            inputs["plan"] = state ? state.plan : undefined;
            inputs["projectId"] = state ? state.projectId : undefined;
            inputs["publicIpv4SubnetSize"] = state ? state.publicIpv4SubnetSize : undefined;
            inputs["rootPassword"] = state ? state.rootPassword : undefined;
            inputs["state"] = state ? state.state : undefined;
            inputs["storage"] = state ? state.storage : undefined;
            inputs["tags"] = state ? state.tags : undefined;
            inputs["updated"] = state ? state.updated : undefined;
            inputs["userData"] = state ? state.userData : undefined;
        } else {
            const args = argsOrState as DeviceArgs | undefined;
            if (!args || args.billingCycle === undefined) {
                throw new Error("Missing required property 'billingCycle'");
            }
            if (!args || args.facility === undefined) {
                throw new Error("Missing required property 'facility'");
            }
            if (!args || args.hostname === undefined) {
                throw new Error("Missing required property 'hostname'");
            }
            if (!args || args.operatingSystem === undefined) {
                throw new Error("Missing required property 'operatingSystem'");
            }
            if (!args || args.plan === undefined) {
                throw new Error("Missing required property 'plan'");
            }
            if (!args || args.projectId === undefined) {
                throw new Error("Missing required property 'projectId'");
            }
            inputs["alwaysPxe"] = args ? args.alwaysPxe : undefined;
            inputs["billingCycle"] = args ? args.billingCycle : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["facility"] = args ? args.facility : undefined;
            inputs["hardwareReservationId"] = args ? args.hardwareReservationId : undefined;
            inputs["hostname"] = args ? args.hostname : undefined;
            inputs["ipxeScriptUrl"] = args ? args.ipxeScriptUrl : undefined;
            inputs["operatingSystem"] = args ? args.operatingSystem : undefined;
            inputs["plan"] = args ? args.plan : undefined;
            inputs["projectId"] = args ? args.projectId : undefined;
            inputs["publicIpv4SubnetSize"] = args ? args.publicIpv4SubnetSize : undefined;
            inputs["storage"] = args ? args.storage : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["userData"] = args ? args.userData : undefined;
            inputs["accessPrivateIpv4"] = undefined /*out*/;
            inputs["accessPublicIpv4"] = undefined /*out*/;
            inputs["accessPublicIpv6"] = undefined /*out*/;
            inputs["created"] = undefined /*out*/;
            inputs["locked"] = undefined /*out*/;
            inputs["networks"] = undefined /*out*/;
            inputs["rootPassword"] = undefined /*out*/;
            inputs["state"] = undefined /*out*/;
            inputs["updated"] = undefined /*out*/;
        }
        super("packet:index/device:Device", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Device resources.
 */
export interface DeviceState {
    /**
     * The ipv4 private IP assigned to the device
     */
    readonly accessPrivateIpv4?: pulumi.Input<string>;
    /**
     * The ipv4 maintenance IP assigned to the device
     */
    readonly accessPublicIpv4?: pulumi.Input<string>;
    /**
     * The ipv6 maintenance IP assigned to the device
     */
    readonly accessPublicIpv6?: pulumi.Input<string>;
    /**
     * If true, a device with OS `custom_ipxe` will
     * continue to boot via iPXE on reboots.
     */
    readonly alwaysPxe?: pulumi.Input<boolean>;
    /**
     * monthly or hourly
     */
    readonly billingCycle?: pulumi.Input<string>;
    /**
     * The timestamp for when the device was created
     */
    readonly created?: pulumi.Input<string>;
    /**
     * Description string for the device
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The facility in which to create the device. To find the facility code, visit [Facilities API docs](https://www.packet.net/developers/api/#facilities), set your API auth token in the top of the page and see JSON from the API response.
     */
    readonly facility?: pulumi.Input<string>;
    /**
     * The id of hardware reservation where you want this device deployed, or `next-available` if you want to pick your next available reservation automatically.
     */
    readonly hardwareReservationId?: pulumi.Input<string>;
    /**
     * The device name
     */
    readonly hostname?: pulumi.Input<string>;
    /**
     * URL pointing to a hosted iPXE script. More
     * information is in the
     * [Custom iPXE](https://help.packet.net/article/26-custom-ipxe)
     * doc.
     */
    readonly ipxeScriptUrl?: pulumi.Input<string>;
    /**
     * Whether the device is locked
     */
    readonly locked?: pulumi.Input<boolean>;
    /**
     * The device's private and public IP (v4 and v6) network details
     */
    readonly networks?: pulumi.Input<pulumi.Input<{ address?: pulumi.Input<string>, cidr?: pulumi.Input<number>, family?: pulumi.Input<number>, gateway?: pulumi.Input<string>, public?: pulumi.Input<boolean> }>[]>;
    /**
     * The operating system slug. To find the slug, or visit [Operating Systems API docs](https://www.packet.net/developers/api/#operatingsystems), set your API auth token in the top of the page and see JSON from the API response.
     */
    readonly operatingSystem?: pulumi.Input<string>;
    /**
     * The device plan slug. To find the plan slug, visit [Device plans API docs](https://www.packet.net/developers/api/#plans), set your auth token in the top of the page and see JSON from the API response.
     */
    readonly plan?: pulumi.Input<string>;
    /**
     * The id of the project in which to create the device
     */
    readonly projectId?: pulumi.Input<string>;
    /**
     * Size of allocated subnet, more
     * information is in the
     * [Custom Subnet Size](https://help.packet.net/article/55-custom-subnet-size) doc.
     */
    readonly publicIpv4SubnetSize?: pulumi.Input<number>;
    /**
     * Root password to the server (disabled after 24 hours)
     */
    readonly rootPassword?: pulumi.Input<string>;
    /**
     * The status of the device
     */
    readonly state?: pulumi.Input<string>;
    /**
     * JSON for custom partitioning. Only usable on reserved hardware. More information in in the [Custom Partitioning and RAID](https://help.packet.net/article/61-custom-partitioning-raid) doc.
     */
    readonly storage?: pulumi.Input<string>;
    /**
     * Tags attached to the device
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The timestamp for the last time the device was updated
     */
    readonly updated?: pulumi.Input<string>;
    /**
     * A string of the desired User Data for the device.
     */
    readonly userData?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Device resource.
 */
export interface DeviceArgs {
    /**
     * If true, a device with OS `custom_ipxe` will
     * continue to boot via iPXE on reboots.
     */
    readonly alwaysPxe?: pulumi.Input<boolean>;
    /**
     * monthly or hourly
     */
    readonly billingCycle: pulumi.Input<string>;
    /**
     * Description string for the device
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The facility in which to create the device. To find the facility code, visit [Facilities API docs](https://www.packet.net/developers/api/#facilities), set your API auth token in the top of the page and see JSON from the API response.
     */
    readonly facility: pulumi.Input<string>;
    /**
     * The id of hardware reservation where you want this device deployed, or `next-available` if you want to pick your next available reservation automatically.
     */
    readonly hardwareReservationId?: pulumi.Input<string>;
    /**
     * The device name
     */
    readonly hostname: pulumi.Input<string>;
    /**
     * URL pointing to a hosted iPXE script. More
     * information is in the
     * [Custom iPXE](https://help.packet.net/article/26-custom-ipxe)
     * doc.
     */
    readonly ipxeScriptUrl?: pulumi.Input<string>;
    /**
     * The operating system slug. To find the slug, or visit [Operating Systems API docs](https://www.packet.net/developers/api/#operatingsystems), set your API auth token in the top of the page and see JSON from the API response.
     */
    readonly operatingSystem: pulumi.Input<string>;
    /**
     * The device plan slug. To find the plan slug, visit [Device plans API docs](https://www.packet.net/developers/api/#plans), set your auth token in the top of the page and see JSON from the API response.
     */
    readonly plan: pulumi.Input<string>;
    /**
     * The id of the project in which to create the device
     */
    readonly projectId: pulumi.Input<string>;
    /**
     * Size of allocated subnet, more
     * information is in the
     * [Custom Subnet Size](https://help.packet.net/article/55-custom-subnet-size) doc.
     */
    readonly publicIpv4SubnetSize?: pulumi.Input<number>;
    /**
     * JSON for custom partitioning. Only usable on reserved hardware. More information in in the [Custom Partitioning and RAID](https://help.packet.net/article/61-custom-partitioning-raid) doc.
     */
    readonly storage?: pulumi.Input<string>;
    /**
     * Tags attached to the device
     */
    readonly tags?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A string of the desired User Data for the device.
     */
    readonly userData?: pulumi.Input<string>;
}