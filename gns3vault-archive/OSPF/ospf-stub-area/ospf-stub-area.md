# OSPF Stub Area

![Network Topology](./topology-ospf-stub-area.jpg)

## Scenario

You are working as a trainee for a company specialized in Fantasy E-books. Since the E-book market in fantasy stories isn't very promising at the moment the company is still using older network equipment. One of their routers is having performance problems because the routing table is becoming too big...it's up to you to find a solution!

## Goal

- All IP addresses have been preconfigured for you.
- Configure OSPF on both routers, use the Areas as specified in the topology picture.
- Router Algrim: Loopback0 should be in Area0
- Achieve full connectivity.
- Router Algrim: create additional loopbacks:
  - L1: 172.16.0.1 /24
  - L2: 172.16.1.1 /24
  - L3: 172.16.2.1 /24
  - L4: 172.16.3.1 /24
- Advertise these networks into OSPF, do not use the "network" command to achieve this.
- Take a look at the routing table of Router Barik, you should see all 4 networks. Make sure you can ping them.
- Change the area type of Area 1 so you don't see the 4 networks anymore but only 1 default route.
- Make sure you can still ping the 4 networks.

## Background

## IOS

- c3640-jk9s-mz.124-16.bin

## Video Solution

- [Watch on YouTube](http://www.youtube.com/watch?v=HaNG9yd4kWs)
