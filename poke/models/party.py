from typing import List

from models.pokemon import Pokemon

from utils.lsjson import load_json, save_json


class Party:
    def __init__(self, starting_pokemon: List[Pokemon]=None):
        if starting_pokemon is None:
            starting_pokemon = []

        self.filled_slots = 0
        self.slots = starting_pokemon


    def __str__(self) -> str:
        txt = f"Current Pokemon: {self.filled_slots}"
        
        for poke in self.slots:
            txt += f"\n {poke}"
        
        return txt

    def save(self, filepath: str):
        # Convert Data
        export_data = []
        for poke in self.slots:
            export_data.append(poke.export())
        
        # Save Data 
        save_json(export_data, filepath)
        
        return True
    
    def load(self, filepath: str):
        ''' Load data from file, overwrites current party and data '''
        # Reset Party State
        self.slots = []
        self.filled_slots = 0

        # Load Raw Data
        raw_data = load_json(filepath)

        for item in raw_data:
            self.slots.append(Pokemon(**item))
            self.filled_slots += 1

        return self
    
    def add(self, new_pokemon: Pokemon):
        if self.filled_slots == 6:
            return False

        self.filled_slots += 1
        self.slots.append(new_pokemon)
        return True
    
    def remove(self, slot_id: int):
        self.filled_slots -= 1
        self.slots.pop(slot_id)