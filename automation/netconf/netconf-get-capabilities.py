from ncclient import manager

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

for capability in m.server_capabilities:
    print(capability)

m.close_session()