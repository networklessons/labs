# VRRP (Virtual Router Redundancy Protocol)

![Network Topology](./topology-vrrp-virtual-router-redundancy-protocol.jpg)

## Scenario

Internet traffic is becoming more and more important since the company you are working for is focused on e-commerce. Every minute that their webservers running webshops are unavailable is causing profit loss. The company decided need a scalable solution and get rid of the single router (NewJersey), so there is no single point of failure anymore. Up to you to start configuring!

## Goal

* All IP addresses have been preconfigured as following:
  * NewYork: F0/0: 192.168.1.1 /24
  * NewYork: F0/1: 192.168.2.1 /24
  * NewJersey: F0/0: 192.168.1.2 /24
  * NewJersey: F0/1: 192.168.2.2 /24
  * L.A.: F0/0: 192.168.1.3 /24
  * L.A.: F0/1: 192.168.2.3 /24
  * HOST: F0/0: 192.168.1.200 /24
  * IPS: F0/0: 192.168.2.254 /24

* The ISP router has the following loopback interfaces, these are used to simulate the Internet:
  * Loopback0: 172.16.1.1 /24
  * Loopback1: 172.16.2.1 /24
  * Loopback2: 172.16.3.1 /24

* The host router has been configured with "no ip routing" which will turn it into an ordinary host.

* OSPF has been configured on all routers except the host router for full connectivity.

* Configure NewYork, Newjersey and L.A. for VRRP, use the group number "1".

* The virtual IP Address should be 192.168.1.254 /24.

* Newjersey should be the master router, when it fails L.A. should take over.

* Hello packets should be sent every 7 seconds.

* Make sure the router with highest priority will always be the Master router.

* Configure authentication for VRRP, use password "vault".

* When the HSRP active router's F0/1 interface goes down, make sure it's no longer the master VRRP router.

* Configure the virtual IP address of VRRP as default gateway on the Host Router.

* Ensure you can ping the loopbacks of the ISP router from the Host router.

* Ensure that whenever 2 out of 3 routers are down, the Host router still has connectivity to the ISP.

## Background

## IOS

c3725-adventerprisek9-mz.124-15.T7.bin

## Topology

## Video Solution

[YouTube Video](http://www.youtube.com/watch?v=J6cAAAC8NvM)
