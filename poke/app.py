import os
import time
import random

# Models
from models.party import Party
from models.pokemon import Pokemon

# Poke API
from poke_api.client import load_pokemon

# Utilities
from utils.lsjson import load_json, save_json

"""
For Next Time

Let the user select a slot and reroll the pokemon in that slot!

"""

def get_random_poke():
    pid = random.randint(1, 500)
    return Pokemon(**load_pokemon(pid))


def main():
    trainer_id = 1234
    datapath = f"data/party/{trainer_id}.json"

    my_party = Party()
    my_party.load(datapath)

    # for _ in range(6):
    #     random_pokemon = get_random_poke()
    #     my_party.add(random_pokemon)
        
    #     time.sleep(1)

    my_party.save(datapath)
    print(my_party)
    

if __name__ == '__main__':
    main()
