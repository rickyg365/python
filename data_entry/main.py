import os

from utils.data_entry import input_config, input_entry, save_json


def main():
    # Start
    print("Welcome to terminal data entry!")
    # Enter Title
    TITLE = input("Enter Data Title(i.e Shopping Item): ")

    # Enter Config
    new_config = input_config()

    # Enter Data
    new_data = input_entry(new_config, TITLE)

    # Save Data
    save_json(new_data, f"data/{TITLE}.json")

    '''
    Later
    # Load Data
    # Edit Data
    # Save New Data
    '''
    return

if __name__ == '__main__':
    main()
