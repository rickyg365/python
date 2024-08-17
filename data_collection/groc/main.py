import os
import json

from typing import Dict
from utils.data_wrapper import DataWrapper, flatten_dict

def custom_str_conversion_func(d):
    return d

SAMPLE_DATA_MAP = {
    "name": custom_str_conversion_func,
    "id": int,
    "data": float
}

def input_entry(data_map):
    data = {}
    for field, type_conversion_func in data_map.items():
        raw_input = input(f"{field}({type_conversion_func.__name__}): ")
        data[field] = type_conversion_func(raw_input)
    return data


if __name__ == "__main__":
    FILENAME = "new_data.json"
    entries = []
    while True:
        new_entry = input_entry(SAMPLE_DATA_MAP)
        entries.append(new_entry)

        # Input More
        again = input("Input another entry?: ")
        if again == 'q':
            break
            
    new_data = DataWrapper(entries, filename=FILENAME)
    new_data.save()
    print(new_data)
    # print(entries)
