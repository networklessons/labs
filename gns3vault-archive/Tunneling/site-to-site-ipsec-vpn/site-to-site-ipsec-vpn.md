# Site-to-Site IPSEC VPN

## Scenario

Your network colleagues were very enthusiastic when you showed them that a GRE tunnel makes it possible to tunnel routing protocols across VPN connections, and after configuring the previous "GRE Tunnel Basic" lab (see our lab section) your colleagues now ask you to configure a basic IPSEC Site-to-Site VPN so they can configure encrypted GRE tunnels later.

## Goal

- All IP addresses have been preconfigured as specified in the topology picture.
- Router Godzilla and Nessie have a loopback interface:
  - Godzilla: Loopback0: 1.1.1.1 /24
  - Nessie: Loopback0: 3.3.3.3 /24
- Configure OSPF on all 3 routers and advertise the following networks:
  - 192.168.12.0 /24
  - 192.168.23.0 /24
  - 1.1.1.0 /24
  - 3.3.3.0 /24
- Ensure that Godzilla and Nessie can ping each other.
- Ensure you can ping 3.3.3.3 from Godzilla, sourced from its Loopback0 interface.
- We are going to configure an IPSEC connection between Router Godzilla and Nessie.
- Create a ISAKMP policy:
  - Authentication: pre-shared-key
  - Encryption: AES 256
  - Hashing: SHA
  - DH: Group 5
  - Lifetime: 3600
- Configure the pre-shared-key "VAULT" which you will use for the IPSEC connection.
- Configure the IPSEC transform-set:
  - Cipher: AES 256
  - ESP (Encapsulating Security Protocol)
  - Hashing: SHA
- Change the IPSEC security association lifetime to 1800 seconds.
- You need to encrypt traffic from Router Godzilla's Loopback0 interface destined to Nessie's Loopback0 interface, create the correct access-list.
- Ensure you have a correct access-list on both Routers.
- Create the correct crypto-map to finish the IPSEC configuration.
- Verify the IPSEC configuration, you can use the following show/debug commands:
  - `show crypto ipsec transform-set`
  - `show crypto map`
  - `show crypto ipsec sa`
  - `debug crypto isakmp`
- Try a ping from Router Godzilla's Loopback0 interface destined to Router Nessie's Loopback0 interface, if your configuration is correct then traffic should be encrypted.

## IOS

- c3640-jk9s-mz.124-16.bin

## Topology

![Site-to-Site IPSEC VPN Topology](http://d3w1odjdta16tt.cloudfront.net/images/stories/gretunnelbasic.jpg)

## Video Solution

[Video Solution on YouTube](http://www.youtube.com/watch?v=S2GZd65AdEw)
