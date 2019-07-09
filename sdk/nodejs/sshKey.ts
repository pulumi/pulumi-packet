// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class SshKey extends pulumi.CustomResource {
    /**
     * Get an existing SshKey resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SshKeyState, opts?: pulumi.CustomResourceOptions): SshKey {
        return new SshKey(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'packet:index/sshKey:SshKey';

    /**
     * Returns true if the given object is an instance of SshKey.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SshKey {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SshKey.__pulumiType;
    }

    /**
     * The timestamp for when the SSH key was created
     */
    public /*out*/ readonly created!: pulumi.Output<string>;
    /**
     * The fingerprint of the SSH key
     */
    public /*out*/ readonly fingerprint!: pulumi.Output<string>;
    /**
     * The name of the SSH key for identification
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The public key. If this is a file, it
     * can be read using the file interpolation function
     */
    public readonly publicKey!: pulumi.Output<string>;
    /**
     * The timestamp for the last time the SSH key was updated
     */
    public /*out*/ readonly updated!: pulumi.Output<string>;

    /**
     * Create a SshKey resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SshKeyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SshKeyArgs | SshKeyState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as SshKeyState | undefined;
            inputs["created"] = state ? state.created : undefined;
            inputs["fingerprint"] = state ? state.fingerprint : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["publicKey"] = state ? state.publicKey : undefined;
            inputs["updated"] = state ? state.updated : undefined;
        } else {
            const args = argsOrState as SshKeyArgs | undefined;
            if (!args || args.name === undefined) {
                throw new Error("Missing required property 'name'");
            }
            if (!args || args.publicKey === undefined) {
                throw new Error("Missing required property 'publicKey'");
            }
            inputs["name"] = args ? args.name : undefined;
            inputs["publicKey"] = args ? args.publicKey : undefined;
            inputs["created"] = undefined /*out*/;
            inputs["fingerprint"] = undefined /*out*/;
            inputs["updated"] = undefined /*out*/;
        }
        super(SshKey.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SshKey resources.
 */
export interface SshKeyState {
    /**
     * The timestamp for when the SSH key was created
     */
    readonly created?: pulumi.Input<string>;
    /**
     * The fingerprint of the SSH key
     */
    readonly fingerprint?: pulumi.Input<string>;
    /**
     * The name of the SSH key for identification
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The public key. If this is a file, it
     * can be read using the file interpolation function
     */
    readonly publicKey?: pulumi.Input<string>;
    /**
     * The timestamp for the last time the SSH key was updated
     */
    readonly updated?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a SshKey resource.
 */
export interface SshKeyArgs {
    /**
     * The name of the SSH key for identification
     */
    readonly name: pulumi.Input<string>;
    /**
     * The public key. If this is a file, it
     * can be read using the file interpolation function
     */
    readonly publicKey: pulumi.Input<string>;
}
