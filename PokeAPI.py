import requests

url = "https://pokeapi.co/api/v2/pokemon/"

try:
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        #print(data)
        #for k,v in data.items():
        #    print(f"Key: {k}\nValue: {v}\n\n")
        print(data["results"])


    else:
        print(f"Error: {response.status_code}")


except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")