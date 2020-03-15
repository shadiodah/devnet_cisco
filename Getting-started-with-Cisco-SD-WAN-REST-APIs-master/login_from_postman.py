import requests

url = "https://sandboxsdwan.cisco.com:8443/j_security_check"

payload = 'j_username=devnetuser&j_password=Cisco123%21'
headers = {
'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data = payload, verify=False)

print(response.text.encode('utf8'))
