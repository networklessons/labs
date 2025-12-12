# BGP Attribute Router ID

![Network Topology](./topology-bgp-attribute-router-id.png)

## Scenario

You are one of the trainees at a fairly small ISP. Your boss is on vacation and all colleagues are out of the office troubleshooting problems at customers. You receive a phonecall of one of the network engineers in NewDelhi who complains you are sending all traffic meant for Paris through his network and he wants it solved in the next 10 minutes. You google a bit for BGP attributes but it isn't making sense much to you at this moment...you do read something about Router ID so maybe that'll be helpful to you...ignorance is bliss right? Let's go!

## Goal

- All IP addresses have been preconfigured for you as specified in the topology picture.
- Configure EBGP between all ASes.
- Advertise the loopback0 interface on router Barcelona in BGP.
- Router Paris should have two paths to reach network 1.1.1.0 /24.
- Ensure router Paris sends traffic to router Sydney to reach network 1.1.1.0 /24. You are only allowed to make changes on router Sydney.

## IOS

c3640-jk9o3s-mz.124-16.bin

## Video Solution

[YouTube - BGP Attribute Router ID Solution](http://www.youtube.com/watch?v=0x--bvHJsuY)
