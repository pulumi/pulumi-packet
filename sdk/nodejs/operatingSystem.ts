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

export let Alpine3:           OperatingSystem = "alpine_3";
export let CentOS6:           OperatingSystem = "centos_6";
export let CentOS7:           OperatingSystem = "centos_7";
export let CoreOSAlpha:       OperatingSystem = "coreos_alpha";
export let CoreOSBeta:        OperatingSystem = "coreos_beta";
export let CoreOSStable:      OperatingSystem = "coreos_stable";
export let CustomIPXE:        OperatingSystem = "custom_ipxe";
export let Debian8:           OperatingSystem = "debian_8";
export let Debian9:           OperatingSystem = "debian_9";
export let FreeBSD10_4:       OperatingSystem = "freebsd_10_4";
export let FreeBSD11_1:       OperatingSystem = "freebsd_11_1";
export let FreeBSD11_2:       OperatingSystem = "freebsd_11_2";
export let FreeBSD12Testing:  OperatingSystem = "freebsd_12_testing";
export let NixOS18_03:        OperatingSystem = "nixos_18_03";
export let NixOS19_03:        OperatingSystem = "nixos_19_03";
export let OpenSUSE42_3:      OperatingSystem = "opensuse_42_3";
export let RancherOS:         OperatingSystem = "rancher";
export let RHEL7:             OperatingSystem = "rhel_7";
export let ScientificLinux6:  OperatingSystem = "scientific_6";
export let SLES12SP3:         OperatingSystem = "suse_sles12_sp3";
export let Ubuntu1404:        OperatingSystem = "ubuntu_14_04";
export let Ubuntu1604:        OperatingSystem = "ubuntu_16_04";
export let Ubuntu1710:        OperatingSystem = "ubuntu_17_10";
export let Ubuntu1804:        OperatingSystem = "ubuntu_18_04";
export let VMWareEsxi6_5:     OperatingSystem = "vmware_esxi_6_5";
export let Windows2012R2:     OperatingSystem = "windows_2012_r2";
export let Windows2016:       OperatingSystem = "windows_2016";

export type OperatingSystem =
    "alpine_3"           |
    "centos_6"           |
    "centos_7"           |
    "coreos_alpha"       |
    "coreos_beta"        |
    "coreos_stable"      |
    "custom_ipxe"        |
    "debian_8"           |
    "debian_9"           |
    "freebsd_10_4"       |
    "freebsd_11_1"       |
    "freebsd_11_2"       |
    "freebsd_12_testing" |
    "nixos_18_03"        |
    "nixos_19_03"        |
    "opensuse_42_3"      |
    "rancher"            |
    "rhel_7"             |
    "scientific_6"       |
    "suse_sles12_sp3"    |
    "ubuntu_14_04"       |
    "ubuntu_16_04"       |
    "ubuntu_17_10"       |
    "ubuntu_18_04"       |
    "vmware_esxi_6_5"    |
    "windows_2012_r2"    |
    "windows_2016"       ;

