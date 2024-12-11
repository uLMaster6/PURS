import requests

response = requests.get('http://192.168.194.5/')

print(response.text)
print(requests.status_codes)
print(response.headers)

response = requests.get('http://192.168.194.5/login')

print(response.text)
print(requests.status_codes)
print(response.headers)