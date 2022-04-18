import os

from typing import List

from utils.load_save import load, save

from grocery_item.model import GroceryItem
from grocery_item.view import SingleRowView, KeySingleRowView
from grocery_item.data_input import input_grocery_item, input_loop


def get_data(loaded_data: List):
    # # Convert Raw Data List into Model List
    # final_data = []
    # for raw_data in loaded_data:
    #     # Parse Raw data into Model
    #     new_item = GroceryItem(**raw_data)
    #     final_data.append(new_item)
    
    # List Comprehension Version
    final_data = [GroceryItem(**raw_data) for raw_data in loaded_data]
    
    return final_data

class GroceryDisplay:
    def __init__(self, filepath: str="frontend_test.json"):
        self.filepath = filepath
        
        self.raw_data = load(filepath)
        self.data = get_data(self.raw_data)
        
        self.view = SingleRowView
        self.controller = "Grocery Data Controller"

    def __str__(self) -> str:
        lines = []

        for item in self.data:
            data = item.to_dict()
            view = self.view(data)
            lines.append(f"{view}")
            # txt += f"{view}\n"
        
        return "\n".join(lines)
    
    def run(self):
        config = self.data[0].config()
        cols, rows = os.get_terminal_size()

        sep = f"{cols*'-'}"
        sep2 = f"{cols*'_'}"

        key_v = {
            "id": "ID",
            "name": "NAME",
            "categories": "CATEGORIES"
        }

        key_view = KeySingleRowView(key_v)

        while True:
            
            os.system("cls")
            print("[ Grocery Display ]")
            print(f"{sep2}")
            print(key_view)
            print(f"{sep}")
            print(self)
            print(f"{sep}")
            print(f"\nChoose an option: \n{sep}\n [S]: Search\n [I]: Input\n [E]: Edit")
            action_choice = input("\n>>> ")
            
            match action_choice:
                case "q":
                    break
                case "i":
                    # Parse output data
                    output_data = input_loop(config)
                    self.raw_data.extend(output_data)
                    new_data = get_data(output_data)
                    self.data.extend(new_data)

                    save(self.raw_data, self.filepath)
                case _:
                    # print("\n[Unknown Input]")
                    input("[ Unknown Input ]: Press Enter to Continue...")
                    continue
            
def main():
    new_display = GroceryDisplay()
    # print(new_display)
    new_display.run()
    

if __name__ == '__main__':
    main()
