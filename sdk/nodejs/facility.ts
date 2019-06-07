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

export let EWR1Facility: Facility = "ewr1";
export let SJC1Facility: Facility = "sjc1";
export let DFW1Facility: Facility = "dfw1";
export let DFW2Facility: Facility = "dfw2";
export let AMS1Facility: Facility = "ams1";
export let NRT1Facility: Facility = "nrt1";
export let SEA1Facility: Facility = "sea1";
export let LAX1Facility: Facility = "lax1";
export let ORD1Facility: Facility = "ord1";
export let ATL1Facility: Facility = "atl1";
export let IAD1Facility: Facility = "iad1";
export let SIN1Facility: Facility = "sin1";
export let HKG1Facility: Facility = "hkg1";
export let SYD1Facility: Facility = "syd1";
export let MRS1Facility: Facility = "mrs1";
export let YYZ1Facility: Facility = "yyz1";
export let FRA2Facility: Facility = "fra2";

/**
 * A Facility represents any valid Packet.net facility that may be targeted with deployments.
 */
export type Facility =
    "ewr1" |
    "sjc1" |
    "dfw1" |
    "dfw2" |
    "ams1" |
    "nrt1" |
    "sea1" |
    "lax1" |
    "ord1" |
    "atl1" |
    "iad1" |
    "sin1" |
    "hkg1" |
    "syd1" |
    "mrs1" |
    "yyz1" |
    "fra2" ;

