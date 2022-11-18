from typing import Dict

'''

'''

def input_entry_data(data_config: Dict[str, any], title: str="Input Data"):
    """  
    sample_config = {
        "name": str,
        "release_date": str,
        "genres": List[str],
    }
    
    return { **data_config }
    """
    output_data = {}
    check_empty = lambda x: "N/A" if x == "" else x
    check_empty_num = lambda n: 0 if n == "" else n

    print(f"\n[ {title} ]\n")
    
    for key, type in data_config.items():
        if type is list:
            output_data[key] = input(f"{key.title()}: ").split(" ")
            continue
        if type is not float and type is not int:
            output_data[key] = check_empty(input(f"{key.title()}: "))
        else:
            output_data[key] = type(check_empty_num(input(f"{key.title()}: ")))
    return output_data


def create_entry_list(data_config: Dict[str, any], title: str="Input Data"):
    """ Loop for inputting multiple entries, creates raw data list """
    raw_data = []
    
    while True:
        new_data = input_entry_data(data_config, title)

        raw_data.append(new_data)

        # Repeat Choice
        again = input("\nAdd another?: ")
        # if again != 'y':
        #     break
        if again == 'q':
            break
    
    return raw_data

