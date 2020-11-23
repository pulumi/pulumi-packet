// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Provides a Packet Block Storage Volume datasource to allow you to read existing volumes.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as packet from "@pulumi/packet";
 *
 * const volume1 = packet.getVolume({
 *     name: "terraform-volume-1",
 *     projectId: local.project_id,
 * });
 * export const volumeSize = volume1.then(volume1 => volume1.size);
 * ```
 */
export function getVolume(args?: GetVolumeArgs, opts?: pulumi.InvokeOptions): Promise<GetVolumeResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("packet:index/getVolume:getVolume", {
        "name": args.name,
        "projectId": args.projectId,
        "volumeId": args.volumeId,
    }, opts);
}

/**
 * A collection of arguments for invoking getVolume.
 */
export interface GetVolumeArgs {
    /**
     * Name of volume for lookup
     */
    readonly name?: string;
    /**
     * The ID the parent Packet project (for lookup by name)
     */
    readonly projectId?: string;
    /**
     * ID of volume for lookup
     */
    readonly volumeId?: string;
}

/**
 * A collection of values returned by getVolume.
 */
export interface GetVolumeResult {
    /**
     * The billing cycle, defaults to hourly
     */
    readonly billingCycle: string;
    readonly created: string;
    readonly description: string;
    /**
     * UUIDs of devices to which this volume is attached
     */
    readonly deviceIds: string[];
    /**
     * The facility slug the volume resides in
     */
    readonly facility: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * Whether the volume is locked or not
     */
    readonly locked: boolean;
    /**
     * The name of the volume
     * * `projectId ` - The project id the volume is in
     */
    readonly name: string;
    /**
     * Performance plan the volume is on
     */
    readonly plan: string;
    readonly projectId: string;
    /**
     * The size in GB of the volume
     */
    readonly size: number;
    readonly snapshotPolicies: outputs.GetVolumeSnapshotPolicy[];
    /**
     * The state of the volume
     */
    readonly state: string;
    readonly updated: string;
    readonly volumeId: string;
}
