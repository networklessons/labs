# Frame Relay End to End Keepalive

## Scenario

Jack and Emma are using frame relay for their network but it seems there are some problems with LMI. Frame relay is being used at router Jack and Emma but they are not directly connected but through a MPLS backbone. As a result LMI is not working as a end-to-end solution. Configure the network so we can use a keepalive mechanism that works.

## Goal

* All IP addresses have been preconfigured for you.
* Router Emma should start by sending keepalive messages, router Jack should only respond to them.
* A keepalive message should be sent every 3 seconds, the event windows should be 6 and the threshold for errors should be 5.
* Configure router Emma so the configuration is attached to the DLCI.
* Configure router Jack so the configuration is attached to the physical interface.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology](./topology-frame-relay-end-to-end-keepalive.png)

## Video Solution

http://www.youtube.com/watch?v=9-5d4kMETnA
