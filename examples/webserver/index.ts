// Copyright 2016-2017, Pulumi Corporation.  All rights reserved.

import * as packet from "@pulumi/packet";
import * as fs from "fs";

let project = new packet.Project("project", {
    name: "pulumi",
});

let sshkey = new packet.SSHKey("key", {
    name: "mykey",
    publicKey: fs.readFileSync("/Users/luke/.ssh/id_rsa.pub").toString(),
});

let vm = new packet.Device("vm", {
    facility: "ewr1",
    billingCycle: "hourly",
    hostname: "lukehoban",
    operatingSystem: "coreos_stable",
    plan: "baremetal_0",
    projectId:  project.id,
}, { dependsOn: [sshkey] });

export let ip = vm.accessPublicIpv4;
