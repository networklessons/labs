FROM ubuntu:26.04@sha256:065aa8626841f16057b78b027b464cd59c4fac36c204c72dcbf48d66f5fa8a96
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
