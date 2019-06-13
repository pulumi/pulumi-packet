// Copyright 2016-2017, Pulumi Corporation.  All rights reserved.

import * as packet from "@pulumi/packet";

let project = new packet.Project("project", {
    name: "pulumi",
});

let vm = new packet.Device("vm", {
    facilities: [packet.Facilities.EWR1],
    billingCycle: packet.BillingCycles.Hourly,
    hostname: "lukehoban",
    operatingSystem: packet.OperatingSystems.CoreOSStable,
    plan: packet.Plans.T1SmallX86,
    projectId:  project.id,
    ipAddressTypes: [packet.IpAddressTypes.PublicIPv4, packet.IpAddressTypes.PrivateIPv4, packet.IpAddressTypes.PublicIPv6]
});

export let ip = vm.accessPublicIpv4;
