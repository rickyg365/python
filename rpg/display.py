import os
from typing import Dict


class Screen:
    def __init__(self, actions: Dict[str, any]=None):
        if actions is None:
            actions = {}

        # Columns, Rows
        self.width, self.length = os.get_terminal_size() # Get terminal size using os module

        # Build screen matrix w/ default value
        self.default_value = ' '
        self.display_grid = self.blank_screen_data
        self.occupied_data = self.reset_occupied_data

        #  "Trigger": action
        self.input_choices = actions

    @property
    def blank_screen_data(self):
        # self.display_grid = [[self.default_value for y in range(self.width)] for x in range(self.length-2)]
        return  [[self.default_value for y in range(self.width)] for x in range(self.length-2)]
    
    @property
    def reset_occupied_data(self):
        # i -> ROWS
        # j -> COLUMNS
        reset_data = {}
        for i in range(self.length):
            for j in range(self.width):
                curr_key = f"{i}{j}"
                reset_data[curr_key] = False

        return reset_data

    def __str__(self):
        grid_text = ""
        for line_data in self.display_grid:
            new_line = ""
            for line_item in line_data:
                new_line += f"{line_item}"
            grid_text += f"{new_line}\n"
        return grid_text
    
    def print_screen(self):
        grid_text = ""
        for line_data in self.display_grid:
            new_line = ""
            for line_item in line_data:
                new_line += f"{line_item}"
            grid_text += f"{new_line}\n"
        os.system('cls')
        print(grid_text)
        input(">>> ")

    def set_grid_point(self, new_char: str, row: int, col: int):
        built_key = f"{row}{col}"
        # Boundary Check
        if row < 0 and row > self.length:
            return False
        if col < 0 and col > self.width:
            return False

        # Check if already occupied
        if self.occupied_data[built_key]:
            return False

        self.display_grid[row][col] = new_char
        self.occupied_data[built_key] = True
        return True
    
    def update_grid_point(self, new_char: str, row: int, col: int):
         # Boundary Check
        if row < 0 and row > self.length:
            return False
        if col < 0 and col > self.width:
            return False

        self.display_grid[row][col] = new_char
        return True

    def draw_text_box(self, text_box_data, start_row: int=0, start_col: int=0):
        for i, row in enumerate(text_box_data):
            r = start_row + i
            if r >= self.length-2:
                continue

            for j, char in enumerate(row):
               
                c = start_col + j

                print(r , c)                  

                if c >= self.width-1:
                    continue

                self.update_grid_point(char, r, c)


    def perform_action(self, trigger: str):
        # if trigger in self.input_choices:
        # empty_function => lambda x: None
        empty_fun = lambda : None
        self.input_choices.get(trigger, empty_fun)()

    def run(self):
        while True:
            os.system('cls')
            print(self)
            user_input = input(">>> ")

            if user_input.lower() == 'q':
                break
            self.perform_action(user_input)



def main():
        
    def action1():
        print(4)
        input()

    def action2():
        print(8)
        input()
    
    sample_actions = {
        "trig1": action1,
        "trig2": action2 
    }
    new_screen = Screen(sample_actions)

    # MAX ROW = 21
    # MAX COLUMN = 72
    new_screen.set_grid_point("X", 21, 71)

    new_screen.run()

if __name__ == '__main__':
    main()





