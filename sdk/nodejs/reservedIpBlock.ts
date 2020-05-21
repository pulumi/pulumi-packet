// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

import {Facility, IpBlockType} from "./index";

/**
 * Provides a resource to create and manage blocks of reserved IP addresses in a project.
 *
 * When a user provisions first device in a facility, Packet API automatically allocates IPv6/56 and private IPv4/25 blocks.
 * The new device then gets IPv6 and private IPv4 addresses from those block. It also gets a public IPv4/31 address.
 * Every new device in the project and facility will automatically get IPv6 and private IPv4 addresses from these pre-allocated blocks.
 * The IPv6 and private IPv4 blocks can't be created, only imported. With this resource, it's possible to create either public IPv4 blocks or global IPv4 blocks.
 *
 * Public blocks are allocated in a facility. Addresses from public blocks can only be assigned to devices in the facility. Public blocks can have mask from /24 (256 addresses) to /32 (1 address). If you create public block with this resource, you must fill the facility argmument.
 *
 * Addresses from global blocks can be assigned in any facility. Global blocks can have mask from /30 (4 addresses), to /32 (1 address). If you create global block with this resource, you must specify type = "globalIpv4" and you must omit the facility argument.
 *
 * Once IP block is allocated or imported, an address from it can be assigned to device with the `packet..IpAttachment` resource.
 *
 */
export class ReservedIpBlock extends pulumi.CustomResource {
    /**
     * Get an existing ReservedIpBlock resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ReservedIpBlockState, opts?: pulumi.CustomResourceOptions): ReservedIpBlock {
        return new ReservedIpBlock(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'packet:index/reservedIpBlock:ReservedIpBlock';

    /**
     * Returns true if the given object is an instance of ReservedIpBlock.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ReservedIpBlock {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ReservedIpBlock.__pulumiType;
    }

    public /*out*/ readonly address!: pulumi.Output<string>;
    /**
     * Address family as integer (4 or 6)
     */
    public /*out*/ readonly addressFamily!: pulumi.Output<number>;
    /**
     * length of CIDR prefix of the block as integer
     */
    public /*out*/ readonly cidr!: pulumi.Output<number>;
    /**
     * Address and mask in CIDR notation, e.g. "147.229.15.30/31"
     */
    public /*out*/ readonly cidrNotation!: pulumi.Output<string>;
    /**
     * Arbitrary description
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Facility where to allocate the public IP address block, makes sense only for type==public_ipv4, must be empty for type==global_ipv4
     */
    public readonly facility!: pulumi.Output<Facility | undefined>;
    public /*out*/ readonly gateway!: pulumi.Output<string>;
    /**
     * boolean flag whether addresses from a block are global (i.e. can be assigned in any facility)
     */
    public /*out*/ readonly global!: pulumi.Output<boolean>;
    public /*out*/ readonly manageable!: pulumi.Output<boolean>;
    public /*out*/ readonly management!: pulumi.Output<boolean>;
    /**
     * Mask in decimal notation, e.g. "255.255.255.0"
     */
    public /*out*/ readonly netmask!: pulumi.Output<string>;
    /**
     * Network IP address portion of the block specification
     */
    public /*out*/ readonly network!: pulumi.Output<string>;
    /**
     * The packet project ID where to allocate the address block
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * boolean flag whether addresses from a block are public
     */
    public /*out*/ readonly public!: pulumi.Output<boolean>;
    /**
     * The number of allocated /32 addresses, a power of 2
     */
    public readonly quantity!: pulumi.Output<number>;
    /**
     * Either "globalIpv4" or "publicIpv4", defaults to "publicIpv4" for backward compatibility
     */
    public readonly type!: pulumi.Output<IpBlockType | undefined>;

