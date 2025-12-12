# IP Output Packet Accounting

## Scenario

Your boss is very interested to know which MAC addresses on the network are responsible for most traffic. Besides MAC addresses you would also like to see how many packets are marked with IP precedence. Time for some accounting...

## Goal

* All IP addresses have been preconfigured for you.
* Configure a loopback0 interface on router Tomb with IP address 3.3.3.3 /24.
* Configure EIGRP AS 1 on all routers and achieve full connectivity.
* Configure IP Output Packet accounting on router Wodan so you can trace packets from router Jack to the loopback0 interface of router Tomb.

## IOS

`c3640-jk9s-mz.124-16.bin`

## Topology

![Network Topology](./topology-ip-output-packet-accounting.png)

## Video Solution

http://www.youtube.com/watch?v=FswWzfWccqY
