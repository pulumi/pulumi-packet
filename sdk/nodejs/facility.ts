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

export const EWR1Facility: Facility = "ewr1";
export const SJC1Facility: Facility = "sjc1";
export const DFW1Facility: Facility = "dfw1";
export const DFW2Facility: Facility = "dfw2";
export const AMS1Facility: Facility = "ams1";
export const NRT1Facility: Facility = "nrt1";
export const SEA1Facility: Facility = "sea1";
export const LAX1Facility: Facility = "lax1";
export const ORD1Facility: Facility = "ord1";
export const ATL1Facility: Facility = "atl1";
export const IAD1Facility: Facility = "iad1";
export const SIN1Facility: Facility = "sin1";
export const HKG1Facility: Facility = "hkg1";
export const SYD1Facility: Facility = "syd1";
export const MRS1Facility: Facility = "mrs1";
export const YYZ1Facility: Facility = "yyz1";
export const FRA2Facility: Facility = "fra2";

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

