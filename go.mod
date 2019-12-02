module github.com/pulumi/pulumi-packet

go 1.12

require (
	github.com/hashicorp/terraform-plugin-sdk v1.1.1
	github.com/pkg/errors v0.8.1
	github.com/pulumi/pulumi v1.6.0
	github.com/pulumi/pulumi-terraform-bridge v1.4.3
	github.com/terraform-providers/terraform-provider-packet v0.0.0-20191105195844-7177a3d7bec9
)

replace github.com/Azure/go-autorest => github.com/Azure/go-autorest v12.4.3+incompatible
