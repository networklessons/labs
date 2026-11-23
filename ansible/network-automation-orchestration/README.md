# Network Automation and Orchestration

Ansible files for the [Network Automation and Orchestration](https://networklessons.com/network-automation/network-automation-and-orchestration) lesson.

These files were written for older Ansible versions and use the `provider` argument of the `ios_config` and `ios_command` modules. Newer playbooks are in the [playbooks](../playbooks/) folder.

## Ubuntu

With these files you can test Ansible on an Ubuntu server.

The [inventory/hosts](ubuntu/inventory/hosts) file has one entry for an Ubuntu server called "ubuntu-test-server" on IP address 10.56.101.21 with username/password "vmware".

There are three playbooks in the [playbooks](ubuntu/playbooks/) folder:

* **update_upgrade_packages.yml**: updates all packages on Ubuntu.
* **install_apache.yml**: installs the Apache web server.
* **copy_html_file.yml**: copies [html/index.html](ubuntu/html/index.html) to the /var/www/html folder.

## Cisco

The [inventory/hosts](cisco/inventory/hosts) file has four switches named DSW1, DSW2, ASW1, and ASW2, reachable through SSH with username "admin" and password "cisco". The campus group refers to all four switches.

There are two playbooks in the [playbooks](cisco/playbooks/) folder:

* **show_ip_interface_brief.yml**: runs the "show ip interface brief" command on all four switches and shows the result.
* **configure_ntp_dns.yml**: makes a backup of the running configuration and configures NTP and DNS servers on all four switches.

You can use the hosts file and playbooks with the VIRL topology in the [virl](cisco/virl/) folder.
