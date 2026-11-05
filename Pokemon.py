import requests, streamlit as st

@st.cache_data
def get_poke_data():
    url = "https://pokeapi.co/api/v2/pokemon?offset=0&limit=1351"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return(f"Error: {response.status_code}")
        
    except requests.exceptions.RequestException as e:
        return(f"An Error occured: {e}")
    
def poke_info(name_or_id: str, data: dict) -> str:
    if not isinstance(data, dict):
        return data
    
    Pokemons = {data["results"][i]["name"] : data["results"][i]["url"] for i in range(len(data["results"]))}
    name_or_id = name_or_id.replace(",", ".")

    if name_or_id.replace(".", "").isnumeric() == True and name_or_id.count(".") <= 1:
        id = float(name_or_id.replace(".", ""))
        if id < 1 or (id > 1025 and id < 10001) or id > 10326 or int(id) != id:
            return("ID is invalid. Please enter a valid name or ID.")
        url2 = f"https://pokeapi.co/api/v2/pokemon/{name_or_id}"
    
    else:
        name = name_or_id.lower()
        if not name in Pokemons:
            return("Name is invalid. Please enter a valid name or ID.")
        url2 = Pokemons[name]
        
    response2 = requests.get(url2)
    data2 = response2.json()
    moves = ", ".join(i['move']['name'].capitalize() for i in data2['moves'])
    
    return(f"ID: {data2['id']}\nName: {data2['name'].capitalize()}\nHeight: {data2['height']}\nWeight: {data2['weight']}\nMoves: {moves}")
    
url = "https://pokeapi.co/api/v2/pokemon?offset=0&limit=1351"

 
data = get_poke_data()
st.title("About which Pokemon do you want to receive information?")

with st.form(key="pokemon_form"):    
    name_or_id = st.text_input("Please enter name or ID(1-1025, 10001-10326) of a Pokemon!")
    submit_button = st.form_submit_button("Get information!")
            
    if submit_button:
        res = poke_info(name_or_id, data)
        st.success(res)