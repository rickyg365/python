import os
import json

from data_object import DataObject
from custom_object import CustomObject


def save_json(data: DataObject, filename: str):
    with open(filename, "w") as save_buf:
        json.dump(data, save_buf, indent=4)
    return True


def load_json(filename: str):
    data = None
    with open(filename, "r") as load_buf:
        data = json.load(load_buf)
    return data


def pprint(data, indent_level: int = 0):
    indentation = indent_level * "  "
    s = ""
    for k, v in data.items():
        cd = v
        if isinstance(v, dict):
            cd = pprint(v, indent_level + 1)

        s += f"\n{indentation}{k}: {cd}"

    return s


if __name__ == "__main__":
    # Filenames
    DATA_FILENAME = "data_object.json"
    CUSTOM_FILENAME = "custom_object.json"

    # Raw Data for creating
    # raw_data = {"name": "Sample Name", "status": "active"}
    # raw_custom_data = {
    #     "id_number": 1,
    #     "data": {"name": "Sample Name", "status": "active"},
    # }

    # Loading Raw Data
    raw_data = load_json(DATA_FILENAME)
    raw_custom_data = load_json(CUSTOM_FILENAME)

    # Creating Objects from raw data
    objects = [
        DataObject(raw_data, DATA_FILENAME),
        CustomObject(**raw_custom_data),
    ]

    for obj in objects:
        # Display Objects
        print(obj)

        # Save Objects
        save_json(obj.export(), obj.filename)

    # Display Raw Data
    s1 = pprint(raw_data)
    s2 = pprint(raw_custom_data)

    print(s1)
    print(s2)
