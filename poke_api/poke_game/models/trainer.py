import os
from typing import List, Dict, Union
from models.pokemon import Pokemon, PokemonBase


class Trainer:
    def __init__(self, name: str, trainer_id: int=None, party: List[Pokemon]=None):
        self.trainer_id = trainer_id
        self.name = name
        self.party = party

    def __str__(self):
        pokemans = "\n".join([f"{p}" for p in self.party])
        txt = f"""
[{self.trainer_id}] {self.name}
{pokemans}
"""
        return txt

    def export(self):
        return {
            'name': self.name,
            'trainer_id': self.trainer_id,
            'party': [p.export() for p in self.party]
        }




if __name__ == "__main__":
    ...