# Extended Access-List

## Scenario

This morning you woke up in a cell feeling dizzy and nauseous, it appears you were kidnapped by a mixture of agents from federal agencies. Your task is to finish this security test, if you pass you might end up becoming their next security agent...with blurry eyes you start your task!

## Goal

* All IP addresses have been configured for you, look at the topology picture for the IP addresses.
* OSPF has been configured for full connectivity.
* All routers are running services like HTTP, HTTPS, TELNET and SSH.
* Make sure you use the most specific wildcard for all your access-lists.
* You are only allowed to use extended access-lists.
* Configure the network so traffic from router CIA's L0 interface towards the HTTP server on 3.3.3.3 is not permitted.
* Configure the network so traffic from router FBI's L1 interface is only allowed to reach the HTTPS server on IP address 33.33.33.33.
* Configure the network so only users from router NSA's L1 interface are allowed to telnet into router CIA.
* Configure the network so users from router FBI's L2 interface are not allowed to ping to router's NSA L1 interface.

## Topology

![Network Topology](./topology-extended-access-list.png)

## Video Solution

[Video Solution](http://www.youtube.com/watch?v=lV6C7ABL1Ug)
