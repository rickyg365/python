import os
import datetime
import json

from models.time import Time, TimeBlock
from dataclasses import dataclass


def load_data(filepath: str):
    with open(filepath, 'r') as in_file:
        new_data = json.load(in_file)    
    return new_data

def save_data(data, filepath: str):
    with open(filepath, 'w') as out_file:
        json.dump(data, out_file, indent=4)


class TimeBlockHandler:
    def __init__(self) -> None:
        self.data = []

    def __str__(self) -> str:
        txt = ""
        return txt
    
    def add_tb(self, title: str, start_time, end_time):
        # auto calculate the duration
        self.data.append(TimeBlock(title, start_time, end_time, duration=1.0))



def main():
    # Raw Data
    # raw_time_data = {
    #     "military": 7,
    #     "minutes": 30,
    #     "hours": 7
    # }

    # raw_timeblock_data = {
    #     "title": "Sample Title",
    #     "start_time": {
    #         "military": 7,
    #         "minutes": 30,
    #         "hours": 7
    #     },
    #     "end_time": {
    #         "military": 7,
    #         "minutes": 30,
    #         "hours": 7
    #     },
    #     "duration": 1.5
    # }

    # Load Data
    time_data_list = load_data("data/time.json")
    timeblock_data_list = load_data("data/timeblock.json")

    # Parse and Print, this can be loaded in another list class
    # new_time_data = [Time(**t) for t in time_data_list]
    
    new_time_data = []
    for t in time_data_list:
        new_obj = Time(**t)
        new_time_data.append(new_obj)
        print(new_obj)



    # new_timeblock_data = [TimeBlock(**tb) for tb in timeblock_data_list]

    new_timeblock_data = []
    for tb in timeblock_data_list:
        # Parse
        parsed_tb = {
            **tb,
            "start_time": Time(**tb.get("start_time")),
            "end_time": Time(**tb.get("end_time"))
        }
        new_obj = TimeBlock(**parsed_tb)
        new_timeblock_data.append(new_obj)
        print(new_obj)


    # Time
    # new_time = Time(**time_data)
    # print(new_time)

    # TImeBlock
    # new_timeblock = TimeBlock(**timeblock_data)
    # print(new_timeblock)
    
    # Saving Data
    # save_data([raw_time_data], "data/time.json")
    # save_data([new_timeblock.export()], "data/timeblock.json")


if __name__ == '__main__':
    main()
