import os
import json



def load_json(filepath: str):
    data = None

    with open(filepath, 'r') as load_buf:
        data = json.load(load_buf)
    
    return data



def save_json(data, filepath: str):
    with open(filepath, 'w') as save_buf:
        json.dump(data, save_buf, indent=4)




