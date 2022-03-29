import os

from model import PeriodicElement
from pynput import keyboard


class Display:
    def __init__(self, input_data_list=None, use_keyboard: bool=True):
        if input_data_list is None:
            input_data_list = []
        self.list = input_data_list
        self.length = len(input_data_list)

        self.curr_element = 0
        self.running = True
        self.use_keyboard = use_keyboard

    def __str__(self) -> str:
        pass

    def get_item(self, item_index: int):
        if item_index > self.length - 1:
            return None
        
        return self.list[item_index]

    def next_item(self):
        self.curr_element += 1

        if self.curr_element > self.length - 1:
            self.curr_element = self.length - 1

    def prev_item(self):
        self.curr_element -= 1

        if self.curr_element < 0:
            self.curr_element = 0
    
    def handle_input(self):
        user_input = input(">>> ")
        if user_input == 'q':
            self.running = False
        
        if user_input == 'n':
            self.next_item()
        if user_input == 'p':
            self.prev_item()

        if len(user_input) and user_input[0] in '0123456789':
            item_number = int(user_input)
            if item_number <= 0:
                self.curr_element = 0
                return
            if item_number > self.length - 1:
                self.curr_element = self.length-1
                return
            self.curr_element = item_number - 1

        return user_input

    def display_current(self):
        os.system('cls')
        # Card View
        # print(self.list[self.curr_element].card_view())

        # Regular View
        print(self.list[self.curr_element])

        
    def on_press(self, key):
        # print(f"{key} pressed!")
        if key == keyboard.Key.right:
            self.next_item()
            self.display_current()
        if key == keyboard.Key.left:
            self.prev_item()
            self.display_current()

    def on_release(self, key):
        # print(f"{key} released!")
        if key == keyboard.Key.esc:
            # Stop listener
            return False
        
    def run(self):
        if self.use_keyboard:

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
        else:
            listener = keyboard.Listener(
                on_press=self.on_press,
                on_release=self.on_release)
            listener.start()
            while self.running:
                self.display_current()
                self.handle_input()


            

def main():
    new_display = Display(use_keyboard=False)
    new_display.run()

if __name__ == '__main__':
    main()

