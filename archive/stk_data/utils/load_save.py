import os
import json

def save_json(data, filepath: str):
    with open(filepath, 'w') as out_json:
        json.dump(data, out_json, indent=4)
    return

