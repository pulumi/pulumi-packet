// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a resource to allow users to manage Virtual Networks in their projects.
 * 
 * To learn more about Layer 2 networking in Packet, refer to
 * * https://support.packet.com/kb/articles/layer-2-configurations
 * * https://support.packet.com/kb/articles/layer-2-overview
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as packet from "@pulumi/packet";
 * 
 * const vlan1 = new packet.Vlan("vlan1", {
 *     description: "VLAN in New Jersey",
 *     facility: "ewr1",
 *     projectId: local_project_id,
 * });
 * ```
 */
export class Vlan extends pulumi.CustomResource {
    /**
     * Get an existing Vlan resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VlanState, opts?: pulumi.CustomResourceOptions): Vlan {
        return new Vlan(name, <any>state, { ...opts, id: id });
    }

    /**
     * Description string
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Facility where to create the VLAN
     */
    public readonly facility!: pulumi.Output<string>;
    /**
     * ID of parent project
     */
    public readonly projectId!: pulumi.Output<string>;
    /**
     * VXLAN segment ID
     */
    public /*out*/ readonly vxlan!: pulumi.Output<number>;

    /**
     * Create a Vlan resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VlanArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VlanArgs | VlanState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as VlanState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["facility"] = state ? state.facility : undefined;
            inputs["projectId"] = state ? state.projectId : undefined;
            inputs["vxlan"] = state ? state.vxlan : undefined;
        } else {
            const args = argsOrState as VlanArgs | undefined;
            if (!args || args.facility === undefined) {
                throw new Error("Missing required property 'facility'");
            }
            if (!args || args.projectId === undefined) {
                throw new Error("Missing required property 'projectId'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["facility"] = args ? args.facility : undefined;
            inputs["projectId"] = args ? args.projectId : undefined;
            inputs["vxlan"] = undefined /*out*/;
        }
        super("packet:index/vlan:Vlan", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Vlan resources.
 */
export interface VlanState {
    /**
     * Description string
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Facility where to create the VLAN
     */
    readonly facility?: pulumi.Input<string>;
    /**
     * ID of parent project
     */
    readonly projectId?: pulumi.Input<string>;
    /**
     * VXLAN segment ID
     */
    readonly vxlan?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a Vlan resource.
 */
export interface VlanArgs {
    /**
     * Description string
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Facility where to create the VLAN
     */
    readonly facility: pulumi.Input<string>;
    /**
     * ID of parent project
     */
    readonly projectId: pulumi.Input<string>;
}
