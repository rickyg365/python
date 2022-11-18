import os
import time

from display import Screen
from text_box import TextBox
from text_box_components import fight_box

from typing import Dict, List

# class Node:
#     def __init__(self, data=None):
#         self.data = data
#         self.next = None

#         # Implement prev for doubly linked list
#         self.prev = None
    
#     def next(self):
#         if self.next is None:
#             return None
#         return self.next


# class ScreenList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
    
#     def add_node(self, new_node: Node):
#         self.tail.next = new_node
#         self.tail = new_node


class Scene:
    def __init__(self, actions: Dict[str, any]=None):
        # [(screen_data, type)]
        self.screen = Screen() # Linked List
        self.current_screen = None
        self.actions = actions

    def __str__(self):
        txt = ""
        return txt

    def perform_action(self, trigger: str):
        # if trigger in self.input_choices:
        # empty_function => lambda x: None
        empty_fun = lambda x: None
        self.actions.get(trigger, empty_fun)(self.screen)

    def run(self):
        while True:
            os.system('cls')
            print(self.screen)
            user_input = input(">>> ")

            if user_input.lower() == 'q':
                break
            self.perform_action(user_input)





def main():
    def fight_action(screen_obj: Screen):
        x_coord = 0
        y_coord = 0
        new_text_box = fight_box()
        
        screen_obj.draw_text_box(new_text_box.data, x_coord, y_coord)
    battle_choices = {
        "fight": fight_action
    }
    battle_scene = Scene(battle_choices)
    battle_scene.run()

if __name__ == '__main__':
    main()
