import os
import json

from typing import List, Any

def load_txt(filepath: str):
    try:
        with open(filepath, 'r') as load_file:
            return load_file.read()
    except FileNotFoundError:
        print(f"File Not Found: {filepath}")
        return None


def save_txt(data: str, filepath: str):
    try:
        with open(filepath, 'w') as save_file:
            save_file.write(data)
    except Exception as e:
        print(e[:50])


def load_json(filepath: str):
    with open(filepath, 'r') as load_json:
        return json.load(load_json)

def save_json(data: Any, filepath: str):
    with open(filepath, 'w') as save_json:
        json.dump(data, save_json, indent=4)
