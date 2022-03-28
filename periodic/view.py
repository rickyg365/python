import os

from model import PeriodicElement
from pynput import keyboard


class Display:
    def __init__(self, input_data_list=None):
        if input_data_list is None:
            input_data_list = []
        self.list = input_data_list
        self.length = len(input_data_list)

        self.curr_element = 0

    def __str__(self) -> str:
        pass

    def next_item(self):
        self.curr_element += 1

        if self.curr_element > self.length:
            self.curr_element = self.length

    def prev_item(self):
        self.curr_element -= 1

        if self.curr_element < 0:
            self.curr_element = 0
    
    def display_current(self):
        os.system('cls')
        print(self.list[self.curr_element])

    def on_press(self, key):
        print(f"{key} pressed!")
        if key == keyboard.Key.right:
            self.next_item()
            self.display_current()
        if key == keyboard.Key.left:
            self.prev_item()
            self.display_current()

    def on_release(self, key):
        print(f"{key} released!")
        if key == keyboard.Key.esc:
            # Stop listener
            return False
        
    def run(self):
        # Blocking
        with keyboard.Listener(
            on_press=self.on_press,
            on_release=self.on_release) as listener:
            listener.join()

        # Non Blocking
        # listener = keyboard.Listener(
        #     on_press=self.on_press,
        #     on_release=self.on_release)
        # listener.start()


def main():
    new_display = Display()
    new_display.run()

if __name__ == '__main__':
    main()

