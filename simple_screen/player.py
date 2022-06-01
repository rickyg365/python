import os

"""
"""
  
class Player:
    def __init__(self):
        self.current_player = "@"
        self.player_pos = [0, 0]
        self.prev_player_pos = [0, 0]

    def __str__(self) -> str:
        txt = ""
        return txt
    
    def move_up(self):
        # Move Up
        self.prev_player_pos = [*self.player_pos]
        self.player_pos[0] = max(self.player_pos[0] - 1, 0)
        return

    def move_down(self, lower_boundary):
        # Move Down
        self.prev_player_pos = [*self.player_pos]
        self.player_pos[0] = min(self.player_pos[0] + 1, lower_boundary)  # lower_boundary = screen.height - 1
        return

    def move_right(self, right_boundary):
        # Move Right
        self.prev_player_pos = [*self.player_pos]
        self.player_pos[1] = min(self.player_pos[1] + 1, right_boundary)  # right_boundary = screen.width - 1
        return

    def move_left(self):
        # Move Left
        self.prev_player_pos = [*self.player_pos]
        self.player_pos[1] = max(self.player_pos[1] - 1, 0)
        return


def main():
    return

if __name__ == '__main__':
    main()
