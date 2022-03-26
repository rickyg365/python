import os

from display import Screen
from text_box import TextBox

# Unsorted
def welcome_box():
    welcome_box_width = 25
    welcome_box_height = 5

    Welcome_lines = [
        "",
        "",
        f"{'Welcome!':^{welcome_box_width}}",
        "",
        ""
    ]

    return TextBox(Welcome_lines, (welcome_box_height, welcome_box_width))


def custom_textbox():
    os.system('cls')
    box_width = int(input("Box Width: "))
    box_height = int(input("Box Height: "))

    box_lines = []
    for i in range(box_height):
        new_line = input(f"{i+1}:> ")

        box_lines.append(f"{new_line:^{box_width}}")

    return TextBox(box_lines, (box_height, box_width))


def test_textbox():
    box_width = 10
    box_height = 5

    box_lines = [
        "",
        "",
        "",
        "",
        ""
    ]

    return TextBox(box_lines, (box_height, box_width))


# Menu


# Battle
def fight_box():
    box_width = 20
    box_height = 3

    box_lines = [
        f"{'Fight':^{box_width//2}}{'Party':^{box_width//2}}",
        "",
        f"{'Bag':^{box_width//2}}{'Run':^{box_width//2}}",
    ]

    return TextBox(box_lines, (box_height, box_width))

def fight_bar(terminal_cols: int):
    # x_coord = term_r - 5
    # y_coord = 2
    box_width = terminal_cols - 4
    box_height = 1

    space_factor = box_width//4
    bar_text = f"{'Fight':^{space_factor}}{'Party':^{space_factor}}{'Bag':^{space_factor}}{'Run':^{space_factor}}"

    box_lines = [f"{bar_text:^{box_width}}"]

    return TextBox(box_lines, (box_height, box_width), "round")
