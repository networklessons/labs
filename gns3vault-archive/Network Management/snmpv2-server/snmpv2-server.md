# SNMPv2 Server

## Scenario

The Agency has created a new security policy and since you are part of the security team you need to help them implement them. Some changes on the network have to be implemented through SNMPv2 and it's up to you to configure your router as a SNMPv2 agent.

## Goal

- All IP addresses have been preconfigured for you.
- Optional: You can use the cloud interface to connect your router to a free syslog server like Kiwi Syslog Server (also works for SNMPv2).
- Configure router Agent so it uses community string "VAULT".
- Configure router Agent so the SNMP contact is "007".
- Configure router Agent so the SNMP location is "Agency".
- Configure router Agent so the largest SNMP packet is 1500.
- Configure router Agent so the router can be reloaded through SNMP.
- Configure router Agent so only network 192.168.12.0 /24 is allowed to contact the router. Dropped packets should be logged.
- Configure router Agent so it has a community string called "README". This should only be used for read-only access.
- Configure router Agent to traps are sent to SNMPv2 server IP address 192.168.12.2. Use community string "VAULT".
- Configure router Agent so it informs a device with IP address 192.168.12.3. Use community string "VAULT".
- Create a loopback0 interface on router Agent with IP address 1.1.1.1 /24.
- Configure router Agent so it doesn't send any traps or informs when something happens with the loopback0 interface.
- Configure router Agent so it generates a trap when a new OSPF LSA is originated.

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology](./topology-snmpv2-server.png)
