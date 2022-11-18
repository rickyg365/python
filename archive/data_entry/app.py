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

def paged_display(data_list, entry_per_page: int):
    """ Takes in list and diaplays it in a paged view! """
    length = len(data_list)
    current_page = 1
    last_page = length/entry_per_page if length%entry_per_page == 0 else length//entry_per_page + 1
    
    start_index = 0
    end_index = entry_per_page

    current_display = ""
    for _, entry in enumerate(data_list[start_index: end_index]):
        

        # Update Index    
        start_index = (current_page - 1) * entry_per_page
        end_index = current_page * entry_per_page
    
    return




class DataEntryApp:
    def __init__(self, title="Data App", default_path="data"):
        if not os.path.exists(default_path):
            os.mkdir(default_path)
        
        self.path = default_path
        self.title = title
        self.data_choices = os.listdir(default_path)
        self.num_choices = len(self.data_choices)

        self.page = 1
        self.last_page = self.num_choices//3 if self.num_choices%3 == 0 else self.num_choices//3 + 1

        self.chosen_dir = ""
        self.current_config = {}
        self.current_save_config = {}  # For saving
        self.current_data = []


    def __str__(self) -> str:
        # Choose by name
        # choices = "\n".join([f"+ {s.replace('_', ' ').title()}" for s in self.data_choices])
        choices = f""
        self.num_choices = len(self.data_choices)  # Update
        '''
        '''
        index = self.page - 1
        # 0, 3
        # 3, 6,
        # 6, 9
        start_index = 3 * index
        end_index = 3 * self.page
        
        # start_index = 3 * index + index
        # end_index = 3 * self.page + index
        
        for _, dir in enumerate(self.data_choices[start_index: end_index]):
            nice_dir_name = dir.replace("_", " ").title()
            choices += f"{start_index + _+1}. {nice_dir_name}\n"
        

        # for _, dir in enumerate(self.data_choices[:min(3, self.num_choices)]):
        #     nice_dir_name = dir.replace("_", " ").title()
        #     if self.num_choices > 3:
        #         choices += f"[N]: Next Page\n{_+1}. {nice_dir_name}"
        #         continue
        #     choices += f"\n{_+1}. {nice_dir_name}"
        
        # config: 3  data: 23

        txt = f"""
[ {self.title} ]
{30*'_'}
Pg.{self.page}  data: {self.chosen_dir}
{30*'-'}
{choices}
<Prev Page   Next Page>
{30*'-'}
[E]: Edit Data
[C]: Create New
[V]: View Data
"""
        return txt
    
    def edit_current_data(self):
        print_list = ["\n".join([f"{k}: {v}" for k,v in e.items()]) for e in self.current_data]
        # for entry in self.current_data:
        #     for k, v in entry.items():
        #         print(f"{k}: {v}")
        print("\n".join(print_list))
        input()
        select_key = input("Select Key: ")
    
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
                continue
            
            # Prev Data Dir Page
            if u_in.lower() == "p":
                next_index = self.page - 1

                if next_index < 0:
                    next_index = 0
                    
                self.page = next_index

                continue

            # Next Data Dir Page
            if u_in.lower() == "n":
                next_index = self.page + 1

                if next_index > self.last_page:
                    next_index = self.last_page

                self.page = next_index
                continue

            if u_in.lower() == 'v':
                print_list = ["\t".join([f"{k}: {v}" for k,v in e.items()]) for e in self.current_data]
                # for entry in self.current_data:
                #     for k, v in entry.items():
                #         print(f"{k}: {v}")
                print("\n".join(print_list))
                input()
                continue

            if u_in in "123456789":
                key = int(u_in) - 1
                self.chosen_dir = self.data_choices[key]

                self.load_data_choice(self.data_choices[key])
                # print(self.data_choices[key])
                continue

        return


def main():
    new_app = DataEntryApp(title="Custom Data App", default_path="data")
    new_app.run()
    return

if __name__ == '__main__':
    main()
