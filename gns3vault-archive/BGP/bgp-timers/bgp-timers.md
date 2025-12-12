# BGP Timers

## Scenario

You are a film producer and part-time network engineer. You use BGP to connect two sites to each other but you feel things are a little slow. Let's see if you can tune up some of those BGP timers.

## Goal

* All IP addresses have been preconfigured for you.
* Configure EBGP between AS 1 and AS 2.
* The BGP scanner should run every 30 seconds on both routers.
* Ensure both routers don't wait till the next BGP advertisement-interval but send updates immediately.
* When there is no activity after 15 seconds the BGP peering should be dropped.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology](./topology-bgp-timers.png)

## Video Solution

[BGP Timers - Video Solution](http://www.youtube.com/watch?v=TTBqpG900YA)
