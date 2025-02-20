import os

from typing import List, Dict, Union


class Item:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        s = f'{self.name}'
        return s
    
    def export(self):
        
        return {
            'name': self.name
        }


if __name__ == "__main__":
    ...