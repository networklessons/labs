# BGP Filtering Maximum Prefix

![Network Topology](./topology-bgp-filtering-maximum-prefix.png)

## Scenario:

The national hedgehog protection foundation needs your help with their network. They are using BGP for their International networking but the router they are using is a bit old and doesn't take many prefixes in its BGP table. You want to ensure there is a maximum number of prefixes your router will accept.

## Goal:

* All IP addresses have been preconfigured for you.
* Configure EBGP between router Sonic and Tails.
* Configure router Sonic so it will remove the BGP neighbor adjacency when it learns more than 8 prefixes.
* Configure router Sonic so it gives a warning once it receives 6 prefixes.
* After the BGP neighbor adjacency has been removed it should retry creating the BGP adjacency in 2 minutes.
* Configure router Tails so it will generate a warning when it receives 4 prefixes but it should never remove the BGP neighbor adjacency.

## Additional Resources

## IOS Image:

* c3640-jk9s-mz.124-16.bin

## Topology:

## Video Solution:

* [YouTube Video Solution](http://www.youtube.com/watch?v=SOMYjacgWOc)
