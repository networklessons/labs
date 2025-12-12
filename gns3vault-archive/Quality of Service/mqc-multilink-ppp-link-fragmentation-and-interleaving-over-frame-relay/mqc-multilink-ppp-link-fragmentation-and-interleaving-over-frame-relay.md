# Multilink PPP Link Fragmentation and Interleaving over Frame Relay

## Scenario

As one of the network engineers for a large frame-relay provider in the US you are asked by your boss to configure QoS. One of your customers insists there will be authentication in the future for his frame-relay connection. You don't have to configure authentication right now but you remember you can do this by using PPP on a frame-relay link. You do have to setup QoS right now though...

## Goal

- All IP addresses have been preconfigured for you.
- Configure Multilink PPP on the frame-relay link between router Kos and Quall.
- Classify and mark TELNET and HTTP traffic on router Kos and Quall. Use DSCP value AF21 for TELNET traffic and AF31 for HTTP traffic.
- Create a policy on router Kos and Quall with the following configuration:
  - TELNET traffic should have 64Kbps of priority bandwidth.
  - HTTP traffic should have 10% of the remaining bandwidth.
- Enable Link fragmentation and interleaving and ensure there is a delay of 20ms on the frame-relay link.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology](./topology-mqc-multilink-ppp-link-fragmentation-and-interleaving-over-frame-relay.png)

**You need to register to download the GNS3 Topology File. (Registration is Free!)**

## Video Solution

http://www.youtube.com/watch?v=odFOoefgL4M
