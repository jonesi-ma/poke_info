import requests

url = "https://jsonplaceholder.typicode.com/"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Fehler: {response.status_code}")