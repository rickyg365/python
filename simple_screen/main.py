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
        r, c = [*self.player.player_pos]
        pr, pc = [*self.player.prev_player_pos]

        # Unset Player
        if self.player.prev_player_pos != self.player.player_pos:
            self.screen.set_pixel(pr, pc, self.screen._blank_square)

        # Set up Player
        self.screen.set_pixel(r, c, self.player.current_player)

        # Debug
        # print(prev_player_pos, player_pos, prev_player_pos != player_pos)
        # input()
    
    def on_press(self, key):
        """     
        case "m":
            # Open Menu
            self.item_menu.open_menu()
            continue
        """
        # print(f"{key} pressed!")
        if key == keyboard.Key.down:
            self.player.move_down(self.screen.height - 1)
            clear_screen()
            # Render Screen
            self.draw_player_on_screen()        
            print(self.screen.render())
        if key == keyboard.Key.up:
            self.player.move_up()
            clear_screen()
            # Render Screen
            self.draw_player_on_screen()        
            print(self.screen.render())
        if key == keyboard.Key.right:
            self.player.move_right(self.screen.width - 1)
            clear_screen()
            # Render Screen
            self.draw_player_on_screen()        
            print(self.screen.render())
        if key == keyboard.Key.left:
            self.player.move_left()
            clear_screen()
            # Render Screen
            self.draw_player_on_screen()        
            print(self.screen.render())
        if hasattr(key, 'char') and key.char == 'm':
            t = threading.Thread(target=self.item_menu.open_menu())
            t.start()        

            clear_screen()
            # Render Screen
            self.draw_player_on_screen()        
            print(self.screen.render())
        
    def on_release(self, key):
        # print(f"{key} released!")
        if key == keyboard.Key.esc:
            # Stop listener
            self.p_running = False
            return False

    def run_display(self):
        if self.use_pynput:
            clear_screen()
            # Render Screen
            self.draw_player_on_screen()        
            print(self.screen.render())

            # while self.p_running:
            # Blocking, handle input
            with keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release) as listener:
                listener.join()

            # Non Blocking
            # listener = keyboard.Listener(
            #     on_press=self.on_press,
            #     on_release=self.on_release)
            # listener.start()

            # while listener.running:
            #     time.sleep(0.05)
            #     clear_screen()
            #     # Render Screen
            #     self.draw_player_on_screen()        
            #     print(self.screen.render())

        else:
            while True:
                clear_screen()
                # Render Screen
                self.draw_player_on_screen()        
                print(self.screen.render())
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
                        self.item_menu.open_menu()
                        continue

                    case _:
                        continue


def main():
    # Game
    new_game = Game()

    # Run Display
    new_game.run_display()


if __name__ == '__main__':
    # clear_screen()
    main()
