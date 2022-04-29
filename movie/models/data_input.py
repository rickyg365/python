from typing import Dict

""" 
"""

# Data Config
data_config = {
    "id": int,
    "name": str
}


def parse_item(input_item, data_configuration: Dict[str, any] = data_config):
    input_data = {}
    # i = {input_data[key]: parse_func(input_item[key]) for key, parse_func in data_configuration.items()}
    for key, parse_func in data_configuration.items():
        input_data[key] = parse_func(input_item[key])

    return input_data
    

def input_item(data_configuration: Dict[str, any]=data_config) -> Dict[str, any]:
    """ Gets data based off of data config and returns cleaned version. """
    input_data = {}
    for key, parse_func in data_configuration.items():
        input_data[key] = parse_func(input(f"[ {key} ]: "))

    return input_data

def main():
    new_item = input_item()
    print(new_item)

if __name__ == '__main__':
    main()
