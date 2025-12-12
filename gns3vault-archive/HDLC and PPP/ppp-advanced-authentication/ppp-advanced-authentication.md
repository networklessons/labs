# PPP Advanced Authentication

![Network Topology](./topology-ppp-advanced-authentication.jpg)

## Scenario

After configuring some basic PPP authentication, the management of the puppet business decided they want to increase security. One of the things they want you to do is change the behavior of using the hostname as username.

## Goal

- Configure the IP addresses as specified in the topology picture.
- Configure the correct hostname on both routers.
- Configure both links for encapsulation PPP.
- Router Kermit should authenticate Grover by using PAP, if it fails it should switch to CHAP, use the S0/0 interfaces.
- Router Grover should refuse PAP authentication and use CHAP authentication, use the S0/0 interfaces.
- Router Kermit should use the alternate CHAP hostname "MUPPET". You are not allowed to change the hostname of any router, use the S0/0 interfaces.
- Configure both routers to they want to authenticate the PPP connection on the S0/1 interfaces by using the fictional radius server at IP address 1.1.1.1, use password "MUPPET" for the fictional radius server.
- In case the radius server fails both routers should use the local database for authentication.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

## Video Solution

[YouTube Video](http://www.youtube.com/watch?v=grb4QyZCB7I)
