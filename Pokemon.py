import requests, streamlit as st

def poke_info(name_or_id: str, data: dict) -> str:
    
    try:
        id = float(name_or_id)
        if id < 1 or id > 1025 and id < 10001 or id > 10326 or int(id) != id:
            return("ID is invalid. Please enter a valid name or ID.")
        id = int(id)
        
        for i in data["results"]:
            pos = i["url"].find("pokemon/")
            if i["url"][pos+len("pokemon/"):-1] == str(id):
                url2 = i["url"]
                break
    
    except:
        name = name_or_id.lower()
        url2 = ""
        for i in data["results"]:
            if i["name"] == name:
                url2 = i["url"]
        
        if not url2:
            return("Name is invalid. Please enter a valid name or ID.")
        
    response2 = requests.get(url2)
    data2 = response2.json()
    moves = ", ".join(i['move']['name'].capitalize() for i in data2['moves'])
    
    return(f"ID: {data2['id']}\nName: {data2['name'].capitalize()}\nHeight: {data2['height']}\nWeight: {data2['weight']}\nMoves: {moves}")
    
url = "https://pokeapi.co/api/v2/pokemon?offset=0&limit=1351"

try: 
    response = requests.get(url)
    
    if response.status_code == 200:
        st.title("About which Pokemon do you want to receive information?")

        with st.form(key="pokemon_form"):    
            name_or_id = st.text_input("Please enter name or ID(1-1025, 10001-10326) of a Pokemon!")
            submit_button = st.form_submit_button("Get information!")
            
            if submit_button:
                data = response.json()
                res = poke_info(name_or_id, data)
                st.success(res)
        
    else:
        print(f"Error: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An Error occured: {e}")