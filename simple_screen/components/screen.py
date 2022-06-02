import os

"""
"""

class Screen:
    def __init__(self, width: int, height: int):
        # height -> rows  |  width -> columns
        self.width = width
        self.height = height
        
        self._blank_square = ' '  # Default Char
        self.rendered = [[self._blank_square for h in range(self.width)] for w in range(self.height)]
    
    def __str__(self) -> str:
        txt = f"{self.rendered}"
        return txt

    def valid_index(self, row: int, col: int):
        valid_row_index = row < self.height
        valid_col_index = col < self.width
        return valid_row_index and valid_col_index

    def get_pixel(self, row: int, col: int):
        # Throws index error if not valid index
        if (self.valid_index(row, col)):
            return self.rendered[row][col]
        return None

    def set_pixel(self, row: int, col: int, new_value: any):
        # Throws index error if not valid index
        if (self.valid_index(row, col)):
            self.rendered[row][col] = new_value
            return True
        return False
    
    def render(self, debug: bool=False):
        # Todo: Add Border
        final_screen = ""
        for i in range(self.height):
            for j in range(self.width):
                if self.valid_index(i, j):
                    #! print(i, j)
                    #! print(self.rendered[i][j])
                    final_screen += self.rendered[i][j]
                
            if i != self.height - 1:
                    final_screen += "\n"
        return final_screen
    

def main():
    # Get Terminal Dimensions
    # columns, rows = os.get_terminal_size()
    # print(rows, columns)

    # Create a screen
    # new_screen = Screen(columns, rows-2)
    # print(new_screen)

    # Set specific pixel
    # new_val = 'x'  # Can be of any length maybe add a check for each square to ensure valid values
    # new_screen.set_pixel(1, 1, new_val)

    # Get specific pixel
    # my_pixel = new_screen.get_pixel(1, 1)
    # print(my_pixel)

    # Render Screen
    # rendered_screen = new_screen.render()
    # print(rendered_screen)
    # input("\n>>> ")

    # Debug
    # print(new_screen)

    return

if __name__ == '__main__':
    main()
