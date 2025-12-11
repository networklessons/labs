# CCNP TSHOOT Troubleshooting 1

This is a containerlab implementation of the CCNP TSHOOT Troubleshooting Lab 1, converted from the original GNS3 topology.

## Overview

This lab provides a pre-configured troubleshooting scenario based on the official Cisco CCNP TSHOOT topology. The network is intentionally "broken" to help you develop troubleshooting skills.

## Topology

The lab consists of:
- **5 Routers**: R1, R2, R3, R4, ISP
- **4 Switches**: DSW1 (L3), DSW2 (L3), ASW1 (L2), ASW2 (L2)
- **4 Endpoints**: Client1, Client2, FTPServer, WebServer

### Network Segments

- **Core Network**: OSPF routing between R1-R2-R3-R4
- **BGP AS 65001**: R1 connected to ISP
- **BGP AS 65002**: ISP providing external connectivity
- **Distribution Layer**: EIGRP between R4 and DSW1/DSW2
- **Access Layer**: VLANs 10, 20, and 200

### VLANs

- **VLAN 10**: Client network (10.2.1.0/24)
- **VLAN 20**: FTP server network (10.2.2.0/24)
- **VLAN 200**: Management network (192.168.1.128/27)

## Deployment

To deploy this lab:

```bash
cd containerlab/labs/troubleshooting/cisco/ccnp-tshoot-troubleshooting-1
sudo containerlab deploy -t ccnp-tshoot-troubleshooting-1.clab.yml
```

To destroy the lab:

```bash
sudo containerlab destroy -t ccnp-tshoot-troubleshooting-1.clab.yml
```

## Troubleshooting Tickets

### Important Note
**Do not use `show run`!** This will spoil the troubleshooting experience. Use appropriate `show` and `debug` commands to develop your troubleshooting skills.

### Ticket #1: Client1 Connectivity
One of the users was working on Client1 but is complaining about no connectivity. A message on the Windows taskbar stated "no network connectivity". A colleague mentioned this might be related to DHCP.

**Investigation areas:**
- DHCP configuration
- VLAN assignments
- Interface status

### Ticket #2: FTP Server Access
After fixing Client1, users from VLAN 10 are unable to connect to the FTP server.

**Investigation areas:**
- Inter-VLAN routing
- EIGRP configuration
- Access lists

### Ticket #3: WebServer Connectivity
Users can connect to the FTP server but cannot reach the external webserver.

**Investigation areas:**
- BGP configuration
- NAT configuration
- Default routing

### Ticket #4: IPv6 Connectivity
The IPv6 team reports they cannot reach 2026::12:/122 from DSW1 or DSW2.

**Investigation areas:**
- IPv6 routing (OSPFv3, RIPng)
- IPv6 addressing
- Tunnel configuration

## Key Technologies

- **OSPF**: Multi-area design with NSSA
- **EIGRP**: Redistribution with OSPF
- **BGP**: eBGP between AS 65001 and AS 65002
- **HSRP**: First Hop Redundancy Protocol
- **Port-channels**: EtherChannel between switches
- **VLANs**: Multiple VLANs with inter-VLAN routing
- **IPv6**: OSPFv3, RIPng, and IPv6 tunnels
- **NAT**: Network Address Translation on R1
- **DHCP**: Dynamic host configuration

## Differences from GNS3 Topology

This Containerlab implementation has the following changes from the original GNS3 topology:

1. **Frame Relay replaced**: Frame Relay interfaces (Serial0/0.12, Serial0/0.23, Serial0/0.34) replaced with point-to-point Ethernet links
2. **Interface naming**: 
   - GNS3: Serial/FastEthernet interfaces
   - Containerlab: Ethernet interfaces (Ethernet0/0, Ethernet0/1, etc.)
3. **No shutdown**: All interfaces include `no shutdown` command (required in Containerlab)
4. **Removed obsolete commands**: Commands specific to GNS3/Dynamips removed

## Management Access

After deployment, devices are accessible via:
- **CLI**: `sudo containerlab exec -t ccnp-tshoot-troubleshooting-1.clab.yml -n <device-name> -- telnet`
- **Management network**: 10.65.98.0/24
  - R1: 10.65.98.11
  - R2: 10.65.98.12
  - R3: 10.65.98.13
  - R4: 10.65.98.14
  - ISP: 10.65.98.15
  - DSW1: 10.65.98.21
  - DSW2: 10.65.98.22
  - ASW1: 10.65.98.31
  - ASW2: 10.65.98.32
  - Client1: 10.65.98.41
  - Client2: 10.65.98.42
  - FTPServer: 10.65.98.43
  - WebServer: 10.65.98.44

## Original Topology

This lab is based on the GNS3 topology located in:
`gns3vault-archive/Troubleshooting/ccnp-tshoot-troubleshooting-1/`

## License

This lab is part of the NetworkLessons.com lab collection.
