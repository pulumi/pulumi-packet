// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Packet
{
    public static class GetIpBlockRanges
    {
        /// <summary>
        /// Use this datasource to get CIDR expressions for allocated IP blocks of all the types in a project, optionally filtered by facility.
        /// 
        /// There are four types of IP blocks in Packet: global IPv4, public IPv4, private IPv4 and IPv6. Both global and public IPv4 are routable from the Internet. Public IPv4 block is allocated in a facility, and addresses from it can only be assigned to devices in that facility. Addresses from Global IPv4 block can be assigned to a device in any facility.
        /// 
        /// The datasource has 4 list attributes: `global_ipv4`, `public_ipv4`, `private_ipv4` and `ipv6`, each listing CIDR notation (`&lt;network&gt;/&lt;mask&gt;`) of respective blocks from the project.
        /// 
        /// {{% examples %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetIpBlockRangesResult> InvokeAsync(GetIpBlockRangesArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetIpBlockRangesResult>("packet:index/getIpBlockRanges:getIpBlockRanges", args ?? new GetIpBlockRangesArgs(), options.WithVersion());
    }


    public sealed class GetIpBlockRangesArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// Facility code filtering the IP blocks. Global IPv4 blcoks will be listed anyway. If you omit this, all the block from the project will be listed.
        /// </summary>
        [Input("facility")]
        public string? Facility { get; set; }

        /// <summary>
        /// ID of the project from which to list the blocks. 
        /// </summary>
        [Input("projectId", required: true)]
        public string ProjectId { get; set; } = null!;

        public GetIpBlockRangesArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetIpBlockRangesResult
    {
        public readonly string? Facility;
        /// <summary>
        /// list of CIDR expressions for Global IPv4 blocks in the project
        /// </summary>
        public readonly ImmutableArray<string> GlobalIpv4s;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// list of CIDR expressions for IPv6 blocks in the project
        /// </summary>
        public readonly ImmutableArray<string> Ipv6s;
        /// <summary>
        /// list of CIDR expressions for Private IPv4 blocks in the project
        /// </summary>
        public readonly ImmutableArray<string> PrivateIpv4s;
        public readonly string ProjectId;
        /// <summary>
        /// list of CIDR expressions for Public IPv4 blocks in the project
        /// </summary>
        public readonly ImmutableArray<string> PublicIpv4s;

        [OutputConstructor]
        private GetIpBlockRangesResult(
            string? facility,

            ImmutableArray<string> globalIpv4s,

            string id,

            ImmutableArray<string> ipv6s,

            ImmutableArray<string> privateIpv4s,

            string projectId,

            ImmutableArray<string> publicIpv4s)
        {
            Facility = facility;
            GlobalIpv4s = globalIpv4s;
            Id = id;
            Ipv6s = ipv6s;
            PrivateIpv4s = privateIpv4s;
            ProjectId = projectId;
            PublicIpv4s = publicIpv4s;
        }
    }
}
