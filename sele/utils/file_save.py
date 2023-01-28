import json

def save_json(filename: str, data):
    with open(filename, 'w') as save_data:
        json.dump(data, save_data)
