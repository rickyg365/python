import os

import json

from utils.data_entry import input_config, input_entry

"""
[ Main Menu ]
___________________________________

A. Shopping Item
B. Test

>>> 


___________________________________

[1]: Add Data
[2]: Edit Data
[3]: Delete Data
[4]: View Data
___________________________________

>>> 


"""



class DataEntryApp:
    def __init__(self, title="Data App", default_path="data"):
        if not os.path.exists(default_path):
            os.mkdir(default_path)
        
        self.path = default_path
        self.title = title
        self.data_choices = os.listdir(default_path)

        self.chosen_dir = ""
        self.current_config = {}
        self.current_save_config = {}  # For saving
        self.current_data = []


    def __str__(self) -> str:
        # Choose by name
        # choices = "\n".join([f"+ {s.replace('_', ' ').title()}" for s in self.data_choices])
        choices = ""
        for _, dir in enumerate(self.data_choices[:min(3, len(self.data_choices))]):
            nice_dir_name = dir.replace("_", " ").title()
            choices += f"\n{_+1}. {nice_dir_name}"
        
        # config: 3  data: 23

        txt = f"""
[ {self.title} ]
{30*'_'}
config: {len(self.current_config)}  data: {len(self.current_data)}
{choices}
{30*'_'}
[E]: Edit Data
[C]: Create New
[V]: View Data
"""
        return txt
    
    def save_current_data(self):
        new_path = f"{self.path}/{self.chosen_dir}"
        if not os.path.exists(new_path):
            os.mkdir(new_path)
        
        # Save Config
        with open(f"{new_path}/config.json", 'w') as out_config_file:
            json.dump(self.current_save_config, out_config_file, indent=4)

        # Save Data
        with open(f"{new_path}/data.json", 'w') as out_data_file:
            json.dump(self.current_data, out_data_file, indent=4)

    
    def load_data_choice(self, dir_name: str) -> bool:
        """ Return True if Loaded, False if load failed """
        new_path = f"{self.path}/{dir_name}"

        if not os.path.exists(new_path):
            return False
        
        # Load Raw Config
        with open(f"{new_path}/config.json") as in_config:
            # loaded_config = json.load(in_config)
            self.current_save_config = json.load(in_config)
        # Todo: convert raw loaded config into working config, decouple typematch from input_config 

        # Load Data
        with open(f"{new_path}/data.json") as in_data:
            # loaded_data = json.load(in_data)
            self.current_data = json.load(in_data)

        # print(loaded_config)
        # print(loaded_data)

        return True
    
    def create_new(self):
        new_name = input("Enter Name (Must be unique): ")
        
        # Update State
        self.chosen_dir = new_name.lower().replace(" ", "_")

        new_config, new_raw_config = input_config()
        
        self.current_config = new_config
        self.current_save_config = new_raw_config
        self.current_data = input_entry(new_config)

        self.save_current_data()

    def run(self):
        while True:
            os.system("cls")
            print(self)
            u_in = input(">>> ")
            if u_in == 'q':
                break

            if u_in.lower() == "c":
                self.create_new()

            if u_in.lower() == 'v':
                print_list = ["\t".join([f"{k}: {v}" for k,v in e.items()]) for e in self.current_data]
                # for entry in self.current_data:
                #     for k, v in entry.items():
                #         print(f"{k}: {v}")
                print("\n".join(print_list))
                input()

            if u_in in "123456789":
                key = int(u_in) - 1
                self.chosen_dir = self.data_choices[key]

                self.load_data_choice(self.data_choices[key])
                # print(self.data_choices[key])

        return


def main():
    new_app = DataEntryApp(title="Custom Data App" ,default_path="data")
    new_app.run()
    return

if __name__ == '__main__':
    main()
