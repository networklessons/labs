# Frame Relay DE Marking

## Scenario

You are the owner of a small ISP company located in The Netherlands. Most of the equipment you have running is fairly old and you have multiple different serial links in use. Bandwidth is an issue and since you don't have the budget to replace any links you are looking for a cheaper solution...think you can compress things?

## Goal

- All IP addresses have been preconfigured for you.
- Configure Frame Relay encapsulation between router Chop and Slice.
- Configure a loopback0 interface with IP address 1.1.1.1 /24 on router Frank.
- Configure OSPF on all routers, ensure you have full connectivity.
- Configure DE marking on router Chop. All IP packets from network 1.1.1.0 /24 should be marked as Discard Eligible when they are sent to router Slice.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology](./topology-frame-relay-de-marking.png)
