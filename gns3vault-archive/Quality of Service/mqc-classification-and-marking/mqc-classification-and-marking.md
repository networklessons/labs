# MQC Classification and Marking

## Scenario

You are the VoIP specialist at the ISP you are working for. To ensure all VoIP traffic has enough bandwidth and low delay you have to implement some Quality of Service settings. It's time to classify and mark some traffic!

## Goal

* All IP addresses have been preconfigured for you.
* Configure an inbound policy on router Line with the following configuration:
  * ICMP traffic from router Frank should get a DSCP value of AF33.
  * RTP traffic from router Frank should get a DSCP value of EF.
  * HTTP traffic from router Frank should get a IP precedence value of 7 (priority).
  * All other traffic should get a DSCP value of AF43.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology](./topology-mqc-classification-and-marking.png)

**You need to register to download the GNS3 Topology File. (Registration is Free!)**
