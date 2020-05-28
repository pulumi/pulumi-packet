// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Packet
{
    public static class GetVolume
    {
        public static Task<GetVolumeResult> InvokeAsync(GetVolumeArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetVolumeResult>("packet:index/getVolume:getVolume", args ?? new GetVolumeArgs(), options.WithVersion());
    }


    public sealed class GetVolumeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of volume for lookup
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// The ID the parent Packet project (for lookup by name)
        /// </summary>
        [Input("projectId")]
        public string? ProjectId { get; set; }

        /// <summary>
        /// ID of volume for lookup
        /// </summary>
        [Input("volumeId")]
        public string? VolumeId { get; set; }

        public GetVolumeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetVolumeResult
    {
        /// <summary>
        /// The billing cycle, defaults to hourly
        /// </summary>
        public readonly string BillingCycle;
        public readonly string Created;
        public readonly string Description;
        /// <summary>
        /// UUIDs of devices to which this volume is attached
        /// </summary>
        public readonly ImmutableArray<string> DeviceIds;
        /// <summary>
        /// The facility slug the volume resides in
        /// </summary>
        public readonly string Facility;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Whether the volume is locked or not
        /// </summary>
        public readonly bool Locked;
        /// <summary>
        /// The name of the volume
        /// * `project_id ` - The project id the volume is in
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Performance plan the volume is on
        /// </summary>
        public readonly string Plan;
        public readonly string ProjectId;
        /// <summary>
        /// The size in GB of the volume
        /// </summary>
        public readonly int Size;
        public readonly ImmutableArray<Outputs.GetVolumeSnapshotPolicyResult> SnapshotPolicies;
        /// <summary>
        /// The state of the volume
        /// </summary>
        public readonly string State;
        public readonly string Updated;
        public readonly string VolumeId;

        [OutputConstructor]
        private GetVolumeResult(
            string billingCycle,

            string created,

            string description,

            ImmutableArray<string> deviceIds,

            string facility,

            string id,

            bool locked,

            string name,

            string plan,

            string projectId,

            int size,

            ImmutableArray<Outputs.GetVolumeSnapshotPolicyResult> snapshotPolicies,

            string state,

            string updated,

            string volumeId)
        {
            BillingCycle = billingCycle;
            Created = created;
            Description = description;
            DeviceIds = deviceIds;
            Facility = facility;
            Id = id;
            Locked = locked;
            Name = name;
            Plan = plan;
            ProjectId = projectId;
            Size = size;
            SnapshotPolicies = snapshotPolicies;
            State = state;
            Updated = updated;
            VolumeId = volumeId;
        }
    }
}
