# SNMP Trap for Syslog

## Scenario

The Agency has created a new security policy and since you are part of the security team you need to help them implement them. From now on all syslog messages need to be sent to a SNMP server using traps.

## Goal

- All IP addresses have been preconfigured for you.
- Optional: You can use the cloud interface to connect your router to a free syslog server like Kiwi Syslog Server (also works for SNMPv2).
- Configure router Agent so it sends a SNMP trap to host 192.168.12.2 for all informational and higher messages.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology](./topology-snmp-trap-for-syslog.png)
