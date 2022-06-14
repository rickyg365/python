import os

import pandas as pd
from models.inventory import Inventory


def main():
    new_inventory = Inventory()
    # new_inventory.run()

    raw_data = [x.export() for x in new_inventory.cached_items.values()]
    c = pd.DataFrame(raw_data)
    l = pd.read_json("data/my_inventory.json")
    l.set_index('name', inplace=True)

    print(c)

    print("space")

    print(l)

if __name__ == '__main__':
    main()
 