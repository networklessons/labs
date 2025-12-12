# MPLS VPN PE CE using OSPF & Sham-Link

![Network Topology](./topology-mpls-vpn-pe-ce-using-ospf.jpg)

## Scenario

You have been dreaming of starting your own ISP for years and now the moment is finally here. You bought a couple of brand new routers and you are about to implement your MPLS backbone. Your first customer has just signed a contract for connecting two sites so there is nothing stopping you. One of your routers will be the "P" router for the backbone. The other two routers will be used as "PE" router to connect the customer's end devices. Your customer is running RIP as their (IGP) internal routing protocol. Your backbone will use OSPF as the IGP....time to create your business!

## Goal

- All IP addresses have been preconfigured for you.
- Every router has a loopback0 interfaced configured as following:
  - HQ: 1.1.1.1 /25
  - PE1: 2.2.2.2 /25
  - P2: 3.3.3.3 /25
  - PE2: 4.4.4.4 /25
  - BRANCH: 5.5.5.5 /25
- Configure OSPF Area 0 at the provider side (Router PE1, PE2 and P).
- Advertise the loopback interfaces as well in OSPF.
- Ensure you have full reachability in the OSPF domain.
- Configure MPLS on all physical interfaces in the service provider domain, do not configure MPLS on physical interfaces pointing towards the customer.
- Configure VRF "customer" on PE1 and PE2 as following:
  - RD 100:1
  - Route-target both 1:100
- On router PE1 and PE2 add the interfaces pointing towards the customer to the VRF you just created.
- Ensure you can ping from within the VRF, try this as following on PE1:
  - `ping vrf customer 192.168.12.1`
- Configure OSPF Area 0 on router HQ and Branch. Advertise the loopbacks as well.
- Configure OSPF on router PE1 and PE2 for the correct VRF "customer".
- Ensure you receive prefixes from the customer routers on your PE routers.
- Configure BGP AS 1 between Router PE1 and PE2.
- Configure the correct BGP address families and make sure communities are sent between neighbors.
- Redistribute OSPF into BGP, use the correct address-family for the VRF "customer".
- Ensure you have full connectivity between router HQ and Branch. You should see each other's OSPF routes that have been carried over the service provider's MPLS backbone.
- The OSPF prefixes on the HQ and Branch router are showing up as O IA (Inter-Area). Change this so they show up as E2 routes.
- Enable OSPF on the serial link between router HQ and Branch, this will be a backup link in case the MPLS Backbone crashes.
- You notice packets are being sent through the backup serial link instead of the MPLS Backbone. Make sure all packets are sent through the MPLS Backbone without removing OSPF on the serial link or shutting down the interface.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

## Video Solution

[MPLS VPN PE CE using OSPF & Sham-Link - Video](http://www.youtube.com/watch?v=gCwrF6muDyM)
