module github.com/pulumi/pulumi-packet

go 1.12

require (
	github.com/hashicorp/terraform-plugin-sdk v1.1.1
	github.com/pkg/errors v0.8.1
	github.com/pulumi/pulumi v1.6.0
	github.com/pulumi/pulumi-terraform-bridge v1.4.3
	github.com/terraform-providers/terraform-provider-packet v1.7.3-0.20191206154114-4102b23d1af8
)

replace github.com/Azure/go-autorest => github.com/Azure/go-autorest v12.4.3+incompatible
