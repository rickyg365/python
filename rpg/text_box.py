import os

from display import Screen

from typing import List, Tuple


class TextBox:
    STYLE = {
        "square": {
            "vertical": "│",
            "horizontal": "─",
            "top_left": "┌",
            "top_right": "┐",
            "bot_left": "└",
            "bot_right": "┘"
        },
        "bold": {
            "vertical": "┃",
            "horizontal": "━",
            "top_left": "┏",
            "top_right": "┓",
            "bot_left": "┗",
            "bot_right": "┛"
        },
        "round": {
            "vertical": "│",
            "horizontal": "─",
            "top_left": "╭",
            "top_right": "╮",
            "bot_left": "╰",
            "bot_right": "╯"
        }
    }
    def __init__(self, text_lines: List[str], dimensions: Tuple[int, int], style: str="round"):
        self.length, self.width = dimensions

        self.style = self.STYLE[style]

        if len(text_lines) != self.length:
            self.text = ["Invalid Text"]
        
        self.text = text_lines
        self.string_cache = None        
        self.data_cache = None
    
    def __str__(self) -> str:
        if self.string_cache is not None:
            return self.string_cache

        output = f"{self.style['top_left']}{self.style['horizontal']*self.width}{self.style['top_right']}"
        text_row_count = len(self.text)
        for i in range(self.length):
            inner_data = ' '*self.width
            if text_row_count <= self.length:
                text_length = len(self.text[i])
                compliment_space = (self.width - text_length) * ' '
                inner_data = f"{self.text[i]}{compliment_space}"
            output += f"\n{self.style['vertical']}{inner_data}{self.style['vertical']}"

        output += f"\n{self.style['bot_left']}{self.style['horizontal']*self.width}{self.style['bot_right']}"

        self.string_cache = output
        return output


    @property
    def data(self):
        if self.data_cache is not None:
            return self.data_cache
        
        raw_data = str(self)

        text_rows = raw_data.split('\n')
        character_matrix = [list(row) for row in text_rows]

        self.data_cache = character_matrix
        return character_matrix


def main():
    box_width = 25
    box_length = 4

    text_lines = [
        f"{'what up dude!':^{box_width}}",
        "",
        "",
        f"{'Yup!':^{box_width}}"
        ]
    new_text_box = TextBox(text_lines, (4, 25))

    print(new_text_box)

    # all_text = ""
    # for row in new_text_box.data:
    #     new_row = ""
    #     for char in row:
    #         new_row += char
    #     all_text += f"{new_row}\n"
    
    # print(all_text)
    new_screen = Screen()

    # for i, row in enumerate(new_text_box.data):
    #     for j, char in enumerate(row):
    #         new_screen.update_grid_point(char, i, j)
    new_screen.draw_text_box(new_text_box.data, 17) # 21 - 4 = 17

    new_screen.print_screen()
    



if __name__ == '__main__':
    main()
