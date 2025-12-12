# Multicast Auto-RP

## Scenario

You are a network engineer and responsible for the main network of Gotham City. Multicast will be needed to send video replays throughout the city, and to decrease network load your boss has decided that you need to implement sparse-dense-mode. The network will be fairly large, so you don't want to configure the RP address manually on every router, let's see if there's an easier way...

## Goal

* All IP addresses have been preconfigured for you.
* Configure OSPF on all routers, advertise all networks. Achieve full connectivity.
* Configure sparse-dense-mode multicast on all routers.
* Configure AutoRP so router Joker is the Rendezvous Point (RP), use the loopback0 interface.
* Configure AutoRP so router Catwoman is the mapping agent (MP), use the loopback0 interface.
* Configure router Batman to join the multicast group 224.4.4.4 on it's Fastethernet interface.
* Make sure you can ping the 224.4.4.4 group address from router Catwoman.

## IOS

* c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology](./topology-multicast-autorp.png)

## Video Solution

http://www.youtube.com/watch?v=KKdq07MqLB0
