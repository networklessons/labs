# MQC Weighted Random Early Detection

## Scenario

You are the VoIP specialist at the ISP you are working for. To ensure all VoIP traffic has enough bandwidth and low delay you have to implement some Quality of Service settings. You read some information about TCP synchronization and windowing. You have a lot of HTTP traffic on your network and you are wondering if random early detection could help you to slow down those HTTP packets...let's kick some IP packets in the bucket!

## Goal

- All IP addresses have been preconfigured for you.
- Configure an inbound policy on router Prio to classify and mark HTTP packets with the DSCP AF41 value.
- Configure an outbound policy on router Line to start dropping HTTP packets when the queue size is between 8 and 32 packets. Once the queue is reaching the maximum you should drop 1 out of every 8 packets.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology](./topology-mqc-weighted-random-early-detection.png)

## Video Solution

[Weighted Random Early Detection Solution](http://www.youtube.com/watch?v=7z8c920Xv48)
