// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Packet Block Storage Volume resource to allow you to
 * manage block volumes on your account.
 * Once created by Terraform, they must then be attached and mounted
 * using the api and `packet_block_attach` and `packet_block_detach`
 * scripts.
 */
export class Volume extends pulumi.CustomResource {
    /**
     * Get an existing Volume resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VolumeState, opts?: pulumi.CustomResourceOptions): Volume {
        return new Volume(name, <any>state, { ...opts, id: id });
    }

    /**
     * A list of attachments, each with it's own `href` attribute
     */
    public /*out*/ readonly attachments: pulumi.Output<{ href: string }[]>;
    /**
     * The billing cycle, defaults to "hourly"
     */
    public readonly billingCycle: pulumi.Output<string>;
    /**
     * The timestamp for when the volume was created
     */
    public /*out*/ readonly created: pulumi.Output<string>;
    /**
     * Optional description for the volume
     */
    public readonly description: pulumi.Output<string | undefined>;
    /**
     * The facility to create the volume in
     */
    public readonly facility: pulumi.Output<string>;
    /**
     * Lock or unlock the volume
     */
    public readonly locked: pulumi.Output<boolean | undefined>;
    /**
     * The name of the volume
     */
    public /*out*/ readonly name: pulumi.Output<string>;
    /**
     * The service plan slug of the volume
     */
    public readonly plan: pulumi.Output<string>;
    /**
     * The packet project ID to deploy the volume in
     */
    public readonly projectId: pulumi.Output<string>;
    /**
     * The size in GB to make the volume
     */
    public readonly size: pulumi.Output<number>;
    /**
     * Optional list of snapshot policies
     */
    public readonly snapshotPolicies: pulumi.Output<{ snapshotCount: number, snapshotFrequency: string }[] | undefined>;
    /**
     * The state of the volume
     */
    public /*out*/ readonly state: pulumi.Output<string>;
    /**
     * The timestamp for the last time the volume was updated
     */
    public /*out*/ readonly updated: pulumi.Output<string>;

    /**
     * Create a Volume resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VolumeArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VolumeArgs | VolumeState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: VolumeState = argsOrState as VolumeState | undefined;
            inputs["attachments"] = state ? state.attachments : undefined;
            inputs["billingCycle"] = state ? state.billingCycle : undefined;
            inputs["created"] = state ? state.created : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["facility"] = state ? state.facility : undefined;
            inputs["locked"] = state ? state.locked : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["plan"] = state ? state.plan : undefined;
            inputs["projectId"] = state ? state.projectId : undefined;
            inputs["size"] = state ? state.size : undefined;
            inputs["snapshotPolicies"] = state ? state.snapshotPolicies : undefined;
            inputs["state"] = state ? state.state : undefined;
            inputs["updated"] = state ? state.updated : undefined;
        } else {
            const args = argsOrState as VolumeArgs | undefined;
            if (!args || args.facility === undefined) {
                throw new Error("Missing required property 'facility'");
            }
            if (!args || args.plan === undefined) {
                throw new Error("Missing required property 'plan'");
            }
            if (!args || args.projectId === undefined) {
                throw new Error("Missing required property 'projectId'");
            }
            if (!args || args.size === undefined) {
                throw new Error("Missing required property 'size'");
            }
            inputs["billingCycle"] = args ? args.billingCycle : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["facility"] = args ? args.facility : undefined;
            inputs["locked"] = args ? args.locked : undefined;
            inputs["plan"] = args ? args.plan : undefined;
            inputs["projectId"] = args ? args.projectId : undefined;
            inputs["size"] = args ? args.size : undefined;
            inputs["snapshotPolicies"] = args ? args.snapshotPolicies : undefined;
            inputs["attachments"] = undefined /*out*/;
            inputs["created"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["state"] = undefined /*out*/;
            inputs["updated"] = undefined /*out*/;
        }
        super("packet:index/volume:Volume", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Volume resources.
 */
export interface VolumeState {
    /**
     * A list of attachments, each with it's own `href` attribute
     */
    readonly attachments?: pulumi.Input<pulumi.Input<{ href?: pulumi.Input<string> }>[]>;
    /**
     * The billing cycle, defaults to "hourly"
     */
    readonly billingCycle?: pulumi.Input<string>;
    /**
     * The timestamp for when the volume was created
     */
    readonly created?: pulumi.Input<string>;
    /**
     * Optional description for the volume
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The facility to create the volume in
     */
    readonly facility?: pulumi.Input<string>;
    /**
     * Lock or unlock the volume
     */
    readonly locked?: pulumi.Input<boolean>;
    /**
     * The name of the volume
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The service plan slug of the volume
     */
    readonly plan?: pulumi.Input<string>;
    /**
     * The packet project ID to deploy the volume in
     */
    readonly projectId?: pulumi.Input<string>;
    /**
     * The size in GB to make the volume
     */
    readonly size?: pulumi.Input<number>;
    /**
     * Optional list of snapshot policies
     */
    readonly snapshotPolicies?: pulumi.Input<pulumi.Input<{ snapshotCount: pulumi.Input<number>, snapshotFrequency: pulumi.Input<string> }>[]>;
    /**
     * The state of the volume
     */
    readonly state?: pulumi.Input<string>;
    /**
     * The timestamp for the last time the volume was updated
     */
    readonly updated?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Volume resource.
 */
export interface VolumeArgs {
    /**
     * The billing cycle, defaults to "hourly"
     */
    readonly billingCycle?: pulumi.Input<string>;
    /**
     * Optional description for the volume
     */
    readonly description?: pulumi.Input<string>;
    /**
     * The facility to create the volume in
     */
    readonly facility: pulumi.Input<string>;
    /**
     * Lock or unlock the volume
     */
    readonly locked?: pulumi.Input<boolean>;
    /**
     * The service plan slug of the volume
     */
    readonly plan: pulumi.Input<string>;
    /**
     * The packet project ID to deploy the volume in
     */
    readonly projectId: pulumi.Input<string>;
    /**
     * The size in GB to make the volume
     */
    readonly size: pulumi.Input<number>;
    /**
     * Optional list of snapshot policies
     */
    readonly snapshotPolicies?: pulumi.Input<pulumi.Input<{ snapshotCount: pulumi.Input<number>, snapshotFrequency: pulumi.Input<string> }>[]>;
}