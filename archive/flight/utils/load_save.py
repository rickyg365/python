import os
import json


def load(filepath: str):
    new_data = None
    with open(filepath, 'r') as in_file:
        new_data = json.load(in_file)
    return new_data

def save(data, filepath: str):
    with open(filepath, 'w') as out_file:
        json.dump(data, out_file, indent=4)
    return True

if __name__ == '__main__':
    ...
