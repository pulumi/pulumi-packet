// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package packet

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a Packet device datasource.
// 
// > **Note:** All arguments including the `rootPassword` and `userData` will be stored in
//  the raw state as plain-text.
// [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
// 
// > This content is derived from https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/d/device.html.markdown.
func LookupDevice(ctx *pulumi.Context, args *LookupDeviceArgs, opts ...pulumi.InvokeOption) (*LookupDeviceResult, error) {
	var rv LookupDeviceResult
	err := ctx.Invoke("packet:index/getDevice:getDevice", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getDevice.
type LookupDeviceArgs struct {
	// Device ID
	DeviceId *string `pulumi:"deviceId"`
	// The device name
	Hostname *string `pulumi:"hostname"`
	// The id of the project in which the devices exists
	ProjectId *string `pulumi:"projectId"`
}


// A collection of values returned by getDevice.
type LookupDeviceResult struct {
	// The ipv4 private IP assigned to the device
	AccessPrivateIpv4 string `pulumi:"accessPrivateIpv4"`
	// The ipv4 management IP assigned to the device
	AccessPublicIpv4 string `pulumi:"accessPublicIpv4"`
	// The ipv6 management IP assigned to the device
	AccessPublicIpv6 string `pulumi:"accessPublicIpv6"`
	AlwaysPxe bool `pulumi:"alwaysPxe"`
	// The billing cycle of the device (monthly or hourly)
	BillingCycle string `pulumi:"billingCycle"`
	// Description string for the device
	Description string `pulumi:"description"`
	DeviceId string `pulumi:"deviceId"`
	// The facility where the device is deployed.
	Facility string `pulumi:"facility"`
	// The id of hardware reservation which this device occupies
	HardwareReservationId string `pulumi:"hardwareReservationId"`
	Hostname string `pulumi:"hostname"`
	// id is the provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	IpxeScriptUrl string `pulumi:"ipxeScriptUrl"`
	// L2 network type of the device, one of "layer3", "layer2-bonded", "layer2-individual", "hybrid"
	NetworkType string `pulumi:"networkType"`
	// The device's private and public IP (v4 and v6) network details. When a device is run without any special network configuration, it will have 3 networks: 
	// * Public IPv4 at `packet_device.name.network.0`
	// * IPv6 at `packet_device.name.network.1`
	// * Private IPv4 at `packet_device.name.network.2`
	// Elastic addresses then stack by type - an assigned public IPv4 will go after the management public IPv4 (to index 1), and will then shift the indices of the IPv6 and private IPv4. Assigned private IPv4 will go after the management private IPv4 (to the end of the network list).
	// The fields of the network attributes are:
	Networks []GetDeviceNetwork `pulumi:"networks"`
	// The operating system running on the device
	OperatingSystem string `pulumi:"operatingSystem"`
	// The hardware config of the device
	Plan string `pulumi:"plan"`
	// Ports assigned to the device
	Ports []GetDevicePort `pulumi:"ports"`
	ProjectId string `pulumi:"projectId"`
	PublicIpv4SubnetSize int `pulumi:"publicIpv4SubnetSize"`
	// Root password to the server (if still available)
	RootPassword string `pulumi:"rootPassword"`
	// List of IDs of SSH keys deployed in the device, can be both user or project SSH keys
	SshKeyIds []string `pulumi:"sshKeyIds"`
	// The state of the device
	State string `pulumi:"state"`
	Storage string `pulumi:"storage"`
	// Tags attached to the device
	Tags []string `pulumi:"tags"`
}

