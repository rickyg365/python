import json

def load_data(filepath: str):
    with open(filepath, 'r') as loaded_in:
        new_data = json.load(loaded_in)
    return new_data

def save_data(data: any, filepath: str):
    with open(filepath, 'w') as saving:
        json.dump(data, saving, indent=4)
