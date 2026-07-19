FROM ubuntu:26.04@sha256:3131b4cc82a783df6c9df078f86e01819a13594b865c2cad47bd1bca2b7063bb
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
