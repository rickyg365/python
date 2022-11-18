import os

from utils.save_load import save_json, load_json
from utils.config import input_raw_config, get_config, parse_raw_config, input_data

""" 
Example Data

config:
    {
        "name": str,
        "price": float,
        "tags": List[str]
        "purchase date": str
        "expiration date": str | None
    }

Data:
    {
        "name": "apple",
        "price": 0.59,
        "tags": ["produce", "fruit"]
        "purchase date": 06/23/2022
        "expiration date": None
    }

"""

def main():
    # Variables
    config_path = "data/config.json"
    data_path = "data/items.json"

    # Load Config
    config = get_config(config_path)
    # print(config)

    # Inpute New Data
    new_data = input_data(config)

    # Save New Data
    save_json(new_data, data_path)

    # while True:
    #     u_in = input(">>> ")
    #     if u_in == 'q':
    #         break
    return

if __name__ == '__main__':
    main()
