# BGP Aggregation AS SET

## Scenario

You work for a large Dutch webdevelopment company as the senior network engineer. Some of the sites are connected to each other through BGP. One of the network engineers in Hoofddorp has created a summary which aggregates some of the networks from AS 3 and advertises them to AS 1. Unfortunately there is a side-effect because AS 3 installs this summary as well.

## Goal

* All IP addresses have been preconfigured for you.
* Configure EBGP between Tilburg and Hoofddorp.
* Configure EBGP between Hoofddorp and Haarlem.
* Configure EBGP between Tilburg and Haarlem.
* Advertise the networks on the loopback interfaces on router Haarlem.
* Create a summary on router Hoofddorp that aggregates to network 172.16.0.0 / 16.
* Ensure AS 3 does not install this summary in its BGP table. You are not allowed to use any filters or prefix/access-lists.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology](./topology-bgp-aggregation-as-set.png)

## Video Solution

[http://www.youtube.com/watch?v=GK8_R7z2ieo](http://www.youtube.com/watch?v=GK8_R7z2ieo)
