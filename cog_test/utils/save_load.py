import os
import json

def save_json(save_data, filepath: str="base_filepath.txt"):
    with open(filepath, 'w') as out_json:
        json.dump(save_data, out_json, indent=4)
    # Return save_data for chaining? hahaha imagine chaining after you save, ya never know
    return save_data


def load_json(filepath: str):
    with open(filepath, 'r') as in_json:
        data = json.load(in_json)
    return data
