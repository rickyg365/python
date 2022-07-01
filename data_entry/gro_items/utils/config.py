import os
import json

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


def input_raw_config():
    print("[ Input Config ]\nkey: key_type")
    config = {}
    
    while True:
        # Input new key/type
        user_input = input(">>> ")

        if user_input == "q":
            break

        # Sanitation
        key, key_type = [x.strip() for x in user_input.split(":")]

        # No Parsing so that we can save as json

        # Assigning
        config[key] = key_type
        
    return config

def parse_raw_config(raw_config):
    parsed_config = {}
    for k, k_type in raw_config.items():
        # Parsing
        match k_type:
            case "str":
                k_type = str
            case "int":
                k_type = int
            case "float":
                k_type = float
            case "list":
                k_type = list
        parsed_config[k] = k_type
    return parsed_config


def get_config(config_path: str="data/config.json"):
    """ Load config if it exists, else create a new one! """
    raw_config = {}

    # Check if config exists
    if not os.path.exists(config_path):
        print("[ Creating New Config ]")
        raw_config = input_raw_config()
        # save_json(config, config_path)
    else:
        print("[ Loading Config ]")
        with open(config_path, 'r') as in_fig:
            raw_config = json.load(in_fig)

    config = parse_raw_config(raw_config)

    return config


def input_data(config):
    running = True
    new_data = []
    
    print("[ Input Data ]")
    
    # Config Key
    config_key = ""
    for k, t in config.items():
        config_key += f"\n{k}: {t}"
    
    print(config_key)
    # Main Loop
    while running:
        new_entry = {}
        print("\n+ new entry +")
        for key, key_type in config.items():            
            u_in = input(f"{key}: ")
            
            if u_in == 'q':
                running = False
                break

            if key_type is list:
                parsed_input = u_in.split(" ")
            else:
                parsed_input = key_type(u_in)

            new_entry[key] = parsed_input
        if len(new_entry) == 0:
            continue
        new_data.append(new_entry)  
    return new_data


def main():
    config_path = "data/config.json"
    config = get_config(config_path)

    print(config)
    data = input_data(config)
    
    print(data)
    return


if __name__ == '__main__':
    main()
