# Containers

This folder contains Docker container images maintained by [networklessons.com](https://networklessons.com). Each subfolder holds the Dockerfile and supporting files for a specific container. Forgejo workflows in [.forgejo/workflows/](../.forgejo/workflows/) build and push each image to Docker Hub automatically every Sunday.

<!-- CONTAINERS_TABLE_START -->
| Container | Description | Docker Hub |
|-----------|-------------|------------|
| [docker-alpine-cisco-yang-explorer](docker-alpine-cisco-yang-explorer/) | Container image that runs Cisco Yang Explorer on Alpine Linux | [networklessons/docker-alpine-cisco-yang-explorer](https://hub.docker.com/r/networklessons/docker-alpine-cisco-yang-explorer) |
| [docker-alpine-freeradius](docker-alpine-freeradius/) | A lightweight container image that runs FreeRADIUS on Alpine Linux | [networklessons/docker-alpine-freeradius](https://hub.docker.com/r/networklessons/docker-alpine-freeradius) |
| [lab-node-ubuntu](lab-node-ubuntu/) | Ubuntu 24.04 base image pre-loaded with networking tools | [networklessons/lab-node-ubuntu](https://hub.docker.com/r/networklessons/lab-node-ubuntu) |
<!-- CONTAINERS_TABLE_END -->
