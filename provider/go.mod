module github.com/pulumi/pulumi-packet/provider/v3

go 1.14

require (
	github.com/hashicorp/terraform-plugin-sdk v1.7.0
	github.com/pulumi/pulumi-terraform-bridge/v2 v2.7.3
	github.com/pulumi/pulumi/sdk/v2 v2.9.1-0.20200825190708-910aa96016cd
	github.com/terraform-providers/terraform-provider-packet v1.7.3-0.20200721180633-2fe2b625ccf9
)

replace github.com/Azure/go-autorest => github.com/Azure/go-autorest v12.4.3+incompatible
