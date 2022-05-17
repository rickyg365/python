import os

from typing import List, Dict
from dataclasses import dataclass, field

"""


"""
@dataclass
class Cube:
    # Default Orientation
    top: str
    bot: str

    front: str
    back: str
    
    left: str
    right: str

    def __str__(self) -> str:
        txt = f"{self.top}{self.bot}\n{self.front}{self.back}\n{self.left}{self.right}"
        return txt


@dataclass
class MatrixCache:
    r: int
    c: int
    data: List[List[any]] = None

    def __post_init__ (self):
        if self.data is None:
            self.data = []
            for i in range(self.r):
                # Row
                new_row = []
                for j in range(self.c):
                    # Col
                    default_val = 1
                    new_row.append(default_val)
                self.data.append(new_row)
        
        return

    def __str__(self) -> str:
        txt = f"Rows: {self.r}\nCols: {self.c}"
        return txt


@dataclass
class UberMatrixCache:
    z: int
    r: int
    c: int

    data: List[MatrixCache]

    def __str__(self) -> str:
        txt = ""
        return txt


    def __str__(self) -> str:
        txt = ""
        return txt


def main():
    # Raw Data
    single_row_col = [ 1, 2, 3]

    matrix = [
        [ 11, 12, 13],
        [ 21, 22, 23],
        [ 31, 32, 33]
    ]

    build_str = ""
    for i in range(len(matrix)):
        new_row = ""
        for j in range(len(matrix[0])):
            new_row += f"{matrix[i][j]} "
        build_str += f"{new_row}\n"
    
    print(build_str)
    prt_key_val = lambda r, c, matrix: print(f"{r}{c}: {matrix[r-1][c-1]}")

    prt_key_val(2, 3, matrix)

    ThDMatrix = [
        [
            [ 111, 112, 113],
            [ 121, 122, 123],
            [ 131, 132, 133]
        ],
        [
            [ 211, 212, 213],
            [ 221, 222, 223],
            [ 231, 232, 233]
        ],
        [
            [ 311, 312, 313],
            [ 321, 322, 323],
            [ 331, 332, 333]
        ],
    ]

    # Raw Build 3d print
    build_str = ""
    for z in range(len(ThDMatrix)):
        new_sheet = ""
        for r in range(len(ThDMatrix[0])):
            new_row = ""
            for c in range(len(ThDMatrix[0][0])):
                new_row += f"{ThDMatrix[z][r][c]} "
            new_sheet += f"{new_row}\n"
        build_str += f"{new_sheet}\n\n"
    
    print(build_str)
    
    # Raw Build 3d print w/ Cache
    cache = {}
    build_str = ""
    for z in range(len(ThDMatrix)):
        new_sheet = ""
        for r in range(len(ThDMatrix[0])):
            new_row = ""
            for c in range(len(ThDMatrix[0][0])):
                make_key = lambda z, r, c: f"{z:02}{r:02}{c:02}"
                
                # Add to the Cache
                new_key = make_key(z, r, c)
                # new_key = f"{z:02}{r:02}{c:02}"
                cache[new_key] = ThDMatrix[z][r][c]
                # Add to new_row string
                new_row += f"{ThDMatrix[z][r][c]} "

            new_sheet += f"{new_row}\n"
        build_str += f"{new_sheet}\n\n"
    
    print(build_str)
    print(cache)
    
    prt_key_val = lambda z, r, c, matrix: print(f"{z}{r}{c}: {matrix[z-1][r-1][c-1]}")

    prt_key_val(2, 3, 2, ThDMatrix)

    """ 
    starting_point top front left corner
    
    """



    return

if __name__ == '__main__':
    main()
