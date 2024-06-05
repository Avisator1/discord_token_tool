import json
import requests

login = input("What is the targets email? ")
password = input("What is the targets password? ")

url = "https://discord.com/api/v9/auth/login"

payload = {
    "login": login,
    "password": password
}

json_payload = json.dumps(payload)


headers = {'Content-Type': 'application/json'}


response = requests.post(url, data=json_payload, headers=headers)

print("Response Status Code:", response.status_code)
print("Response Content:", response.text)