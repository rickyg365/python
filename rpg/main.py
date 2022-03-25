import os

from py import test

from display import Screen
from text_box import TextBox


term_c, term_r = os.get_terminal_size()

def show_welcome_box(screen_obj):
    welcome_box_width = 25
    welcome_box_height = 5

    Welcome_lines = [
        "",
        "",
        f"{'Welcome!':^{welcome_box_width}}",
        "",
        ""
    ]

    welcome_box = TextBox(Welcome_lines, (welcome_box_height, welcome_box_width))

    screen_obj.draw_text_box(welcome_box.data, term_r//2 - (welcome_box_height//2 + 2), term_c//2 - (welcome_box_width//2 + 2))


def add_custom_textbox(screen_obj: Screen):
    os.system('cls')
    x_coord = int(input("row start: "))
    y_coord = int(input("column start: "))
    box_width = int(input("Box Width: "))
    box_height = int(input("Box Height: "))

    box_lines = []
    for i in range(box_height):
        new_line = input(f"{i+1}:> ")

        box_lines.append(f"{new_line:^{box_width}}")

    new_text_box = TextBox(box_lines, (box_height, box_width))

    screen_obj.draw_text_box(new_text_box.data, x_coord, y_coord)

def test_textbox(screen_obj):
    os.system('cls')
    x_coord = int(input("X: "))
    y_coord = int(input("Y: "))
    box_width = 10
    box_height = 5

    box_lines = [
        "",
        "",
        "",
        "",
        ""
    ]

    new_text_box = TextBox(box_lines, (box_height, box_width))

    screen_obj.draw_text_box(new_text_box.data, x_coord, y_coord)


def clear_screen(screen_obj: Screen):
    screen_obj.reset_screen()


def battle_box(screen_obj):
    x_coord = 0
    y_coord = 0
    box_width = 25
    box_height = 5

    box_lines = [
        "",
        f"{'Fight':^{box_width//2}} {'Party':^{box_width//2}}",
        "",
        f"{'Bag':^{box_width//2}} {'Run':^{box_width//2}}",
        "",
    ]

    new_text_box = TextBox(box_lines, (box_height, box_width))

    screen_obj.draw_text_box(new_text_box.data, x_coord, y_coord)



def battle_status_bar(screen_obj):
    x_coord = term_r - 5
    y_coord = 2
    
    box_width = term_c - 5
    box_height = 1

    space_factor = box_width//4
    bar_text = f"{'Fight':^{space_factor}}{'Party':^{space_factor}}{'Bag':^{space_factor}}{'Run':^{space_factor}}"

    box_lines = [f"{bar_text:^{box_width}}"]

    bar_text_box = TextBox(box_lines, (box_height, box_width), "bold")

    screen_obj.draw_text_box(bar_text_box.data, x_coord, y_coord)


def fill(screen_obj: Screen):
    os.system('cls')
    fill_char = input(">>> ")
    screen_obj.fill_screen(fill_char)


def main():
    actions_map = {
        "welcome": show_welcome_box,
        "test": test_textbox,
        "add": add_custom_textbox,
        "battle": battle_box,
        "bar": battle_status_bar,
        "fill": fill,
        "cls": clear_screen
    }

    new_screen = Screen(actions_map)

    new_screen.run()


if __name__ == '__main__':
    main()
