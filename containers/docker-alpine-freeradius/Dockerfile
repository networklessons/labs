FROM alpine:latest
LABEL maintainer="info@networklessons.com"

RUN apk update && \
    apk add \
    freeradius \
    freeradius-eap \
    freeradius-radclient && \
    rm /var/cache/apk/*

# Redirect logs to STDOUT
RUN ln -sf /dev/stdout /var/log/radius/radius.log

EXPOSE \
    1812/udp \
    1813/udp

CMD ["radiusd","-xx","-f"]
