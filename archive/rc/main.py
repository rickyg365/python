import os
from turtle import width

from numpy import size

"""  

## ####
#.P...#
#.....#
#.....#
#######

w = 5
h = 3

grid = [15]
"""

def parse_coord_key(i: int, j: int):
    """ Takes in i, j coord and returns key i_j """
    return f"{i}_{j}"
    
def unparse_coord_key(key: str):
    """ Takes in key and returns i, j coord """
    i, j = key.split("_")
    return int(i), int(j)

class Cell:
    def __init__(self, i: int, j: int, default_char: str="."):
        self.i = i
        self.j = j

        self.char = default_char
    
    def __str__(self) -> str:
        txt = f"{self.char}"
        return txt


class Grid:
    def __init__(self, cols, rows):        
        self.w = cols
        self.h = rows
        self.size = cols*rows

        self.data = {}  # Key: value -> "i_j": Cell
        self.display = ""
        self.default_char = "."

        self.reset_grid()
        self.build_display()
    
    def __str__(self):
        self.build_display()
        return self.display
    
    def build_blank_grid(self):
        output = {}
        for i in range(self.h):
            for j in range(self.w):
                new_key = parse_coord_key(i, j)
                output[new_key] = Cell(i, j, self.default_char)
        return output

    def build_display(self):
        self.display = ""
        # Build Display from Grid List using w, h
        for i in range(self.h):
            self.display += "\n"
            for j in range(self.w):
                new_key = parse_coord_key(i, j)
                self.display += f"{self.data[new_key]}"
    
    def edit_cell(self, i, j, new_char):
        chosen_key = parse_coord_key(i, j)
        self.data[chosen_key] = new_char
    
    def reset_cell(self, i, j):
        chosen_key = parse_coord_key(i, j)
        self.data[chosen_key] = self.default_char
    
    def reset_grid(self):
        self.data = self.build_blank_grid()
    

def main():
    # Create Grid and Grid List
    w = 5
    h = 3

    default_char = "."

    # Build Grid List 1D
    grid = []

    for i in range(h):
        for j in range(w):
            new_cell = Cell(i, j, default_char)
            grid.append(new_cell)

    # Build Display from Grid List using w, h
    display = ""
    index = 0

    for i in range(h):
        display += "\n"
        for j in range(w):
            new_cell = grid[index]
            display += f"{new_cell}"
            index += 1

    # Combined
    # grid = []
    # display = ""
    # for i in range(h):
    #     display += "\n"
    #     for j in range(w):
    #         new_cell = Cell(i, j, default_char)
    #         grid.append(new_cell)
    #         display += f"{new_cell}"

    print(grid)
    print(display)


class Player:
    def __init__(self, start_r: int, start_c: int, char_repr: str):
        self.r = start_r
        self.c = start_c
        self.char = char_repr

    def __str__(self) -> str:
        return self.char
    
    def update_position(self, r, c):
        self.r = r
        self.c = c

if __name__ == '__main__':
    # main()

    display_grid = Grid(10, 5)
    player_char = "@"
    pr, pc = 0, 0

    # Add player to grid
    display_grid.edit_cell(pr, pc, player_char)

    while True:
        os.system('cls')
        print(display_grid)
        u_in = input("\n>>> ")

        match u_in:
            case 'q':
                break

            case 'size':
                # Resize Grid
                w = int(input("Width: "))
                h = int(input("Height: "))

                display_grid = Grid(w, h)

            case 'e':
                # Edit Cell
                r = int(input("R: "))
                c = int(input("C: "))
                new_char = input("New Char: ")

                display_grid.edit_cell(r, c, new_char)
            
            case 'w':
                # Go Up
                display_grid.reset_cell(pr, pc)
                pr -= 1

                display_grid.edit_cell(pr, pc, player_char)
            
            case 's':
                # Go Down
                display_grid.reset_cell(pr, pc)
                pr += 1

                display_grid.edit_cell(pr, pc, player_char)
                
            case 'a':
                 # Go Left
                display_grid.reset_cell(pr, pc)
                pc -= 1

                display_grid.edit_cell(pr, pc, player_char)
            
            case 'd':
                 # Go Right
                display_grid.reset_cell(pr, pc)
                pc += 1

                display_grid.edit_cell(pr, pc, player_char)
                
            case 'r':
                # Reset Grid
                display_grid.reset_grid()

            case _:
                pass
