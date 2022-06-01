import os
import sys

from screen import Screen
from player import Player

"""
Movement with w, a, s, d

use pynput or some other keyread module instead of input() for taking in user input
"""

def clear_screen():
    clear_command = "clear"

    if sys.platform == "win32":
        clear_command = "cls"
    
    os.system(clear_command)


def draw_player_on_screen(player: Player, screen: Screen):
    r, c = [*player.player_pos]
    pr, pc = [*player.prev_player_pos]


    # Unset Player
    if player.prev_player_pos != player.player_pos:
        screen.set_pixel(pr, pc, screen._blank_square)

    # Set up Player
    screen.set_pixel(r, c, player.current_player)

    # Debug
    # print(prev_player_pos, player_pos, prev_player_pos != player_pos)
    # input()
    return


def run_display(screen: Screen):
    player = Player()

    while True:
        clear_screen()
        # Render Screen
        draw_player_on_screen(player, screen)        
        print(screen.render())
        user_input = input("\n[input]: ")

        # Do something to screen based on input
        match user_input.lower():
            case "q":
                break

            case "s":
                # Move Down
                player.move_down(screen.height - 1)

            case "w":
                # Move Up
                player.move_up()

            case "d":
                # Move Right
                player.move_right(screen.width - 1)

            case "a":
                # Move Left
                player.move_left()

            case _:
                continue


def main():
    # Get Terminal Dimensions
    columns, rows = os.get_terminal_size()
    # print(rows, columns)

    # Create a screen
    new_screen = Screen(columns, rows-2)
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

    # Run Display
    run_display(new_screen)

    # Debug
    # print(new_screen)

if __name__ == '__main__':
    # clear_screen()
    main()
