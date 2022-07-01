import json

def save_json(data: any, filepath: str, filemode: str='w'):
    """ Save data to json (Overwrite) """
    with open(filepath, filemode) as out_json:
        json.dump(data, out_json, indent=4)
    return data # for Chaining


def load_json(filepath: str):
    with open(filepath, 'r') as in_json:
        data = json.load(in_json)
    return data
