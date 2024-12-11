import requests
# 1. primjer
response = requests.get('https://httpbin.org/user-agent')
for k, v in response.headers.items():
    print(f'{k}: {v}')
print(response.json())


# 2. Primjer
params = {
"id": 1
}
response = requests.get('https://httpbin.org/response-headers', params=params)
for k, v in response.headers.items():
    print(f'{k}: {v}')
print(response.json())


# 3. Primjer
payload = {
"temperatura": 25,
"vlaga": 20
}
response = requests.post('https://httpbin.org/post', data=payload)
for k, v in response.headers.items():
    print(f'{k}: {v}')
print(response.json())


# 4. Primjer
payload = {
"temperatura": 25,
"vlaga": 20
}
response = requests.post('https://httpbin.org/post', json=payload)
for k, v in response.headers.items():
    print(f'{k}: {v}')
print(response.json())


# 5. Primjer
import requests
response = requests.get('https://httpbin.org/user-agent')
print(response.content)
print(response.content.decode('UTF-8'))
print(response.text)
print(response.json())
print(response.json().get('user-agent'))


# 6. Primjer
response = requests.get('https://httpbin.org/user-agent')
print(response.status_code)
if response.status_code == requests.codes.ok:
    print('Statusni kod je OK')
print(response.headers)
print(response.headers.get('Content-Type'))