# MQC Two Rate Three-Color Policer

## Scenario

You work for a large provider in India as a senior network engineer specialized in Quality of Service. All the customers of the service provider have an Ethernet connection which is capable of delivering speeds up to 10Mbps. The ISP has different subscriptions and you need to enforce that customers only get what they are paying for...when traffic exceeds a certain rate you need to police it!

## Goal

- All IP addresses have been preconfigured for you.
- Configure router Line to police all TELNET traffic heading for router Jack with the following configuration:
- Configure a CIR rate of 64Kbps, the DSCP value should be set to AF21.
- Configure a PIR rate of 128Kbps the DSCP value should be set to 0.
- Traffic that is violating should be dropped.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology](./topology-mqc-two-rate-three-color-policer.png)

## Video Solution

[Two Rate Three-Color Policer Solution](http://www.youtube.com/watch?v=jD3G53CMuIU)
