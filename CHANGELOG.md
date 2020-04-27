CHANGELOG
=========

## HEAD (Unreleased)
* Regenerate datasource examples to be async

---

## 2.0.1 (2020-04-23)
* Upgrade to v2.8.1 of the Packet Terraform Provider

## 2.0.0 (2020-04-17)
* Upgrade to Pulumi v2.0.0
* Upgrade to pulumi-terraform-bridge v2.0.0

## 1.10.0 (2020-04-02)
* Upgrade to Pulumi v1.13.1
* Upgrade to pulumi-terraform-bridge v1.8.4
* Upgrade terraform sdk to v1.7.0
* Update layout to support go Modules

## 1.9.0 (2020-03-24)
* Upgrade to v2.8.0 of the Packet Terraform Provider

## 1.8.0 (2020-03-23)
* Upgrade to Pulumi v1.12.1
* Upgrade to pulumi-terraform-bridge v1.8.2

## 1.7.0 (2020-02-27)
* Upgrade to v2.7.5 of the Packet Terraform Provider

## 1.6.0 (2020-01-29)
* Upgrade to v2.7.4 of the Packet Terraform Provider
* Upgrade to pulumi-terraform-bridge v1.6.4

## 1.5.0 (2020-01-06)
* Upgrade to pulumi-terraform-bridge v1.5.2

## 1.4.0 (2019-12-13)
* Upgrade to v2.7.3 of the Packet Terraform Provider
* Namespace names in .NET SDK are adjusted to PascalCase
([#49](https://github.com/pulumi/pulumi-packet/pull/49)).

## 1.3.0 (2019-12-11)
* Upgrade to v2.7.2 of the Packet Terraform Provider

  **PLEASE NOTE:**
  `packet.Connect` has been removed from this resource. It was `deprecated` in
  v1.2.0 and the underlying resource was removed in this release

## 1.2.0 (2019-12-04)
* Upgrade to support go 1.13.x
* Upgrade to pulumi-terraform-bridge v1.4.3

## 1.1.0 (2019-11-15)
* Upgrade to v2.6.1 of the Packet Terraform Provider
* Add support for DotNet SDK Generation

## 1.0.0 (2019-10-18)
* Regenerate SDK based on tf2pulumi 0.6.0
* Upgrade to v2.5.0 of the Packet Terraform Provider

## 0.4.13 (2019-09-24)
* Upgrade to v2.4.0 of the Packet Terraform Provider

## 0.4.12 (2019-09-05)
* Upgrade to Pulumi v1.0.0
* Include missing support for `packet.getDevice` datasource

## 0.4.11 (2019-08-29)
* Upgrade to pulumi-terraform 3f206601e7

## 0.4.10 (2019-08-20)
* Depend on latest pulumi package

## 0.4.9 (2019-08-09)
* Upgrade to pulumi-terraform@9db2fc93cd

## 0.4.8 (2019-08-08)
* Update to pulumi-terraform@013b95b1c8
* Upgrade to v2.3.0 of the Packet Terraform Provider

## 0.4.7 (2019-07-09)
* Fix detailed diffs with nested computed values.

## 0.4.6 (2019-07-08)
* Communicate detailed information about the difference between a resource's desired and actual state during a Pulumi update

## 0.4.5 (2019-06-21)
* Update to pulumi-terraform@3635bed3a5 which stops maps containing `.` being treated as nested maps.

## 0.4.4 (2019-06-15)
* Add TypeScript type guards for each resource class
* Add constants for Facility types
* Add constants for Plan types
* Add constants for OperatingSystem types
* Add constants for BillingCycle types
* Add constants for NetworkType types
* Add constants for IpAddressType types
* Add constants for IpBlockType types

## 0.4.3 (2019-04-05)
* Update to v2.2.1 of the Packet.net provider

## 0.4.2 (2019-05-28)
* Update to v2.2.0 of the Packet.net provider

## 0.4.1 (2019-04-30)
* Update to v2.1.0 of the Packet.net provider
* BREAKING: the `facility` property has been deprecated in favour of the `facilities` property throughout the provider

## 0.3.2 (2019-04-22)
* Update to v1.6.1 of the Packet.net Terraform provider

## 0.3.1 (2019-04-05)
* Update to v1.6.0 of the Packet.net Terraform provider

## 0.3.0 (2019-03-06)
* Update to the latest version of the `pulumi` SDK

## 0.2.0 (2019-02-22)
* Update to v1.4.1 of the Packet.net Terraform provider
* Add support for the `deleteBeforeReplace` resource option and improved delete-before-replace behaviour introduced in Pulumi v0.16.14

## 0.1.0 (2019-02-01)
* Initial Release
