import os

class Cell:
    def __init__(self, default_char: str="."):
        self.value = default_char

    def __str__(self) -> str:
        txt = f"{self.value}"
        return txt
    
class Grid:
    def __init__(self, width: int, height: int, default_char: str="."):
        self.w = width
        self.h = height

        self.default_char = default_char
        self.data = self.create_new_grid(default_char)

    def __str__(self) -> str:
        txt = ""
        return txt
    
    def fill_grid(self):
        for i in range(self.h):
            new_row = []
            for j in range(self.w):
                new_row.append(self.default_char)
            self.data.append(new_row)
    
    def create_new_grid(self, char: str):
        new_grid = [[self.default_char for j in self.w] for i in self.h]
        # new_grid = []
        # for row_num in range(self.h):
        #     new_row = []
        #     for col_num in range(self.w):
        #         # DO SOMETHING
        #         new_row.append(char)
        #     new_grid.append(new_row)
        return new_grid
    
    def iterate_grid(self):
        for row_num, row in enumerate(self.data):
            for col_num, col_val in enumerate(row):
                # DO SOMETHING
                pass
        





def main():
    return

if __name__ == '__main__':
    main()
