import os

import json

from typing import Callable, Dict


class Entry:
    def __str__(self) -> str:
        txt = f"Entry: "
        return txt
    
    def export(self):
        """ TBI: export all attribute names and values
        { 
            attr_name: attr_value,
            ...
        } 
        """
        pass


def input_config(type_match: Dict[str, Callable]=None):
    """ Create Entry Config 
    {
        key_name: key_type,
        ...
    }

    Default type_match
    type_match = {
            "str": str,
            "int": int,
            "float": float,
            "custom": func
        }
    """
    # Defaults
    if type_match is None:
        type_match = {
            "str": str,
            "int": int,
            "float": float,
            "bool": bool
        }
    # Starter Variables
    config = {}
    raw_config = {}

    # Infinite loop
    while True:
        new_key = input("\nEnter New Key(or q to quit): ")
        # Break Condition
        if new_key == 'q':
            break

        new_type = input("Corresponding Type: ")
        
        raw_config[new_key] = new_type

        # Check Key
        new_type = type_match[new_type]

        # Add to config
        config[new_key] = new_type
    return config, raw_config

def input_entry(config: Dict[str, Callable], title: str="New Entry"):
    # Starter Variables
    final_data = []

    # Main Loop
    while True:
        print(f"\n[ {title} ]")
        current_entry = {}
        # Input Entry
        for key in config.keys():
            # Add Data Point
            fix_type = config[key]
            current_entry[key] = fix_type(input(f"{key.title()}: "))

        final_data.append(current_entry)

        again = input("Add Another? (y/n): ")
        if again in ['n', 'q']:
            break
    
    return final_data


def save_json(save_data, filepath: str="data/save_data_default.json"):
    if not os.path.exists("data"):
        return False

    with open(filepath, 'w') as out_json:
        json.dump(save_data, out_json, indent=4)
    return True

def main():
    my_config = input_config()
    my_data = input_entry(my_config, "Custom Entry")

    print(my_config)
    print(my_data)

    save_json(my_data)


if __name__ == '__main__':
    main()
