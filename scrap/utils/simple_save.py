import os
import json


def save_json(data, filename: str="load_file.json"):
    with open(filename, 'w') as save:
        json.dump(data, save)

def load_json(filename: str="load_file.json"):
    data = None
    with open(filename, 'r') as load:
        data = json.load(load)
    return data



if __name__ == "__main__":
    FILENAME = "TEST_FILE.json"
    SAMPLE_DATA = {
        "name": "Joe Mama",
        "id": 1
    }
    save_json(SAMPLE_DATA, FILENAME)

    test_data = load_json(FILENAME)

    print(f"{test_data=}")



