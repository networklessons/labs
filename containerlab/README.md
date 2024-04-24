
# Containerlab

You can deploy a lab like this:

```bash
cd /home/ubuntu/labs/containerlab/labs/cisco/nx-os/vxlan/vxlan-evpn-ingress-replication
```

Make sure you have a `.clab.yml` topology file:

```bash
ls -lh
total 4.0K
-rw-r--r-- 1 ubuntu ubuntu 2.5K Apr 10 12:27 vxlan-evpn-ingress-replication.clab.yml
```

Deploy it:

```bash
sudo clab deploy
INFO[0000] Containerlab v0.54.0 started                 
INFO[0000] Parsing & checking topology file: vxlan-evpn-ingress-replication.clab.yml 
INFO[0000] Creating docker network: Name="statics", IPv4Subnet="172.100.100.0/24", IPv6Subnet="", MTU=1500 
INFO[0000] Creating lab directory: /home/ubuntu/labs/containerlab/labs/cisco/nx-os/vxlan/vxlan-evpn-ingress-replication/clab-vvxlan-evpn-ingress-replication 
INFO[0000] Creating container: "graphite"               
INFO[0000] Creating container: "spine2"                 
INFO[0000] Creating container: "s4"                     
INFO[0000] Creating container: "s3"                     
INFO[0000] Creating container: "leaf2"                  
INFO[0000] Creating container: "leaf3"                  
INFO[0000] Creating container: "leaf4"                  
INFO[0000] Creating container: "s1"                     
INFO[0000] Creating container: "s2"                     
INFO[0000] Creating container: "spine1"                 
INFO[0000] Creating container: "leaf1"                  
INFO[0002] Created link: spine2:eth3 <--> leaf3:eth2    
INFO[0002] Created link: leaf3:eth3 <--> s3:eth1        
INFO[0002] Created link: spine2:eth2 <--> leaf2:eth2    
INFO[0002] Created link: leaf2:eth3 <--> s2:eth1        
INFO[0002] Created link: spine2:eth4 <--> leaf4:eth2    
INFO[0002] Created link: spine2:eth1 <--> leaf1:eth2    
INFO[0002] Created link: spine1:eth1 <--> leaf1:eth1    
INFO[0003] Created link: spine1:eth2 <--> leaf2:eth1    
INFO[0003] Created link: leaf1:eth3 <--> s1:eth1        
INFO[0003] Created link: leaf4:eth3 <--> s4:eth1        
INFO[0003] Created link: spine1:eth3 <--> leaf3:eth1    
INFO[0003] Created link: spine1:eth4 <--> leaf4:eth1    
INFO[0003] Executed command "sh -c graphite_motd.sh 8080" on the node "graphite". stdout:
Graphite visualization 🎨 http://localhost:8080/graphite 
INFO[0003] Adding containerlab host entries to /etc/hosts file 
INFO[0003] Adding ssh config for containerlab nodes     
INFO[0003] 🎉 New containerlab version 0.54.1 is available! Release notes: https://containerlab.dev/rn/0.54/#0541
Run 'containerlab version upgrade' to upgrade or go check other installation options at https://containerlab.dev/install/ 
+----+-----------------------------------------------+--------------+-------------------------------------------+------------+---------+--------------------+--------------+
| #  |                     Name                      | Container ID |                   Image                   |    Kind    |  State  |    IPv4 Address    | IPv6 Address |
+----+-----------------------------------------------+--------------+-------------------------------------------+------------+---------+--------------------+--------------+
|  1 | clab-vvxlan-evpn-ingress-replication-graphite | 41edc8096094 | netreplica/graphite                       | linux      | running | 172.100.100.100/24 | N/A          |
|  2 | clab-vvxlan-evpn-ingress-replication-leaf1    | 4719cf9b4037 | vrnetlab/vr-n9kv:10.2.7                   | cisco_n9kv | running | 172.100.100.12/24  | N/A          |
|  3 | clab-vvxlan-evpn-ingress-replication-leaf2    | 32d4c2cf0844 | vrnetlab/vr-n9kv:10.2.7                   | cisco_n9kv | running | 172.100.100.13/24  | N/A          |
|  4 | clab-vvxlan-evpn-ingress-replication-leaf3    | c87880e74b32 | vrnetlab/vr-n9kv:10.2.7                   | cisco_n9kv | running | 172.100.100.14/24  | N/A          |
|  5 | clab-vvxlan-evpn-ingress-replication-leaf4    | 647bdfae3e69 | vrnetlab/vr-n9kv:10.2.7                   | cisco_n9kv | running | 172.100.100.15/24  | N/A          |
|  6 | clab-vvxlan-evpn-ingress-replication-s1       | 353f4e9f95fc | networklessons/ubuntu-network-host:latest | linux      | running | 172.100.100.16/24  | N/A          |
|  7 | clab-vvxlan-evpn-ingress-replication-s2       | 3fe88df67366 | networklessons/ubuntu-network-host:latest | linux      | running | 172.100.100.17/24  | N/A          |
|  8 | clab-vvxlan-evpn-ingress-replication-s3       | dfc8dcfa6d55 | networklessons/ubuntu-network-host:latest | linux      | running | 172.100.100.18/24  | N/A          |
|  9 | clab-vvxlan-evpn-ingress-replication-s4       | 2a6edece548d | networklessons/ubuntu-network-host:latest | linux      | running | 172.100.100.19/24  | N/A          |
| 10 | clab-vvxlan-evpn-ingress-replication-spine1   | 6bb41596c109 | vrnetlab/vr-n9kv:10.2.7                   | cisco_n9kv | running | 172.100.100.10/24  | N/A          |
| 11 | clab-vvxlan-evpn-ingress-replication-spine2   | 930492f12e16 | vrnetlab/vr-n9kv:10.2.7                   | cisco_n9kv | running | 172.100.100.11/24  | N/A          |
+----+-----------------------------------------------+--------------+-------------------------------------------+------------+---------+--------------------+--------------+
```