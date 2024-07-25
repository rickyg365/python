import os
from typing import List, Dict, Any


class Screen:
    def __init__(self, width: int, height: int, settings=None):
        self.width = width
        self.height = height
        self.data = self.build_default_screen()
        self.settings = settings

    def __str__(self):
        txt = self.convert_matrix_to_str()
        return txt

    def convert_matrix_to_str(self, matrix: List[List[str]] = None):
        if matrix is None:
            matrix = self.data

        new_string = ""
        for row in matrix:
            for char in row:
                new_string += f"{char}"
            new_string += "\n"

        return new_string

    def build_default_screen(self) -> List[List[str]]:
        data = []
        default_char = " "
        for row in range(self.height):
            row_arr = []
            for col in range(self.width):
                row_arr.append(default_char)
            data.append(row_arr)
        return data

    def update_pixel(self, row: int, col: int, new_character: str):
        if row < self.height and col < self.width and row * col >= 0:
            self.data[row][col] = new_character

    def update_w_matrix(self, row_start: int, col_start: int, new_matrix: List[List[str]]):
        for r, row in enumerate(new_matrix):
            for c, char in enumerate(row):
                update_coord_r = row_start + r
                update_coord_c = col_start + c

                if update_coord_c > self.width or update_coord_r > self.height:
                    continue
                if update_coord_r < 0 or update_coord_c < 0:
                    continue

                self.data[update_coord_r][update_coord_c] = char

    def update_w_string(self, row_start: int, col_start: int, new_string: str):
        new_data = [list(data) for data in new_string.split("\n")]
        self.update_w_matrix(row_start, col_start, new_data)


class SleekScreen:
    def __init__(self, width: int, height: int, settings=None):
        self.width = width
        self.height = height
        self.data = self.build_default_screen()
        self.settings = settings

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

    def update_pixel(self, row: int, col: int, new_character: str):
        if row < self.height and col < self.width and row * col >= 0:
            self.data[row][col] = new_character

    def update_w_matrix(self, row_start: int, col_start: int, new_matrix: List[List[str]]):
        for r, row in enumerate(new_matrix):
            for c, char in enumerate(row):
                update_coord_r = row_start + r
                update_coord_c = col_start + c

                if update_coord_c > self.width or update_coord_r > self.height:
                    continue
                if update_coord_r < 0 or update_coord_c < 0:
                    continue

                self.data[update_coord_r][update_coord_c] = char

    def update_w_string(self, row_start: int, col_start: int, new_string: str):
        new_data = [list(data) for data in new_string.split("\n")]
        self.update_w_matrix(row_start, col_start, new_data)


def main():
    SAMPLE_DATA = [
        [".", "-",  "-",  "-",  "-",  "-", "."],
        [".", " ",  " ",  " ",  " ",  " ", "."],
        [".", " ",  " ",  " ",  " ",  " ", "."],
        ["'", "-",  "-",  "-",  "-",  "-", "'"],
    ]
    SAMPLE_TEXT_DATA = f"""#######
#######
 )   (
 ///\\\\
"""

    new_screen = Screen(12, 6)
    new_sscreen = SleekScreen(12, 6)

    print(new_screen)

    print()

    new_screen.update_pixel(0, 0, "S")
    new_screen.update_w_matrix(1, 1, SAMPLE_DATA)
    print(new_screen)

    print("Sleek Screen")

    print(new_sscreen)

    print()

    new_sscreen.update_pixel(0, 0, "S")
    new_sscreen.update_w_string(1, 1, SAMPLE_TEXT_DATA)
    print(new_sscreen)


if __name__ == "__main__":
    main()
