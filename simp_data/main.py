import os
import json


def save_json(data, filename: str):
    with open(filename, 'w') as save_buf:
        json.dump(data, save_buf, indent=4)
    return

def load_json(filename: str):
    data = None
    with open(filename, 'r') as load_buf:
        data = json.load(load_buf)
    return data


def create_data_config(num: int=0):
    config = {}
    cond = True
    i = 0
    while cond:
        k = input("Key: ")

        if num == 0 and k == 'q':
            break

        t = input("Type: ")

        config[k] = t

        i += 1
        if num > 0:
            if i == num:
                cond = False
    return config


def create_type_map():
    return

def input_data(config, type_map):
    return





def main():
    fixed_var = input("Variable number of keys?: ")
    num_keys = 0
    if fixed_var == 'n':
        num_keys = int(input("How many keys?: "))
    
    sample_config = create_data_config(num_keys)

    save_prompt = input("Save config?: ")
    if save_prompt == 'y':
        fname = input("Config name: ")
        save_json(sample_config, f"config/{fname}.json")
    
    print(sample_config)

if __name__ == "__main__":
    main()
