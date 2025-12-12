# OSPF over Frame-Relay

![Network Topology](./topology-ospf-over-frame-relay.jpg)

## Scenario

After successfully configuring the previous frame-relay lab you feel it's time to try and run OSPF over this frame-relay link. OSPF knows many different network types and every type has a different solution, up to you to try them all out!

Hint: this lab uses the same topology as the "Frame-Relay Basics" lab, make sure you configured this lab first, then continue with this one.

## Goal

* Create loopbacks on all routers:
  * Paris: 1.1.1.1 /24
  * Berlin: 2.2.2.2 /24
  * Stockholm: 3.3.3.3 /24
* Configure OSPF on all routers using the point-to-multipoint interface (192.168.123.X subnet).
* Advertise all loopbacks in OSPF.
* Paris should be the OSPF designated router.
* Configure the OSPF network type on all routers to "Broadcast", ensure you have full connectivity to all subnets.
* Configure the OSPF network type on all routers to "Non-Broadcast", ensure you still have full connectivity.
* Configure the OSPF network type on all routers to "Point-to-Multipoint", ensure you still have full connectivity.
* Configure the OSPF network type on all routers to "Point-to-Multipoint non-broadcast", ensure you still have full connectivity.

## IOS

* c3640-jk9s-mz.124-16.bin

## Topology

## Video Solution

* [YouTube Video](http://www.youtube.com/watch?v=oEZfeyf8_p4)
