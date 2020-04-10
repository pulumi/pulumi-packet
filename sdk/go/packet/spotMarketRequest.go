// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package packet

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides a Packet Spot Market Request resource to allow you to
// manage spot market requests on your account. For more detail on Spot Market, see [this article in Packing documentaion](https://www.packet.com/developers/docs/getting-started/deployment-options/spot-market/).
type SpotMarketRequest struct {
	pulumi.CustomResourceState

	// Maximum number devices to be created
	DevicesMax pulumi.IntOutput `pulumi:"devicesMax"`
	// Miniumum number devices to be created
	DevicesMin pulumi.IntOutput `pulumi:"devicesMin"`
	// Facility IDs where devices should be created
	Facilities pulumi.StringArrayOutput `pulumi:"facilities"`
	// Device parameters. See device resource for details
	InstanceParameters SpotMarketRequestInstanceParametersOutput `pulumi:"instanceParameters"`
	// Maximum price user is willing to pay per hour per device
	MaxBidPrice pulumi.Float64Output `pulumi:"maxBidPrice"`
	// Project ID
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed
	WaitForDevices pulumi.BoolPtrOutput `pulumi:"waitForDevices"`
}

// NewSpotMarketRequest registers a new resource with the given unique name, arguments, and options.
func NewSpotMarketRequest(ctx *pulumi.Context,
	name string, args *SpotMarketRequestArgs, opts ...pulumi.ResourceOption) (*SpotMarketRequest, error) {
	if args == nil || args.DevicesMax == nil {
		return nil, errors.New("missing required argument 'DevicesMax'")
	}
	if args == nil || args.DevicesMin == nil {
		return nil, errors.New("missing required argument 'DevicesMin'")
	}
	if args == nil || args.Facilities == nil {
		return nil, errors.New("missing required argument 'Facilities'")
	}
	if args == nil || args.InstanceParameters == nil {
		return nil, errors.New("missing required argument 'InstanceParameters'")
	}
	if args == nil || args.MaxBidPrice == nil {
		return nil, errors.New("missing required argument 'MaxBidPrice'")
	}
	if args == nil || args.ProjectId == nil {
		return nil, errors.New("missing required argument 'ProjectId'")
	}
	if args == nil {
		args = &SpotMarketRequestArgs{}
	}
	var resource SpotMarketRequest
	err := ctx.RegisterResource("packet:index/spotMarketRequest:SpotMarketRequest", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSpotMarketRequest gets an existing SpotMarketRequest resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSpotMarketRequest(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SpotMarketRequestState, opts ...pulumi.ResourceOption) (*SpotMarketRequest, error) {
	var resource SpotMarketRequest
	err := ctx.ReadResource("packet:index/spotMarketRequest:SpotMarketRequest", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SpotMarketRequest resources.
type spotMarketRequestState struct {
	// Maximum number devices to be created
	DevicesMax *int `pulumi:"devicesMax"`
	// Miniumum number devices to be created
	DevicesMin *int `pulumi:"devicesMin"`
	// Facility IDs where devices should be created
	Facilities []string `pulumi:"facilities"`
	// Device parameters. See device resource for details
	InstanceParameters *SpotMarketRequestInstanceParameters `pulumi:"instanceParameters"`
	// Maximum price user is willing to pay per hour per device
	MaxBidPrice *float64 `pulumi:"maxBidPrice"`
	// Project ID
	ProjectId *string `pulumi:"projectId"`
	// On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed
	WaitForDevices *bool `pulumi:"waitForDevices"`
}

type SpotMarketRequestState struct {
	// Maximum number devices to be created
	DevicesMax pulumi.IntPtrInput
	// Miniumum number devices to be created
	DevicesMin pulumi.IntPtrInput
	// Facility IDs where devices should be created
	Facilities pulumi.StringArrayInput
	// Device parameters. See device resource for details
	InstanceParameters SpotMarketRequestInstanceParametersPtrInput
	// Maximum price user is willing to pay per hour per device
	MaxBidPrice pulumi.Float64PtrInput
	// Project ID
	ProjectId pulumi.StringPtrInput
	// On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed
	WaitForDevices pulumi.BoolPtrInput
}

func (SpotMarketRequestState) ElementType() reflect.Type {
	return reflect.TypeOf((*spotMarketRequestState)(nil)).Elem()
}

type spotMarketRequestArgs struct {
	// Maximum number devices to be created
	DevicesMax int `pulumi:"devicesMax"`
	// Miniumum number devices to be created
	DevicesMin int `pulumi:"devicesMin"`
	// Facility IDs where devices should be created
	Facilities []string `pulumi:"facilities"`
	// Device parameters. See device resource for details
	InstanceParameters SpotMarketRequestInstanceParameters `pulumi:"instanceParameters"`
	// Maximum price user is willing to pay per hour per device
	MaxBidPrice float64 `pulumi:"maxBidPrice"`
	// Project ID
	ProjectId string `pulumi:"projectId"`
	// On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed
	WaitForDevices *bool `pulumi:"waitForDevices"`
}

// The set of arguments for constructing a SpotMarketRequest resource.
type SpotMarketRequestArgs struct {
	// Maximum number devices to be created
	DevicesMax pulumi.IntInput
	// Miniumum number devices to be created
	DevicesMin pulumi.IntInput
	// Facility IDs where devices should be created
	Facilities pulumi.StringArrayInput
	// Device parameters. See device resource for details
	InstanceParameters SpotMarketRequestInstanceParametersInput
	// Maximum price user is willing to pay per hour per device
	MaxBidPrice pulumi.Float64Input
	// Project ID
	ProjectId pulumi.StringInput
	// On resource creation - wait until all desired devices are active, on resource destruction - wait until devices are removed
	WaitForDevices pulumi.BoolPtrInput
}

func (SpotMarketRequestArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*spotMarketRequestArgs)(nil)).Elem()
}
