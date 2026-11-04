import requests

url = "https://catfact.ninja/fact"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"{data["fact"]} Length:{data["length"]}")
else:
    print(f"Fehler: {response.status_code}")