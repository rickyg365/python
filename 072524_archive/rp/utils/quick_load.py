import json
DEFAULT_PATH = "data/data.json"

def load_json(filename: str):
    data = None
    with open(filename, 'r') as loaded_data:
        data = json.load(loaded_data)
    return data


def save_json(data, filename: str):
    with open(filename, 'w') as save_buf:
        json.dump(data, save_buf, indent=4)
    return










