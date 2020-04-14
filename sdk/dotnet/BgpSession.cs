// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Packet
{
    /// <summary>
    /// Provides a resource to manage BGP sessions in Packet Host. Refer to [Packet BGP documentation](https://www.packet.com/developers/docs/network/advanced/local-and-global-bgp/) for more details.
    /// 
    /// You need to have BGP config enabled in your project.
    /// 
    /// BGP session must be linked to a device running [BIRD](https://bird.network.cz) or other BGP routing daemon which will control route advertisements via the session to Packet's upstream routers. 
    /// </summary>
    public partial class BgpSession : Pulumi.CustomResource
    {
        /// <summary>
        /// `ipv4` or `ipv6`
        /// </summary>
        [Output("addressFamily")]
        public Output<string> AddressFamily { get; private set; } = null!;

        /// <summary>
        /// Boolean flag to set the default route policy. False by default.
        /// </summary>
        [Output("defaultRoute")]
        public Output<bool?> DefaultRoute { get; private set; } = null!;

        /// <summary>
        /// ID of device 
        /// </summary>
        [Output("deviceId")]
        public Output<string> DeviceId { get; private set; } = null!;

        [Output("status")]
        public Output<string> Status { get; private set; } = null!;


        /// <summary>
        /// Create a BgpSession resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public BgpSession(string name, BgpSessionArgs args, CustomResourceOptions? options = null)
            : base("packet:index/bgpSession:BgpSession", name, args ?? new BgpSessionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private BgpSession(string name, Input<string> id, BgpSessionState? state = null, CustomResourceOptions? options = null)
            : base("packet:index/bgpSession:BgpSession", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing BgpSession resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static BgpSession Get(string name, Input<string> id, BgpSessionState? state = null, CustomResourceOptions? options = null)
        {
            return new BgpSession(name, id, state, options);
        }
    }

    public sealed class BgpSessionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// `ipv4` or `ipv6`
        /// </summary>
        [Input("addressFamily", required: true)]
        public Input<string> AddressFamily { get; set; } = null!;

        /// <summary>
        /// Boolean flag to set the default route policy. False by default.
        /// </summary>
        [Input("defaultRoute")]
        public Input<bool>? DefaultRoute { get; set; }

        /// <summary>
        /// ID of device 
        /// </summary>
        [Input("deviceId", required: true)]
        public Input<string> DeviceId { get; set; } = null!;

        public BgpSessionArgs()
        {
        }
    }

    public sealed class BgpSessionState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// `ipv4` or `ipv6`
        /// </summary>
        [Input("addressFamily")]
        public Input<string>? AddressFamily { get; set; }

        /// <summary>
        /// Boolean flag to set the default route policy. False by default.
        /// </summary>
        [Input("defaultRoute")]
        public Input<bool>? DefaultRoute { get; set; }

        /// <summary>
        /// ID of device 
        /// </summary>
        [Input("deviceId")]
        public Input<string>? DeviceId { get; set; }

        [Input("status")]
        public Input<string>? Status { get; set; }

        public BgpSessionState()
        {
        }
    }
}
