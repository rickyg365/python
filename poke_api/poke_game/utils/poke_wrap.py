import os
import requests

from utils.utils import progress_bar, save_json, load_json

from typing import List, Dict, Union

"""
Poke API Wrapper
_______________________________________________

[ ] Get Collection of pokemon
[ ] Get Pokemon by
    [*] Number
    [ ] Name
[ ] Get Item
[ ] Get Ability

_______________________________________________
ENDPOINT: https://pokeapi.co/api/v2/pokemon/ditto
ENDPOINT: https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0
"""

def hit_poke_api(url: str, output_path: str="data/last_hit.json"):
    """ Hit Poke API - cached """
    data = None
    
    # Try Loading Data
    data_exists = os.path.isfile(output_path)
    
    if data_exists:
        return load_json(output_path)

    # Request
    print("+1 hit to pokeapi")
    r = requests.get(url)
    
    data = r.json()    
    save_json(data, output_path)

    return data



def get_pokemon(pokemon_no: Union[str, int]=None, save_dir: str="data/raw_data/"):
    """ Get Pokemon Data """
    POKE_URL = f"https://pokeapi.co/api/v2/pokemon/{pokemon_no}"
    POKE_PATH = f"{save_dir}no_{pokemon_no}.json"

    # Request or not?  
    data = hit_poke_api(POKE_URL, POKE_PATH)

    return data



def get_pokemon_collection(num_pokemon: Union[str, int]=None, offset: Union[str, int]=0, save_dir: str="data/raw_collections/"):
    """ Get Pokemon Data """
    POKE_URL = f"https://pokeapi.co/api/v2/pokemon?limit={num_pokemon}&offset={offset}"
    POKE_PATH = f"{save_dir}{offset}_{int(offset) + int(num_pokemon)}.json"

    # Request or not?  
    data = hit_poke_api(POKE_URL, POKE_PATH)

    return data.get('results', None)







if __name__ == "__main__":
    # Choose Pokemon
    SAMPLE_NO = input("Choose Pokemon Number: ")

    # Get data or load if already pulled
    poke_data = get_pokemon(SAMPLE_NO)
    print(poke_data)


    poke_collection = get_pokemon_collection(9, save_dir="data/collections/")
    
    for item in poke_collection:
        n = item['name']
        u = item['url']
        print(f"{n.title()} > {u}")
