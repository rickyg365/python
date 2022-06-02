import os
import sys

from pynput import keyboard


def clear_screen():
    clear_command = "clear" if sys.platform != "win32" else "cls"
    os.system(clear_command)


class Menu:
    def __init__(self, keyboard=False) -> None:
        self.menu_cursor = ">"
        self.height = 8
        self.width = 14

        self.cursor_x = 2
        self.cursor_y = 0

        self.use_pynput = keyboard

        self.rows = [
            f"Option #1",
            f"Option #2",
            f"Option #3",
            f"Option #4",
            f"Option #5"

        ]

        self.methods = {
            "w": self.cursor_up,
            "s": self.cursor_down,
            "a": self.accept,
            "b": self.back,
            "x": self.close_menu,
        }
    
    def __str__(self) -> str:
        txt = [
            f".{'-'*self.width}.",
            ]

        for _, line in enumerate(self.rows):
            padded_line = f"|   {line:<{self.width-3}}|"
            if _ == self.cursor_y:
                padded_line = f"||{self.menu_cursor} {line:<{self.width-3}}|"
                # padded_line[self.cursor_x] = self.menu_cursor
            txt.append(padded_line)
            
        txt.append(f"'{'-'*self.width}'")
        

        return "\n".join(txt)

    def cursor_up(self):
        self.cursor_y = max(self.cursor_y-1, 0)

    def cursor_down(self):
        self.cursor_y = min(self.cursor_y+1, len(self.rows)-1)

    def accept(self):
        print("Accept!")
        input()
        return

    def back(self):
        print("Back!")
        input()
        return

    def close_menu(self):
        print("Closed Menu!")
        input()
        return
    
    def run_method(self, method_choice: str):
        self.methods.get(method_choice, lambda : print("Invalid Menu Choice"))()

    def on_press(self, key):
        # print(f"{key} pressed!")
        if key == keyboard.Key.up:
            self.cursor_up()
            clear_screen()
            print(self)
        if key == keyboard.Key.down:
            self.cursor_down()
            clear_screen()
            print(self)
        
    def on_release(self, key):
        # print(f"{key} released!")
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    def open_menu(self):
        if self.use_pynput:
            clear_screen()
            print(self)
            # Blocking
            with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release,
                suppress=True) as menu_listener:
                menu_listener.join()

        else:
            # simple menu loop
            while True:
                clear_screen()
                print(self)
                user_input = input(">>> ")

                match user_input:
                    case "q":
                        break

                    case _:
                        self.run_method(user_input)
                        # print("Invalid Input")



def main():
    # Menu
    # new_menu = Menu()
    # new_menu.open_menu()
    
    return

if __name__ == '__main__':
    main()
