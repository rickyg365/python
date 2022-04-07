import os
import json
from typing import Callable

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

def save_data(filepath: str, save_data):
    # Save Data
    with open(filepath, 'w') as out_json:
        json.dump(save_data, out_json, indent=4)

def get_single(input_str: str, parsing_func: Callable=None):
    user_input = input(input_str).strip()
    
    # Parse Input
    if parsing_func is not None:
        user_input = parsing_func(user_input)
    
    return user_input

def get_multi_input(input_str: str, repitions: int, parsing_func: Callable=None):
    output = []
    if repitions == 0:
        # Good Big Number
        repitions = 99
    
    print(input_str)

    for i in range(repitions):
        user_input = input(f"{i+1}: ").strip()

        if user_input == 'q':
            return output

        # Parse Input
        if parsing_func is not None:
            user_input = parsing_func(user_input)

        output.append(user_input)
    return output

def recipe_input():
    recipe_data = {}

    recipe_data['name'] = get_single("Recipe Name: ")
    recipe_data['description'] = get_single("Recipe Description: ")

    raw_ingredient_list = get_multi_input("Ingredient(name, quantity)", 0)
    
    parsed_ingredients = {}

    for raw_ingredient in raw_ingredient_list:
        name, quantity = raw_ingredient.split(", ")
        parsed_ingredients[name.title()] = quantity
        
    recipe_data['ingredients'] = parsed_ingredients

    recipe_data['steps'] = get_multi_input("Recipe Step", 0)

    return recipe_data


def main():
    test_data = load_data("data/test_data.json")
    # print(test_data)

    test_recipe = Recipe(**test_data)
    test_recipe.set_detail_level(False)
    print(test_recipe)

    # sing = get_single("Test Input: ")
    # print(sing)

    # mult = get_multi_input("Test Input", 5)
    # print(mult)

    recipe_data = recipe_input()
    new_recipe = Recipe(**recipe_data)
    print(new_recipe)

    # Save Data
    test_savepath = "data/test_save.json"
    save_data(test_savepath, new_recipe.export())

if __name__ == '__main__':
    main()
