import os
import time

from user import User
from utils.screen import Screen

from screen_test import test


def game(screen: Screen):
    USER = User("@")

    while True:
        USER.perform_action()
        X = USER.coordinates[0]
        Y = USER.coordinates[1]

        # Draw Cell
        screen.update_cell(Y, X, USER.symbol)

        # Display Screen
        os.system("cls")
        print(screen)
        user_action = input(">>> ")
        if user_action == "q":
            break

        USER.update_action(user_action)

        # Undraw Cell
        screen.update_cell(Y, X, " ")

        # # Pause and Clear Screen
        # time.sleep(.5)

def main():
    WIDTH, HEIGHT = os.get_terminal_size()   # Columns, Lines

    # Create Screens
    s1 = Screen()
    s2 = Screen(WIDTH - 2, HEIGHT - 3, True)

    # print(s1)
    # print(s2)


    # Test Screens
    # test(s1)
    # test(s2)


    # Test Games
    game(s1)
    game(s2)
   


if __name__ == "__main__":
    main()





"""
─	━	│	┃	┄	┅	┆	┇	┈	┉	┊	┋	┌	┏
┐	┓	└	┗	┘	┛	├	
┣	┤	┫	┬	
┳	┴	┻	┼	
╋	╌	╍	╎	╏
═	║	╔	╗	╚	╝	
╠	╣	╦	╩	╬	╭	╮	╯
╰	╴	╵	╶	╷	╸	╹	╺	╻
"""