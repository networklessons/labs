FROM ubuntu:24.04@sha256:c4a8d5503dfb2a3eb8ab5f807da5bc69a85730fb49b5cfca2330194ebcc41c7b
LABEL maintainer="info@networklessons.com"

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    freeradius \
    freeradius-utils && \
    rm -rf /var/lib/apt/lists/*

RUN ln -sf /dev/stdout /var/log/freeradius/radius.log

EXPOSE \
    1812/udp \
    1813/udp

CMD ["freeradius","-xx","-f"]
