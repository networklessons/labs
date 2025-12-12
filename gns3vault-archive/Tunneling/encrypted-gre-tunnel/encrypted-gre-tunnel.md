# Encrypted GRE Tunnel

## Scenario

Your colleagues at "BigLabs" are very pleased with your performance so far...you managed to successfully configure the "Basic GRE" lab and the "Site-to-Site IPSEC VPN" lab. Now it's time to show them who the true networking expert is and teach them how to configure a Secure GRE tunnel. This allows you to send routing protocol updates through the GRE tunnel, and use IPSEC to encrypt this traffic....let's do it!

## Goal

- All IP addresses are preconfigured as specified in the topology picture.
- Router Godzilla and Nessie have the following loopback interfaces:
  - Godzilla: Loopback0: 1.1.1.1 /24 Loopback1: 11.11.11.11 /24
  - Nessie: Loopback0: 3.3.3.3 /24 Loopback1: 33.33.33.33 /24
- Configure EIGRP AS1 on all 3 routers, only advertise the 192.168.12.0 and 192.168.23.0 network, do not advertise the loopbacks.
- Ensure Router Godzilla and Nessie can ping each other.
- Configure a GRE tunnel between Router Godzilla and Nessie.
- Configure the 192.168.13.0 /24 network on the GRE tunnel:
  - Godzilla: 192.168.13.1
  - Nessie: 192.168.13.3
- Ensure you can ping the IP addresses that you configured on the tunnel interface.
- Configure OSPF and use network commands to advertise the network on the GRE tunnel.
- Advertise Loopback1 in OSPF on Router Godzilla and Nessie.
- Ensure you establish a OSPF neighbour relationship and that you see the loopback1 interfaces in the routing table.
- Now it's time to setup the IPSEC connection!
- Create an IKE Policy with the following parameters:
  - Authentication: pre-shared-key
  - Encryption: AES 256
  - Hashing: sha
  - DH: Group 5
  - Lifetime: 3600
- The pre-shared-key should be "VAULT".
- Create an IPSEC Transform-set with the following parameters:
  - ESP (Encapsulating Security Payload)
  - Encryption: AES 256
  - Hashing: SHA-HMAC
- Create the correct access-lists to encrypt the GRE tunnel traffic.
- Create the correct crypto-map to finish the IPSEC configuration.
- Verify the IPSEC configuration, you can use the following show/debug commands:
  - `show crypto ipsec transform-set`
  - `show crypto map`
  - `show crypto ipsec sa`
  - `debug crypto isakmp`

## IOS

c3640-jk9s-mz.124-16.bin

## Topology

![Network Topology - GRE Tunnel Basic](http://d3w1odjdta16tt.cloudfront.net/images/stories/gretunnelbasic.jpg)

## Video Solution

[Encrypted GRE Tunnel - Video Solution](http://www.youtube.com/watch?v=H2RweQsjOrw)
