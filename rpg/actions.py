import os
from display import Screen

from text_box_components import welcome_box, custom_textbox, test_textbox, fight_bar, fight_box

def clear_screen(screen_obj: Screen):
    screen_obj.reset_screen()


def fill(screen_obj: Screen):
    os.system('cls')
    fill_char = input(">>> ")
    screen_obj.fill_screen(fill_char)


def add_welcome_box(screen_obj: Screen):
    new_welcome_box = welcome_box()

    row_center, col_center = (screen_obj.length//2 - (new_welcome_box.length//2 + 1), screen_obj.width//2 - (new_welcome_box.width//2 + 1))
    screen_obj.draw_text_box(new_welcome_box.data, row_center, col_center)

def add_custom_textbox(screen_obj: Screen):
    new_custom_box = custom_textbox()

    row_center, col_center = (screen_obj.length//2 - (new_custom_box.length//2 + 1), screen_obj.width//2 - (new_custom_box.width//2 + 1))
    screen_obj.draw_text_box(new_custom_box.data, row_center, col_center)

def add_test_box(screen_obj: Screen):
    new_test_box = test_textbox()

    row_center, col_center = (screen_obj.length//2 - (new_test_box.length//2 + 1), screen_obj.width//2 - (new_test_box.width//2 + 1))
    screen_obj.draw_text_box(new_test_box.data, row_center, col_center)

def battle_box(screen_obj: Screen):
    new_battle_box = fight_box()

    row_center, col_center = (screen_obj.length//2 - (new_battle_box.length//2 + 1), screen_obj.width//2 - (new_battle_box.width//2 + 1))
    screen_obj.draw_text_box(new_battle_box.data, row_center, col_center)

def battle_status_bar(screen_obj: Screen):
    new_battle_bar = fight_bar(screen_obj.width)

    row_center, col_center = screen_obj.length - 5, 0
    screen_obj.draw_text_box(new_battle_bar.data, row_center, col_center)
