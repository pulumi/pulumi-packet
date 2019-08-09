// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Use this data source to get CIDR expression for precreated IPv6 and IPv4 blocks in Packet.
 * You can then use the cidrsubnet TF builtin function to derive subnets.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as packet from "@pulumi/packet";
 * 
 * const projectId = "<UUID_of_your_project>";
 * const test = pulumi.output(packet.getPrecreatedIpBlock({
 *     addressFamily: 6,
 *     facility: "ewr1",
 *     projectId: projectId,
 *     public: true,
 * }));
 * const web1 = new packet.Device("web1", {
 *     billingCycle: "hourly",
 *     facilities: ["ewr1"],
 *     hostname: "web1",
 *     operatingSystem: "ubuntu1604",
 *     plan: "t1.small.x86",
 *     projectId: projectId,
 * });
 * const fromIpv6Block = new packet.IpAttachment("fromIpv6Block", {
 *     cidrNotation: test.apply(test => (() => {
 *         throw "tf2pulumi error: NYI: call to cidrsubnet";
 *         return (() => { throw "NYI: call to cidrsubnet"; })();
 *     })()),
 *     deviceId: web1.id,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/d/precreated_ip_block.html.markdown.
 */
export function getPrecreatedIpBlock(args: GetPrecreatedIpBlockArgs, opts?: pulumi.InvokeOptions): Promise<GetPrecreatedIpBlockResult> & GetPrecreatedIpBlockResult {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetPrecreatedIpBlockResult> = pulumi.runtime.invoke("packet:index/getPrecreatedIpBlock:getPrecreatedIpBlock", {
        "addressFamily": args.addressFamily,
        "facility": args.facility,
        "global": args.global,
        "projectId": args.projectId,
        "public": args.public,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getPrecreatedIpBlock.
 */
export interface GetPrecreatedIpBlockArgs {
    /**
     * 4 or 6, depending on which block you are looking for.
     */
    readonly addressFamily: number;
    /**
     * Facility of the searched block. (Optional) Only allowed for non-global blocks.
     */
    readonly facility?: string;
    /**
     * Whether to look for global block. Default is false for backward compatibility.
     */
    readonly global?: boolean;
    /**
     * ID of the project where the searched block should be.
     */
    readonly projectId: string;
    /**
     * Whether to look for public or private block. 
     */
    readonly public: boolean;
}

/**
 * A collection of values returned by getPrecreatedIpBlock.
 */
export interface GetPrecreatedIpBlockResult {
    readonly address: string;
    readonly addressFamily: number;
    readonly cidr: number;
    /**
     * CIDR notation of the looked up block.
     */
    readonly cidrNotation: string;
    readonly facility?: string;
    readonly gateway: string;
    readonly global?: boolean;
    readonly manageable: boolean;
    readonly management: boolean;
    readonly netmask: string;
    readonly network: string;
    readonly projectId: string;
    readonly public: boolean;
    readonly quantity: number;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
