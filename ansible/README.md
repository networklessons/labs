# Ansible

This folder contains Ansible playbooks you can run against your network devices.

For example, here is how to copy all running configurations on NX-OS devices in a Containerlab lab.

Containerlab automatically creates Ansible inventory files when you deploy a lab. Here's the content of a lab:

```bash
ls -lh ./containerlab/labs/vxlan/cisco/vxlan-multicast-anycast-rp-nx-os/
total 12K
drwxrwxr-x+ 7 root   root   4.0K May 22 14:56 clab-vxlan-multicast-anycast-rp-nx-os
-rw-r--r--  1 ubuntu ubuntu 2.5K May 23 11:44 vxlan-multicast-anycast-rp-nx-os.clab.yml
```
Here's what that `clab-vxlan-multicast-anycast-rp-nx-os` folder looks like:

```bash
ls -lh ./containerlab/labs/vxlan/cisco/vxlan-multicast-anycast-rp-nx-os/clab-vxlan-multicast-anycast-rp-nx-os/
total 108K
-rw-rw-r--+ 1 root root 1.1K May 23 11:49 ansible-inventory.yml
-rw-r--r--+ 1 root root  934 May 23 11:49 authorized_keys
drwxrwxr-x+ 3 root root 4.0K May 22 14:56 leaf1
drwxrwxr-x+ 3 root root 4.0K May 22 14:56 leaf2
drwxrwxr-x+ 3 root root 4.0K May 22 14:56 spine1
drwxrwxr-x+ 3 root root 4.0K May 22 14:56 spine2
-rw-rw-r--+ 1 root root  65K May 23 11:49 topology-data.json
```

Here's the generated Ansible inventory file:

```bash
cat ./containerlab/labs/vxlan/cisco/vxlan-multicast-anycast-rp-nx-os/clab-vxlan-multicast-anycast-rp-nx-os/ansible-inventory.yml 
all:
  vars:
    # The generated inventory is assumed to be used from the clab host.
    # Hence no http proxy should be used. Therefore we make sure the http
    # module does not attempt using any global http proxy.
    ansible_httpapi_use_proxy: false
  children:
    cisco_n9kv:
      vars:
        # ansible_connection: set ansible_connection variable if required
        ansible_user: admin
        ansible_password: admin
      hosts:
        clab-vxlan-multicast-anycast-rp-nx-os-leaf1:
          ansible_host: 172.100.100.12
        clab-vxlan-multicast-anycast-rp-nx-os-leaf2:
          ansible_host: 172.100.100.13
        clab-vxlan-multicast-anycast-rp-nx-os-spine1:
          ansible_host: 172.100.100.10
        clab-vxlan-multicast-anycast-rp-nx-os-spine2:
          ansible_host: 172.100.100.11
    linux:
      hosts:
        clab-vxlan-multicast-anycast-rp-nx-os-graphite:
          ansible_host: 172.100.100.100
        clab-vxlan-multicast-anycast-rp-nx-os-s1:
          ansible_host: 172.100.100.16
        clab-vxlan-multicast-anycast-rp-nx-os-s2:
          ansible_host: 172.100.100.17
```
We can run a playbook against that inventory file. For example, let's save all configs:

```bash
cd ./containerlab/labs/vxlan/cisco/vxlan-multicast-anycast-rp-nx-os/clab-vxlan-multicast-anycast-rp-nx-os

ansible-playbook -i ansible-inventory.yml /home/ubuntu/labs/ansible/playbooks/cisco-nx-os-save-running-config.yml
```

You'll see this output:

```bash
PLAY [Download running configuration from Cisco NX-OS devices] *************************************************************************************************************

TASK [Fetch the running config] ********************************************************************************************************************************************
ok: [clab-vxlan-multicast-anycast-rp-nx-os-spine1]
ok: [clab-vxlan-multicast-anycast-rp-nx-os-leaf2]
ok: [clab-vxlan-multicast-anycast-rp-nx-os-spine2]
ok: [clab-vxlan-multicast-anycast-rp-nx-os-leaf1]

TASK [Save running config to a file] ***************************************************************************************************************************************
changed: [clab-vxlan-multicast-anycast-rp-nx-os-spine1]
changed: [clab-vxlan-multicast-anycast-rp-nx-os-leaf2]
changed: [clab-vxlan-multicast-anycast-rp-nx-os-leaf1]
changed: [clab-vxlan-multicast-anycast-rp-nx-os-spine2]

PLAY RECAP *****************************************************************************************************************************************************************
clab-vxlan-multicast-anycast-rp-nx-os-leaf1 : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
clab-vxlan-multicast-anycast-rp-nx-os-leaf2 : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
clab-vxlan-multicast-anycast-rp-nx-os-spine1 : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0   
clab-vxlan-multicast-anycast-rp-nx-os-spine2 : ok=2    changed=1    unreachable=0    failed=0    skipped=0    rescued=0    ignored=0
```

