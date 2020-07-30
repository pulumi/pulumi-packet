// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package packet

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a resource to allow users to manage Virtual Networks in their projects.
//
// To learn more about Layer 2 networking in Packet, refer to
// * https://www.packet.com/resources/guides/layer-2-configurations/
// * https://www.packet.com/developers/docs/network/advanced/layer-2/
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
// 		_, err := packet.NewVlan(ctx, "vlan1", &packet.VlanArgs{
// 			Description: pulumi.String("VLAN in New Jersey"),
// 			Facility:    pulumi.String("ewr1"),
// 			ProjectId:   pulumi.Any(local.Project_id),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Vlan struct {
	pulumi.CustomResourceState

	// Description string
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// Facility where to create the VLAN
	Facility pulumi.StringOutput `pulumi:"facility"`
	// ID of parent project
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// VXLAN segment ID
	Vxlan pulumi.IntOutput `pulumi:"vxlan"`
}

// NewVlan registers a new resource with the given unique name, arguments, and options.
func NewVlan(ctx *pulumi.Context,
	name string, args *VlanArgs, opts ...pulumi.ResourceOption) (*Vlan, error) {
	if args == nil || args.Facility == nil {
		return nil, errors.New("missing required argument 'Facility'")
	}
	if args == nil || args.ProjectId == nil {
		return nil, errors.New("missing required argument 'ProjectId'")
	}
	if args == nil {
		args = &VlanArgs{}
	}
	var resource Vlan
	err := ctx.RegisterResource("packet:index/vlan:Vlan", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVlan gets an existing Vlan resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVlan(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VlanState, opts ...pulumi.ResourceOption) (*Vlan, error) {
	var resource Vlan
	err := ctx.ReadResource("packet:index/vlan:Vlan", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Vlan resources.
type vlanState struct {
	// Description string
	Description *string `pulumi:"description"`
	// Facility where to create the VLAN
	Facility *string `pulumi:"facility"`
	// ID of parent project
	ProjectId *string `pulumi:"projectId"`
	// VXLAN segment ID
	Vxlan *int `pulumi:"vxlan"`
}

type VlanState struct {
	// Description string
	Description pulumi.StringPtrInput
	// Facility where to create the VLAN
	Facility pulumi.StringPtrInput
	// ID of parent project
	ProjectId pulumi.StringPtrInput
	// VXLAN segment ID
	Vxlan pulumi.IntPtrInput
}

func (VlanState) ElementType() reflect.Type {
	return reflect.TypeOf((*vlanState)(nil)).Elem()
}

type vlanArgs struct {
	// Description string
	Description *string `pulumi:"description"`
	// Facility where to create the VLAN
	Facility string `pulumi:"facility"`
	// ID of parent project
	ProjectId string `pulumi:"projectId"`
}

// The set of arguments for constructing a Vlan resource.
type VlanArgs struct {
	// Description string
	Description pulumi.StringPtrInput
	// Facility where to create the VLAN
	Facility pulumi.StringInput
	// ID of parent project
	ProjectId pulumi.StringInput
}

func (VlanArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*vlanArgs)(nil)).Elem()
}
