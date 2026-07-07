FROM ubuntu:26.04@sha256:b7f48194d4d8b763a478a621cdc81c27be222ba2206ca3ca6bc42b49685f3d9e
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
