"""
Date: 06/01/2022
"""


class Player:
    def __init__(self):
        self.current_player = "@"

        self.pos = [0, 0]
        self.prev_pos = [0, 0]

        self.player_items = {}

    def __str__(self) -> str:
        txt = ""
        return txt
    
    def add_item(self, name: str, amount: int=1):
        self.player_items[name] = amount + self.player_items.get(name, 0)

    def remove_item(self, name: str, amount: int=1):
        curr_amount = self.player_items.get(name, 0)
        if curr_amount - amount > 0:
            self.player_items[name] -= amount
        if curr_amount - amount == 0:
            del self.player_items[name]
        return

    def get_items(self):
        """ Returns a dict of current items """
        return self.player_items

    def move_up(self):
        # Move Up
        self.prev_pos = [*self.pos]
        self.pos[0] = max(self.pos[0] - 1, 0)
        return

    def move_down(self, lower_boundary):
        # Move Down
        self.prev_pos = [*self.pos]
        self.pos[0] = min(self.pos[0] + 1, lower_boundary)  # lower_boundary = screen.height - 1
        return

    def move_right(self, right_boundary):
        # Move Right
        self.prev_pos = [*self.pos]
        self.pos[1] = min(self.pos[1] + 1, right_boundary)  # right_boundary = screen.width - 1
        return

    def move_left(self):
        # Move Left
        self.prev_pos = [*self.pos]
        self.pos[1] = max(self.pos[1] - 1, 0)
        return

