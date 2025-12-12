# IPv6 EIGRP

## Scenario

After waking up from cryosleep the year appears to be 2020 and there is not a single IPv4 address left on the planet. The last thing you remember are the stories about the end of IPv4 and the migration plans for IPv6...now it seems this is all reality! It's up to you to configure EIGRP for IPv6 and make the network operational...resistance is futile ;)

## Goal

- You are not allowed to use IPv4 addresses.
- You are not allowed to use any IPv6 global unicast addresses except the ones on the loopback interfaces.
- Use the MAC-address for the last 64 bits of the IPv6 addresses required for the FastEthernet links.
- Configure EIGRP AS 6 and achieve full connectivity between the networks on the loopback interfaces.
- Configure the FastEthernet 0/0 interface of router Romulan so EIGRP can use up to 75% of available bandwidth.
- Configure EIGRP authentication between router Borg and Klingon. Use password GNS3VAULT.
- Change the EIGRP hello interval to 9 seconds between router Vulcan and Borg.

## Background

## IOS

- c3725-adventerprisek9-mz.124-15.T7.bin

## Topology

![Network Topology](./topology-ipv6-eigrp.png)

## Video Solution

[Watch on YouTube](http://www.youtube.com/watch?v=Tn-ZCa1uhZI)
