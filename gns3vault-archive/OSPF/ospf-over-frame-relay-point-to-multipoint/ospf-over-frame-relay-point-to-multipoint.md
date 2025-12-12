# OSPF Over Frame-Relay: Point-to-Multipoint

![Network Topology](./topology-ospf-over-frame-relay-point-to-multipoint.jpg)

## Scenario

As the senior network engineer for a Dutch fishing company you are responsible for connecting all the different branch offices to the main network. The WAN technology you are using is Frame Relay, and you need to run OSPF over this WAN connection.

## Goal

- The frame-relay switch has been preconfigured for you, as you can see in the topology picture the following PVCs has been configured:

  **Router Barracuda to Salmon:**
  - Barracuda: DLCI 102
  - Salmon: DLCI 201

  **Router Barracuda to Herring:**
  - Barracuda: DLCI 103
  - Salmon: DLCI 301

- Router Barracuda is the "Hub" router and the other 2 routers are the "Spoke" routers.
- Do not change any configuration on the Frame-Relay switch.
- Configure the following IP addresses:

  **Router Barracuda:**
  - S0/0: 192.168.123.1 /24
  - L0: 1.1.1.1 /24

  **Router Salmon:**
  - S0/0: 192.168.123.2 /24
  - L0: 2.2.2.2 /24

  **Router Herring:**
  - S0/0: 192.168.123.3 /24
  - L0: 3.3.3.3 /24

- Configure all serial interfaces for encapsulation Frame-Relay.
- Disable Frame-relay inverse arp on all serial interfaces.
- Configure the correct frame-relay map statements on all routers and make sure you can ping every IP address.
- Configure the OSPF network type to "point-to-multipoint" on all serial interfaces.
- Configure OSPF on all 3 routers, make sure you have full connectivity. All IP addresses including the loopbacks should be reachable.
- You are not allowed to use the "neighbor" command in the OSPF configuration.

---

## IOS

- c3640-jk9s-mz.124-16.bin

## Topology

## Video Solution

- [OSPF Over Frame-Relay Point-to-Multipoint Video](http://www.youtube.com/watch?v=TP1MkYHCru8)
