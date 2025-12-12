# PVST (Per Vlan Spanning Tree)

![Network Topology](./topology-pvst-per-vlan-spanning-tree.png)

## Scenario:

**_For this lab you need REAL hardware. You can't use switches in GNS3!_**

**_You need at least Catalyst 2950 switches for this lab._**

You are the network engineer for a company in Florida that is specialized in campus LAN designs. One of your customers is having issues with their network and it seems their spanning-tree topology has been misconfigured. The network has a number of non-Cisco devices so you need to run an IEEE version of spanning-tree.

## Goal:

* Ensure all switches run PVST (default on most Cisco switches).
* Create VLAN 10, 20 and 30 on all switches.
* Ensure SW1 is the root bridge for VLAN 10.
* Ensure SW2 is the root bridge for VLAN 20.
* Ensure SW3 is the root bridge for VLAN 30.
* Ensure SW2 prefers the path through SW3 to reach the root bridge in VLAN 10. You are only allowed to change the cost.
* Ensure SW3 prefers interface fa0/14 to reach the root bridge for VLAN 10. You are only allowed to change the port priority.
* Ensure BPDUs are sent every second for VLAN 20.
* Ensure the switches detect a problem in VLAN 30 after 6 seconds of not receiving BPDUs.

## IOS:

Basic IOS for the switches should be sufficient. No special features needed.

## Topology:

## Video Solution:

http://www.youtube.com/watch?v=EJEuC9Gkta8&
