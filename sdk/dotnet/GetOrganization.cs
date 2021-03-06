// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Packet
{
    public static class GetOrganization
    {
        /// <summary>
        /// Provides a Packet organization datasource.
        /// </summary>
        public static Task<GetOrganizationResult> InvokeAsync(GetOrganizationArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetOrganizationResult>("packet:index/getOrganization:getOrganization", args ?? new GetOrganizationArgs(), options.WithVersion());
    }


    public sealed class GetOrganizationArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The organization name
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// The UUID of the organization resource
        /// </summary>
        [Input("organizationId")]
        public string? OrganizationId { get; set; }

        public GetOrganizationArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetOrganizationResult
    {
        /// <summary>
        /// Description string
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Logo URL
        /// </summary>
        public readonly string Logo;
        public readonly string Name;
        public readonly string OrganizationId;
        /// <summary>
        /// UUIDs of project resources which belong to this organization
        /// </summary>
        public readonly ImmutableArray<string> ProjectIds;
        /// <summary>
        /// Twitter handle
        /// </summary>
        public readonly string Twitter;
        /// <summary>
        /// Website link
        /// </summary>
        public readonly string Website;

        [OutputConstructor]
        private GetOrganizationResult(
            string description,

            string id,

            string logo,

            string name,

            string organizationId,

            ImmutableArray<string> projectIds,

            string twitter,

            string website)
        {
            Description = description;
            Id = id;
            Logo = logo;
            Name = name;
            OrganizationId = organizationId;
            ProjectIds = projectIds;
            Twitter = twitter;
            Website = website;
        }
    }
}
