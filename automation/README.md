# Automation

Scripts and files for the network automation and programmability lessons.

## [NETCONF](netconf/)

Python scripts that use [ncclient](https://github.com/ncclient/ncclient) to talk to a Cisco IOS XE router through NETCONF. Used in the [Device Programmability](https://networklessons.com/network-automation/device-programmability) lesson.

* **netconf-get-capabilities.py**: shows the NETCONF capabilities of the router.
* **netconf-get-running-configuration.py**: retrieves the running configuration.
* **netconf-get-running-configuration-filter.py**: retrieves the interfaces from the running configuration with a filter.
* **netconf-edit-config-loopback.py**: creates interface Loopback1 with IP address 1.1.1.1/32.
* **netconf-delete-config-loopback.py**: deletes interface Loopback1.

## [gRPC](grpc/)

Python scripts to test gRPC on a Cisco IOS XR router. Used in the [Device Programmability](https://networklessons.com/network-automation/device-programmability) lesson.

* **grpc-cisco-get-config.py**: retrieves configuration data for the YANG module "Cisco-IOS-XR-ipv4-arp-cfg" and container "arpgmp". Returns data in JSON format.
* **grpc-cisco-replace-config.py**: replaces configuration data. This example adds the ARP entry in **ios-xr-arp-entry.json** to the router.

## [CSR1000V REST API](csr1000v-rest-api/)

Python scripts that use the CSR1000V REST API. Used in the [Introduction to REST API](https://networklessons.com/network-automation/introduction-to-rest-api) lesson.

* **get-interface.py**: retrieves information about the Loopback0 interface.
* **put-interface.py**: changes the description and IP address of the Loopback0 interface.

## [Kubernetes](kubernetes/)

Sample deployment file for the [Network Automation and Orchestration](https://networklessons.com/network-automation/network-automation-and-orchestration) lesson. It creates a pod with an nginx and a php-fpm container.

This file uses the old `extensions/v1beta1` API, which current Kubernetes versions no longer support. Use `apiVersion: apps/v1` and add a `selector` on a current cluster.
