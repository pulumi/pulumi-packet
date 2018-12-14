// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Packet SSH key resource to allow you manage SSH
 * keys on your account. All SSH keys on your account are loaded on
 * all new devices, they do not have to be explicitly declared on
 * device creation.
 */
export class SSHKey extends pulumi.CustomResource {
    /**
     * Get an existing SSHKey resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SSHKeyState, opts?: pulumi.CustomResourceOptions): SSHKey {
        return new SSHKey(name, <any>state, { ...opts, id: id });
    }

    /**
     * The timestamp for when the SSH key was created
     */
    public /*out*/ readonly created: pulumi.Output<string>;
    /**
     * The fingerprint of the SSH key
     */
    public /*out*/ readonly fingerprint: pulumi.Output<string>;
    /**
     * The name of the SSH key for identification
     */
    public readonly name: pulumi.Output<string>;
    /**
     * The public key. If this is a file, it
     * can be read using the file interpolation function
     */
    public readonly publicKey: pulumi.Output<string>;
    /**
     * The timestamp for the last time the SSH key was updated
     */
    public /*out*/ readonly updated: pulumi.Output<string>;

    /**
     * Create a SSHKey resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SSHKeyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: SSHKeyArgs | SSHKeyState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: SSHKeyState = argsOrState as SSHKeyState | undefined;
            inputs["created"] = state ? state.created : undefined;
            inputs["fingerprint"] = state ? state.fingerprint : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["publicKey"] = state ? state.publicKey : undefined;
            inputs["updated"] = state ? state.updated : undefined;
        } else {
            const args = argsOrState as SSHKeyArgs | undefined;
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
        super("packet:index/sSHKey:SSHKey", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering SSHKey resources.
 */
export interface SSHKeyState {
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
 * The set of arguments for constructing a SSHKey resource.
 */
export interface SSHKeyArgs {
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
