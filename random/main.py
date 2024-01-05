import os
import json

import time

from datetime import datetime as dt

"""
Basic Gameplan

Data

{
    uid: {
        uid: "uid",
        name: "name",
        date_created: "date"
    }
}



Frontend

- [uid] name date_created




Date Formats
____________________________
%a Weekday
%A Weekday (full)
%w Weekday (number)

%d Day of the Month

%b Month 
%B Month (full)
%m Month (number)

%y Year (number)
%Y Year (full number)

%H Hour (24 hour)
%I Hour (12 hour)

%p Am/Pm 

%M Minute
%S Second

%j Day of Year
%W Week Number
"""

class DataPoint:
    def __init__(self, uid: int, name: str, date_created: str):
        self.id = uid
        self.name = name
        self.date_created = date_created

    def __str__(self) -> str:
        s = f"""
id = {self.id}
name = {self.name}
date_created = {self.date_created}
"""
        return s

    def display_entry(self):
        return f"[{self.id:03}] {self.name}  {self.date_created}"

# Creating Sample Data
def create_data_point(prev_id: int=None):
    DATETIME_FORMAT = f"%d_%m_%y_%I%M"
    new_data = {
        "uid": prev_id + 1,
        "name": "Fake Name",
        "date_created": dt.now().strftime(DATETIME_FORMAT)
    }
    return new_data


# Handle Files
def save_data(data, filename: str="file.json"):
    with open(filename, 'w') as save_buffer:
        json.dump(data, save_buffer,indent=4)

def load_data(filename: str):
    data = None
    with open(filename, 'r') as load_buffer:
        data = json.load(load_buffer)

    proccessed_data = {k: DataPoint(**v) for k, v in data.items()}
    return proccessed_data


# Frontend
def frontend_entry(data_point):
    uid = data_point.get("uid", None)
    name = data_point.get("name", None)
    date_created = data_point.get("date_created", None)
    
    return f"[{uid:03}] {name}  {date_created}"



def create_sample_entries(num_entries: int=20, save_file: bool=1):
    '''
    dep:
    - save_data
    '''
    # Create Sample Entries
    FILENAME = "entry_sample_data.json"
    CURRENT_ID = 0
    ENTRIES = {}

    for _ in range(num_entries):
        new_data = create_data_point(CURRENT_ID)
        CURRENT_ID += 1
        
        new_id = CURRENT_ID  # new_data.get("uid", 0)

        ENTRIES[new_id] = new_data
        time.sleep(65)

    if save_file:
        save_data(ENTRIES, FILENAME)

    return ENTRIES


def build_display():
    '''
    dep:
    - CLASS: DataPoint
    - frontend_entry()
    '''
    # Build Display
    display = ""
    for _ in ENTRIES.values():
        display += f"\n{_.display_entry()}"
    return display


if __name__ == "__main__":    
    # Load Entries
    ENTRIES = load_data("entry_sample_data.json")
    # print(ENTRIES)
    
    DISPLAY = build_display()
    print(DISPLAY)



