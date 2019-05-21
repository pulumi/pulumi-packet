// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a resource to attach elastic IP subnets to devices.
 * 
 * To attach an IP subnet from a reserved block to a provisioned device, you must derive a subnet CIDR belonging to
 * one of your reserved blocks in the same project and facility as the target device.
 * 
 * For example, you have reserved IPv4 address block 147.229.10.152/30, you can choose to assign either the whole
 * block as one subnet to a device; or 2 subnets with CIDRs 147.229.10.152/31' and 147.229.10.154/31; or 4 subnets
 * with mask prefix length 32. More about the elastic IP subnets is [here](https://support.packet.com/kb/articles/elastic-ips).
 * 
 * Device and reserved block must be in the same facility.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as packet from "@pulumi/packet";
 * 
 * // Reserve /30 block of max 2 public IPv4 addresses in Parsippany, NJ (ewr1) for myproject
 * const myblock = new packet.ReservedIpBlock("myblock", {
 *     facility: "ewr1",
 *     projectId: local_project_id,
 *     quantity: 2,
 * });
 * // Assign /32 subnet (single address) from reserved block to a device
 * const firstAddressAssignment = new packet.IpAttachment("first_address_assignment", {
 *     cidrNotation: myblock.cidrNotation.apply(cidrNotation => `${(() => { throw "NYI: call to cidrhost"; })()}/32`),
 *     deviceId: packet_device_mydevice.id,
 * });
 * ```
 */
export class IpAttachment extends pulumi.CustomResource {
    /**
     * Get an existing IpAttachment resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: IpAttachmentState, opts?: pulumi.CustomResourceOptions): IpAttachment {
        return new IpAttachment(name, <any>state, { ...opts, id: id });
    }

    public /*out*/ readonly address!: pulumi.Output<string>;
    /**
     * Address family as integer (4 or 6)
     */
    public /*out*/ readonly addressFamily!: pulumi.Output<number>;
    /**
     * length of CIDR prefix of the subnet as integer
     */
    public /*out*/ readonly cidr!: pulumi.Output<number>;
    /**
     * CIDR notation of subnet from block reserved in the same
     * project and facility as the device
     */
    public readonly cidrNotation!: pulumi.Output<string>;
    /**
     * ID of device to which to assign the subnet
     */
    public readonly deviceId!: pulumi.Output<string>;
    /**
     * IP address of gateway for the subnet
     */
    public /*out*/ readonly gateway!: pulumi.Output<string>;
    public /*out*/ readonly global!: pulumi.Output<boolean>;
    public /*out*/ readonly manageable!: pulumi.Output<boolean>;
    public /*out*/ readonly management!: pulumi.Output<boolean>;
    /**
     * Subnet mask in decimal notation, e.g. "255.255.255.0"
     */
    public /*out*/ readonly netmask!: pulumi.Output<string>;
    /**
     * Subnet network address
     */
    public /*out*/ readonly network!: pulumi.Output<string>;
    /**
     * boolean flag whether subnet is reachable from the Internet
     */
    public /*out*/ readonly public!: pulumi.Output<boolean>;

    /**
     * Create a IpAttachment resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: IpAttachmentArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: IpAttachmentArgs | IpAttachmentState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as IpAttachmentState | undefined;
            inputs["address"] = state ? state.address : undefined;
            inputs["addressFamily"] = state ? state.addressFamily : undefined;
            inputs["cidr"] = state ? state.cidr : undefined;
            inputs["cidrNotation"] = state ? state.cidrNotation : undefined;
            inputs["deviceId"] = state ? state.deviceId : undefined;
            inputs["gateway"] = state ? state.gateway : undefined;
            inputs["global"] = state ? state.global : undefined;
            inputs["manageable"] = state ? state.manageable : undefined;
            inputs["management"] = state ? state.management : undefined;
            inputs["netmask"] = state ? state.netmask : undefined;
            inputs["network"] = state ? state.network : undefined;
            inputs["public"] = state ? state.public : undefined;
        } else {
            const args = argsOrState as IpAttachmentArgs | undefined;
            if (!args || args.cidrNotation === undefined) {
                throw new Error("Missing required property 'cidrNotation'");
            }
            if (!args || args.deviceId === undefined) {
                throw new Error("Missing required property 'deviceId'");
            }
            inputs["cidrNotation"] = args ? args.cidrNotation : undefined;
            inputs["deviceId"] = args ? args.deviceId : undefined;
            inputs["address"] = undefined /*out*/;
            inputs["addressFamily"] = undefined /*out*/;
            inputs["cidr"] = undefined /*out*/;
            inputs["gateway"] = undefined /*out*/;
            inputs["global"] = undefined /*out*/;
            inputs["manageable"] = undefined /*out*/;
            inputs["management"] = undefined /*out*/;
            inputs["netmask"] = undefined /*out*/;
            inputs["network"] = undefined /*out*/;
            inputs["public"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super("packet:index/ipAttachment:IpAttachment", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering IpAttachment resources.
 */
export interface IpAttachmentState {
    readonly address?: pulumi.Input<string>;
    /**
     * Address family as integer (4 or 6)
     */
    readonly addressFamily?: pulumi.Input<number>;
    /**
     * length of CIDR prefix of the subnet as integer
     */
    readonly cidr?: pulumi.Input<number>;
    /**
     * CIDR notation of subnet from block reserved in the same
     * project and facility as the device
     */
    readonly cidrNotation?: pulumi.Input<string>;
    /**
     * ID of device to which to assign the subnet
     */
    readonly deviceId?: pulumi.Input<string>;
    /**
     * IP address of gateway for the subnet
     */
    readonly gateway?: pulumi.Input<string>;
    readonly global?: pulumi.Input<boolean>;
    readonly manageable?: pulumi.Input<boolean>;
    readonly management?: pulumi.Input<boolean>;
    /**
     * Subnet mask in decimal notation, e.g. "255.255.255.0"
     */
    readonly netmask?: pulumi.Input<string>;
    /**
     * Subnet network address
     */
    readonly network?: pulumi.Input<string>;
    /**
     * boolean flag whether subnet is reachable from the Internet
     */
    readonly public?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a IpAttachment resource.
 */
export interface IpAttachmentArgs {
    /**
     * CIDR notation of subnet from block reserved in the same
     * project and facility as the device
     */
    readonly cidrNotation: pulumi.Input<string>;
    /**
     * ID of device to which to assign the subnet
     */
    readonly deviceId: pulumi.Input<string>;
}
