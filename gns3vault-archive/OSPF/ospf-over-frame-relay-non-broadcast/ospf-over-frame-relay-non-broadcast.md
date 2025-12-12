# OSPF Over Frame-Relay: Non-Broadcast

![Network Topology](./topology-ospf-over-frame-relay-non-broadcast.jpg)

## Scenario

As the senior network engineer for a Dutch fishing company you are responsible for connecting all the different branch offices to the main network. The WAN technology you are using is Frame Relay, and you need to run OSPF over this WAN connection. One of the restrictions is that you are unable to send broadcast traffic on this frame-relay link.

## Goal

* The frame-relay switch has been preconfigured for you, as you can see in the topology picture the following PVC's has been configured:

  **Router Barracuda to Salmon:**
  - Barracuda: DLCI 102
  - Salmon: DLCI 201

  **Router Barracuda to Herring:**
  - Barracuda: DLCI 103
  - Salmon: DLCI 301

* Router Barracuda is the "Hub" router and the other 2 routers are the "Spoke" routers.
* Do not change any configuration on the Frame-Relay switch.
* Configure the following IP addresses:

  **Router Barracuda:**
  - S0/0: 192.168.123.1 /24
  - L0: 1.1.1.1 /24

  **Router Salmon:**
  - S0/0: 192.168.123.2 /24
  - L0: 2.2.2.2 /24

  **Router Herring:**
  - S0/0: 192.168.123.3 /24
  - L0: 3.3.3.3 /24

* Configure all serial interfaces for encapsulation Frame-Relay.
* Disable Frame-relay inverse arp on all serial interfaces.
* Configure the correct frame-relay map statements on all routers and make sure you can ping every IP address. You are not allowed to use the "broadcast" command.
* Configure the OSPF network type to "non-broadcast" on all serial interfaces.
* Configure OSPF on all 3 routers, make sure you have full connectivity. All IP addresses including the loopbacks should be reachable.
* Make sure router Salmon and Herring can never be the Designated or Backup designated router.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

## Video Solution

[OSPF Over Frame-Relay: Non-Broadcast on YouTube](http://www.youtube.com/watch?v=ZdjwF3IRoHg)
