import os
import json

from models.recipe import Recipe
from models.recipe_book import RecipeBook


def load_data(filepath: str):
    # import data
    with open(filepath, 'r') as in_data:
        data = json.load(in_data)

    return data



def main():
    test_data = load_data("data/test_data.json")
    print(test_data)

if __name__ == '__main__':
    main()
