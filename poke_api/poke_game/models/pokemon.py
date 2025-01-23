import os
from typing import List, Dict, Union

from utils.utils import progress_bar, save_json, load_json
from utils.poke_wrap import get_pokemon

"""
PokeAPI Pokemon Data/Object Models
____________________________________________
Goals
[ ] Pokemon(Species)
[ ] Pokemon(Individual)

____________________________________________
* Current impl combines both
"""

class PokemonBase:
    def __init__(self, name: str=None, number: int=None):
        self.number = number
        self.name = name
        # type

    def __str__(self):
        s = f"""{self.number}) {self.name.title()}"""
        return s
    
    @classmethod
    def from_api_json(cls, data: Dict):
        """
        This function depends on the shape of the data from pokeapi
        """
        name = data.get('name', "???")
        number = data.get('id', "???")

        return cls(name, number)
    
    def export(self):
        return {
            "number": self.number,
            "name": self.name,
        }

class Pokemon(PokemonBase):
    def __init__(self, name: str=None, number: int=None, nickname: str="", health: int=100, current_health: int=None):
        super().__init__(name=name, number=number)

        # Data
        self.nickname = nickname
        self.health = health
        self.current_health = health if current_health is None else current_health


    def __str__(self):
        chosen_name = self.name.title() if self.nickname == '' else self.nickname
        s = f"""{self.number}) {chosen_name}
HP {self.current_health:>3}/{self.health:<3} {progress_bar(self.current_health, self.health)}
"""
        return s
    
    @classmethod
    def from_pokemon_base(cls, data: PokemonBase):
        """
        This function depends on PokemonBase
        """
        return cls(**data.export())
    
    def export(self):
        return {
            **super().export(),
            "health": self.health,
            "current_health": self.current_health
        }


if __name__ == "__main__":
    SAMPLE_NO = input("Choose Pokemon Number: ")
    POKE_PATH = f"data/pokemon/no_{SAMPLE_NO}.json"

    CREATE_INDV = False

    # Try Loading Data, 
    data_exists = os.path.isfile(POKE_PATH)
    
    # Data Exists | Data from API
    poke_data = load_json(POKE_PATH) if data_exists else get_pokemon(SAMPLE_NO)
    poke_base_object = PokemonBase(**poke_data) if data_exists else PokemonBase.from_api_json(poke_data)
    print(f"Pokemon Base Loaded: {poke_base_object}")

    u_in = input("(c)reate individual\n(l)oad individual\n>>> ")

    match u_in:
        case 'c':
            # Create new Indvidual
            CREATE_INDV = True
            poke_object = Pokemon.from_pokemon_base(poke_base_object)
            poke_object.nickname = input("Choose a nickname: ")
            print(poke_object)

        case 'l':
            # Load Individual
            dir_name = "data/individuals"
            files = os.listdir(dir_name)

            choices = "\nSelect a Pokemon:\n"
            for _, file in enumerate(files):
                filename, ext = file.split('.')
                species_no, nickname = filename.split('_')
                choices += f"{_}) {nickname}\n"
            
            user_input = input(f"{choices}>>> ")

            poke_object = load_json(f"data/individuals/{files[int(user_input)]}")

        case _:
            pass

    # Save object data
    if not data_exists:
        save_json(poke_base_object.export(), POKE_PATH)
        if CREATE_INDV:
            save_json(poke_object.export(), f"data/individuals/{poke_object.number}_{poke_object.nickname}.json")
