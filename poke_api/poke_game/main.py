import os
import requests
from typing import List, Dict, Union

from utils.utils import progress_bar, save_json, load_json, load_data_if_exists
from utils.poke_wrap import get_pokemon, get_pokemon_cached, load_pokemon, get_pokemon_collection
from models.pokemon import Pokemon, PokemonSpecies
from models.trainer import Trainer

"""
_______________________________________
https://pokeapi.co/api/v2/pokemon/ditto

"""

class Game:
    def __init__(self):
        self.pokemon_path = "data/individuals/game_data.json"
        self.pokemon_species_path = "data/pokemon"

        self.player = None
        self.pokemon = {}
        self.pokemon_species_cache = {}

        # load pokemon data
        raw_data = load_data_if_exists(self.pokemon_path)
        if raw_data is not None:
            self.pokemon = {nn: Pokemon(**rd) for nn, rd in raw_data.items()}

        raw_data = load_data_if_exists(f"data/pokemon/cached.json")
        if raw_data is not None:
            self.pokemon_species_cache = {nn: PokemonSpecies(**rd) for nn, rd in raw_data.items()}

    def __str__(self):
        pass

    def save(self):
        # Save base pokemon Cache
        pokemon_data = {no: obj.export() for no, obj in self.pokemon_species_cache.items()}
        save_json(pokemon_data, f"data/pokemon/cached.json")

        # Save Individuals
        idv_data = {nn: obj.export() for nn, obj in self.pokemon.items()}        
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
        data = self.pokemon_species_cache.get(fixed_key, None)

        if data is None:
            # Try Loading Data
            POKE_PATH = f"{self.pokemon_species_path}/no_{pokemon_no}.json"

            data_exists = os.path.isfile(POKE_PATH)
            
            # Load data from [ File |  API ]
            # poke_data = get_pokemon_cached(pokemon_no, save_dir=self.pokemon_species_path)
            poke_data = load_pokemon(POKE_PATH) if data_exists else get_pokemon(pokemon_no)
            
            # Create Object from [ loaded data | raw Api data ]
            poke_base_object = PokemonSpecies(**poke_data) if data_exists else PokemonSpecies.from_api_json(poke_data)

            # Add to cache
            self.pokemon_species_cache[fixed_key] = poke_base_object
            
            # Save object data if no file
            # if not data_exists:
            #     save_json(poke_base_object.export(), POKE_PATH)

        return poke_base_object
    
    def create_individual_pokemon(self):
        # Create new Indvidual from species
        SAMPLE_NO = input("\nChoose Pokemon Number: ")

        # Load Pokemon base data
        poke_base_object = self.load_base_pokemon(SAMPLE_NO)
        print(f"Pokemon Base Loaded: {poke_base_object}")
        
        # Create Individual Pokemon
        poke_object = Pokemon.from_pokemon_base(poke_base_object)
        poke_object.nickname = input("Choose a nickname: ")

        # Add to cache
        self.pokemon[poke_object.nickname] = poke_object
        return poke_object
    
    def load_individual(self):
        """ Loads Chosen indv or returns Default(last)"""
        DEFAULT = self.pokemon[-1]
        cached_choices = "\n".join(self.pokemon.keys())
        chosen = input(f"""\nSelect a Pokemon:
{cached_choices}

>>> """)

        # Load chosen object
        poke_object = self.pokemon.get(chosen.lower(), DEFAULT)

        return poke_object

    def run(self):
        # Game Variables
        G_RUNNING = True
        self.player = Trainer("Jeff")

        while G_RUNNING:
            curr_pokemon = "\n".join(self.pokemon.keys())
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
                    # Create Individual Pokemon
                    poke_object = self.create_individual_pokemon()

                    print(poke_object)
                case 'l':
                    # Load Individuals from cache
                    loaded_poke = self.load_individual()
                    print(loaded_poke)

                case 's':
                    # Save
                    self.save()

                case 'q':
                    G_RUNNING = False

                case _:
                    pass

            self.player.party = self.pokemon.values()
            print(self.player)
            
        return


if __name__ == "__main__":
    g = Game()
    g.run()


