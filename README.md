[![Build Status](https://travis-ci.com/pulumi/pulumi-packet.svg?token=eHg7Zp5zdDDJfTjY8ejq&branch=master)](https://travis-ci.com/pulumi/pulumi-packet)

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

    $ go get github.com/pulumi/pulumi-packet/sdk/go/...
    
## Configuration

The following configuration points are available:

- `packet:authToken` - (Required) This is your Packet API Auth token. This can also be specified with the 
  `PACKET_AUTH_TOKEN` shell environment variable.

## Reference

For detailed reference documentation, please visit [the API docs][1].


[1]: https://pulumi.io/reference/pkg/nodejs/@pulumi/packet/index.html
