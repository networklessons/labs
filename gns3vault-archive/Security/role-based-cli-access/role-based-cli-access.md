# Role Based CLI Access

## Scenario

As the security specialist for your company you want to ensure employees don't get more access than they need to. At this moment everyone is logging in using privilege level 15 for your routers and you want to ensure this doesn't happen anymore in the future.

## Goals

- All IP addresses have been preconfigure for you.
- Configure a role called "TRAINEE" on router Rollin.
- Role "TRAINEE" should be able to change the IP address on loopback0.
- Configure a role called "DEBUG" on router Rollin.
- Role "DEBUG" should be able to use all debug commands.
- Configure a role called "ALLMIGHTY" on router Rollin.
- Role "ALLMIGHTY" should be able to do whatever role "TRAINEE" and "DEBUG" can do.
- To authenticate the roles you should use password "VAULT".

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology](./topology-role-based-cli-access.png)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=XOBzlMOZ2Bs)
