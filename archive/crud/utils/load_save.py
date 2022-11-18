import os
import json

from typing import List, Dict, Any

"""
Handle loading and saving in various file formats
- json
    - Cases to handle
        1. dir part of filepath does not exist
- csv
"""


# Json
def load_json(filepath: str):
    try:
        with open(filepath, 'r') as load_file:
            return json.load(load_file)
    except FileNotFoundError:
        print(f"[FileNotFoundError] Could not load {filepath}!")

def save_json(data: Dict[str, Any], filepath: str | None = "data/temp_save.json"):
    try:
        with open(filepath, 'w') as save_file:
            json.dump(data, save_file, indent=4)
    except FileNotFoundError:
        print(f"[FileNotFoundError] Could not save to {filepath}")

