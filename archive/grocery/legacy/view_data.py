import os

from grocery_view import SingleRowView
from main import load, save, GroceryItem


def show_data(filepath):
    # Load in data
    raw_data = load(filepath)
    output_data = []

    for item in raw_data:
        new_groc_item = GroceryItem(**item)
        output_data.append(new_groc_item)

        new_view = SingleRowView(item)
        print(new_view)

    return


def main():
    show_data("test_input.json")

if __name__ == '__main__':
    main()
