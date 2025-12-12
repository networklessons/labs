# Unicast Reverse Path Forwarding (URPF)

## Scenario

As part of the security team you are always looking for ways to improve security within the company. Recently you are being plagued by different sources sending spoofed IP packets. You want to protect your network by checking for the source IP addresses using Unicast Reverse Path Forwarding. Let's see if you can find the root of this one...

## Goal

* All IP addresses have been configured for you, look at the topology picture for the IP addresses.
* OSPF has been preconfigured for you.
* Configure router Mirror so traffic on the FastEthernet 1/0 interface will be dropped if the source IP address doesn't match the next hop address that router Mirror has in its routing table.
* Configure router Mirror so traffic on the FastEthernet 0/0 interface will be dropped if the source IP address doesn't match anything that router Mirror has in its routing table.
* Configure router Mirror so all dropped packets are logged.

## Topology

![Network Topology](./topology-unicast-reverse-path-forwarding-urpf.png)

## Video Solution

[http://www.youtube.com/watch?v=fV7GQXAvPcc](http://www.youtube.com/watch?v=fV7GQXAvPcc)
