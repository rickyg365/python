from typing import List, Dict, Any

"""
┌─┐
│ │
└─┘

╭─╮
│ │
╰─╯
"""


class Screen:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.data = self.build_default_screen()

    def __str__(self):
        txt = self.convert_matrix_to_str()
        return txt

    def convert_matrix_to_str(self, matrix: List[List[str]] = None):
        if matrix is None:
            matrix = self.data

        return "\n".join(["".join(row) for row in matrix])

    def build_default_screen(self) -> List[List[str]]:
        default_char = " "

        return [[default_char for c in range(self.width)] for r in range(self.height)]

    def clear_screen(self):
        self.data = self.build_default_screen()

    def update_pixel(self, row: int, col: int, new_character: str):
        if row < self.height and col < self.width and row * col >= 0:
            self.data[row][col] = new_character

    def update_w_matrix(self, row_start: int, col_start: int, new_matrix: List[List[str]]):
        for r, row in enumerate(new_matrix):
            for c, char in enumerate(row):
                update_coord_r = row_start + r
                update_coord_c = col_start + c

                if update_coord_c >= self.width or update_coord_r >= self.height:
                    continue
                if update_coord_r < 0 or update_coord_c < 0:
                    continue

                self.data[update_coord_r][update_coord_c] = char

    def update_w_string(self, row_start: int, col_start: int, new_string: str):
        new_data = [list(data) for data in new_string.split("\n")]
        self.update_w_matrix(row_start, col_start, new_data)


class BorderScreen(Screen):
    def __init__(self, width: int, height: int, rounded=False):
        super().__init__(width, height)
        default_settings = {
            "def": " ",
            "occ": "*",
            "vertical": "│",
            "horizontal": "─",
            "tl": "┌",
            "tr": "┐",
            "bl": "└",
            "br": "┘",
        }

        if rounded:
            default_settings = {
                **default_settings,
                "tl": "╭",
                "tr": "╮",
                "bl": "╰",
                "br": "╯",
            }

        self.settings = default_settings

    def __str__(self):
        # Characters
        SIDE_PANEL = self.settings['vertical']
        HORIZONTAL_PANEL = self.settings['horizontal']

        CORNER_TL = self.settings['tl']
        CORNER_TR = self.settings['tr']
        CORNER_BL = self.settings['bl']
        CORNER_BR = self.settings['br']

        txt = "\n".join([SIDE_PANEL + "".join(row) +
                        SIDE_PANEL for row in self.data])

        top = f"{CORNER_TL}{self.width * HORIZONTAL_PANEL}{CORNER_TR}\n"
        bot = f"\n{CORNER_BL}{self.width * HORIZONTAL_PANEL}{CORNER_BR}"

        return top + txt + bot


if __name__ == "__main__":
    screen = BorderScreen(12, 6, True)
    print(screen)
