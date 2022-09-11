from lib2to3.pgen2 import token
import requests
import json
from requests.auth import HTTPBasicAuth


def get_token():
        token = requests.post("https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token"),
        auth= HTTPBasicAuth(username="devnetuser", password="Cisco123!"),
        headers={"content-type": "application/json"},
        verify=False,
        data = token.json()
        return data["token"]
    
get_token()