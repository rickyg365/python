import os
import json

from typing import List, Dict, Union


def save_json(data, filename: str):
    try:        
        with open(filename, 'w') as save_buf:
            json.dump(data, save_buf, indent=4)
    except Exception as e:
        print(e)

    return True


def load_json(filename: str):
    data = None

    with open(filename, 'a+') as load_buf:
        data = json.load(load_buf)
    
    return data









