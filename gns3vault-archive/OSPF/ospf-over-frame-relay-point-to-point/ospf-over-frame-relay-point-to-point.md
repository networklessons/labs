# OSPF Over Frame-Relay: Point-to-Point

![Network Topology](./topology-ospf-over-frame-relay-point-to-point.jpg)

## Scenario

As the senior network engineer for a Dutch fishing company you are responsible for connecting all the different branch offices to the main network. The WAN technology you are using is Frame Relay, and you need to run OSPF over this WAN connection. It's impossible to broadcast on this WAN connection.

## Goal

- The frame-relay switch has been preconfigured for you, as you can see in the topology picture the following PVC's has been configured:
  - Router Barracuda to Salmon:
    - Barracuda: DLCI 102
    - Salmon: DLCI 201
  - Router Barracuda to Herring:
    - Barracuda: DLCI 103
    - Herring: DLCI 301

- Router Barracuda is the "Hub" router and the other 2 routers are the "Spoke" routers.

- Do not change any configuration on the Frame-Relay switch.

- You will need to create sub-interfaces on Router Barracuda.

- Configure the following IP addresses:
  - Router Barracuda:
    - S0/0.102: 192.168.12.1 /24
    - S0/0.103: 192.168.13.1 /24
    - L0: 1.1.1.1 /24
  - Router Salmon:
    - S0/0.201: 192.168.12.2 /24
    - L0: 2.2.2.2 /24
  - Router Herring:
    - S0/0.301: 192.168.13.3 /24
    - L0: 3.3.3.3 /24

- Configure all serial interfaces for encapsulation Frame-Relay.

- Disable Frame-relay inverse arp on all serial interfaces.

- Use 'clear frame-relay inarp' to make sure the ARP table is cleared.

- Configure the correct DLCI numbers on all routers and make sure you can ping every IP address from router Barracuda.

- Configure the OSPF network type to "point-to-point" on all serial interfaces.

- Configure OSPF on all 3 routers, make sure you have full connectivity. All IP addresses including the loopbacks should be reachable.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

## Video Solution

http://www.youtube.com/watch?v=85FvtIVuGBQ
