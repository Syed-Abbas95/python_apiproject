import requests

url = "http://18.132.73.146:5200/data"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
