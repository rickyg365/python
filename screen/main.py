import os
import math


class Screen:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.settings = {
            "fill_char": "*",
            "empty_char": " "
        }

        self.data = self.build_screen_data()

    def __str__(self):
        debug_txt = f"W: {self.width}  H: {self.height}"

        # Build Screen
        screen_txt = self.build_display()

        return screen_txt

    def build_screen_data(self):
        fill = self.settings.get("fill_char", "*")
        empty = self.settings.get("empty_char", " ")

        return [[fill for y in range(self.width)] for x in range(self.height)]

    def build_display(self):
        display_txt = "\n".join(["".join(r) for r in self.data])
        return display_txt

    def update_pixel(self, row: int, column: int, new_char: str):
        # Lower Boundaries
        lower_row_bound = row < 0
        lower_column_bound = column < 0

        # Upper Boundaries
        upper_row_bound = row >= self.height
        upper_column_bound = column >= self.width

        if lower_row_bound or lower_column_bound:
            # Handle Bondary by just not
            return

        if upper_row_bound or upper_column_bound:
            # Handle Bondary by just not
            return

        self.data[row][column] = new_char


def main():
    WIDTH = 8
    HEIGHT = 4

    screen = Screen(WIDTH, HEIGHT)

    print(screen, end="\n\n")

    # for _ in range(round((8**2 + 4**2)**(1/2))):
    for _ in range(round(math.sqrt(8**2 + 4**2))):
        screen.update_pixel(_, 2*_, "-")

    print(screen)


if __name__ == "__main__":
    main()