The configuration files will be in the folder you ran the playbook from:

```bash
ls -lh clab-vxlan*
-rw-rw-r-- 1 ubuntu ubuntu 3.7K May 23 19:06 clab-vxlan-multicast-anycast-rp-nx-os-leaf1_startup-config.cfg
-rw-rw-r-- 1 ubuntu ubuntu 3.7K May 23 19:06 clab-vxlan-multicast-anycast-rp-nx-os-leaf2_startup-config.cfg
-rw-rw-r-- 1 ubuntu ubuntu 3.6K May 23 19:06 clab-vxlan-multicast-anycast-rp-nx-os-spine1_startup-config.cfg
-rw-rw-r-- 1 ubuntu ubuntu 3.6K May 23 19:06 clab-vxlan-multicast-anycast-rp-nx-os-spine2_startup-config.cfg
```

## Troubleshooting

If you create and destroy different labs, it's possible that your SSH keys on devices change. When you try to run an Ansible playbook, you might get this error:

```
PLAY [Download running configuration from Cisco NX-OS devices] *************************************************************************************************************

TASK [Fetch the running config] ********************************************************************************************************************************************
fatal: [clab-vxlan-multicast-anycast-rp-nx-os-leaf2]: FAILED! => {"changed": false, "module_stderr": "\nlibssh: The authenticity of host '172.100.100.13' can't be established due to 'Host is unknown: 5a:5d:9c:23:6f:7a:98:25:3f:29:a4:e8:ee:9f:55:82:79:ff:60:f3'.\nThe ssh-rsa key fingerprint is SHA1:Wl2cI296mCU/KaTo7p9Vgnn/YPM.", "module_stdout": "", "msg": "MODULE FAILURE\nSee stdout/stderr for the exact error"}
fatal: [clab-vxlan-multicast-anycast-rp-nx-os-leaf1]: FAILED! => {"changed": false, "module_stderr": "\nlibssh: The authenticity of host '172.100.100.12' can't be established due to 'Host is unknown: 5d:61:f8:c5:29:96:0d:bb:8c:c6:4d:2e:0d:21:f5:4a:41:2c:dd:7b'.\nThe ssh-rsa key fingerprint is SHA1:XWH4xSmWDbuMxk0uDSH1SkEs3Xs.", "module_stdout": "", "msg": "MODULE FAILURE\nSee stdout/stderr for the exact error"}
fatal: [clab-vxlan-multicast-anycast-rp-nx-os-spine1]: FAILED! => {"changed": false, "module_stderr": "\nlibssh: The authenticity of host '172.100.100.10' can't be established due to 'Host is unknown: 69:b6:06:00:cd:d0:09:48:22:b4:21:e5:5f:16:c5:f7:24:57:47:6c'.\nThe ssh-rsa key fingerprint is SHA1:abYGAM3QCUgitCHlXxbF9yRXR2w.", "module_stdout": "", "msg": "MODULE FAILURE\nSee stdout/stderr for the exact error"}
fatal: [clab-vxlan-multicast-anycast-rp-nx-os-spine2]: FAILED! => {"changed": false, "module_stderr": "\nlibssh: The authenticity of host '172.100.100.11' can't be established due to 'Host is unknown: 1b:4f:9b:4e:82:66:f8:85:2d:59:5f:63:7e:a5:5c:f7:c3:53:df:f4'.\nThe ssh-rsa key fingerprint is SHA1:G0+bToJm+IUtWV9jfqVc98NT3/Q.", "module_stdout": "", "msg": "MODULE FAILURE\nSee stdout/stderr for the exact error"}
```

You can solve this by disabling ssh-rsa key fingerprint checking for Ansible:

```bash
sudo vim /etc/ansible/ansible.cfg
```

And add this:

```
[defaults]
host_key_checking = False
```