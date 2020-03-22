module github.com/pulumi/pulumi-packet

go 1.13

require (
	github.com/hashicorp/terraform-plugin-sdk v1.1.1
	github.com/pkg/errors v0.8.1
	github.com/pulumi/pulumi v1.12.2-0.20200313044354-8111d33438b9
	github.com/pulumi/pulumi-terraform-bridge v1.8.2
	github.com/terraform-providers/terraform-provider-packet v1.7.3-0.20200226132411-763d24acef79
)

replace github.com/Azure/go-autorest => github.com/Azure/go-autorest v12.4.3+incompatible
