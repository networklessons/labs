# EIGRP Point-to-Point Bandwidth Pacing

![Network Topology](./topology-eigrp-point-to-point-bandwidth-pacing.png)

## Scenario:

A large international ISP has hired you as one of their network engineers. The ISP still has a fairly large customer that is using an older frame-relay network. All of your colleagues are too busy working with MPLS and you are the only one who is capable of fixing frame-relay problems. Whenever router Tilburg is sending major EIGRP updates there are problems with congestion. Think you can tune EIGRP so this network won't have congestion anymore?

## Goal:

- All IP addresses have been preconfigured for you as specified in the topology picture.
- Every router has a loopback0 interface:
  - Tilburg: 1.1.1.1 /24
  - NewDelhi: 2.2.2.2 /24
  - Berlin: 3.3.3.3 /24
  - Paris: 4.4.4.4 /24
  - NewYork: 5.5.5.5 /24
- You are not allowed to make any changes to the frame-relay configurations.
- In this topology you can see 4 spoke routers but in reality there are 10 spoke routers. I didn't add them all to save CPU power when you run this topology. Each PVC has a CIR of 64kbps.
- Router Tilburg has a serial interface 0/0 that only has a physical bandwidth of 256kbps.
- Configure EIGRP AS 1 on all routers and make sure you have full connectivity.
- Whenever router Tilburg sends EIGRP updates to all spoke routers there is congestion because the physical bandwidth of serial interface s0/0 is only 256kbps.
- Configure your network so the bandwidth reflects the CIR on the PVCs and EIGRP will only use 50% of the CIR.

## IOS:

- c3640-jk9s-mz.124-16.bin

## Topology:
