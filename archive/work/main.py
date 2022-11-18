import os

from models.time_block import TimeBlock
from utils.custom_time import Time
from utils.handle_data import load_data, save_data

from utils.data_parser import TimeBlockCleaner

"""
# print(new_block.export())
# Create Repeated Fake data
# new_test_list = [new_block.export() for x in range(5)]
# with open("data/test_time_block.json", 'w') as out_file:
#     json.dump(new_test_list, out_file, indent=4)
"""


def input_time(title_text: str = "") -> Time:
    check_empty = lambda x: "0" if x == "" else x 
    print(title_text)
    
    hour = check_empty(input("Hour: "))
    minute = check_empty(input("Minute: "))
    second = check_empty(input("Second: "))
    am = True if input("AM?: ") in  ["", "y"] else False

    return Time(int(hour), int(minute), int(second), am)

def input_block() -> TimeBlock:
    title = input("\nTitle: ")
    description = input("Description: ")
    print(f"{40*'_'}")

    start_time = input_time("[Start Time]")
    print(f"{40*'-'}")
    end_time = input_time("[End Time]")
    print(f"{40*'_'}")

    # custom_size = input("Custom Size?: ")

    return TimeBlock(title, description, start_time, end_time)


def main():
    # Load Data
    load_path = "data/test_time_block.json"
    import_data = load_data(load_path)

    obj_list = []
    for raw_data_point in import_data:
        # Clean Raw Data
        parsed_data = TimeBlockCleaner(raw_data_point)
        # cleaned_start = Time(**raw_data_point["start_time"])
        # cleaned_end = Time(**raw_data_point["end_time"])

        # parsed_data = {
        #     **raw_data_point,
        #     "start_time": cleaned_start,
        #     "end_time": cleaned_end
        # }

        new_time_block = TimeBlock(**parsed_data, size=35)
        obj_list.append(new_time_block)

    # Save Data
    # obj_list = []
    # save_list = []
    # for _ in range(2):
    #     new_block = input_block()

    #     obj_list.append(new_block)
    #     save_list.append(new_block.export())
    
    # save_data(save_list, "data/test_save.json")

    # Print
    for obj in obj_list:
        print(obj)

if __name__ == '__main__':
    main()
