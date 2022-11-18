import os
import requests
from models.pokemon import Pokemon




def load_pokemon(id: int):
    # Validate Input
    if id <= 0:
        id = 1

    if id > 939:
        id = 939

    # Request Data
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")

    if response.status_code != 200:
        # In case of error, return  None | Default
        return None

    # Raw Data
    raw_data = response.json()

    # Extract Data from response data structure
    poke_id = raw_data.get("id")
    poke_name = raw_data.get("name")
    #           raw_data["types"][0]["type"]["name"]
    poke_type = raw_data.get("types")[0].get("type").get("name")
    poke_abilities = raw_data["abilities"][0]["ability"]["name"]
    
    # Can parse data into wanted type
    return {
            "id": poke_id,
            "name": poke_name,
            "type": poke_type
            }


def main():
    new_data = load_pokemon(7)

    new_pokemon = Pokemon(**new_data)

    print(new_pokemon)

if __name__ == '__main__':
    main()
    