    /**
     * Create a ReservedIpBlock resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ReservedIpBlockArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ReservedIpBlockArgs | ReservedIpBlockState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as ReservedIpBlockState | undefined;
            inputs["address"] = state ? state.address : undefined;
            inputs["addressFamily"] = state ? state.addressFamily : undefined;
            inputs["cidr"] = state ? state.cidr : undefined;
            inputs["cidrNotation"] = state ? state.cidrNotation : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["facility"] = state ? state.facility : undefined;
            inputs["gateway"] = state ? state.gateway : undefined;
            inputs["global"] = state ? state.global : undefined;
            inputs["manageable"] = state ? state.manageable : undefined;
            inputs["management"] = state ? state.management : undefined;
            inputs["netmask"] = state ? state.netmask : undefined;
            inputs["network"] = state ? state.network : undefined;
            inputs["projectId"] = state ? state.projectId : undefined;
            inputs["public"] = state ? state.public : undefined;
            inputs["quantity"] = state ? state.quantity : undefined;
            inputs["type"] = state ? state.type : undefined;
        } else {
            const args = argsOrState as ReservedIpBlockArgs | undefined;
            if (!args || args.projectId === undefined) {
                throw new Error("Missing required property 'projectId'");
            }
            if (!args || args.quantity === undefined) {
                throw new Error("Missing required property 'quantity'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["facility"] = args ? args.facility : undefined;
            inputs["projectId"] = args ? args.projectId : undefined;
            inputs["quantity"] = args ? args.quantity : undefined;
            inputs["type"] = args ? args.type : undefined;
            inputs["address"] = undefined /*out*/;
            inputs["addressFamily"] = undefined /*out*/;
            inputs["cidr"] = undefined /*out*/;
            inputs["cidrNotation"] = undefined /*out*/;
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
        super(ReservedIpBlock.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ReservedIpBlock resources.
 */
export interface ReservedIpBlockState {
    readonly address?: pulumi.Input<string>;
    /**
     * Address family as integer (4 or 6)
     */
    readonly addressFamily?: pulumi.Input<number>;
    /**
     * length of CIDR prefix of the block as integer
     */
    readonly cidr?: pulumi.Input<number>;
    /**
     * Address and mask in CIDR notation, e.g. "147.229.15.30/31"
     */
    readonly cidrNotation?: pulumi.Input<string>;
    /**
     * Arbitrary description
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Facility where to allocate the public IP address block, makes sense only for type==public_ipv4, must be empty for type==global_ipv4
     */
    readonly facility?: pulumi.Input<Facility>;
    readonly gateway?: pulumi.Input<string>;
    /**
     * boolean flag whether addresses from a block are global (i.e. can be assigned in any facility)
     */
    readonly global?: pulumi.Input<boolean>;
    readonly manageable?: pulumi.Input<boolean>;
    readonly management?: pulumi.Input<boolean>;
    /**
     * Mask in decimal notation, e.g. "255.255.255.0"
     */
    readonly netmask?: pulumi.Input<string>;
    /**
     * Network IP address portion of the block specification
     */
    readonly network?: pulumi.Input<string>;
    /**
     * The packet project ID where to allocate the address block
     */
    readonly projectId?: pulumi.Input<string>;
    /**
     * boolean flag whether addresses from a block are public
     */
    readonly public?: pulumi.Input<boolean>;
    /**
     * The number of allocated /32 addresses, a power of 2
     */
    readonly quantity?: pulumi.Input<number>;
    /**
     * Either "globalIpv4" or "publicIpv4", defaults to "publicIpv4" for backward compatibility
     */
    readonly type?: pulumi.Input<IpBlockType>;
}

/**
 * The set of arguments for constructing a ReservedIpBlock resource.
 */
export interface ReservedIpBlockArgs {
    /**
     * Arbitrary description
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Facility where to allocate the public IP address block, makes sense only for type==public_ipv4, must be empty for type==global_ipv4
     */
    readonly facility?: pulumi.Input<Facility>;
    /**
     * The packet project ID where to allocate the address block
     */
    readonly projectId: pulumi.Input<string>;
    /**
     * The number of allocated /32 addresses, a power of 2
     */
    readonly quantity: pulumi.Input<number>;
    /**
     * Either "globalIpv4" or "publicIpv4", defaults to "publicIpv4" for backward compatibility
     */
    readonly type?: pulumi.Input<IpBlockType>;
}
