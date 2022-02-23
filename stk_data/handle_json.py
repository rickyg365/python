import os
import json


def save_json(filepath, data):
    with open(filepath, 'w') as out_json:
        json.dump(data , out_json, indent=4)
    return

def load_json(filepath):
    new_data = None
    with open(filepath, 'r') as in_json:
        new_data = json.load(in_json)
    return new_data
