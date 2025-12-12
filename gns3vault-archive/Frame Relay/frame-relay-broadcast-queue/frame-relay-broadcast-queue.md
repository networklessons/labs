# Frame Relay Broadcast Queue

## Scenario

Jack and Emma are using frame relay but it seems there is so much broadcast traffic that the link is experiencing congestion. You need to make sure this will not happen in the future without using QoS or influencing any routing protocols (except RIPv1).

## Goal

* All IP addresses have been preconfigured for you.
* Configure router Jack and Emma so the broadcast queue has a maximum of 50 packets. The rate should only be 64KBps and there shouldn't be more than 20 packets per second.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology](./topology-frame-relay-broadcast-queue.png)

## Video Solution

http://www.youtube.com/watch?v=RiwOadVowvs
