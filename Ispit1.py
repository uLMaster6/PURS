import requests

# 1. zadatak

poruka = {
    "ime": "Luka",
    "prezime": "Psenicnjak",
    "ip": "192.168.194.113"
}

response = requests.post('http://192.168.194.5', json = poruka)

print(response.status_code)
print(response.text)

# 2. Zadatak
params = {"id": "202"}

response = requests.get('http://192.168.194.5/hocu_bod', params=params)

print(response.status_code)
print(response.text)
print(response.headers)

# 3. Zadatak
response = requests.post('http://192.168.194.5/svi_bodovi')

print(response.text)
print(response.status_code)
print(response.headers)
