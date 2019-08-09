// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package packet

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a resource to create and manage blocks of reserved IP addresses in a project.
// 
// When a user provisions first device in a facility, Packet API automatically allocates IPv6/56 and private IPv4/25 blocks.
// The new device then gets IPv6 and private IPv4 addresses from those block. It also gets a public IPv4/31 address.
// Every new device in the project and facility will automatically get IPv6 and private IPv4 addresses from these pre-allocated blocks.
// The IPv6 and private IPv4 blocks can't be created, only imported. With this resource, it's possible to create either public IPv4 blocks or global IPv4 blocks.
// 
// Public blocks are allocated in a facility. Addresses from public blocks can only be assigned to devices in the facility. Public blocks can have mask from /24 (256 addresses) to /32 (1 address). If you create public block with this resource, you must fill the facility argmument.
// 
// Addresses from global blocks can be assigned in any facility. Global blocks can have mask from /30 (4 addresses), to /32 (1 address). If you create global block with this resource, you must specify type = "globalIpv4" and you must omit the facility argument.
// 
// Once IP block is allocated or imported, an address from it can be assigned to device with the `.IpAttachment` resource.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/reserved_ip_block.html.markdown.
type ReservedIpBlock struct {
	s *pulumi.ResourceState
}

// NewReservedIpBlock registers a new resource with the given unique name, arguments, and options.
func NewReservedIpBlock(ctx *pulumi.Context,
	name string, args *ReservedIpBlockArgs, opts ...pulumi.ResourceOpt) (*ReservedIpBlock, error) {
	if args == nil || args.ProjectId == nil {
		return nil, errors.New("missing required argument 'ProjectId'")
	}
	if args == nil || args.Quantity == nil {
		return nil, errors.New("missing required argument 'Quantity'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["facility"] = nil
		inputs["projectId"] = nil
		inputs["quantity"] = nil
		inputs["type"] = nil
	} else {
		inputs["facility"] = args.Facility
		inputs["projectId"] = args.ProjectId
		inputs["quantity"] = args.Quantity
		inputs["type"] = args.Type
	}
	inputs["address"] = nil
	inputs["addressFamily"] = nil
	inputs["cidr"] = nil
	inputs["cidrNotation"] = nil
	inputs["gateway"] = nil
	inputs["global"] = nil
	inputs["manageable"] = nil
	inputs["management"] = nil
	inputs["netmask"] = nil
	inputs["network"] = nil
	inputs["public"] = nil
	s, err := ctx.RegisterResource("packet:index/reservedIpBlock:ReservedIpBlock", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ReservedIpBlock{s: s}, nil
}

// GetReservedIpBlock gets an existing ReservedIpBlock resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetReservedIpBlock(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ReservedIpBlockState, opts ...pulumi.ResourceOpt) (*ReservedIpBlock, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["address"] = state.Address
		inputs["addressFamily"] = state.AddressFamily
		inputs["cidr"] = state.Cidr
		inputs["cidrNotation"] = state.CidrNotation
		inputs["facility"] = state.Facility
		inputs["gateway"] = state.Gateway
		inputs["global"] = state.Global
		inputs["manageable"] = state.Manageable
		inputs["management"] = state.Management
		inputs["netmask"] = state.Netmask
		inputs["network"] = state.Network
		inputs["projectId"] = state.ProjectId
		inputs["public"] = state.Public
		inputs["quantity"] = state.Quantity
		inputs["type"] = state.Type
	}
	s, err := ctx.ReadResource("packet:index/reservedIpBlock:ReservedIpBlock", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ReservedIpBlock{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *ReservedIpBlock) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *ReservedIpBlock) ID() *pulumi.IDOutput {
	return r.s.ID()
}

func (r *ReservedIpBlock) Address() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["address"])
}

// Address family as integer (4 or 6)
func (r *ReservedIpBlock) AddressFamily() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["addressFamily"])
}

// length of CIDR prefix of the block as integer
func (r *ReservedIpBlock) Cidr() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["cidr"])
}

// Address and mask in CIDR notation, e.g. "147.229.15.30/31"
func (r *ReservedIpBlock) CidrNotation() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["cidrNotation"])
}

// Facility where to allocate the public IP address block, makes sense only for type==public_ipv4, must be empty for type==global_ipv4
func (r *ReservedIpBlock) Facility() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["facility"])
}

func (r *ReservedIpBlock) Gateway() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["gateway"])
}

// boolean flag whether addresses from a block are global (i.e. can be assigned in any facility)
func (r *ReservedIpBlock) Global() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["global"])
}

func (r *ReservedIpBlock) Manageable() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["manageable"])
}

func (r *ReservedIpBlock) Management() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["management"])
}

// Mask in decimal notation, e.g. "255.255.255.0"
func (r *ReservedIpBlock) Netmask() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["netmask"])
}

// Network IP address portion of the block specification
func (r *ReservedIpBlock) Network() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["network"])
}

// The packet project ID where to allocate the address block
func (r *ReservedIpBlock) ProjectId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["projectId"])
}

// boolean flag whether addresses from a block are public
func (r *ReservedIpBlock) Public() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["public"])
}

// The number of allocated /32 addresses, a power of 2
func (r *ReservedIpBlock) Quantity() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["quantity"])
}

// Either "globalIpv4" or "publicIpv4", defaults to "publicIpv4" for backward compatibility
func (r *ReservedIpBlock) Type() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["type"])
}

// Input properties used for looking up and filtering ReservedIpBlock resources.
type ReservedIpBlockState struct {
	Address interface{}
	// Address family as integer (4 or 6)
	AddressFamily interface{}
	// length of CIDR prefix of the block as integer
	Cidr interface{}
	// Address and mask in CIDR notation, e.g. "147.229.15.30/31"
	CidrNotation interface{}
	// Facility where to allocate the public IP address block, makes sense only for type==public_ipv4, must be empty for type==global_ipv4
	Facility interface{}
	Gateway interface{}
	// boolean flag whether addresses from a block are global (i.e. can be assigned in any facility)
	Global interface{}
	Manageable interface{}
	Management interface{}
	// Mask in decimal notation, e.g. "255.255.255.0"
	Netmask interface{}
	// Network IP address portion of the block specification
	Network interface{}
	// The packet project ID where to allocate the address block
	ProjectId interface{}
	// boolean flag whether addresses from a block are public
	Public interface{}
	// The number of allocated /32 addresses, a power of 2
	Quantity interface{}
	// Either "globalIpv4" or "publicIpv4", defaults to "publicIpv4" for backward compatibility
	Type interface{}
}

// The set of arguments for constructing a ReservedIpBlock resource.
type ReservedIpBlockArgs struct {
	// Facility where to allocate the public IP address block, makes sense only for type==public_ipv4, must be empty for type==global_ipv4
	Facility interface{}
	// The packet project ID where to allocate the address block
	ProjectId interface{}
	// The number of allocated /32 addresses, a power of 2
	Quantity interface{}
	// Either "globalIpv4" or "publicIpv4", defaults to "publicIpv4" for backward compatibility
	Type interface{}
}
