import csv
import json

from typing import List, Dict

from models.grocery_item import GroceryItem

"""
Maybe abstract json and csv into seperate data handlers and use bridge pattern
"""

class GroceryList:
    def __init__(self, custom_filepath:str="data/new_list"):
        self.items = []
        self.total = 0.00

        self.json_path = f"{custom_filepath}.json"
        self.csv_path = f"{custom_filepath}.csv"

    def __repr__(self) -> str:
        sep = f"{40*'-'}"

        text = f"[ Grocery List ]:\n{sep}"
        # Iterate thorugh items
        for _, item in enumerate(self.items, start=1):
            text += f"\n {_:>2}. {item}"      
        # Add final total
        text += f"\n{sep}\nTotal: ${self.total:.2f}\n{sep}"
        return text

    def select_item(self, item_id: int) -> GroceryItem:
        return
    
    def select_all(self) -> List[GroceryItem]:
        return self.items

    def add_item(self, grocery_item: GroceryItem):
        self.items.append(grocery_item)
        self.total += grocery_item.price

    def delete_item(self, item_id: int):
        return

    def edit_item(self, item_id: int):
        return

    def export(self) -> List[Dict[str, any]]:
        export_list = []

        for item in self.items:
            export_list.append(item.export())
        
        return export_list

    def load_json(self, new_filepath: str=None):
        """ Load Recipes from json format """
        if new_filepath is None:
            new_filepath = self.json_path

        with open(new_filepath, 'r') as in_json:
            load_data = json.load(in_json)
        
        for data_entry in load_data:
            self.add_item(GroceryItem(**data_entry))

        return True
    
    def load_csv(self, new_filepath: str=None):
        """ Load Recipes from csv format """
        if new_filepath is None:
            new_filepath = self.csv_path

        with open(new_filepath, 'r') as in_csv:
            csv_data = csv.reader(in_csv)

            for _, line in enumerate(csv_data):
                if _ == 0:
                    continue

                # Dynamically build dict or not that would add an extra for loop
                # Parse and add data
                new_data = {
                    "name": line[0],
                    "price": float(line[1]),
                    "amount": int(line[2]) if line[2] != '' else 0,
                    "unit": line[3] if line[3] != '' else 'ct',
                    "purchase_date": line[4],
                    "expiration_date": line[5] if line[5] else ""
                }

                self.add_item(GroceryItem(**new_data))

        return True

    def save_json(self, new_filepath: str=None):
        """ Save Recipes to json format """
        if new_filepath is None:
            new_filepath = self.json_path
        
        with open(new_filepath, 'w') as out_json:
            json.dump(self.export(), out_json, indent=4)

        return True

    def save_csv(self, new_filepath:str=None):
        """ Save Recipes to csv format """
        if new_filepath is None:
            new_filepath = self.csv_path

        with open(new_filepath, 'w', newline='') as out_csv:
            # Hard Coded find better alternative (inpect/get_members, dir)
            attributes = ['name', 'price', 'amount', 'unit', 'purchase_date', 'expiration_date']
            writer = csv.DictWriter(out_csv, fieldnames=attributes)

            writer.writeheader()
            for item in self.items:
                writer.writerow(item.export())

        return True    


def main():
    
    # Create Grocery List
    grocery_list = GroceryList()

    # Handle JSON
    # grocery_list.load_json()
    # grocery_list.save_json()

    # Handle CSV
    grocery_list.load_csv()
    # grocery_list.save_csv()
    
    print(grocery_list)


if __name__ == '__main__':
    main()




