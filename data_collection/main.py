import os
import json

from datetime import datetime
from dataclasses import dataclass



@dataclass
class Item:
    name: str
    price: float

@dataclass
class Store:
    unique_id: str
    name: str

def save_json(data, filepath: str="default.json"):
    with open(filepath, 'w') as save_buf:
        json.dump(data, save_buf, indent=4)
    return True

def load_json(filepath: str="default.json"):
    data = None
    with open(filepath, 'r') as load_buf:
        data = json.load(load_buf)
    
    return data


def program():
    # Show Metadata(filepath, current data)
    # Load File
    # Edit Data
    # Add Data
    # Delete Data
    ...


if __name__ == "__main__":
    # program()
    # Variables
    DEFAULT_FILE = "sample.json"
    DEFAULT_DATA = {
        "id": 0,
        "name": "Sample Name"
    }

    # Load File
    if os.path.isfile(DEFAULT_FILE):
        DEFAULT_DATA = load_json(DEFAULT_FILE)

    # Add Data
    
    # Delete Data
    # Display Data
    # Edit Data
    
    ...

