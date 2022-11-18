import os
import json
from typing import List, Dict

from models.animal import Animal
from models.keeper import Keeper
# from models.guest import Guest
from models.exhibit import Exhibit


""" 
Model: Zoo

Zoo(zoo_name: str, exhibits: List[Exhibit], animals: List[Animal], keepers: List[Keeper], loadpath: str=None):
    exhibits = Exhibit[]
    animals = Animal[]
    keepers = Keeper[]

    path = loadpath
    
    if self.path is not None:
        self.load()

"""
class Zoo:
    def __init__(self, name: str, filepath: str="data/default.json", animals: List[Animal]=None, keepers: List[Keeper]=None, exhibits: List[Exhibit]=None):
        # Meta Data
        self.name = name

        self.guest_full_count = 0
        self.animal_full_count = 0
        self.keeper_full_count = 0
        self.exhibit_full_count = 0

        self.max_guest_limit = 200

        # Calculate these in the future
        # num_of_guests * ticket_cost
        
        self.monthly_income = 1000  
        
        # Calculate these in the future    
        # (num_of_animals * avg_cost_per_feed) + (num_of_exhibits * avg_cost_per_exhibit) + (num_employees * avg_salary) + electricity + water
        
        self.monthly_expense = 900

        # Animals
        self.animals = animals
        
        # Employees
        '''
        total employees
        on-shift employees
        '''
        self.keepers = keepers
        
        # Exhibits
        '''
        total exhibits
        open exhibits
        '''
        self.exhibits = exhibits

        # Loading
        self.path = filepath
        
        
        if self.load():
            # Refresh Count after loading
            self.refresh_count()
    
    
    def export(self):
        output_data = {
            "name": self.name,
            "filepath": self.path,
            "animals": [a.export() for a in self.animals],
            "keepers": [k.export() for k in self.keepers]
        }
        return output_data
    
    def intake(self, new_data):
        self.name = new_data['name']
        self.path = new_data.get('filepath', "data/no_path.json")
        self.animals = [Animal(**ra) for ra in new_data.get('animals', [])]
        self.keepers = [Keeper(**rk) for rk in new_data.get('keepers', [])]
        # RAD - Raw Animal Data
        return

    def load(self) -> bool:
        """ True if loaded, else False """
        if os.path.exists(self.path):
            with open(self.path, 'r') as in_data:
                new_data = json.load(in_data)
                self.intake(new_data)
            return True
        return False
    
    def save(self):
        # Build Export data
        export_data = self.export()

        with open(self.path, 'w') as out_file:
            json.dump(export_data, out_file, indent=4)

    def refresh_count(self):
        self.animal_full_count = len(self.animals)
        self.keeper_full_count = len(self.keepers)
        self.exhibit_full_count = len(self.exhibits)
        


def main():
    return


if __name__ == '__main__':
    main()
