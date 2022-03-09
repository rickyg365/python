import os, sys

from models.grocery_item import GroceryItem
from grocery_list import GroceryList


def clear_screen():
    if sys.platform != 'win32':
        os.system('clear')
    else:
        os.system('cls')

# Get Grocery data from input
def grocery_item_form() -> GroceryItem:
    new_data = {
        "name": input("Item Name: "),
        "price": float(input("Item Price: ")),
        "purchase_date": input("Date purchased: ")
    }
    
    new_grocery_item = GroceryItem(**new_data)
    
    # Created custom setter hehehe prob not best practice but its fun
    new_grocery_item.quantity = input("Enter Quantity( amount unit ): ")
 
    return new_grocery_item


def main():
    # Create Grocery List
    grocery_list = GroceryList()
    grocery_list.load_json()

    while True:
        # Display
        clear_screen()
        print(f"{grocery_list}\n")
        
        try:
            new_shopping_item = grocery_item_form()
            grocery_list.add_item(new_shopping_item)
        except KeyboardInterrupt:
            # Save Data
            grocery_list.save_json("data/new_list.json")
            grocery_list.save_csv("data/new_list.csv")
            
            break


if __name__ == '__main__':
    main()

