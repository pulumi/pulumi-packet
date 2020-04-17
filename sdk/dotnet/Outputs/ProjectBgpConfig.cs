// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Packet.Outputs
{

    [OutputType]
    public sealed class ProjectBgpConfig
    {
        /// <summary>
        /// Autonomous System Numer for local BGP deployment
        /// </summary>
        public readonly int Asn;
        /// <summary>
        /// `private` or `public`, the `private` is likely to be usable immediately, the `public` will need to be review by Packet engineers
        /// </summary>
        public readonly string DeploymentType;
        /// <summary>
        /// The maximum number of route filters allowed per server
        /// </summary>
        public readonly int? MaxPrefix;
        /// <summary>
        /// Password for BGP session in plaintext (not a checksum)
        /// </summary>
        public readonly string? Md5;
        /// <summary>
        /// status of BGP configuration in the project
        /// </summary>
        public readonly string? Status;

        [OutputConstructor]
        private ProjectBgpConfig(
            int asn,

            string deploymentType,

            int? maxPrefix,

            string? md5,

            string? status)
        {
            Asn = asn;
            DeploymentType = deploymentType;
            MaxPrefix = maxPrefix;
            Md5 = md5;
            Status = status;
        }
    }
}