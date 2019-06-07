// Copyright 2016-2018, Pulumi Corporation.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

export let C2LargeARM:  Plan = "c2.large.arm";
export let C2MediumX86: Plan = "c2.medium.x86";
export let C1SmallX86:  Plan = "baremetal_1";
export let C1LargeARM:  Plan = "baremetal_2a";
export let C1XLargeX86: Plan = "baremetal_3";
export let X2XLargeX86: Plan = "x2.xlarge.x86";
export let X1SmallX86:  Plan = "baremetal_1e";
export let G2LargeX86:  Plan = "g2.large.x86";
export let M2XLargeX86: Plan = "m2.xlarge.x86";
export let M1XLargeX86: Plan = "baremetal_2";
export let T1SmallX86:  Plan = "baremetal_0";
export let S1LargeX86:  Plan = "baremetal_s";


/**
 * A Plan represents any valid Packet.net Plan that may be deployed.
 */
export type Plan =
    "c2.large.arm"  |
    "c2.medium.x86" |
    "g2.large.x86"  |
    "m2.xlarge.x86" |
    "x2.xlarge.x86" |
    "baremetal_2a"  |
    "baremetal_1"   |
    "baremetal_3"   |
    "baremetal_2"   |
    "baremetal_s"   |
    "baremetal_0"   |
    "baremetal_1e"  ;

