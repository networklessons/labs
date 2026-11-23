import requests
import urllib3
import json


ip_address = '172.16.1.100'
interface = 'loopback0'
username = 'admin'
password = 'admin'

def get_token():
    """
    Authenticate and get token
    """

    url = 'https://%s:55443/api/v1/auth/token-services' % ip_address
    auth = (username, password) 
    headers = {'Content-Type':'application/json'}
    response = requests.post(url, auth=auth, headers=headers, verify=False)
    json_data = json.loads(response.text)
    token = json_data['token-id']
    print('We received token: %s' % token)
    return token

def get_interface(token, interface):
    """
    Retrieve interface information from router.
    """
    
    url = 'https://%s:55443/api/v1/interfaces/%s' % (ip_address, interface)
    headers={ 'Content-Type': 'application/json', 'X-auth-token': token}

    response = requests.get(url, headers=headers, verify=False)
    json_data = json.loads(response.text)
    print("Here is the interface information: \n")
    print(json.dumps(json_data, indent=4, separators=(',', ': ')))


# Disable unverified HTTPS request warnings.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Get token.
token = get_token()

# GET interface information.
get_interface(token, interface)