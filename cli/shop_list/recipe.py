import os
import random

from typing import List, Dict, Union
from enum import Enum


# class MeasurementUnit:
#     def __init__(self):
#         pass

# Linked List Approach
class Node:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.next = None
        self.previous = None

class MeasurementList:
    def __init__(self, raw_data: List[List[str, int]]):
        self.root = None
        self.tail = None
        self.current_node = None
        self.load_initial_data(raw_data)

    def load_initial_data(self, raw_data: List[List[str, int]]):                
        previous_node = None

        for i in raw_data:
            name, ratio = i
            new_node = Node(name=name, value=ratio)

            if previous_node is None:
                # Set root node
                self.root = new_node
                previous_node = new_node
                continue

            previous_node.next = new_node
            new_node.previous = previous_node
            previous_node = new_node
            self.current_node = new_node
        
        self.tail = self.current_node

        return
    
    def traverse(self, steps: int):
        return


WET_MEASURES = [
    ['FLUID_OUNCE', 1],
    ['CUP', 8],
    ['PINT', 16],
    ['QUART', 32],
    ['GALLON', 128],
]

WET_LIST = None
previous_node = None

for i in WET_MEASURES:
    name, ratio = i
    new_node = Node(name=name, value=ratio)

    if previous_node is None:
        # Set root node
        WET_LIST = new_node
        previous_node = new_node
        continue

    previous_node.next = new_node
    new_node.previous = previous_node
    previous_node = new_node

# Enum Approach
class WetMeasurementUnit(Enum):
    FLUID_OUNCE = 1
    CUP = 8
    PINT = 16
    QUART = 32
    GALLON = 128
    # Distance from base units
 
class DryMeasurementUnit(Enum):
    TEASPOON = 1
    TABLESPOON = 3
    QUARTER = 12
    HALF = 24
    CUP = 48
    # Distance from base units
 
def wet_to_dry():
    # 1 fluid ounce = 2 tablespoons
    return

class Ingredient:
    # Assume linear units like meters
    UNIT_SYMBOLS = {
            'FLUID_OUNCE': 'fl',
            'CUP': 'cup',
            'PINT': 'pt',
            'QUART': 'qt',
            'GALLON': 'gal',
            'TEASPOON': 'tea',
            'TABLESPOON': 'tb',
            'QUARTER': 'qrt',
            'HALF': 'hlf',
        }
    def __init__(self, name: str, amount: int=None, unit: Union[WetMeasurementUnit, DryMeasurementUnit]=None):
        self.name = name
        self.amount = amount
        self.unit = unit

    def __str__(self):
        s = f"{self.amount:>3} {self.UNIT_SYMBOLS.get(self.unit.name, '?'):<3} | {self.name}"
        return s
    
    def convert_unit(self, new_unit: Union[WetMeasurementUnit, DryMeasurementUnit]=None):
        # Get new exp
        new_multiplier = self.unit.value/new_unit.value

        # Update Internal state
        self.unit = new_unit
        self.amount = (self.amount) * new_multiplier

        return
    
    def simplify(self):
        if self.amount%self.unit.value > 0:
            # Can be simplified
            pass
        
        return


class Recipe:
    def __init__(self, name:str, ingredients: List[Ingredient]):
        self.name = name
        self.ingredients = ingredients

        # Derived Variables
        # Total Cost
        # Bill of Materials

    def __str__(self):
        built_txt = '\n'.join(f"{i}" for i in self.ingredients)
        s = f'''{self.name}
{built_txt}
'''
        return s
    
    def add_ingredient(self):
        return
    
    def get_ingredient(self):
        return
    
    def update_ingredient(self):
        return
    
    def remove_ingredient(self):
        return
    
    def export(self):
        return {}
    
class RecipeBook:
    def __init__(self, recipes: List[Recipe]):
        self.recipes = recipes

    def __str__(self):
        
        built_txt = '\n'.join(f"{r.name}" for r in self.recipes)
        s = f'''Number of Recipes: {len(self.recipes)}

{built_txt}

'''
        return s
    
    def add_recipe(self):
        return
    
    def get_recipe(self):
        return
    
    def update_recipe(self):
        return
    
    def remove_recipe(self):
        return
    
    def export(self):
        return {}


def build_sample_recipe(recipe_name: str="Sample Recipe"):
    dry_units = [
        DryMeasurementUnit.TEASPOON, 
        DryMeasurementUnit.TABLESPOON, 
        DryMeasurementUnit.QUARTER, 
        DryMeasurementUnit.HALF, 
        DryMeasurementUnit.CUP
    ]
    wet_units = [
        WetMeasurementUnit.FLUID_OUNCE,
        WetMeasurementUnit.CUP,
        WetMeasurementUnit.PINT,
        WetMeasurementUnit.QUART,
        WetMeasurementUnit.GALLON
    ]

    POSSIBLE_UNITS = [*dry_units, *wet_units]

    data = []
    for _ in range(5):
        r = random.randint(1, 100)
        new_ingredient = Ingredient(
            name=f"Ingredient #{_}",
            amount=r,
            unit=POSSIBLE_UNITS[r%(len(POSSIBLE_UNITS))]
        )

        data.append(new_ingredient)
    return Recipe(recipe_name, data)

def build_sample_recipe_book():
    data = []
    for _ in range(3):
        new_recipe = build_sample_recipe(f"Sample Recipe #{_}")
        data.append(new_recipe)

    return RecipeBook(data)

if __name__ == "__main__":
    INGREDIENT_DATA = {
        'name': "Butter",
        'amount': "10",
        'unit': WetMeasurementUnit.CUP
    }
    RECIPE_DATA = [Ingredient(**INGREDIENT_DATA) for _ in range(5)]
    RECIPE_BOOK_DATA = [Recipe('misc', RECIPE_DATA) for _ in range(3)]  # is [*r] same as r

    sample_ingredient = Ingredient(**INGREDIENT_DATA)
    sample_recipe = build_sample_recipe("Test Recipe")
    sample_recipe_book = build_sample_recipe_book()

    print(f"""
{sample_ingredient}
__________________________
{sample_recipe}
__________________________
{sample_recipe_book}

""")

