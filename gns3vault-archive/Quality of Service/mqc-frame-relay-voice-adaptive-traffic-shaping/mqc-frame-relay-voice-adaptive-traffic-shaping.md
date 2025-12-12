# MQC Frame Relay Voice-Adaptive Traffic Shaping

## Scenario

As one of the network engineers for a large frame-relay provider in the US you are asked by your boss to configure QoS. Whenever there is congestion there is a certain amount that could be dropped from customers, it's up to you to configure it!

## Goal

* All IP addresses have been preconfigured for you.
* Configure router Kos so there is a priority queue of 64Kbps for VoIP packets on the frame-relay link.
* Configure router Kos so you don't exceed the CIR rate of 128Kbps when there are VoIP packets in the queue.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology](./topology-mqc-frame-relay-voice-adaptive-traffic-shaping.png)

## Video Solution

[Video Solution](http://www.youtube.com/watch?v=gR8IM_pdty0)
