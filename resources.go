// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package packet

import (
	"unicode"

	"github.com/hashicorp/terraform/helper/schema"
	"github.com/hashicorp/terraform/terraform"
	"github.com/pulumi/pulumi-terraform/pkg/tfbridge"
	"github.com/pulumi/pulumi/pkg/resource"
	"github.com/pulumi/pulumi/pkg/tokens"
	"github.com/terraform-providers/terraform-provider-packet/packet"
)

// all of the token components used below.
const (
	// packages:
	mainPkg = "packet"
	// modules:
	mainMod = "index" // the y module
)

// makeMember manufactures a type token for the package and the given module and type.
func makeMember(mod string, mem string) tokens.ModuleMember {
	return tokens.ModuleMember(mainPkg + ":" + mod + ":" + mem)
}

// makeType manufactures a type token for the package and the given module and type.
func makeType(mod string, typ string) tokens.Type {
	return tokens.Type(makeMember(mod, typ))
}

// makeDataSource manufactures a standard resource token given a module and resource name.  It
// automatically uses the main package and names the file by simply lower casing the data source's
// first character.
func makeDataSource(mod string, res string) tokens.ModuleMember {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]
	return makeMember(mod+"/"+fn, res)
}

// makeResource manufactures a standard resource token given a module and resource name.  It
// automatically uses the main package and names the file by simply lower casing the resource's
// first character.
func makeResource(mod string, res string) tokens.Type {
	fn := string(unicode.ToLower(rune(res[0]))) + res[1:]
	return makeType(mod+"/"+fn, res)
}

// preConfigureCallback is called before the providerConfigure function of the underlying provider.
// It should validate that the provider can be configured, and provide actionable errors in the case
// it cannot be. Configuration variables can be read from `vars` using the `stringValue` function -
// for example `stringValue(vars, "accessKey")`.
func preConfigureCallback(vars resource.PropertyMap, c *terraform.ResourceConfig) error {
	return nil
}

// Provider returns additional overlaid schema and metadata associated with the provider..
func Provider() tfbridge.ProviderInfo {
	// Instantiate the Terraform provider
	p := packet.Provider().(*schema.Provider)

	// Create a Pulumi provider mapping
	prov := tfbridge.ProviderInfo{
		P:           p,
		Name:        "packet",
		Description: "A Pulumi package for creating and managing X cloud resources.",
		Keywords:    []string{"pulumi", "packet"},
		License:     "Apache-2.0",
		Homepage:    "https://pulumi.io",
		Repository:  "https://github.com/pulumi/pulumi-packet",
		Config: map[string]*tfbridge.SchemaInfo{
			"auth_token": {
				Default: &tfbridge.DefaultInfo{
					EnvVars: []string{"PACKET_AUTH_TOKEN"},
				},
			},
		},
		PreConfigureCallback: preConfigureCallback,
		Resources: map[string]*tfbridge.ResourceInfo{
			// Map each resource in the Terraform provider to a Pulumi type. An example
			// is below.
			"packet_bgp_session": {Tok: makeResource(mainMod, "BgpSession")},
			"packet_connect": {
				Tok: makeResource(mainMod, "Connect"),
				Fields: map[string]*tfbridge.SchemaInfo{
					"facility": {
						Type: makeType(mainMod, "Facility"),
					},
				},
			},
			"packet_device": {
				Tok: makeResource(mainMod, "Device"),
				Fields: map[string]*tfbridge.SchemaInfo{
					"billing_cycle": {
						Type: makeType(mainMod, "BillingCycle"),
					},
					"facilities": {
						Elem: &tfbridge.SchemaInfo{Type: makeType(mainMod, "Facility")},
					},
					"network_type": {
						Type: makeType(mainMod, "NetworkType"),
					},
					"operating_system": {
						Type: makeType(mainMod, "OperatingSystem"),
					},
					"plan": {
						Type: makeType(mainMod, "Plan"),
					},
				},
			},
			"packet_ip_attachment":        {Tok: makeResource(mainMod, "IpAttachment")},
			"packet_organization":         {Tok: makeResource(mainMod, "Organization")},
			"packet_port_vlan_attachment": {Tok: makeResource(mainMod, "PortVlanAttachment")},
			"packet_project":              {Tok: makeResource(mainMod, "Project")},
			"packet_project_ssh_key":      {Tok: makeResource(mainMod, "ProjectSshKey")},
			"packet_reserved_ip_block": {
				Tok: makeResource(mainMod, "ReservedIpBlock"),
				Fields: map[string]*tfbridge.SchemaInfo{
					"facility": {
						Type: makeType(mainMod, "Facility"),
					},
				},
			},
			"packet_spot_market_request": {Tok: makeResource(mainMod, "SpotMarketRequest")},
			"packet_ssh_key":             {Tok: makeResource(mainMod, "SshKey")},
			"packet_vlan": {
				Tok: makeResource(mainMod, "Vlan"),
				Fields: map[string]*tfbridge.SchemaInfo{
					"facility": {
						Type: makeType(mainMod, "Facility"),
					},
				},
			},
			"packet_volume": {
				Tok: makeResource(mainMod, "Volume"),
				Fields: map[string]*tfbridge.SchemaInfo{
					"facility": {
						Type: makeType(mainMod, "Facility"),
					},
				},
			},
			"packet_volume_attachment": {Tok: makeResource(mainMod, "VolumeAttachment")},
		},
		DataSources: map[string]*tfbridge.DataSourceInfo{
			// Map each resource in the Terraform provider to a Pulumi function. An example
			// is below.
			"packet_operating_system":    {Tok: makeDataSource(mainMod, "getOperatingSystem")},
			"packet_precreated_ip_block": {Tok: makeDataSource(mainMod, "getPrecreatedIpBlock")},
			"packet_spot_market_price":   {Tok: makeDataSource(mainMod, "getSpotMarketPrice")},
		},
		JavaScript: &tfbridge.JavaScriptInfo{
			// List any npm dependencies and their versions
			Dependencies: map[string]string{
				"@pulumi/pulumi": "^0.17.1",
			},
			DevDependencies: map[string]string{
				"@types/node": "^8.0.25", // so we can access strongly typed node definitions.
				"@types/mime": "^2.0.0",
			},
			// See the documentation for tfbridge.OverlayInfo for how to lay out this
			// section, or refer to the AWS provider. Delete this section if there are
			// no overlay files.
			Overlay: &tfbridge.OverlayInfo{
				DestFiles: []string{
					"billingCycle.ts",
					"facility.ts",
					"networkType.ts",
					"operatingSystem.ts",
					"plan.ts",
				},
			},
		},
		Python: &tfbridge.PythonInfo{
			// List any Python dependencies and their version ranges
			Requires: map[string]string{
				"pulumi": ">=0.17.1,<0.18.0",
			},
		},
	}

	return prov
}
