import os
import requests
from models.pokemon import Pokemon


def load_pokemon(id: int):
    if id <= 0:
        id = 0

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")

    if response.status_code != 200:
        return None
    data = response.json()
    poke_id = data.get("id")
    poke_name = data.get("name")
    poke_type = data.get("types")[0].get("type").get("name")
    poke_abilities = data["abilities"][0]["ability"]["name"]
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
    
