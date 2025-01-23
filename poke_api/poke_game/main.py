import os
import requests
from typing import List, Dict, Union

from utils.utils import progress_bar, save_json, load_json
from utils.poke_wrap import get_pokemon, get_pokemon_collection
from models.pokemon import Pokemon, PokemonBase
from models.trainer import Trainer

"""
_______________________________________
https://pokeapi.co/api/v2/pokemon/ditto

"""

class Game:
    def __init__(self):
        self.pokemon_path = "data/individuals/game_data.json"
        self.base_pokemon_path = "data/pokemon"

        self.player = None
        self.individuals = {}
        self.base_pokemon_cache = {}

        # load data
        raw_data = load_json(self.pokemon_path)
        self.individuals = {nn: Pokemon(**rd) for nn, rd in raw_data.items()}

    def __str__(self):
        pass

    def save(self):
        # Save base pokemon Cache
        # save_json(self.base_pokemon_cache, self.base_pokemon_path)

        # Save Individuals
        idv_data = {nn: obj.export() for nn, obj in self.individuals.items()}        
        save_json(idv_data, self.pokemon_path)

        return
            
    def load_base_pokemon(self, pokemon_no: Union[int, str]):
        """ Load Pokemon base object - cached
        1. Checks cache
        2. Checks if file exists
        3. Loads data or Pulls from api
        5. Add to cache (app usage)
        6. Save to file (long term storage)
        """
        fixed_key = f"{pokemon_no}"
        data = self.base_pokemon_cache.get(fixed_key, None)

        if data is None:
            # Try Loading Data
            POKE_PATH = f"{self.base_pokemon_path}/no_{pokemon_no}.json"
            data_exists = os.path.isfile(POKE_PATH)
            
            # Load data from [ File |  API ]
            poke_data = load_json(POKE_PATH) if data_exists else get_pokemon(pokemon_no)
            
            # Create Object from [ loaded data | raw Api data ]
            poke_base_object = PokemonBase(**poke_data) if data_exists else PokemonBase.from_api_json(poke_data)

            # Add to cache
            self.base_pokemon_cache[fixed_key] = poke_base_object
            
            # Save object data if no file
            if not data_exists:
                save_json(poke_base_object.export(), POKE_PATH)

        return poke_base_object
    
    def create_individual_pokemon(self):
        return
    
    def load_individual(self):
        return

    def run(self):
        # Game Variables
        G_RUNNING = True
        self.player = Trainer("Jeff")

        while G_RUNNING:
            curr_pokemon = "\n".join(self.individuals.keys())
            main_menu = f"""Current Pokemon:
{curr_pokemon}
__________________________
(c)reate individual
(l)oad individual
(s)ave data
(q)uit

"""

            u_in = input(f"{main_menu}>>> ")

            match u_in:
                case 'c':
                    # Create new Indvidual from species
                    SAMPLE_NO = input("\nChoose Pokemon Number: ")

                    # Load Pokemon base data
                    poke_base_object = self.load_base_pokemon(SAMPLE_NO)
                    print(f"Pokemon Base Loaded: {poke_base_object}")
                    
                    # Create Individual Pokemon
                    poke_object = Pokemon.from_pokemon_base(poke_base_object)
                    poke_object.nickname = input("Choose a nickname: ")

                    # Add to cache
                    self.individuals[poke_object.nickname] = poke_object

                    print(poke_object)
                case 'l':
                    # Load Individuals from cache
                    cached_choices = "\n".join(self.individuals.keys())

                    # Display Options
                    user_input = input(f"""\nSelect a Pokemon:
{cached_choices}

>>> """)

                    # Load chosen object
                    poke_object = self.individuals[user_input.lower()]

                    # Add to cache
                    if poke_object.nickname not in self.individuals.keys():
                        self.individuals[poke_object.nickname] = poke_object

                    print(poke_object)

                case 's':
                    # Save
                    self.save()

                case 'q':
                    G_RUNNING = False

                case _:
                    pass

            self.player.party = self.individuals.values()
            print(self.player)
            
        return


if __name__ == "__main__":
    g = Game()
    g.run()


