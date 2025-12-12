# EIGRP Multipoint Bandwidth Pacing

## Scenario

A large international ISP has hired you as one of their network engineers. The ISP still has a fairly large customer that is using an older frame-relay network. All of your colleagues are too busy working with MPLS and you are the only one who is capable of fixing frame-relay problems. The network is experiencing congestion especially when router Paris is sending traffic to router New York. Can you fix this network?

## Goal

- All IP addresses have been preconfigured for you as specified in the topology picture.
- Every router has a loopback0 interface:
  - Tilburg: 1.1.1.1 /24
  - NewDelhi: 2.2.2.2 /24
  - Berlin: 3.3.3.3 /24
  - Paris: 4.4.4.4 /24
  - NewYork: 5.5.5.5 /24
- You are not allowed to make any changes to the frame-relay configurations.
- The ISP has configured the following CIR for each PVC:
  - NewDelhi: 128kbps
  - Berlin: 128kbps
  - Paris: 256kbps
  - NewYork: 64kbps
- Configure EIGRP AS 1 on all routers and make sure you have full connectivity.
- Configure your network so the bandwidth reflects the CIR on the PVCs and there are no congestion problems with EIGRP.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology](./topology-eigrp-multipoint-bandwidth-pacing.png)
