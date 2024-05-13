from typing import List, Dict

"""
SAMPLE DATA

ID: int
NAME: str
URL: str
PRICE: float
DATE_CREATED: datetime.now()
"""


def create_defaulted_data(config: Dict[str, str], type_map=None):
    if type_map is None:
        type_map =  {
            "int": (0, int),
            "float": (0.00, float),
            "str": ("", str),
            "other": (None, None)
        }

    new_data = {}
    for attr_name, attr_type in config.items():
        if attr_type in type_map.keys():
            new_data[attr_name] = type_map[attr_type][0]
        else:
            new_data[attr_name] = type_map['other'][0]
    
    return new_data


def input_data(config: Dict[str, str], type_map=None):
    if type_map is None:
        type_map = {
            "int": (0, int),
            "float": (0.00, float),
            "str": ("", str),
            "other": (None, None)
        }

    new_data = {}
    for attr_name, attr_type in config.items():
        user_input = input(f"{attr_name}<{attr_type}>: ")
        if attr_type in type_map.keys():
            new_data[attr_name] = type_map[attr_type][1](user_input)
        else:
            new_data[attr_name] = user_input

    return new_data



if __name__ == "__main__":    
    SAMPLE_CONFIG = {
        "ID": "int",
        "NAME": "str",
        "URL": "str",
        "PRICE": "float",
        "DATE_CREATED": "date",
    }

    dd = create_defaulted_data(SAMPLE_CONFIG)
    ud = input_data(SAMPLE_CONFIG)
    print(dd)
    print(ud)

    # Save Config
    # save_json(SAMPLE_CONFIG, "data/configs/sample_config.json")

