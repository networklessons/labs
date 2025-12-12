# Spanning Tree BPDU Guard

![Network Topology](./topology-spanning-tree-bpdu-guard.png)

## Scenario:

**_For this lab you need REAL hardware. You can't use switches in GNS3!_**

**_You need at least Catalyst 2950 switches for this lab._**

You are working as the network engineer at a school located in Germany. The network has been having issues last month after students took a CCNA class. You want to make sure the access layer of the network is more secure. When students try to mess with spanning-tree it should block the interface they are connected to.

## Goal:

* Ensure all switches run PVST (default on most Cisco switches).
* Ensure that whenever you receive a BPDU from router Neo it will block the interface.
* After 400 seconds the interface should enable itself automatically again.

## IOS:

Basic IOS for the switches should be sufficient. No special features needed.

## Topology:

## Video Solution:

[Video: Spanning Tree BPDU Guard Solution](http://www.youtube.com/watch?v=1VI_WAk4AcU)
