# TCP Intercept

## Scenario

As part of the security team you are always looking for ways to improve security within the company. Lately the company is under fire by TCP SYN floods. You don't have any budget to buy some firewalls so you decide to look for a cheaper solution to solve this problem. You heard some good things about the "TCP Intercept" feature so you decide to look into it.

## Goal

- All IP addresses have been configured for you, look at the topology picture for the IP addresses.
- OSPF has been preconfigured for you on all routers.
- Configure Telnet on router Flash.
- Configure router Mirror so it closes half-open connections to router Flash after 15 seconds.
- Configure router Mirror so it starts closing half-open connections when there is more than one connection per second. It should keep doing this until the connection rate is about one per three minutes.
- Configure router Mirror so it only allows 20 half-open connections. Drop connections until you hit 15 half-open connections.

## Topology

![Network Topology](./topology-tcp-intercept.png)

**You need to register to be able to download the GNS3 Topology File. (Registration is Free!)**
