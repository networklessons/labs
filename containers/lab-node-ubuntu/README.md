# Lab Node Ubuntu

[Lab Node Ubuntu on Docker Hub](https://hub.docker.com/r/networklessons/lab-node-ubuntu)

> **Warning:** Do not use this container in production. It contains default usernames, passwords, and/or keys and is intended only for locally hosted labs.

Ubuntu 24.04 base image pre-loaded with networking tools:

- vim
- nmap
- iperf3
- hping3
- tcpdump
- curl, netcat, dnsutils, socat
- openssh-server
- iproute2

Use this as a host, server, or node in emulators such as EVE-NG, Containerlab, GNS3, etc.

## SSH

The container runs an SSH server on port 22. A `lab` user (password: `lab`) is created at boot with passwordless sudo. To switch to root:

```
sudo su
```

## Change MAC address

```
ip link set dev eth1 address 00:50:c2:53:40:01
```

## Change IP address

### Delete the current IP address

Find the current address:

```
ip addr show eth1
```

Then remove it:

```
ip addr del current.ip.address/xx dev eth1
```

### Add the new IP address

```
ip addr add 192.168.12.1/24 dev eth1
```

### Enable the interface

```
ip link set eth1 up
```

## ARP / NDISC

### View ARP cache

```
ip neigh show dev eth1
```

### Flush ARP & NDISC cache

```
ip -s -s neighbor flush all
```

## Static routes

View current routes:

```
ip route
```

Add a static route:

```
ip route add 192.168.0.0/16 via 192.168.12.254 dev eth1
```
