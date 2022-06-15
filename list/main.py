import json

from typing import List, Dict
from dataclasses import dataclass, field

# Data
from utils.insert_data import input_anime_entry_data

# Models and Views
from models.entry import AnimeEntry
from views.terminal_views import AnimeView, ComplexView

""" 
Data Journey


Input Data -> Raw Data -> Parsed Data -> Working Model/Data -> View -> Displayed

"""
def save(data, filepath):
    with open(filepath, 'w') as out_file:
        json.dump(data, out_file, indent=4)
    return

def load(filepath):
    with open(filepath, 'r') as in_file:
        data = json.load(in_file)
    return data

def create_anime_list():
    """ Loop for inputting multiple anime entries, creates raw data list """
    raw_data = []
    
    while True:
        new_data = input_anime_entry_data()

        raw_data.append(new_data)

        # Repeat Choice
        again = input("\nAdd another?: ")
        if again != 'y':
            break
    
    return raw_data


def main():
    # Test input anime data
    # new_anime_data = input_anime_entry_data()

    # Test Create new anime entry obj
    # new_anime_entry = AnimeEntry(**new_anime_data)

    # Create Views
    # simple_v = AnimeView(new_anime_entry)
    # complex_v = ComplexView(new_anime_entry)

    # Display
    # print('-'* 55)
    # print(new_anime_entry)

    # print(simple_v)
    # print(complex_v)

    # Create Raw List
    new_raw_list = create_anime_list()

    # Working and View List, We should only need 
    # to convert the current chosen obj into working and view
    new_working_list = [AnimeEntry(**rd) for rd in new_raw_list]
    new_view_list = [AnimeView(ae) for ae in new_working_list]

    # Display Views
    for view in new_view_list:
        print(view)

    # Save Raw Data as json
    save(new_raw_list, "data/raw_anime_list.json")

    # Save Working Data as pickle
    # Save View ?????


if __name__ == '__main__':
    main()
