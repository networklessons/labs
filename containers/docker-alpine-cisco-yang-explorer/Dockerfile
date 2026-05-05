FROM ubuntu:26.04

ENV DEBIAN_FRONTEND=noninteractive

# Install required packages
RUN apt-get update && apt-get install -y \
    gcc \
    git \
    python3 \
    python3-dev \
    python3-pip \
    python3-lxml \
    python3-virtualenv \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip3 install pyang graphviz --break-system-packages

# Install Cisco Yang Explorer
WORKDIR /cisco-yang-explorer
RUN git clone https://github.com/CiscoDevNet/yang-explorer.git && \
    cd yang-explorer && \
    sh setup.sh && \
    sed -i 's/bash/sh/g' start.sh && \
    sed -i "s/HOST='localhost'/HOST=\$HOSTNAME/g" start.sh

WORKDIR /cisco-yang-explorer/yang-explorer
CMD ["sh", "start.sh"]
