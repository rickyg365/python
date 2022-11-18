import json

# DEFAULT FILEPATH
default_filepath = "data/default_save.json"


def load(filepath: str=default_filepath):
    """ Load json data from filepath """
    new_data = None
    with open(filepath, 'r') as in_file:
        new_data = json.load(in_file)
    return new_data

def save(save_data, filepath: str=default_filepath):
    """ Save data into a json at given filepath """
    with open(filepath, 'w') as out_file:
        json.dump(save_data, out_file, indent=4)
    return True

