import json
from models.grocery_item import GroceryItem


def load_json(self, new_filepath: str=None):
    """ Load Recipes from json format """
    if new_filepath is None:
        new_filepath = self.json_path

    with open(new_filepath, 'r') as in_json:
        load_data = json.load(in_json)
    
    for data_entry in load_data:
        self.add_item(GroceryItem(**data_entry))

    return True


def save_json(self, new_filepath: str=None):
    """ Save Recipes to json format """
    if new_filepath is None:
        new_filepath = self.json_path
    
    with open(new_filepath, 'w') as out_json:
        json.dump(self.export(), out_json, indent=4)

    return True
