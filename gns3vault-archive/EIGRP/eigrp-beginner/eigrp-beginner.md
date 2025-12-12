# EIGRP Beginner

![Network Topology](./topology-eigrp-beginner.jpg)

## Scenario

Company XYZ decided to upgrade their network to Cisco only equipment and implement the EIGRP routing protocol. It's up to you to get the job done!

## Goal

- Configure all IP addresses as specified in the topology.
- Create 3 loopback interfaces:
  - Router X: 172.16.1.0 /24
  - Router Y: 172.16.2.0 /24
  - Router Z: 172.16.3.0 /24
- Configure EIGRP on all routers, use AS number 100. Achieve full connectivity
- You notice that when you start a ping from router Y's loopback to the loopback of router X that this is not possible, you need to fix the problem.
- Change the bandwidth so traffic from router Z to router Y's loopback interface uses the link between X and Z.
- Change the EIGRP configuration on all routers so load and reliability are also used as metrics.
- RouterX: create a summary towards Router Y and Z for the 172.16.1.0 /24 network. It should appear as 172.16.0.0 /16.
- Configure EIGRP authentication on all routers:
  - Key-Chain: XYZ
  - Key-ID: 1
  - Password: vault
- Create key-ID 2 in the XYZ key-chain and configure a accept and send-lifetime.
  - Key-ID 1: valid from 1 June 2010 till 14 June 2010.
  - Key-ID 2: valid from 14 June 2010 till 28 June 2010.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=aadOWeM0gb0)
