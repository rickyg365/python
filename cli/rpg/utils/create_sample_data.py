import os

from models.character import Character, Item, Skill
from utils.file_handle import save_json

def generate_sample_data(save_dir: str=""):
    ITEMS = []
    SKILLS = []

    for _ in range(5):
        new_item = Item(name=f'Item #{_}')
        ITEMS.append(new_item)

    for _ in range(5):
        new_skill = Skill(name=f'Skill #{_}', description=f'This is the description of skill #{_}')
        SKILLS.append(new_skill)

    # Create dir if doesnt exist
    os.makedirs(save_dir, exist_ok=True)

    save_json([i.export() for i in ITEMS], f'{save_dir + "/"}items.json')
    save_json([s.export() for s in SKILLS], f'{save_dir + "/"}skills.json')
