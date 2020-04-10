module github.com/pulumi/pulumi-packet/provider/v2

go 1.13

require (
	github.com/hashicorp/terraform-plugin-sdk v1.7.0
	github.com/pulumi/pulumi-terraform-bridge/v2 v2.0.0-beta.1
	github.com/pulumi/pulumi/sdk/v2 v2.0.0-beta.3
	github.com/terraform-providers/terraform-provider-packet v1.7.3-0.20200323143909-5faafa6f60de
)

replace github.com/Azure/go-autorest => github.com/Azure/go-autorest v12.4.3+incompatible
