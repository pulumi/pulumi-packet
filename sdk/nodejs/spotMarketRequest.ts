// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Provides a Packet Spot Market Request resource to allow you to
 * manage spot market requests on your account. For more detail on Spot Market, see [this article in Packet documentaion](https://www.packet.com/developers/docs/getting-started/deployment-options/spot-market/).
 * 
 * ## Example Usage
 * 
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as packet from "@pulumi/packet";
 * 
 * // Create a spot market request
 * const req = new packet.SpotMarketRequest("req", {
 *     projectId: local.project_id,
 *     maxBidPrice: 0.03,
 *     facilities: ["ewr1"],
 *     devicesMin: 1,
 *     devicesMax: 1,
 *     instance_parameters: {
 *         hostname: "testspot",
 *         billingCycle: "hourly",
 *         operatingSystem: "coreosStable",
 *         plan: "t1.small.x86",
 *     },
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/spot_market_request.html.markdown.
 */
export class SpotMarketRequest extends pulumi.CustomResource {
    /**
     * Get an existing SpotMarketRequest resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SpotMarketRequestState, opts?: pulumi.CustomResourceOptions): SpotMarketRequest {
        return new SpotMarketRequest(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'packet:index/spotMarketRequest:SpotMarketRequest';

    /**
     * Returns true if the given object is an instance of SpotMarketRequest.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SpotMarketRequest {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SpotMarketRequest.__pulumiType;
    }

    /**
     * Maximum number devices to be created
     */
    public readonly devicesMax!: pulumi.Output<number>;
    /**
     * Miniumum number devices to be created
     */
    public readonly devicesMin!: pulumi.Output<number>;
    /**
     * Facility IDs where devices should be created
     */
    public readonly facilities!: pulumi.Output<string[]>;
    /**
     * Device parameters. See device resource for details
     */
    public readonly instanceParameters!: pulumi.Output<outputs.SpotMarketRequestInstanceParameters>;
    /**
     * Maximum price user is willing to pay per hour per device
     */
    public readonly maxBidPrice!: pulumi.Output<number>;
    /**
     * Project ID
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed
     */
    public readonly waitForDevices!: pulumi.Output<boolean | undefined>;

    /**
     * Create a SpotMarketRequest resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SpotMarketRequestArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SpotMarketRequestArgs | SpotMarketRequestState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as SpotMarketRequestState | undefined;
            inputs["devicesMax"] = state ? state.devicesMax : undefined;
            inputs["devicesMin"] = state ? state.devicesMin : undefined;
            inputs["facilities"] = state ? state.facilities : undefined;
            inputs["instanceParameters"] = state ? state.instanceParameters : undefined;
            inputs["maxBidPrice"] = state ? state.maxBidPrice : undefined;
            inputs["projectId"] = state ? state.projectId : undefined;
            inputs["waitForDevices"] = state ? state.waitForDevices : undefined;
        } else {
            const args = argsOrState as SpotMarketRequestArgs | undefined;
            if (!args || args.devicesMax === undefined) {
                throw new Error("Missing required property 'devicesMax'");
            }
            if (!args || args.devicesMin === undefined) {
                throw new Error("Missing required property 'devicesMin'");
            }
            if (!args || args.facilities === undefined) {
                throw new Error("Missing required property 'facilities'");
            }
            if (!args || args.instanceParameters === undefined) {
                throw new Error("Missing required property 'instanceParameters'");
            }
            if (!args || args.maxBidPrice === undefined) {
                throw new Error("Missing required property 'maxBidPrice'");
            }
            if (!args || args.projectId === undefined) {
                throw new Error("Missing required property 'projectId'");
            }
            inputs["devicesMax"] = args ? args.devicesMax : undefined;
            inputs["devicesMin"] = args ? args.devicesMin : undefined;
            inputs["facilities"] = args ? args.facilities : undefined;
            inputs["instanceParameters"] = args ? args.instanceParameters : undefined;
            inputs["maxBidPrice"] = args ? args.maxBidPrice : undefined;
            inputs["projectId"] = args ? args.projectId : undefined;
            inputs["waitForDevices"] = args ? args.waitForDevices : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(SpotMarketRequest.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SpotMarketRequest resources.
 */
export interface SpotMarketRequestState {
    /**
     * Maximum number devices to be created
     */
    readonly devicesMax?: pulumi.Input<number>;
    /**
     * Miniumum number devices to be created
     */
    readonly devicesMin?: pulumi.Input<number>;
    /**
     * Facility IDs where devices should be created
     */
    readonly facilities?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Device parameters. See device resource for details
     */
    readonly instanceParameters?: pulumi.Input<inputs.SpotMarketRequestInstanceParameters>;
    /**
     * Maximum price user is willing to pay per hour per device
     */
    readonly maxBidPrice?: pulumi.Input<number>;
    /**
     * Project ID
     */
    readonly projectId?: pulumi.Input<string>;
    /**
     * On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed
     */
    readonly waitForDevices?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a SpotMarketRequest resource.
 */
export interface SpotMarketRequestArgs {
    /**
     * Maximum number devices to be created
     */
    readonly devicesMax: pulumi.Input<number>;
    /**
     * Miniumum number devices to be created
     */
    readonly devicesMin: pulumi.Input<number>;
    /**
     * Facility IDs where devices should be created
     */
    readonly facilities: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Device parameters. See device resource for details
     */
    readonly instanceParameters: pulumi.Input<inputs.SpotMarketRequestInstanceParameters>;
    /**
     * Maximum price user is willing to pay per hour per device
     */
    readonly maxBidPrice: pulumi.Input<number>;
    /**
     * Project ID
     */
    readonly projectId: pulumi.Input<string>;
    /**
     * On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed
     */
    readonly waitForDevices?: pulumi.Input<boolean>;
}
