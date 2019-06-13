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

export module Facilities {
    export const EWR1: Facility = "ewr1";
    export const SJC1: Facility = "sjc1";
    export const DFW1: Facility = "dfw1";
    export const DFW2: Facility = "dfw2";
    export const AMS1: Facility = "ams1";
    export const NRT1: Facility = "nrt1";
    export const SEA1: Facility = "sea1";
    export const LAX1: Facility = "lax1";
    export const ORD1: Facility = "ord1";
    export const ATL1: Facility = "atl1";
    export const IAD1: Facility = "iad1";
    export const SIN1: Facility = "sin1";
    export const HKG1: Facility = "hkg1";
    export const SYD1: Facility = "syd1";
    export const MRS1: Facility = "mrs1";
    export const YYZ1: Facility = "yyz1";
    export const FRA2: Facility = "fra2";
}

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

