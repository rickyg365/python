import os

from datetime import datetime

from utils.simp_lib import prettify_dict
from utils.simp_data import create_defaulted_data, input_data
from utils.easy_save import save_json, load_json


"""
TBD
- Choose and load configs use filenames as string
- Create different collections of data also using filename as string
"""


def main():
    FILENAME = "data/sample_collection.json"
    CONFIG_FILEPATH = "data/configs/sample_config.json"
    

    data = []
    # Check if files exist 
    if os.path.isfile(FILENAME):
        data = load_json(FILENAME)

    if os.path.isfile(CONFIG_FILEPATH):
        SAMPLE_CONFIG = load_json(CONFIG_FILEPATH)

    # Track Save Status
    added_data = False
    save_data = False
    
    while True:
        display = "\n".join([prettify_dict(d) for d in data])
        print(f"""
{display}""")
        user_hint = f"""New Data: {'*' if added_data else ' '}  Save: {'*' if save_data else ' '}
[ (a)dd | (s)ave | (q)uit ]
"""
        u_in = input(f"{user_hint}>>> ")

        match u_in:
            case "a":
                new_point = input_data(SAMPLE_CONFIG)
                data.append(new_point)
                added_data = True
            case "s":
                save_data = True
            case "q":
                break
            case _:
                pass

        
    if added_data and save_data:
        save_json(data, FILENAME)
        added_data = False
    return




if __name__ == "__main__":
    main()