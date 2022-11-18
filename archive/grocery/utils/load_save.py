import json
from typing import List, Dict

def save(data, filepath: str):
    """ Save Raw Data as given filepath """
    with open(filepath, 'w') as out_file:
        json.dump(data, out_file, indent=4)
    return True

def load(filepath: str) -> List[Dict[str, any]]:
    """ Load in Raw Data from given filepath """
    with open(filepath, 'r') as in_file:
        new_data = json.load(in_file)
    return new_data
