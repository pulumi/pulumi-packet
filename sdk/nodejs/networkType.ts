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

export module NetworkTypes {
    export const Layer3:           NetworkType = "layer3";
    export const Hybrid:           NetworkType = "hybrid";
    export const Layer2Individual: NetworkType = "layer2-individual";
    export const Layer2Bonded:     NetworkType = "layer2-bonded";
}

export type NetworkType =
    "layer3"            |
    "hybrid"            |
    "layer2-individual" |
    "layer2-bonded"     ;
