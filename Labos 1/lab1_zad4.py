import requests

response = requests.get('http://192.168.194.5/temperatura')

if response.headers.get('Content-Type') == 'application/json':
    print(response.json().get('temperatura'))