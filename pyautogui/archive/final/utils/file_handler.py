import json


def load_json(filename):
    data = None
    with open(filename, 'r') as load_buf:
        data = json.load(load_buf)
    return data

def save_json(data, filename: str):
    with open(filename, 'w') as save_buf:
        json.dump(data, save_buf, indent=4)
    return

