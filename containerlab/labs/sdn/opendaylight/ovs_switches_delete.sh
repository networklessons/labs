# Delete OVS Switches
ovs-vsctl --if-exists del-br sdn-spine1
ovs-vsctl --if-exists del-br sdn-leaf1
ovs-vsctl --if-exists del-br sdn-leaf2

# Delete links
ip link delete odl-s1l1
ip link delete odl-s1l2