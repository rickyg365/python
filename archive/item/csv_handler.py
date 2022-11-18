import csv
from models.grocery_item import GroceryItem


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
