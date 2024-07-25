import os

from datetime import datetime

from utils.simp_lib import prettify_dict
from utils.simp_data import create_defaulted_data, input_data, create_config, get_config_options
from utils.easy_save import save_json, load_json


"""
TBD
- Choose and load configs use filenames as string
- Create different collections of data also using filename as string
"""


def main():
    DATA_PATH = "data/sample_collection.json"
    CONFIG_PATH = "data/configs/sample_config.json"
    
    data = []
    SAMPLE_CONFIG = None

    # Check if files exist 
    if os.path.isfile(DATA_PATH):
        data = load_json(DATA_PATH)

    if os.path.isfile(CONFIG_PATH):
        SAMPLE_CONFIG = load_json(CONFIG_PATH)

    # Track Save Status
    added_data = False
    
    while True:
        print(f"""
Config:
{prettify_dict(SAMPLE_CONFIG)}

[New Data: {'*' if added_data else ' '}]
[ (a)dd | (c)reate config | (d)isplay data | (e)dit settings | (s)ave | (q)uit ]""")
        
        u_in = input(f">>> ")

        match u_in:
            case "a":
                # Show prev data
                # display = "\n".join([prettify_dict(d) for d in data])
                # print(display)

                new_point = input_data(SAMPLE_CONFIG)
                data.append(new_point)
                added_data = True

            case 'c':
                filename = input("Choose filename: ")
                new_config = create_config()
                save_json(new_config, f"data/configs/{filename}")

            case "d":
                display = "\n".join([prettify_dict(d) for d in data])
                print(display)
                input("")

            case "e":
                options = '\n'.join(get_config_options())
                print(options)
                input(">>> ")
            case "s":
                if added_data:
                    save_json(data, DATA_PATH)
                    added_data = False
                    print("Data Saved!")
                else:
                    print("No Data to Save!")
            case "q":
                break
            case _:
                pass

        
    return




if __name__ == "__main__":
    main()
    




