import os
import requests

from utils.utils import progress_bar, save_json, load_json, load_data_if_exists

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

def hit_poke_api(url: str):
    """ Hit Poke API - cached """
    print("+1 hit to pokeapi")
    
    data = None
    
    # Request
    r = requests.get(url)
    data = r.json()

    return data


def load_pokemon(path: str):
    # Try Loading Data
    data = load_data_if_exists(path)
    return data

def get_pokemon(pokemon_no: Union[str, int]=None):
    """ Get Pokemon Data - hits api
    """
    POKE_URL = f"https://pokeapi.co/api/v2/pokemon/{pokemon_no}"
    data = hit_poke_api(POKE_URL)

    return data

def get_pokemon_cached(pokemon_no: Union[str, int]=None, save_dir: str="data/raw_data", force_reload: bool=False):
    """ Get Pokemon Data 
    
Checks for save data first then hits api
    """
    POKE_URL = f"https://pokeapi.co/api/v2/pokemon/{pokemon_no}"
    POKE_PATH = f"{save_dir}/no_{pokemon_no}.json"
    
    if force_reload:
        return hit_poke_api(POKE_URL)

    # Try Loading Data
    data = load_data_if_exists(POKE_PATH)
    
    if data is None:
        data = hit_poke_api(POKE_URL)

    return data



def get_pokemon_collection(num_pokemon: Union[str, int]=None, offset: Union[str, int]=0, save_dir: str="data/raw_collections/"):
    """ Get Pokemon Data """
    POKE_URL = f"https://pokeapi.co/api/v2/pokemon?limit={num_pokemon}&offset={offset}"
    POKE_PATH = f"{save_dir}{offset}_{int(offset) + int(num_pokemon)}.json"

    # Request or not?
    data = load_data_if_exists(POKE_PATH)

    if data is None:
        data = hit_poke_api(POKE_URL)

    return data.get('results', None)



if __name__ == "__main__":
    # Choose Pokemon
    SAMPLE_NO = input("Choose Pokemon Number: ")

    # Get data or load if already pulled
    poke_data = get_pokemon(SAMPLE_NO)
    print(poke_data)


    poke_collection = get_pokemon_collection(9, save_dir="data/collections")
    
    for item in poke_collection:
        n = item['name']
        u = item['url']
        print(f"{n.title()} > {u}")
