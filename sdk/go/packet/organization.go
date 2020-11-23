// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package packet

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a resource to manage organization resource in Packet.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-packet/sdk/v3/go/packet"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := packet.NewOrganization(ctx, "tfOrganization1", &packet.OrganizationArgs{
// 			Description: pulumi.String("quux"),
// 			Name:        pulumi.String("foobar"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Organization struct {
	pulumi.CustomResourceState

	Created pulumi.StringOutput `pulumi:"created"`
	// Description string.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Logo URL.
	Logo pulumi.StringPtrOutput `pulumi:"logo"`
	// The name of the Organization.
	Name pulumi.StringOutput `pulumi:"name"`
	// Twitter handle.
	Twitter pulumi.StringPtrOutput `pulumi:"twitter"`
	Updated pulumi.StringOutput    `pulumi:"updated"`
	// Website link.
	Website pulumi.StringPtrOutput `pulumi:"website"`
}

// NewOrganization registers a new resource with the given unique name, arguments, and options.
func NewOrganization(ctx *pulumi.Context,
	name string, args *OrganizationArgs, opts ...pulumi.ResourceOption) (*Organization, error) {
	if args == nil || args.Name == nil {
		return nil, errors.New("missing required argument 'Name'")
	}
	if args == nil {
		args = &OrganizationArgs{}
	}
	var resource Organization
	err := ctx.RegisterResource("packet:index/organization:Organization", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetOrganization gets an existing Organization resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetOrganization(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *OrganizationState, opts ...pulumi.ResourceOption) (*Organization, error) {
	var resource Organization
	err := ctx.ReadResource("packet:index/organization:Organization", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Organization resources.
type organizationState struct {
	Created *string `pulumi:"created"`
	// Description string.
	Description *string `pulumi:"description"`
	// Logo URL.
	Logo *string `pulumi:"logo"`
	// The name of the Organization.
	Name *string `pulumi:"name"`
	// Twitter handle.
	Twitter *string `pulumi:"twitter"`
	Updated *string `pulumi:"updated"`
	// Website link.
	Website *string `pulumi:"website"`
}

type OrganizationState struct {
	Created pulumi.StringPtrInput
	// Description string.
	Description pulumi.StringPtrInput
	// Logo URL.
	Logo pulumi.StringPtrInput
	// The name of the Organization.
	Name pulumi.StringPtrInput
	// Twitter handle.
	Twitter pulumi.StringPtrInput
	Updated pulumi.StringPtrInput
	// Website link.
	Website pulumi.StringPtrInput
}

func (OrganizationState) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationState)(nil)).Elem()
}

type organizationArgs struct {
	// Description string.
	Description *string `pulumi:"description"`
	// Logo URL.
	Logo *string `pulumi:"logo"`
	// The name of the Organization.
	Name string `pulumi:"name"`
	// Twitter handle.
	Twitter *string `pulumi:"twitter"`
	// Website link.
	Website *string `pulumi:"website"`
}

// The set of arguments for constructing a Organization resource.
type OrganizationArgs struct {
	// Description string.
	Description pulumi.StringPtrInput
	// Logo URL.
	Logo pulumi.StringPtrInput
	// The name of the Organization.
	Name pulumi.StringInput
	// Twitter handle.
	Twitter pulumi.StringPtrInput
	// Website link.
	Website pulumi.StringPtrInput
}

func (OrganizationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*organizationArgs)(nil)).Elem()
}

type OrganizationInput interface {
	pulumi.Input

	ToOrganizationOutput() OrganizationOutput
	ToOrganizationOutputWithContext(ctx context.Context) OrganizationOutput
}

func (Organization) ElementType() reflect.Type {
	return reflect.TypeOf((*Organization)(nil)).Elem()
}

func (i Organization) ToOrganizationOutput() OrganizationOutput {
	return i.ToOrganizationOutputWithContext(context.Background())
}

func (i Organization) ToOrganizationOutputWithContext(ctx context.Context) OrganizationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(OrganizationOutput)
}

type OrganizationOutput struct {
	*pulumi.OutputState
}

func (OrganizationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*OrganizationOutput)(nil)).Elem()
}

func (o OrganizationOutput) ToOrganizationOutput() OrganizationOutput {
	return o
}

func (o OrganizationOutput) ToOrganizationOutputWithContext(ctx context.Context) OrganizationOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(OrganizationOutput{})
}
