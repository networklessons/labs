# BGP Next hop self

![Network Topology](./topology-bgp-next-hop-self.png)

## Scenario:

As a junior networking engineer you were always fascinated with science fiction movies, that's why you are now working at a company specialized in special effects. The closest you got to light speed was sending bits and bytes with electricity through wires...nevertheless there is a task waiting for you. You need to configure BGP between your network (AS100) and the service provider (AS200). Setting up BGP was no problem for you, but users behind router Luke are complaining they can't access networks in AS 200. Time for you to solve this problem...you feel the force is strong within you so this should be a piece of cake!

## Goal:

* All IP addresses have been preconfigured as specified in the topology picture.
* Configure IBGP between router Hansolo and Luke, use AS 100, use the loopback0 interfaces as source for BGP.
* Configure EBGP between router Hansolo and Leia.
* Ensure both BGP neighbor relationships are up.
* Router HanSolo: Advertise the 192.168.12.0/24 network into BGP.
* Router Leia: Advertise the 3.3.3.0 /24 on the loopback interface into BGP.
* Ensure you can ping this network from router Hansolo.
* Try to ping this network from router Luke, why does this fail?
* Fix this problem by using a BGP command on router Hansolo. You are not allowed to advertise the 192.168.13.X network in BGP.

## IOS:

c3640-jk9s-mz.124-16.bin

## Topology:

## Video Solution:

http://www.youtube.com/watch?v=kjQ6cUcyVfI
