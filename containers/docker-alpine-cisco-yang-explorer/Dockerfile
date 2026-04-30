FROM alpine:3.9

# Install required packages
RUN apk add \
gcc \
git \
python \
python-dev \
py-pip \
py-crypto \
py-lxml \
py-virtualenv && \
pip install pyang graphviz

# Install Cisco Yang Explorer
WORKDIR /cisco-yang-explorer
RUN git clone https://github.com/CiscoDevNet/yang-explorer.git && \
cd yang-explorer && \
sh setup.sh && \
sed -i 's/bash/sh/g' start.sh && \
sed -i -e 's/HOST=\'localhost\'/HOST=$HOSTNAME/g' start.sh

WORKDIR /cisco-yang-explorer/yang-explorer
CMD ["sh", "start.sh"]
