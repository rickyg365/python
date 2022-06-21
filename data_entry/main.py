import os
import json

from utils.data_entry import input_config, input_entry, save_json


def display_dirs(path):
    if os.path.exists(path):
        print(os.listdir(path))
        # Overkill
        # for (dirpath, dirnames, filenames) in os.walk(path):
        #     print("\n+")
        #     print(dirpath)
        #     print(dirnames)
        #     print(filenames)
        return True
    return False


def main():
    # Start
    print("Welcome to terminal data entry!")
    # Enter Title
    TITLE = input("Enter Data Title(i.e Shopping Item): ")

    # # Enter Config
    # new_config, new_raw_config = input_config()

    # # Enter Data
    # new_data = input_entry(new_config, TITLE)


    # Create Dir 
    new_path = TITLE.replace(" ", "_").lower()

    
    # Load Config
    with open(f"data/{new_path}/config.json") as in_config:
        loaded_config = json.load(in_config)

    # Load Data
    with open(f"data/{new_path}/data.json") as in_data:
        loaded_data = json.load(in_data)

    print(loaded_config)
    print(loaded_data)


    # # Save Data
    # if not os.path.exists(f"data/{new_path}"):
    #     os.mkdir(f"data/{new_path}")

    # # Save Config
    # save_json(new_raw_config, f"data/{new_path}/config.json")

    # # Save Data
    # save_json(new_data, f"data/{new_path}/data.json")


    '''
    Later
    # Load Data
    # Edit Data
    # Save New Data
    '''
    return

if __name__ == '__main__':
    # main()
    display_dirs("data")
