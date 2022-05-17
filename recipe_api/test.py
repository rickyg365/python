import os
import datetime
from soc import *

def main():
    raw_data = {
        "name": "banana",
        "price": 3.12,
        "quantity": 5,
        "unit": "single",
        "expiration_date": "05/16/22",
        "purchase_date": datetime.datetime.now().strftime("%D")  # Todays date
    }

    new_item = GroceryItem(**raw_data)
    print(new_item)
    print(new_item.export())

    save_data = []
    save_data.append(new_item.export())

    for _ in range(2):
        save_data.append(input_raw_grocery_data())
    
    save_grocery_data(save_data, "data/test_save.json")
    

if __name__ == '__main__':
    main()
