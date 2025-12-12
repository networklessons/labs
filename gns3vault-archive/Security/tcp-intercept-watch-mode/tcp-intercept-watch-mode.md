# TCP Intercept Watch Mode

## Scenario

As part of the security team you are always looking for ways to improve security within the company. Lately the company is under fire by TCP SYN floods. You don't have any budget to buy some firewalls so you decide to look for a cheaper solution to solve this problem. You heard some good things about the "TCP Intercept" feature so you decide to look into it.

## Goal

- All IP addresses have been configured for you, look at the topology picture for the IP addresses.
- OSPF has been preconfigured for you on all routers.
- Configure router Mirror so it resets all connections that don't finish the TCP 3 way handshake within 10 seconds by sending a RST to router Flash.

## Topology

![Network Topology](./topology-tcp-intercept-watch-mode.png)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=3VuILNNh25E)
