import os

from typing import List, Dict

from dataclasses import dataclass


@dataclass
class Cube:
    # Default Orientation
    top: str
    bot: str

    front: str
    back: str
    
    left: str
    right: str

    current_face: str = "front"

    def __str__(self) -> str:
        if self.current_face == "all":
            txt = f"T: {self.top}\nB: {self.bot}\nF: {self.front}\nBK: {self.back}\nL: {self.left}\nR: {self.right}"
        if self.current_face == "front":
            txt = f"{self.front}"
        return txt


class Region:
    length: int
    width: int
    depth: int

    data: List[List[List[any]]]


def main():
    # T, B, F, BK, L, R
    color_order = ["g", "g", "r", "r", "b", "b"]

    cells = []
    for _ in range(5):
        new_cell = Cube(*color_order)
        print(new_cell)
        cells.append(new_cell)


        
    return

if __name__ == '__main__':
    main()
