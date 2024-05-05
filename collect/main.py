import os

from typing import List, Dict
from datetime import datetime

import json


def save_json(data, filename: str):
    with open(filename, 'w') as save_buf:
        json.dump(data, save_buf, indent=4)
    return


def load_json(filename: str):
    data = None
    with open(filename, 'r') as load_buf:
        data = json.load(load_buf)
    return data

"""
SAMPLE DATA

ID: int
NAME: str
URL: str
PRICE: float
DATE_CREATED: datetime.now()
"""

SAMPLE_CONFIG = {
    "ID": "int",
    "NAME": "str",
    "URL": "str",
    "PRICE": "float",
    "DATE_CREATED": "date"

}

def prettify_dict(data):
    new_str = ""
    for k, v in data.items():
        new_str += f"{k}: {v} \n"
    return new_str


def create_defaulted_data(config: Dict[str, str]):
    new_data = {}
    for attr_name, attr_type in config.items():
        match attr_type:
            case 'int':
                new_data[attr_name] = 0
            case 'float':
                new_data[attr_name] = 0.00
            case 'str':
                new_data[attr_name] = ""
            case 'date':
                new_data[attr_name] = f"{datetime.now()}"

            case _:
                pass
    
    return new_data

def input_data(config: Dict[str, str]):
    new_data = {}
    for attr_name, attr_type in config.items():
        user_input = input(f"{attr_name}<{attr_type}>: ")
        match attr_type:
            case 'int':
                new_data[attr_name] = int(user_input)
            case 'float':
                new_data[attr_name] = float(user_input)
            case 'str':
                new_data[attr_name] = user_input
            case 'date':
                new_data[attr_name] = user_input

            case _:
                pass
    

    return new_data

def main():
    FILENAME = "data/collected_data.json"
    # dd = create_defaulted_data(SAMPLE_CONFIG)
    # ud = input_data(SAMPLE_CONFIG)

    data = []
    # Check if load data exist 
    if os.path.isfile(FILENAME):
        data = load_json(FILENAME)

    added_data = False
    while True:
        display = "\n".join([prettify_dict(d) for d in data])
        print(f"""
{display}
""")
        u_in = input(">>> ")

        if u_in == 'q':
            break

        new_point = input_data(SAMPLE_CONFIG)
        data.append(new_point)
        added_data = True

    if added_data:
        save_json(data, FILENAME)
    return




if __name__ == "__main__":
    main()