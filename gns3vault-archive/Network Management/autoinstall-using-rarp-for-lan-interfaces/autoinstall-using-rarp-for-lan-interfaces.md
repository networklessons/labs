# AutoInstall using RARP for LAN Interfaces

## Scenario

You are the network engineer at a company specialized in creating virtual worlds. The last few months the company gained quite some new customers, for each customer a new router has to be installed and to save time you want to make sure you can automatically them using the auto-install feature.

## Goal

* All IP addresses have been preconfigured for you (except router Flynn).
* EIGRP has been configured for connectivity.
* Router Flynn should request an IP address for the FastEthernet 0/0 interface using RARP.
* Router Quorra should give router Flynn IP address 192.168.12.1.
* Router Flynn has to receive its configuration file from router Jarvis.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology](./topology-autoinstall-using-rarp-for-lan-interfaces.png)
