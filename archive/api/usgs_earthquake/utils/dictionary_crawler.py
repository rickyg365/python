from pickletools import pystring


import os
from typing import Dict, List


test_dictionary = {
    "level_0": {
        "level_1": {
            "level_2": 0
        },
        "level_1_2": {
            "level_2": 0
        }
    },
    "level_0_2": {
        "level_1": {
            "level_2": 0
        }
    }
}



def explore_dict(dict_to_explore: Dict[str, any], prefix=""):
    output_dict = {}
    for k, v in dict_to_explore.items():
        flattened_val = v
        if type(v) is dict:
            flattened_val = explore_dict(v, prefix=f"{prefix}{k}_")
            output_dict = {
                **output_dict,
                **flattened_val
            }
        if type(v) is list:
            #TODO Turn this into a seperate aprse list for dict function
            # new_list = [explore_dict(x) for x in v if type(x) is dict]
            updated_list = []
            for item in v:
                if type(item) is dict:
                    updated_list.append(explore_dict(item))
                if type(item) is list:
                    updated_list.append(explore_dict(item))
                else:
                    updated_list.append(item)

            flattened_val = flatten_list()
        else:
            output_dict[f"{prefix}{k}"] = flattened_val
    
    return output_dict


def main():
    print(explore_dict(test_dictionary))
    return

if __name__ == '__main__':
    main()
