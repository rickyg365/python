import os

from dataclasses import dataclass
from typing import List, Dict


class Vector:
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y

    def __str__(self):
        text = f"{self.x}i+{self.y}j"
        return text


class ComplexNum:
    def __init__(self, real:int, imaginary:int):
        self.real = real
        self.img = imaginary

    def __str__(self):
        text = f"{self.real}+{self.img}i"
        return text
    


def main():
    c1 = ComplexNum(1, 2)
    c2 = ComplexNum(3, 2)

    print(f"Complex #1: {c1}")
    print(f"Complex #2: {c2}")
 
    v1 = Vector(1, 2)
    v2 = Vector(3, 2)     

    print(f"Vector #1: {v1}")
    print(f"Vector #2: {v2}")


if __name__ == '__main__':
    main()

