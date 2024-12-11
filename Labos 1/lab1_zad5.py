import requests

poruka = {
    "temperatura": "69"
}

response = requests.post('http://192.168.194.5/temperatura', json = poruka)

print(response.text)
print(response.status_code)

