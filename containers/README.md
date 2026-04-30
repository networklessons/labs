# Containers

This folder contains Docker container images maintained by [networklessons.com](https://networklessons.com). Each subfolder holds the Dockerfile and supporting files for a specific container. Forgejo workflows in [.forgejo/workflows/](../.forgejo/workflows/) build and push each image to Docker Hub automatically every Sunday.

| Container | Description | Docker Hub |
|-----------|-------------|------------|
| [docker-alpine-cisco-yang-explorer](docker-alpine-cisco-yang-explorer/) | Cisco Yang Explorer web UI running on Alpine Linux | [networklessons/docker-alpine-cisco-yang-explorer](https://hub.docker.com/r/networklessons/docker-alpine-cisco-yang-explorer) |
| [docker-alpine-freeradius](docker-alpine-freeradius/) | FreeRADIUS server running on Alpine Linux | [networklessons/docker-alpine-freeradius](https://hub.docker.com/r/networklessons/docker-alpine-freeradius) |
| [lab-node-ubuntu](lab-node-ubuntu/) | Ubuntu-based node with networking tools for lab environments | [networklessons/lab-node-ubuntu](https://hub.docker.com/r/networklessons/lab-node-ubuntu) |
