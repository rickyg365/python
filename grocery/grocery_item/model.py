from typing import List, Dict
from dataclasses import dataclass

""" 
sample_grocery_data = {
    "id": "prodfru001",
    'name': "apple",
    "category": ["produce", "fruit"],
}
"""


@dataclass
class GroceryItem:
    id: str
    name: str
    categories: List[str]

    # Private Vars
    _data = None
    _config_cache = None

    def __post_init__(self):
        self.cache()

    def __str__(self) -> str:
        txt_id = f"id: {self.id}"
        txt_name = f"name: {self.name}"
        txt_categories = f"Categories: [ {' | '.join(self.categories)} ]"

        return f"{txt_id}\n{txt_name}\n{txt_categories}"
    
    def to_dict(self):
        # Hardcoded
        # output = {
        #     "id": self.id,
        #     "name": self.name,
        #     "categories": self.categories
        # }

        # Pythonic
        output = vars(self)

        # Remove Private
        return {k: v for (k, v) in output.items() if k[0] != '_'}
    
    def cache(self):
        # Use cached data, makes a copy
        if self._data is None:
            self._data = self.to_dict()
    
    def generate_config(self):
        type_map = {
            list: "list",
            str: "str",
            int: "int",
            dict: "dict"
        }

        return {k:type_map[type(v)] for (k, v) in self._data.items()}

    def config(self):
        if self._config_cache is None:
            self._config_cache = self.generate_config()
        return self._config_cache



def main():
    sample_grocery_data = {
        "id": "prodfru001",
        'name': "apple",
        "categories": ["produce", "fruit"],
    }

    new_item = GroceryItem(**sample_grocery_data)
    new_item_data = new_item.to_dict()

    new_item_config = new_item.config()


    # Display
    print(new_item)
    print(new_item_data)
    print(new_item_config)


if __name__ == '__main__':
    main()
