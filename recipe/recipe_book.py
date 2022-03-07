import os
import json
from tracemalloc import start

from typing import List, Dict

from recipe import Recipe
from get_recipe import RecipeFetcher


class RecipeBook:
    def __init__(self, starting_list: List[Recipe]=None):
        if starting_list is None:
            starting_list = []

        self.recipes = starting_list
        self.fetcher = RecipeFetcher()

    def __repr__(self) -> str:
        text = f"[ Recipe Book ]:\n"
        for _, item in enumerate(self.recipes):
            text += f"\n  {_}. {item.name}"        
        return text

    def download_recipe(self, query: any):
        """ Download a recipe using a partial name or recipe id # """
        # Use Recipe Fetcher to search query
        # Parse Recipe
        # Convert to Recipe Object
        # Append to main list
        return

    def select_recipe(self, recipe_id: int) -> Recipe:
        return
    
    def select_all(self) -> List[Recipe]:
        return self.recipes

    def add_recipe(self, raw_recipe: Dict[str, any]):
        return

    def delete_recipe(self, recipe_id: int):
        return

    def edit_recipe(self, recipe_id: int):
        return

    def load_json(self):
        """ Load Recipes from json format """
        return
    
    def load_csv(self):
        """ Load Recipes from csv format """
        return

    def save_json(self):
        """ Save Recipes to json format """
        return

    def save_csv(self):
        """ Save Recipes to csv format """
        return
    


def main():
    return

if __name__ == '__main__':
    main()




