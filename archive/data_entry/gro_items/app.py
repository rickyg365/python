import os
import json

from utils.save_load import save_json, load_json
from utils.config import input_raw_config, get_config, parse_raw_config, input_data


class GroceryDataApp:
    def __init__(self, default_filepath: str, default_config_path: str):
        self.filepath = default_filepath
        self.config_path = default_config_path

        self.config = None
        self.raw_config = None

        self.data = None

        # Initial Load
        self.get_config()


    def __str__(self) -> str:
        config_txt = "\n".join([f"{k}: {t}" for k, t in self.raw_config.items()])

        txt = f"""
Filepath: {self.filepath}        
Config path: {self.config_path}
_______________________
{config_txt}
_______________________
"""
        return txt

    def get_config(self):
        """ Load config if it exists, else create a new one! """
        # Check if config exists
        if not os.path.exists(self.config_path):
            print("[ Creating New Config ]")
            self.raw_config = input_raw_config()
        else:
            print("[ Loading Config ]")
            with open(self.config_path, 'r') as in_fig:
                self.raw_config = json.load(in_fig)

        self.config = parse_raw_config(self.raw_config)

        return self.config

    def save(self):
        """ Save Current Data """
        return
    
    def load(self):
        """ Load Data if file exists """
        return

    def run(self):
        while True:
            options = f"""
[ Grocery Data App ]
{self}
[N]: New Config
[I]: Input Data
[S]: Save Data
[L]: Load Data
"""
            print(options)
            user_input = input(">>> ")

            match user_input:
                case "q":
                    break
                # New Config
                case "n":
                    print("New Config")
                    self.raw_config = input_raw_config()
                    self.config = parse_raw_config(self.raw_config)

                # Input Data
                case "i":
                    print("Input Data")
                    self.data = input_data(self.config)
                # Save Data
                case "s":
                    print("Save")
                    save_json(self.data, self.filepath)
                # Load Data
                case "l":
                    new_filepath = input("New Filepath: ")
                    self.data = load_json(new_filepath)
                case _:
                    print("Unrecognized Input")
        return  

def main():
    # # Variables
    # config_path = "data/config.json"
    # data_path = "data/items.json"

    # # Load Config
    # config = get_config(config_path)
    # # print(config)

    # # Inpute New Data
    # new_data = input_data(config)

    # # Save New Data
    # save_json(new_data, data_path)
    new_app = GroceryDataApp("data/items.json", "data/config.json")

    new_app.run()

    return

if __name__ == '__main__':
    main()
