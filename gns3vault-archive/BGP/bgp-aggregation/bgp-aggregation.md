# BGP Aggregation

![Network Topology](./topology-bgp-aggregation.png)

## Scenario:

John and Jim are setting up their own ISP and start by configuring BGP between their routers. Because they want to make sure not to advertise too many prefixes they want to configure BGP aggregation. It's up to you to make it happen.

## Goal:

- All IP addresses have been preconfigured for you.
- Configure EBGP between router John and Jim. Pick whatever AS you like.
- Advertise all loopback interfaces on router Jim in BGP.
- Create a summary for the loopback interfaces on router Jim. Ensure you don't have any overlapping address space.
- In the future you will add networks with the 20.0.0.0 /8 address space. Create a summary for this range on router John and advertise it in BGP. You are not allowed to configure it on any loopback interfaces.

## IOS:

c3640-jk9s-mz.124-16.bin

## Topology:

## Video Solution:

[Video: BGP Aggregation Solution](http://www.youtube.com/watch?v=8NDypnPLlB4)
