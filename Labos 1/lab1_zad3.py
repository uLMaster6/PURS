import requests

payload = {
    "username": "PURS",
    "password": "1234"
}

response = requests.post('http://192.168.194.5/login', json = payload)

if response.status_code == requests.codes.ok:
    print('Statusni kod OK')

print(response.text)
print(response.status_code)


payload['password'] = ''

response = requests.post('http://192.168.194.5/login', json = payload)


print(response.text)
print(response.status_code)
