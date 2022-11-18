import json

from typing import List, Dict
from dataclasses import dataclass, field

# Data
from utils.insert_data import create_entry_list, input_entry_data

# Models and Views
from models.entry import Entry, ENTRY_CONFIG
from views.terminal_views import View, ComplexView

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


def main():
    title = "Shopping Data"
    # sample_config = {
    #     "name": str,
    #     "price": float,
    #     "amount": int,
    #     "data": list
    # }

    # Test entry input
    # new_data = create_entry_list(sample_config, title)

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
    new_raw_list = create_entry_list(ENTRY_CONFIG, title)

    # Working and View List, We should only need 
    # to convert the current chosen obj into working and view
    new_working_list = [Entry(**rd) for rd in new_raw_list]
    new_view_list = [View(ae) for ae in new_working_list]

    # Display Views
    for view in new_view_list:
        print(view)

    # Save Raw Data as json
    save(new_raw_list, "data/raw_list.json")

    # Save Working Data as pickle
    # Save View ?????


if __name__ == '__main__':
    main()
