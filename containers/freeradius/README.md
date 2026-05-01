# FreeRADIUS

A container image that runs [FreeRADIUS](https://freeradius.org/) on [Ubuntu 24.04](https://hub.docker.com/_/ubuntu).

FreeRADIUS is a widely used open-source RADIUS server that handles authentication, authorization, and accounting (AAA) for network access. This image is useful for lab environments where you need a RADIUS server for testing 802.1X, EAP, or network device AAA authentication.

## Docker Hub

The image is available on Docker Hub: [networklessons/freeradius](https://hub.docker.com/r/networklessons/freeradius)

## Configuration

Configure the following files before starting the container. Example files are included in this folder.

- `clients.conf` — defines RADIUS clients (switches, routers) and their shared secrets
- `users` — defines user accounts and attributes such as VLAN assignments
- `eap` — EAP module configuration for 802.1X authentication (optional)

## How to use

### Docker run

```
docker run \
  -p 1812:1812/udp \
  -p 1813:1813/udp \
  -v /path/to/clients.conf:/etc/freeradius/3.0/clients.conf \
  -v /path/to/users:/etc/freeradius/3.0/users \
  --name freeradius \
  networklessons/freeradius
```

### Docker Compose

```yaml
version: '2'
services:
  freeradius:
    image: networklessons/freeradius
    ports:
      - 1812:1812/udp
      - 1813:1813/udp
    volumes:
      - "./clients.conf:/etc/freeradius/3.0/clients.conf"
      - "./users:/etc/freeradius/3.0/users"
```
