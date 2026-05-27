#!/bin/bash

# Create switches
ovs-vsctl --may-exist add-br sdn-spine1
ovs-vsctl --may-exist add-br sdn-leaf1
ovs-vsctl --may-exist add-br sdn-leaf2

# Static MAC addresses
ovs-vsctl set bridge sdn-spine1 other-config:hwaddr=00:50:c2:53:10:01
ovs-vsctl set bridge sdn-leaf1 other-config:hwaddr=00:50:c2:53:20:01
ovs-vsctl set bridge sdn-leaf2 other-config:hwaddr=00:50:c2:53:30:01

# Switch options
# SPINE1
ovs-vsctl set bridge sdn-spine1 fail_mode=secure
ovs-vsctl set bridge sdn-spine1 protocols=OpenFlow13
ovs-vsctl set-controller sdn-spine1 tcp:172.100.100.10:6653

# LEAF1
ovs-vsctl set bridge sdn-leaf1 fail_mode=secure
ovs-vsctl set bridge sdn-leaf1 protocols=OpenFlow13
ovs-vsctl set-controller sdn-leaf1 tcp:172.100.100.10:6653

# LEAF2
ovs-vsctl set bridge sdn-leaf2 fail_mode=secure
ovs-vsctl set bridge sdn-leaf2 protocols=OpenFlow13
ovs-vsctl set-controller sdn-leaf2 tcp:172.100.100.10:6653
