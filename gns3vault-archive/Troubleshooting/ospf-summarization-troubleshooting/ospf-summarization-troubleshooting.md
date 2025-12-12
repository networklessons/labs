# OSPF Summarization Troubleshooting

## OSPF Summarization Troubleshooting

## Scenario

Mystical Corporation is using OSPF within their autonomous system. Their network is configured using different areas which seems to be working fine. One of the network engineers configured a summary for area 0 but it seems it's not working, up to you to solve the problem.

## Goal

* All IP addresses have been preconfigured for you as specified in the topology picture.
* OSPF is preconfigured with the areas as specified in the topology picture.
* **Do not use show run**! (this will spoil the fun :) use the appropriate 'show' and 'debug' commands. This will teach you the skills needed to become a true troubleshooting master.
* Configure the network so you have full connectivity, make sure you use the areas as seen in the topology picture.
* Configure a summary on router Chimaera for the two loopback interfaces of router Cerberus. Ensure the summary is as specific as possible. The summary should show up as an interarea router, not as an external route.
* Ensure router Cyclops only sees the summary and not the specific routes.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology](./topology-ospf-summarization-troubleshooting.png)

## Video Solution

[OSPF Summarization Troubleshooting Video](http://www.youtube.com/watch?v=pIVOJqnawzQ)
