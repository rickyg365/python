import os
import json

from models.recipe import Recipe
from models.recipe_book import RecipeBook

""" 
Goals:
- Input data
- save and load as json
- display data
- analyze data?
"""

def load_data(filepath: str):
    # import data
    with open(filepath, 'r') as in_data:
        loaded_data = json.load(in_data)
    return loaded_data



def main():
    test_data = load_data("data/test_data.json")
    print(test_data)

    recipe = Recipe(**test_data)
    print(recipe.full_str())

if __name__ == '__main__':
    main()
