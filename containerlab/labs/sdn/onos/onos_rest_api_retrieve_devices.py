import requests
from requests.auth import HTTPBasicAuth

# ONOS REST API settings
onos_url = 'http://172.100.100.10:8181/onos/v1/hosts'
onos_user = 'onos'
onos_pass = 'rocks'

try:
    # Fetch information from API
    response = requests.get(onos_url, auth=HTTPBasicAuth(onos_user, onos_pass))

    # Check if request was successful
    if response.status_code == 200:
        data = response.json()

        # Iterate through the hosts list
        for host in data['hosts']:
            mac = host['mac']
            # A host might have multiple IPs or none
            ips = host.get('ipAddresses', ['No IP'])

            print(f"Found host with MAC {mac} and IP {ips}")
    else:
        print(f"Failed to retrieve data. Status Code: {response.status_code}")

except Exception as e:
    print(f"An error occurred: {e}")