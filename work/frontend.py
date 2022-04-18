import os
from utils.custom_time import Time
from utils.handle_data import save_data, load_data
from models.time_block import TimeBlock

""" Handle Input """

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

def repeated_input(count: int, savepath: str = ""):
    # Create Data
    obj_list = []
    save_list = []
    for _ in range(count):
        new_block = input_block()

        obj_list.append(new_block)
        save_list.append(new_block.export())
    
    if savepath != "":
        save_data(save_list, savepath)
    return obj_list

def infinite_input(savepath: str=""):
    # Create Data
    obj_list = []
    save_list = []
    while True:
        new_block = input_block()

        obj_list.append(new_block)
        save_list.append(new_block.export())

        cont = input("Continue?: ")

        if cont == 'q':
            break
    
    if savepath != "":
        save_data(save_list, savepath)

    return obj_list

def main():
    # Create Data
    results = repeated_input(2, "data/test_save.json")
    for result in results:
        print(result)

if __name__ == '__main__':
    main()
