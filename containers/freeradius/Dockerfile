FROM ubuntu:26.04@sha256:da6fc2be547864451aa253836dd926da33623312df4a9a243e35dc877c378a78
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
