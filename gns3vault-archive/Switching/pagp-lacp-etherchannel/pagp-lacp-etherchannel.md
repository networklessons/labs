# PAgP LACP Etherchannel

## Scenario

**For this lab you need REAL hardware. You can't use switches in GNS3!**

**You need at least Catalyst 2950 switches for this lab.**

You are a master of spanning tree and specialized in migration scenarios. Corkscrew inc. is one of your customers and they are having issues with their switches. There are many VLANs in the network and you would like to reduce the number of spanning tree calculations. As a result you decide to implement MST (Multiple Spanning Tree) for them.

## Goal

- Configure PAgP between SW1 and SW2. SW1 should actively try to form an Etherchannel and SW2 should only respond to requests.
- Configure LACP between SW1 and SW3. SW1 should actively try to form an Etherchannel and SW3 should only respond to requests.
- Configure an Etherchannel between SW2 and SW3. You are not allowed to use any protocol for negotiation.
- Configure the etherchannel between SW1 and SW2 to use destination MAC address load-balancing.

## IOS

Basic IOS for the switches should be sufficient. No special features needed.

## Topology

![Network Topology](./topology-pagp-lacp-etherchannel.png)

## Video Solution

[YouTube Video](http://www.youtube.com/watch?v=SohMnr_H4R4)
