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

netconf_filter = """
<filter>
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface></interface>
  </interfaces>
</filter>"""

netconf_reply = m.get_config("running", filter=netconf_filter)

print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())

m.close_session()