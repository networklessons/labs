# Multipoint One-Way Redistribution

Your local neighborhood pet shop has asked you to help them solve some network problems. The pet shop is running OSPF and recently bought another shop that is running EIGRP. To achieve connectivity they use redistribution but now some users are complaining about unreachable networks and the slowness of the network. Someone at the pet shop tried one-way redistribution but had trouble with non-optimal paths. They decided to configure multipoint one-way redistribution but this also introduced the problem of flapping networks...think you can solve it?

## Goal

* All IP addresses have been preconfigured for you.
* Configure OSPF on router Ace and Aggie and only advertise network 192.168.12.0 /24.
* Configure EIGRP AS 1 on router Ace, Aggie and Abu. Only advertise network 192.168.13.0 /24 and 192.168.23.0 /24.
* Redistribute the loopback0 interface in EIGRP AS 1 on router Abu.
* Redistribute EIGRP information into OSPF on router Ace and Aggie.
* Check router Ace and Aggie for possible redistribution problems and solve the problem.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology](./topology-multipoint-one-way-redistribution.png)

## Video Solution

http://www.youtube.com/watch?v=zMozo8uLmzs
