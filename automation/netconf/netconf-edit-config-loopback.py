from ncclient import manager
import xml.dom.minidom

# IOS XE Settings
ios_xe_host = "172.16.1.1"
ios_xe_port = 830
ios_xe_username = "cisco"
ios_xe_password = "cisco"

m = manager.connect(
    host=ios_xe_host,
    port=ios_xe_port,
    username=ios_xe_username,
    password=ios_xe_password,
    hostkey_verify=False,
    look_for_keys=False
)

netconf_interface_template = """
<config>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
                <interface>
                        <name>Loopback1</name>
                        <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
                        <enabled>true</enabled>
                        <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
                                <address>
                                        <ip>1.1.1.1</ip>
                                        <netmask>255.255.255.255</netmask>
                                </address>
                        </ipv4>
                </interface>
        </interfaces>
</config>
"""

netconf_reply = m.edit_config(netconf_interface_template, target = "running")

print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

m.close_session()