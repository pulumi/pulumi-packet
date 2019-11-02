// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package packet

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this datasource to retrieve attributes of the Project API resource.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/d/project.html.markdown.
func LookupProject(ctx *pulumi.Context, args *GetProjectArgs) (*GetProjectResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
		inputs["projectId"] = args.ProjectId
	}
	outputs, err := ctx.Invoke("packet:index/getProject:getProject", inputs)
	if err != nil {
		return nil, err
	}
	return &GetProjectResult{
		BackendTransfer: outputs["backendTransfer"],
		BgpConfig: outputs["bgpConfig"],
		Created: outputs["created"],
		Name: outputs["name"],
		OrganizationId: outputs["organizationId"],
		PaymentMethodId: outputs["paymentMethodId"],
		ProjectId: outputs["projectId"],
		Updated: outputs["updated"],
		UserIds: outputs["userIds"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getProject.
type GetProjectArgs struct {
	// The name which is used to look up the project
	Name interface{}
	// The UUID by which to look up the project
	ProjectId interface{}
}

// A collection of values returned by getProject.
type GetProjectResult struct {
	// Whether Backend Transfer is enabled for this project
	BackendTransfer interface{}
	// Optional BGP settings. Refer to [Packet guide for BGP](https://support.packet.com/kb/articles/bgp).
	BgpConfig interface{}
	// The timestamp for when the project was created
	Created interface{}
	Name interface{}
	// The UUID of this project's parent organization
	OrganizationId interface{}
	// The UUID of payment method for this project
	PaymentMethodId interface{}
	ProjectId interface{}
	// The timestamp for the last time the project was updated
	Updated interface{}
	// List of UUIDs of user accounts which beling to this project
	UserIds interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}