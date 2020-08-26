[![Actions Status](https://github.com/pulumi/pulumi-packet/workflows/master/badge.svg)](https://github.com/pulumi/pulumi-packet/actions)
[![Slack](http://www.pulumi.com/images/docs/badges/slack.svg)](https://slack.pulumi.com)
[![NPM version](https://badge.fury.io/js/%40pulumi%2Fpacket.svg)](https://www.npmjs.com/package/@pulumi/packet)
[![Python version](https://badge.fury.io/py/pulumi-packet.svg)](https://pypi.org/project/pulumi-packet)
[![NuGet version](https://badge.fury.io/nu/pulumi.packet.svg)](https://badge.fury.io/nu/pulumi.packet)
[![PkgGoDev](https://pkg.go.dev/badge/github.com/pulumi/pulumi-packet/sdk/v3/go)](https://pkg.go.dev/github.com/pulumi/pulumi-packet/sdk/v3/go)
[![License](https://img.shields.io/npm/l/%40pulumi%2Fpulumi.svg)](https://github.com/pulumi/pulumi-packet/blob/master/LICENSE)

# Packet provider

The Packet resource provider for Pulumi lets you use [Packet](https://www.packet.com/) resources in your cloud programs.  To use
this package, please [install the Pulumi CLI first](https://pulumi.io/).


## Installing

This package is available in many languages in the standard packaging formats.

### Node.js (Java/TypeScript)

To use from JavaScript or TypeScript in Node.js, install using either `npm`:

    $ npm install @pulumi/packet

or `yarn`:

    $ yarn add @pulumi/packet

### Python

To use from Python, install using `pip`:

    $ pip install pulumi_packet

### Go

To use from Go, use `go get` to grab the latest version of the library

    $ go get github.com/pulumi/pulumi-packet/sdk/v2/go/...
    
### .NET

To use from .NET, install using `dotnet add package`:

    $ dotnet add package Pulumi.Packet

## Configuration

The following configuration points are available:

- `packet:authToken` - (Required) This is your Packet API Auth token. This can also be specified with the 
  `PACKET_AUTH_TOKEN` shell environment variable.

## Reference

For further information, please visit [the Packet provider docs](https://www.pulumi.com/docs/intro/cloud-providers/packet) or for detailed reference documentation, please visit [the API docs](https://www.pulumi.com/docs/reference/pkg/packet).
