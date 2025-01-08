import os

from utils.file_handle import save_json, load_json
from game_engine.character import Character
from game_engine.item import Item, Equipment, EquipmentLoadout


if __name__ == "__main__":
    CHARACTER_DATA = load_json("data/character.json")
    c = Character(**CHARACTER_DATA)
    print(c)
    
    new_data = c.export()
    save_json(new_data, 'data/new_character.json')

