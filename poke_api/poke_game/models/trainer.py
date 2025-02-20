import os
from typing import List, Dict, Union
from models.pokemon import Pokemon, PokemonSpecies


class Trainer:
    def __init__(self, name: str, trainer_id: int=None, party: List[Union[Pokemon, Dict]]=None, inventory: List=None):
        self.trainer_id = trainer_id
        self.name = name
        self.party = party
        self.inventory = inventory  # if isinstance(inventory[0], Item) else [Item(**i) for i in inventory]
        
        if party is not None:
            self.party = party if isinstance(party[0], Pokemon) else [Pokemon(**p) for p in party]

    def __str__(self):
        pokemans = "\n".join([f"{p}" for p in self.party])
        txt = f"""
[{self.trainer_id}] {self.name}
{pokemans}
"""
        return txt
    
    def add_pokemon(self, pokemon: Pokemon):
        if len(self.party) >= 6:
            # Must handle error
            print("too many party members")
            return
        self.party.append(pokemon)

    def export(self):
        return {
            'name': self.name,
            'trainer_id': self.trainer_id,
            'party': [p.export() for p in self.party]
        }




if __name__ == "__main__":
    ...