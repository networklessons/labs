# Cisco Yang Explorer

Container image that runs [Cisco Yang Explorer](https://github.com/CiscoDevNet/yang-explorer) on [Alpine Linux](https://hub.docker.com/_/alpine).

Cisco Yang Explorer is a web-based tool for browsing, editing, and testing YANG data models for network devices. It supports NETCONF and lets you interact with device YANG models through a graphical interface — useful for learning and testing model-driven programmability.

## Docker Hub

The image is available on Docker Hub: [networklessons/docker-alpine-cisco-yang-explorer](https://hub.docker.com/r/networklessons/docker-alpine-cisco-yang-explorer)

## How to use

Start the container and open the following URL in your browser:

```
http://localhost:8088/static/YangExplorer.html
```

### Docker run

```
docker run -p 8088:8088 networklessons/docker-alpine-cisco-yang-explorer
```

### Docker Compose

```yaml
version: '2'
services:
  cisco-yang-explorer:
    image: networklessons/docker-alpine-cisco-yang-explorer
    ports:
      - 8088:8088/tcp
```
