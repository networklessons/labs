# UDP Forwarding

## Scenario

The smurf village hasn't seen many changes the last 30 years but they did install a village-wide network using routers from a popular brand. Unfortunately for you there is one legacy TFTP application that needs broadcast capability throughout the network, let's see if you can smurf your way out of this one.

## Goal

- All IP addresses have been preconfigured for you.
- Configure router Gargamel so it can forward UDP Broadcast TFTP packets to router Papa.
- Ensure no other UDP broadcast packets will be forwarded.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology](./topology-udp-forwarding.png)

## Video Solution

http://www.youtube.com/watch?v=hNknfs1HwP0
