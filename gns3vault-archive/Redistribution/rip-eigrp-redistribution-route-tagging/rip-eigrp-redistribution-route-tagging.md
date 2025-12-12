# RIP EIGRP Redistribution Route Tagging

## Scenario

The Australia Zoo has hired you as a network engineer responsible for all bits & bytes in the zoo. As an experiment the zoo decided to have the kangaroos and dolphins around the same lake to study the interaction between the animals. Both departments need to have access to each other's data which means you'll have to exchange routing information. To make sure there is no single point of failure you will use router Lassie and Willy to configure two-way redistribution. This however will also introduce new problems like routing loops or sub-optimal routing, it's up to you to enable redistribution and solve any problems along the way...

## Goal

* All IP addresses have been preconfigured for you.
* RIP and EIGRP have been preconfigured for you on the corresponding routers.
* Enable two-way redistribution between RIP and EIGRP on router Lassie and Willy.
* You notice that router Willy or Lassie are sending traffic to 4.4.4.4 towards router Flipper, make sure you get rid of this sub-optimal routing.
* Use route tagging to accomplish this.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology](./topology-rip-eigrp-redistribution-route-tagging.png)
