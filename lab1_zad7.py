import requests

response = requests.get('http://ip.jsontest.com')

print(response.status_code)
print(response.json().get('ip'))