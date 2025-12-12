# VLANs and Trunks

![Network Topology](./topology-vlans-and-trunks.png)

## Scenario:

**_For this lab you need REAL hardware. You can't use switches in GNS3!_**

**_You only need layer 2 switches for this lab. The Cisco Catalyst 2950 or higher will work._**

The school you work for has a flat network design and they only use layer 2 switches. One of the teachers built the network in his own time but he has no clue what he exactly did. There is only one VLAN and there have been issues with applications that generate too much broadcast traffic. It's up to you to segment the network and implement some VLANs.

## Goal:

- Create the following VLANs and configure the correct names:
  - VLAN 10: name Engineering
  - VLAN 20: name Marketing
  - VLAN 30: name Research
  - VLAN 40: name Sales
  - VLAN 50: name Management
- Configure fa0/1 on SW1 as an access interface in VLAN 10
- Configure fa0/2 on SW2 as an access interface in VLAN 20
- One of the links between SW1 and SW2 should use ISL encapsulation
- One of the links between SW2 and SW3 is not allowed to dynamically negotiate a trunking protocol
- One of the links between SW1 and SW3 should never send any DTP messages
- Only VLAN 1, 10 and VLAN 20 are allowed between SW1 and SW2
- Only VLAN 1, 10, 20, 40 and 50 are allowed between SW2 and SW3
- The native VLAN between SW1 and SW3 should be VLAN 50 on both links

## IOS:

Basic IOS for the switches should be sufficient. No special features needed.

## Topology:

## Video Solution:

[Video Solution on YouTube](http://www.youtube.com/watch?v=k8OwNfTtRpU&)
