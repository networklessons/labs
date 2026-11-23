from iosxr_grpc.cisco_grpc_client import CiscoGRPCClient

# IOS XR gRPC settings:
ios_xr_ip = "172.16.1.1"
ios_xr_port = 57400
ios_xr_timeout = 10
ios_xr_username = "cisco"
ios_xr_password = "cisco"

# YANG
yang_module = "Cisco-IOS-XR-ipv4-arp-cfg"
yang_container = "arpgmp"

# Connect to IOS XR router.
client = CiscoGRPCClient(ios_xr_ip, ios_xr_port, ios_xr_timeout,ios_xr_username,ios_xr_password)

path = '{"%s:%s": [null]}' % (yang_module,yang_container)
result = client.getconfig(path)
print(result[1])