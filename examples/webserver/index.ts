// Copyright 2016-2017, Pulumi Corporation.  All rights reserved.

import * as packet from "@pulumi/packet";

let project = new packet.Project("project", {
    name: "pulumi",
});

let vm = new packet.Device("vm", {
    facilities: [packet.EWR1Facility],
    billingCycle: packet.HourlyBilling,
    hostname: "lukehoban",
    operatingSystem: packet.CoreOSStable,
    plan: packet.T1SmallX86,
    projectId:  project.id,
    ipAddressTypes: [packet.PublicIPv4, packet.PrivateIPv4, packet.PublicIPv6]
});

export let ip = vm.accessPublicIpv4;
