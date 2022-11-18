import os
from typing import List, Dict
from dataclasses import dataclass

""" 
Model: Animal

"""

@dataclass
class Animal:
    name: str

    width: int = 0
    height: int = 0

    feed_per_day: int = 4

    def __str__(self):
        txt = f"Animal: {self.name} [{self.width}x{self.height}]"
        return txt

    def set_height(self, height: int):
        self.height = height
        return self
    
    def set_width(self, width: int):
        self.width = width
        return self

    def set_feed_amount(self, new_amount: int):
        self.feed_per_day = new_amount
        return self  # For Chaining??? lol
    
    def export(self):
        return {
            "name": self.name,
            "width": self.width,
            "height": self.height,
            "feed_per_day": self.feed_per_day
        }


def main():
    return

if __name__ == '__main__':
    main()
