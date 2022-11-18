import os
import json

from typing import Dict, List

def load(filepath: str):
    with open(filepath, 'r') as in_file:
        new_data = json.load(in_file)
    return new_data


def input_grocery_item(data_config: Dict[str, str]):
    split_list_char = " "
    user_input = {}
    # Iterate through all keys
    for key, key_type in data_config.items():
        new_data_point = input(f"{key.title()} (q to Quit): ")

        if new_data_point == 'q':
            return False

        # Parse input
        match key_type:
            case "str":
                parsed_data_point = str(new_data_point)
            case "int":
                parsed_data_point = int(new_data_point)
            case "list":
                parsed_data_point = new_data_point.split(split_list_char)
            case _:
                parsed_data_point = new_data_point
        # Add to new dictionary
        user_input[key] = parsed_data_point
    return user_input

def input_loop(data_config):
    input_list = []

    while True:
        os.system("cls")
        user_input = input_grocery_item(data_config)

        if not user_input:
            break
        
        input_list.append(user_input)

    return input_list


def main():
    config = load("config.json")
    new_data = input_grocery_item(config)
    print(new_data)
    

if __name__ == '__main__':
    main()
