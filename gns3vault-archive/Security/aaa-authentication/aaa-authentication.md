# AAA Authentication

## Scenario

As part of the security team you are always looking for ways to improve security within the company. You want to get rid of all the local vty/console logins within your network so you decide to setup a radius server. Routers should use the external radius server for authentication from now on...let's see if you can secure this one!

## Goal

* All IP addresses have been configured for you, look at the topology picture for the IP addresses.
* Configure router Fuzz so it uses the (fictional) radius server at IP address 192.168.23.3. Updates should be sourced from the loopback0 interface.
* Configure router Fuzz so console access uses a local username 'console' with password 'vault'.
* Configure router Fuzz so VTY access uses the radius server, when it fails it should switch to a local username 'telnet' with password 'unsafe'.
* Configure router Fuzz so everyone sees the message "ID required" when they try to login using AAA.

## Topology

![Network Topology](./topology-aaa-authentication.png)
