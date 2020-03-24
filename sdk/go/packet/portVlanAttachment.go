// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package packet

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a resource to attach device ports to VLANs.
//
// Device and VLAN must be in the same facility.
//
// If you need this resource to add the port back to bond on removal, set `forceBond = true`.
//
// To learn more about Layer 2 networking in Packet, refer to
//
// * https://www.packet.com/resources/guides/layer-2-configurations/ 
// * https://www.packet.com/developers/docs/network/advanced/layer-2/
//
// ## Attribute Referece
//
// * `id` - UUID of device port used in the assignment
// * `vlanId` - UUID of VLAN API resource
// * `portId` - UUID of device port
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/port_vlan_attachment.html.markdown.
type PortVlanAttachment struct {
	pulumi.CustomResourceState

	// ID of device to be assigned to the VLAN
	DeviceId pulumi.StringOutput `pulumi:"deviceId"`
	// Add port back to the bond when this resource is removed. Default is false.
	ForceBond pulumi.BoolPtrOutput `pulumi:"forceBond"`
	// Mark this VLAN a native VLAN on the port. This can be used only if this assignment assigns second or further VLAN to the port. To ensure that this attachment is not first on a port, you can use `dependsOn` pointing to another packet_port_vlan_attachment, just like in the layer2-individual example above. 
	Native pulumi.BoolPtrOutput `pulumi:"native"`
	PortId pulumi.StringOutput `pulumi:"portId"`
	// Name of network port to be assigned to the VLAN
	PortName pulumi.StringOutput `pulumi:"portName"`
	VlanId pulumi.StringOutput `pulumi:"vlanId"`
	// VXLAN Network Identifier, integer
	VlanVnid pulumi.IntOutput `pulumi:"vlanVnid"`
}

// NewPortVlanAttachment registers a new resource with the given unique name, arguments, and options.
func NewPortVlanAttachment(ctx *pulumi.Context,
	name string, args *PortVlanAttachmentArgs, opts ...pulumi.ResourceOption) (*PortVlanAttachment, error) {
	if args == nil || args.DeviceId == nil {
		return nil, errors.New("missing required argument 'DeviceId'")
	}
	if args == nil || args.PortName == nil {
		return nil, errors.New("missing required argument 'PortName'")
	}
	if args == nil || args.VlanVnid == nil {
		return nil, errors.New("missing required argument 'VlanVnid'")
	}
	if args == nil {
		args = &PortVlanAttachmentArgs{}
	}
	var resource PortVlanAttachment
	err := ctx.RegisterResource("packet:index/portVlanAttachment:PortVlanAttachment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPortVlanAttachment gets an existing PortVlanAttachment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPortVlanAttachment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PortVlanAttachmentState, opts ...pulumi.ResourceOption) (*PortVlanAttachment, error) {
	var resource PortVlanAttachment
	err := ctx.ReadResource("packet:index/portVlanAttachment:PortVlanAttachment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering PortVlanAttachment resources.
type portVlanAttachmentState struct {
	// ID of device to be assigned to the VLAN
	DeviceId *string `pulumi:"deviceId"`
	// Add port back to the bond when this resource is removed. Default is false.
	ForceBond *bool `pulumi:"forceBond"`
	// Mark this VLAN a native VLAN on the port. This can be used only if this assignment assigns second or further VLAN to the port. To ensure that this attachment is not first on a port, you can use `dependsOn` pointing to another packet_port_vlan_attachment, just like in the layer2-individual example above. 
	Native *bool `pulumi:"native"`
	PortId *string `pulumi:"portId"`
	// Name of network port to be assigned to the VLAN
	PortName *string `pulumi:"portName"`
	VlanId *string `pulumi:"vlanId"`
	// VXLAN Network Identifier, integer
	VlanVnid *int `pulumi:"vlanVnid"`
}

type PortVlanAttachmentState struct {
	// ID of device to be assigned to the VLAN
	DeviceId pulumi.StringPtrInput
	// Add port back to the bond when this resource is removed. Default is false.
	ForceBond pulumi.BoolPtrInput
	// Mark this VLAN a native VLAN on the port. This can be used only if this assignment assigns second or further VLAN to the port. To ensure that this attachment is not first on a port, you can use `dependsOn` pointing to another packet_port_vlan_attachment, just like in the layer2-individual example above. 
	Native pulumi.BoolPtrInput
	PortId pulumi.StringPtrInput
	// Name of network port to be assigned to the VLAN
	PortName pulumi.StringPtrInput
	VlanId pulumi.StringPtrInput
	// VXLAN Network Identifier, integer
	VlanVnid pulumi.IntPtrInput
}

func (PortVlanAttachmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*portVlanAttachmentState)(nil)).Elem()
}

type portVlanAttachmentArgs struct {
	// ID of device to be assigned to the VLAN
	DeviceId string `pulumi:"deviceId"`
	// Add port back to the bond when this resource is removed. Default is false.
	ForceBond *bool `pulumi:"forceBond"`
	// Mark this VLAN a native VLAN on the port. This can be used only if this assignment assigns second or further VLAN to the port. To ensure that this attachment is not first on a port, you can use `dependsOn` pointing to another packet_port_vlan_attachment, just like in the layer2-individual example above. 
	Native *bool `pulumi:"native"`
	// Name of network port to be assigned to the VLAN
	PortName string `pulumi:"portName"`
	// VXLAN Network Identifier, integer
	VlanVnid int `pulumi:"vlanVnid"`
}

// The set of arguments for constructing a PortVlanAttachment resource.
type PortVlanAttachmentArgs struct {
	// ID of device to be assigned to the VLAN
	DeviceId pulumi.StringInput
	// Add port back to the bond when this resource is removed. Default is false.
	ForceBond pulumi.BoolPtrInput
	// Mark this VLAN a native VLAN on the port. This can be used only if this assignment assigns second or further VLAN to the port. To ensure that this attachment is not first on a port, you can use `dependsOn` pointing to another packet_port_vlan_attachment, just like in the layer2-individual example above. 
	Native pulumi.BoolPtrInput
	// Name of network port to be assigned to the VLAN
	PortName pulumi.StringInput
	// VXLAN Network Identifier, integer
	VlanVnid pulumi.IntInput
}

func (PortVlanAttachmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*portVlanAttachmentArgs)(nil)).Elem()
}

