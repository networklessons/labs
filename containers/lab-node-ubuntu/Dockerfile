# Use Ubuntu 24.04 as the base image
FROM ubuntu:26.04

# Avoid prompts from apt
ENV DEBIAN_FRONTEND=noninteractive

# Update apt cache and install networking tools
RUN apt-get update && apt-get install -y \
    vim \
    iputils-ping \
    iproute2 \
    curl \
    dnsutils \
    nmap \
    iperf3 \
    hping3 \
    tcpdump \
    socat \
    openssh-server \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Add lab user for SSH.
RUN useradd -rm -d /home/ubuntu -s /bin/bash -g root -G sudo -u 1010 lab && \
    echo 'lab:lab' | chpasswd && \
    mkdir /var/run/sshd

# Grant lab user passwordless sudo privileges
RUN echo 'lab ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers.d/lab

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
