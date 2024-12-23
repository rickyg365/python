from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:  # Only imports the below statements during type checking
    from game_engine.character import Character

import os
import sqlite3
from typing import List, Dict, Callable

'''
Goals:
- save/load data
- basic crud operations


DATA

Form
data = {
    'name': ...,
}

Object
Item(**data)

    handles parsing data into correct datatype


Items
- Key
- Consumable
- Equipment

'''

ITEM_DATA = {
    'key': 'ttrrppid',
    'name': 'Potion',
    'item_type': 'consumable',
    'description': 'Heals a small amount of health.',
    'attributes': {
        'health': 10
    },
}

WOODEN_SWORD = {
    'key': 'ttrrppid',
    'name': 'Wooden Sword',
    'item_type': 'weapon',
    'description': 'A small wooden sword',
    'attributes': {
        'attack': 10,
        'critical_chance': 0
    },   
}

EQUIPMENT_DATA = {
    'key': 'ttrrppid',
    'name': 'Wooden Shield',
    'item_type': 'equipment',
    'description': 'A small wooden shield',  # be careful not to get a splinter.
    'attributes': {
        'defense': 8,
        'block_chance': 10
    },
}

class ItemType:
    ABBRV = {
        'item': '???',
        'weapon': 'WPN',
        'equipment': 'EQP',
        'consumable': 'CON',
    }
    def __init__(self, item_type: str):
        # Default invalid to 'item'
        if item_type not in self.ABBRV.keys():
            item_type = 'item'

        self.item_type = item_type
        self.abbrv = self.ABBRV[item_type]

    def export(self):
        return {
            'item_type': self.item_type
        }


class Item:
    def __init__(self, item_type: str, key: str, name: str, description: str):
        self.item_type = ItemType(item_type)
        self.key = key
        self.name = name
        self.description = description
    
    def __str__(self):
        s = f'[{self.item_type.abbrv}] {self.name}: {self.description}'
        return s

    def data_map(self):
        return {
            'item_type': str,
            'key': str,
            'name': str,
            'description': str,
        }

    def export(self):
        return {
            'key': self.key,
            'name': self.name,
            'description': self.description,
            **self.item_type.export()
        }


class Consumable(Item):
    def __init__(self, key: str, name: str, description: str, attributes: Dict, **kwargs):
        super().__init__(item_type='consumable', key=key, name=name, description=description)
        self.attributes = attributes

    def __str__(self):
        s = f'{self.name}'
        return s

    def use(self, target: Character):
        for key, value in self.attributes.items():
            target.apply_buff(key, value)

class Equipment(Item):
    def __init__(self, key: str, name: str, description: str, attributes: Dict, **kwargs):
        super().__init__(item_type='equipment', key=key, name=name, description=description)
        self.attributes = attributes

    def __str__(self):
        s = f'{self.name}'
        return s

    def apply(self, target: Character):
        for attribute, value in self.attributes.items():
            target.apply_buff(attribute, value)

    def remove(self, target: Character):
        for attribute, value in self.attributes.items():
            target.apply_buff(attribute, -1*value)


class Inventory:
    def __init__(self, filename: str='default_appdata.json', data: List=None):
        self.filename = filename
        
        if data is None:
            data = list()
        
        self.length = len(data)
        self.data = data


    def __str__(self):
        items = '\n'.join([f"{i}" for i in self.data])
        s = f'''
Inventory
_________________________________
{items}
'''
        return s
    
    def meta_data(self):
        s = f'{self.length}] {self.filename}'
        return s

    def add(self, new_item: Item):
        self.data.append(new_item)
        self.length += 1

        return new_item
    
    def add_multiple(self, new_item: Item, amount: int=2):
        for _ in range(amount):
            self.add(new_item)
    
    def get(self, idx: int):
        return self.data[idx]
    
    def remove(self, idx: int):
        self.length -= 1
        return self.data.pop()
    
    def update(self, idx: int, new_data: Dict):
        i = self.data[idx]

        for k, v in new_data.items():
            if not hasattr(i, k):
                continue
            setattr(i, k, v)

        return i
    


if __name__ == "__main__":
    item = Consumable(**ITEM_DATA)
    sword = Equipment(**WOODEN_SWORD)


    inv = Inventory('default_inventory.json', [item, sword])

    print(inv)

    inv.add(item)
    inv.add(sword)
    inv.add(Equipment(**WOODEN_SWORD))
    inv.add(Equipment(**WOODEN_SWORD))

    print(inv)



