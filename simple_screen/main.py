import os

import threading
from pynput import keyboard

from utils.clear_screen import clear_screen

from components.menu import Menu
from components.screen import Screen
from components.player import Player

"""

"""

class Game:
    def __init__(self, use_pynput: bool=True):
        # Get Terminal Dimensions
        columns, rows = os.get_terminal_size()
        # print(rows, columns)

        self.screen = Screen(columns, rows-2)  # Row -2 for no pynput, can use full height for pynput
        self.player = Player()
        self.item_menu = Menu(True)
        
        self.use_pynput = use_pynput
        self.p_running = True

    def draw_player_on_screen(self):
        r, c = [*self.player.pos]
        pr, pc = [*self.player.prev_pos]

        # Unset Player
        if self.player.prev_pos != self.player.pos:
            self.screen.set_pixel(pr, pc, self.screen._blank_square)

        # Set up Player
        self.screen.set_pixel(r, c, self.player.current_player)

        # Debug
        # print(prev_player_pos, player_pos, prev_player_pos != player_pos)
        # input()

    def draw_status_on_screen(self):
        raw_status = " | ".join([f"{k}: {v%999:03}" for k, v in self.player.get_items().items()])
        if raw_status == "":
            raw_status = "Empty"
        status = f"[ {raw_status} ]"
        if len(raw_status) > self.screen.width:
            status = raw_status[:self.screen.width - 4]
        
        for _, character in enumerate(status):
            self.screen.set_pixel(self.screen.height - 1, _, character)

    
    def display(self):
        clear_screen()
        # Render Screen
        self.draw_player_on_screen()
        self.draw_status_on_screen()
        #? self.draw_obstacles()
        print(self.screen.render())
    
    def on_press(self, key):
        # print(f"{key} pressed!")
        if key == keyboard.Key.down:
            self.player.move_down(self.screen.height - 1)
            self.display()

        if key == keyboard.Key.up:
            self.player.move_up()
            self.display()

        if key == keyboard.Key.right:
            self.player.move_right(self.screen.width - 1)
            self.display()
            
        if key == keyboard.Key.left:
            self.player.move_left()
            self.display()
            
        if hasattr(key, 'char') and key.char == 'm':
            t = threading.Thread(target=self.item_menu.open())
            t.start()

            self.display()
        if hasattr(key, 'char') and key.char == 'i':
            
            self.player.add_item("Wood")
            self.player.add_item("Metal")
            self.player.add_item("Dirt", 5)

            self.display()
        
    def on_release(self, key):
        # print(f"{key} released!")
        if key == keyboard.Key.esc:
            # Stop listener
            self.p_running = False
            return False

    def run_display(self):
        if self.use_pynput:
            self.display()

            # Blocking, handle input
            with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release,
                suppress=True) as listener:
                listener.join()

        else:
            while True:
                self.display()
                user_input = input("\n[input]: ")

                # Do something to screen based on input
                match user_input.lower():
                    case "q":
                        break

                    case "s":
                        # Move Down
                        self.player.move_down(self.screen.height - 1)

                    case "w":
                        # Move Up
                        self.player.move_up()

                    case "d":
                        # Move Right
                        self.player.move_right(self.screen.width - 1)

                    case "a":
                        # Move Left
                        self.player.move_left()
                    
                    case "m":
                        # Open Menu
                        self.item_menu.open()
                        continue

                    case _:
                        continue


def main():
    # Game
    new_game = Game(use_pynput=True)

    # Run Display
    new_game.run_display()


if __name__ == '__main__':
    main()
