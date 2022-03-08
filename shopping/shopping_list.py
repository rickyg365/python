import os
import csv
import json

from typing import List, Dict

from shopping_item import ShoppingItem


def get_shopping_item() -> ShoppingItem:
    item_name = input("Item Name: ")
    item_price = float(input("Item Price: "))
    raw_item_quantity, item_unit = input("Enter Quantity( amount unit ): ").split(" ")

    item_quantity = int(raw_item_quantity)

    return ShoppingItem(item_name, item_price, item_quantity, item_unit)


class ShoppingList:
    def __init__(self, starting_list: List[ShoppingItem]=None):
        if starting_list is None:
            starting_list = []

        self.items = starting_list
        self.total = 0.00

        self.default_filepath = "shopping_list.json"

    def __repr__(self) -> str:
        sep = f"{40*'-'}"

        text = f"[ Shopping List ]:\n{sep}"

        for _, item in enumerate(self.items, start=1):
            text += f"\n {_:>2}. {item}"      

        text += f"\n{sep}\nTotal: ${self.total:.2f}\n{sep}"

        return text

    def select_item(self, item_id: int) -> ShoppingItem:
        return
    
    def select_all(self) -> List[ShoppingItem]:
        return self.items

    def add_item(self, shopping_item: ShoppingItem):
        self.items.append(shopping_item)
        self.total += shopping_item.price
        return True

    # def add_new_item(self, raw_item: Dict[str, any]):
    #     self.items.append(ShoppingItem(**raw_item))
    #     return True

    def delete_item(self, item_id: int):
        return

    def edit_item(self, item_id: int):
        return

    def load_json(self):
        """ Load Recipes from json format """
        with open(self.default_filepath, 'r') as in_json:
            load_data = json.load(in_json)
        
        for data_entry in load_data:
            self.add_item(ShoppingItem(**data_entry))

        return True
    
    def load_csv(self):
        """ Load Recipes from csv format """
        with open("shopping_list.csv", 'r') as in_csv:
            csv_data = csv.reader(in_csv)

            for _, line in enumerate(csv_data):
                if _ == 0:
                    continue

                item_name = line[0]
                item_price = float(line[1])
                item_amount = int(line[2]) if line[2] != '' else 0
                item_unit = line[3] if line[3] != '' else 'ct'

                new_item = ShoppingItem(item_name, item_price, item_amount, item_unit)
                self.add_item(new_item)

        return True

    def save_json(self):
        """ Save Recipes to json format """
        new_list = []
        for item in self.items:
            export_data = item.export()
            new_list.append(export_data)
        
        with open(self.default_filepath, 'w') as out_json:
            json.dump(new_list, out_json, indent=4)

        return True

    def save_csv(self):
        """ Save Recipes to csv format """
        return
    


def main():
    
    # Create Shopping List
    shopping_list = ShoppingList()

    # while True:
    #     new_shopping_item = get_shopping_item()

    #     shopping_list.add_item(new_shopping_item)

    #     cont = input("Continue? (y/n): ")

    #     if cont == 'n':
    #         break
    


    # shopping_list.load_csv()
    shopping_list.load_json()

    # shopping_list.save_json()
    
    print("")
    print(shopping_list)


if __name__ == '__main__':
    main()




