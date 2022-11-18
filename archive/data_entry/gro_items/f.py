from pickletools import pystring


import os
import json

import datetime

from models.grocery_item import GroceryItem, GroceryList

from utils.save_load import save_json, load_json
from utils.config import input_raw_config, get_config, parse_raw_config, input_data


"""  
Config controls the following,
needs to be checked manually.
    GroceryItem()
    GroceryList()

    GroceryApp()


Data Flow
----------------------------------------------------------
Raw Data:
    Dict[str, any]
    * input_data() gives list of raw_data

Parsed Data:
    GroceryItem(*Raw Data)

Controlled by App:
    raw_data_list = input_data(sample_config)
    App.data = GroceryList([GroceryItem(*rd) for rd in raw_data_list])

----------------------------------------------------------



"""

def clear_screen():
    """ Clear Console Screen """
    os.system("cls")  #  Windows
    return


class GroceryApp:
    def __init__(self, config_path: str="data/config.json", data_path: str="data/grocery"):
        """
        data_path points to dir containing folder of store names 
        w. indv dates/shopping trips saved as files
        
        """
        self.config_path = config_path
        self.raw_config = None  # Dict[str, str]
        self.config = None  # Dict[str, any]

        self.data_path = data_path
        self.data = None

        self.store = ""
        self.date = ""

        # Initial Load
        self.get_config()

    def __str__(self) -> str:
        config_txt = "\n".join([f"{k}: {t}" for k, t in self.raw_config.items()])

        stores = "\n".join([x.title() for x in os.listdir(self.data_path)])

        txt = f"""[ Grocery Data App ]
Loaded Data: {self.store.title()} {self.date.replace("_", "/")}
_______________________

{stores}
_______________________

"""
        return txt

    def get_config(self):
        """ Load config if it exists, else create a new one! """
        # Check if config exists
        if not os.path.exists(self.config_path):
            # Create New Config
            self.raw_config = input_raw_config()
        else:
            # Load Config
            with open(self.config_path, 'r') as in_fig:
                self.raw_config = json.load(in_fig)

        # Parse Config
        self.config = parse_raw_config(self.raw_config)

        return self.config  # For Chaining

    def save(self):
        """ Save Current Data and Config """
        # Create Save Path
        save_path = f"{self.data_path}/{self.store}/{self.date}.json"
        
        # Save
        with open(save_path, 'a') as save_file:
            json.dump(self.data, save_file, indent=4)

        if input("save config?: ") == 'y':
            with open(self.config_path, 'w') as config:
                json.dump(self.raw_config, config, indent=4)
        return

    def load(self):
        """ Load Data if file exists """
        # Initial Data and Load Path
        new_data = None
        load_path = f"{self.data_path}/{self.store}/{self.date}.json"

        # If Path exists Load
        if os.path.exists(load_path):
            with open(load_path, 'r') as load_file:
                new_data = json.load(load_file)

        return new_data

    def run(self):
        # Main Loop
        while True:
            clear_screen()
            options = f"""{self}
[N]: New Config, Move this to a new Settings Tab

[I]: Input Data
[E]: Edit Data
[D]: Delete Data
[V]: View Data

[S]: Save Data  (Save Current Data)
[L]: Load Data, (Store, Date) -> Loads Data
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
                    self.store = input("Store: ")
                    self.date = input("Date: ")

                    raw_data = input_data(self.config) 
                    self.data = GroceryList([GroceryItem(**rd) for rd in raw_data])
                
                # View Data
                case "v":
                    print("View Data")
                    print(self.data.display())
                    input("")

                # Save Data
                case "s":
                    print("Save")
                    if self.store == "":
                        self.store = input("Store name: ")
                    if self.date == "":
                        self.date = input("Date: ")
                    
                    self.save()

                # Load Data
                case "l":
                    self.store = input("Store: ")
                    self.date = input("Date(yyyy_mm_dd): ")

                    raw_data = self.load()
                    self.data = GroceryList([GroceryItem(**d) for d in raw_data])

                case _:
                    print("Unrecognized Input")
        return  


def main():
    # Get todays date in format: year_month_day
    # date_format = "%Y_%m_%d"
    # current_date = datetime.datetime.now().strftime(date_format)  # year_month_day 

    # print(current_date)
    
    # App Instance
    config_filepath = "data/config.json"
    grocery_data_filepath = "data/grocery"
    
    new_app = GroceryApp(config_filepath, grocery_data_filepath)
    new_app.run()
    # print(new_app)
    

if __name__ == '__main__':
    main()
 