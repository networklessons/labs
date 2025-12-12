# AAA Exec Authorization

## Scenario

As part of the security team you are always looking for ways to improve security within the company. You want to get rid of all the local vty/console logins within your network so you decide to setup a radius server. Routers should use the external radius server for authentication from now on...let's see if you can secure this one!

## Goal

* All IP addresses have been configured for you, look at the topology picture for the IP addresses.
* Configure router Fuzz so users have to be authorized when they want to use the console. Use the (fictional) RADIUS server at IP address 192.168.23.3 for this. When the radius server is unreachable you should use the local username "test" with password "vault" for authentication.
* Username "test" should have privilege level 5.

## Topology

![Network Topology](./topology-aaa-exec-authorization.png)
