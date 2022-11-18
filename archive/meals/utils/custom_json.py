import json
from typing import List, Dict


def save_json(data: Dict[str, any], filepath: str):
    try:
        with open(filepath, 'w') as save:
            json.dump(data, save, indent=4)
    except Exception as e:
        print(e)

def load_json(filepath: str):
    with open(filepath, 'r') as load:
        new_data = json.load(load)
    return new_data

