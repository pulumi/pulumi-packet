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
    public sealed class GetDeviceBgpNeighborsBgpNeighborResult
    {
        /// <summary>
        /// IP address version, 4 or 6
        /// </summary>
        public readonly int AddressFamily;
        /// <summary>
        /// Local autonomous system number
        /// </summary>
        public readonly int CustomerAs;
        /// <summary>
        /// Local used peer IP address
        /// </summary>
        public readonly string CustomerIp;
        /// <summary>
        /// Whether BGP session is password enabled
        /// </summary>
        public readonly bool Md5Enabled;
        /// <summary>
        /// BGP session password in plaintext (not a checksum)
        /// </summary>
        public readonly string Md5Password;
        /// <summary>
        /// Whether the neighbor is in EBGP multihop session
        /// </summary>
        public readonly bool Multihop;
        /// <summary>
        /// Peer AS number (different than customer_as for EBGP)
        /// </summary>
        public readonly int PeerAs;
        /// <summary>
        /// Array of IP addresses of this neighbor's peers
        /// </summary>
        public readonly ImmutableArray<string> PeerIps;
        /// <summary>
        /// Array of incoming routes. Each route has attributes:
        /// </summary>
        public readonly ImmutableArray<Outputs.GetDeviceBgpNeighborsBgpNeighborRoutesInResult> RoutesIns;
        /// <summary>
        /// Array of outgoing routes in the same format
        /// </summary>
        public readonly ImmutableArray<Outputs.GetDeviceBgpNeighborsBgpNeighborRoutesOutResult> RoutesOuts;

        [OutputConstructor]
        private GetDeviceBgpNeighborsBgpNeighborResult(
            int addressFamily,

            int customerAs,

            string customerIp,

            bool md5Enabled,

            string md5Password,

            bool multihop,

            int peerAs,

            ImmutableArray<string> peerIps,

            ImmutableArray<Outputs.GetDeviceBgpNeighborsBgpNeighborRoutesInResult> routesIns,

            ImmutableArray<Outputs.GetDeviceBgpNeighborsBgpNeighborRoutesOutResult> routesOuts)
        {
            AddressFamily = addressFamily;
            CustomerAs = customerAs;
            CustomerIp = customerIp;
            Md5Enabled = md5Enabled;
            Md5Password = md5Password;
            Multihop = multihop;
            PeerAs = peerAs;
            PeerIps = peerIps;
            RoutesIns = routesIns;
            RoutesOuts = routesOuts;
        }
    }
}
