import os
import json


def save_json(export_data, filepath: str):
    # if not os.path.exists(filepath):
        #     os.makedirs(filepath)  # Permission Error

    with open(filepath, 'w') as save_file:
        json.dump(export_data, save_file, indent=4)
    return True

def load_json(filepath: str):
    raw_data = None
    with open(filepath, 'r') as loaded_file:
            raw_data = json.load(loaded_file)
    return raw_data

