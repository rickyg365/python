import os

from scene import Scene

# from text_box_components import welcome_box, custom_textbox, test_textbox, fight_box, fight_bar
from actions import add_welcome_box, add_test_box, add_custom_textbox, battle_box, battle_status_bar, clear_screen, fill


"""
Program: Main Rpg
Author: Rickyg3
Date: 03/25/2022
"""

def main():
    actions_map = {
        "welcome": add_welcome_box,
        "test": add_test_box,
        "add": add_custom_textbox,
        "battle": battle_box,
        "bar": battle_status_bar,
        "fill": fill,
        "cls": clear_screen
    }

    new_scene = Scene(actions_map)

    new_scene.run()


if __name__ == '__main__':
    main()
