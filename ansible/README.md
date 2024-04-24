# Ansible

This folder contains Ansible playbooks you can run against your network devices.

For example, here is how to copy all running configurations on NX-OS devices in a Containerlab lab:

```bash
ubuntu@containerlab2:~/labs/containerlab/labs/cisco/nx-os/vxlan/vxlan-evpn-spine-leaf$ ls -lh
total 12K
drwxrwxr-x+ 9 root   root   4.0K Apr  9 09:54 clab-vxlan-evpn-spine-leaf
-rw-r--r--  1 ubuntu ubuntu 2.5K Apr  9 09:53 vxlan-evpn-spine-leaf.clab.yml
```
Containerlab automatically generates Ansible inventory files. You can run the playbook like this:

```bash
ansible-playbook -i ./clab-vxlan-evpn-spine-leaf/ansible-inventory.yml /home/ubuntu/labs/ansible/
playbooks/cisco-nx-os-save-running-config.yml 

PLAY [Download running configuration from Cisco NX-OS devices] **************************************************************************************************************************

TASK [Fetch the running config] *********************************************************************************************************************************************************
ok: [clab-vxlan-evpn-spine-leaf-leaf3]
ok: [clab-vxlan-evpn-spine-leaf-leaf4]
ok: [clab-vxlan-evpn-spine-leaf-leaf2]
ok: [clab-vxlan-evpn-spine-leaf-leaf1]
ok: [clab-vxlan-evpn-spine-leaf-spine1]
ok: [clab-vxlan-evpn-spine-leaf-spine2]

TASK [Save running config to a file] ****************************************************************************************************************************************************
changed: [clab-vxlan-evpn-spine-leaf-leaf2]
changed: [clab-vxlan-evpn-spine-leaf-leaf1]
changed: [clab-vxlan-evpn-spine-leaf-leaf3]
changed: [clab-vxlan-evpn-spine-leaf-leaf4]
changed: [clab-vxlan-evpn-spine-leaf-spine1]
changed: [clab-vxlan-evpn-spine-leaf-spine2]

PLAY RECAP ******************************************************************************************************************************************************************************
clab-vxlan-evpn-spine-leaf-leaf1 : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
clab-vxlan-evpn-spine-leaf-leaf2 : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
clab-vxlan-evpn-spine-leaf-leaf3 : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
clab-vxlan-evpn-spine-leaf-leaf4 : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
clab-vxlan-evpn-spine-leaf-spine1 : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
clab-vxlan-evpn-spine-leaf-spine2 : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```
