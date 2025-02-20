import os

from item import Item
from typing import List, Dict, Union

class Collection:
    def __init__(self, data: List[Union[Dict, Item]]=None):
        obj = data[0] if data is not None else 0
        self.data = data if isinstance(obj, Item) else [Item(**i) for i in data]

    def __str__(self):
        items = '\n'.join([f"{i}" for i in self.data])
        s = f'{items}'
        return s
    
    def export(self):
        return {
            'data': [i.export() for i in self.data]
        }

if __name__ == "__main__":
    Data = [
        {
            "name": "water"
        },
        {
            "name": "cup"
        },
        {
            "name": "spoon"
        },
    ]
    c = Collection(Data)

    print(c)
