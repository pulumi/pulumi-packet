// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a resource to manage BGP sessions in Packet Host. Refer to [Packet BGP documentation](https://support.packet.com/kb/articles/bgp) for more details.
 * 
 * You need to have BGP config enabled in your project.
 * 
 * BGP session must be linked to a device running [BIRD](https://bird.network.cz) or other BGP routing daemon which will control route advertisements via the session to Packet's upstream routers. 
 */
export class BgpSession extends pulumi.CustomResource {
    /**
     * Get an existing BgpSession resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BgpSessionState, opts?: pulumi.CustomResourceOptions): BgpSession {
        return new BgpSession(name, <any>state, { ...opts, id: id });
    }

    /**
     * `ipv4` or `ipv6`
     */
    public readonly addressFamily!: pulumi.Output<string>;
    /**
     * Boolean flag to set the default route policy. False by default.
     */
    public readonly defaultRoute!: pulumi.Output<boolean | undefined>;
    /**
     * ID of device 
     */
    public readonly deviceId!: pulumi.Output<string>;
    public /*out*/ readonly status!: pulumi.Output<string>;

    /**
     * Create a BgpSession resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: BgpSessionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: BgpSessionArgs | BgpSessionState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as BgpSessionState | undefined;
            inputs["addressFamily"] = state ? state.addressFamily : undefined;
            inputs["defaultRoute"] = state ? state.defaultRoute : undefined;
            inputs["deviceId"] = state ? state.deviceId : undefined;
            inputs["status"] = state ? state.status : undefined;
        } else {
            const args = argsOrState as BgpSessionArgs | undefined;
            if (!args || args.addressFamily === undefined) {
                throw new Error("Missing required property 'addressFamily'");
            }
            if (!args || args.deviceId === undefined) {
                throw new Error("Missing required property 'deviceId'");
            }
            inputs["addressFamily"] = args ? args.addressFamily : undefined;
            inputs["defaultRoute"] = args ? args.defaultRoute : undefined;
            inputs["deviceId"] = args ? args.deviceId : undefined;
            inputs["status"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super("packet:index/bgpSession:BgpSession", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering BgpSession resources.
 */
export interface BgpSessionState {
    /**
     * `ipv4` or `ipv6`
     */
    readonly addressFamily?: pulumi.Input<string>;
    /**
     * Boolean flag to set the default route policy. False by default.
     */
    readonly defaultRoute?: pulumi.Input<boolean>;
    /**
     * ID of device 
     */
    readonly deviceId?: pulumi.Input<string>;
    readonly status?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a BgpSession resource.
 */
export interface BgpSessionArgs {
    /**
     * `ipv4` or `ipv6`
     */
    readonly addressFamily: pulumi.Input<string>;
    /**
     * Boolean flag to set the default route policy. False by default.
     */
    readonly defaultRoute?: pulumi.Input<boolean>;
    /**
     * ID of device 
     */
    readonly deviceId: pulumi.Input<string>;
}
