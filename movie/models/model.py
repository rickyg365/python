import os

from typing import List, Dict
from dataclasses import dataclass


@dataclass
class Movie:
    id: int
    name: str

    def __str__(self) -> str:
        txt = f"[{self.id:03}] {self.name}"
        return txt

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }
    
@dataclass
class Show:
    id: int
    name: str

    def __str__(self) -> str:
        txt = f"[{self.id:03}] {self.name}"
        return txt
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }



def main():
    # Create Movie and Show object
    new_movie = Movie(1, "Test Movie")
    new_show = Show(1, "Test Show")

    # Display
    print(new_movie)
    print(new_show)


if __name__ == '__main__':
    main()
