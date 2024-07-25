import os
import time

from screen import Screen, BorderScreen


class Drawable:
    def __init__(self, initial_data=None):
        self.data = initial_data

    def draw(self, screen: Screen, row: int, col: int):
        screen.update_w_matrix(row, col, self.data)


def test_txt_files():
    # sample_screen = BorderScreen(52, 19, True)
    sample_screen = Screen(52, 19)

    TXT_1 = "sample_scene.txt"
    TXT_2 = "input_screen_scene.txt"

    with open(TXT_1, 'r', encoding='utf-8') as text_file_1:
        data1 = text_file_1.read()

    with open(TXT_2, 'r',  encoding='utf-8') as text_file_2:
        data2 = text_file_2.read()

    sample_screen.update_w_string(0, 0, data1)
    print(sample_screen)

    sample_screen.clear_screen()
    sample_screen.update_w_string(0, 0, data2)
    print(sample_screen)


i_data = [
    ["*", "*"],
    ["*", "*"]
]

obj = Drawable(i_data)


def main():
    RUNNING = True

    wsize = os.get_terminal_size()

    SCREEN_WIDTH = wsize[0] - 2
    SCREEN_HEIGHT = wsize[1] - 3

    # Setup Screens
    INTRO_SCREEN = BorderScreen(SCREEN_WIDTH, SCREEN_HEIGHT, True)
    INTRO_SCREEN.update_w_string(1, 1, "Game Introduction")

    BATTLE_SCREEN = BorderScreen(SCREEN_WIDTH, SCREEN_HEIGHT, True)
    BATTLE_SCREEN.update_w_string(1, 1, "BATTLE")

    INVENTORY_SCREEN = BorderScreen(SCREEN_WIDTH, SCREEN_HEIGHT, True)
    INVENTORY_SCREEN.update_w_string(1, 1, "INVENTORY")

    DEFAULT_SCREEN = BorderScreen(SCREEN_WIDTH, SCREEN_HEIGHT, True)
    DEFAULT_SCREEN.update_w_string(
        1, 1, f"""DEFAULT\n(B)attle\n(I)nventory\n""")

    MAIN_SCREEN = DEFAULT_SCREEN

    # Intro
    print(INTRO_SCREEN)
    input("Press [Enter] to Continue...")

    while RUNNING:
        print("cls")
        os.system("cls")
        print(MAIN_SCREEN)
        MAIN_SCREEN.clear_screen()
        # Set Options
        MAIN_SCREEN.update_w_string(
            1, 1, f"""DEFAULT\n(B)attle\n(I)nventory\n""")

        obj.draw(MAIN_SCREEN, 2, 2)

        user_input = input(">>> ")

        match user_input.lower():
            # Battle
            case "b":
                MAIN_SCREEN = BATTLE_SCREEN

            # Inventory
            case "i":
                MAIN_SCREEN = INVENTORY_SCREEN

            # Quit
            case "q":
                RUNNING = False

            # Spells
            case _:
                pass


if __name__ == "__main__":
    main()
