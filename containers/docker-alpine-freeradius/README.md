# FreeRADIUS

A lightweight container image that runs [FreeRADIUS](https://freeradius.org/) on [Alpine Linux](https://hub.docker.com/_/alpine).

FreeRADIUS is a widely used open-source RADIUS server that handles authentication, authorization, and accounting (AAA) for network access. This image is useful for lab environments where you need a RADIUS server for testing 802.1X, EAP, or network device AAA authentication.

## Docker Hub

The image is available on Docker Hub: [networklessons/docker-alpine-freeradius](https://hub.docker.com/r/networklessons/docker-alpine-freeradius)

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
  -v /path/to/clients.conf:/etc/raddb/clients.conf \
  -v /path/to/users:/etc/raddb/users \
  --name freeradius \
  networklessons/docker-alpine-freeradius
```

### Docker Compose

```yaml
version: '2'
services:
  freeradius:
    image: networklessons/docker-alpine-freeradius
    ports:
      - 1812:1812/udp
      - 1813:1813/udp
    volumes:
      - "./clients.conf:/etc/raddb/clients.conf"
      - "./users:/etc/raddb/users"
```

## Kubernetes

Deployment manifests, ConfigMaps, and Services for running this container in Kubernetes are available in the [kubernetes/](kubernetes/) folder.
