// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a resource to manage organization resource in Packet.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as packet from "@pulumi/packet";
 * 
 * // Create a new Project
 * const tfOrganization1 = new packet.Organization("tf_organization_1", {
 *     description: "quux",
 *     name: "foobar",
 * });
 * ```
 */
export class Organization extends pulumi.CustomResource {
    /**
     * Get an existing Organization resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: OrganizationState, opts?: pulumi.CustomResourceOptions): Organization {
        return new Organization(name, <any>state, { ...opts, id: id });
    }

    public /*out*/ readonly created!: pulumi.Output<string>;
    /**
     * Description string.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Logo URL.
     */
    public readonly logo!: pulumi.Output<string | undefined>;
    /**
     * The name of the Organization.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Twitter handle.
     */
    public readonly twitter!: pulumi.Output<string | undefined>;
    public /*out*/ readonly updated!: pulumi.Output<string>;
    /**
     * Website link.
     */
    public readonly website!: pulumi.Output<string | undefined>;

    /**
     * Create a Organization resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: OrganizationArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: OrganizationArgs | OrganizationState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as OrganizationState | undefined;
            inputs["created"] = state ? state.created : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["logo"] = state ? state.logo : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["twitter"] = state ? state.twitter : undefined;
            inputs["updated"] = state ? state.updated : undefined;
            inputs["website"] = state ? state.website : undefined;
        } else {
            const args = argsOrState as OrganizationArgs | undefined;
            if (!args || args.name === undefined) {
                throw new Error("Missing required property 'name'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["logo"] = args ? args.logo : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["twitter"] = args ? args.twitter : undefined;
            inputs["website"] = args ? args.website : undefined;
            inputs["created"] = undefined /*out*/;
            inputs["updated"] = undefined /*out*/;
        }
        super("packet:index/organization:Organization", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Organization resources.
 */
export interface OrganizationState {
    readonly created?: pulumi.Input<string>;
    /**
     * Description string.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Logo URL.
     */
    readonly logo?: pulumi.Input<string>;
    /**
     * The name of the Organization.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Twitter handle.
     */
    readonly twitter?: pulumi.Input<string>;
    readonly updated?: pulumi.Input<string>;
    /**
     * Website link.
     */
    readonly website?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a Organization resource.
 */
export interface OrganizationArgs {
    /**
     * Description string.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Logo URL.
     */
    readonly logo?: pulumi.Input<string>;
    /**
     * The name of the Organization.
     */
    readonly name: pulumi.Input<string>;
    /**
     * Twitter handle.
     */
    readonly twitter?: pulumi.Input<string>;
    /**
     * Website link.
     */
    readonly website?: pulumi.Input<string>;
}
