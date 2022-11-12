import os
import random
from typing import List, Dict, Any

"""
# - Wall
  - Empty
O - Start
X - Finish
"""
class MazeCell:
    def __init__(self, character: str=None):
        self.current_value = character

    def __str__(self):
        txt = f"{self.current_value}"
        return txt

    def update(self, new_value):
        self.current_value = new_value


class Maze:
    def __init__(self, rows, cols, settings: Dict[str, Any]=None):
        if settings is None:
            settings = {
                "outer_wall": True,
                "probabilities": {
                    "wall": .26,
                    "empty": .75
                },
                "characters": {
                    "wall": '#',
                    "empty": ' ',
                    "start": 'o',
                    "finish": 'x',
                },
                "has_enterance": True,
                "has_exit": True
            }
        
        self.settings = settings
        self.data = self.create_maze(cols, rows)

    def __str__(self):
        txt = "\n".join("".join([f"{cell}" for cell in row]) for row in self.data)
        return txt

    def create_maze(self, w, h):
        top, left = 0, 0
        bot, right = h, w

        start_count = 0
        end_count = 0

        new_maze = []
        for i in range(h):
            new_row = []
            for j in range(w):
                chosen = ' '  # Default 
                r = random.random()

                if start_count < 1 and self.settings['has_enterance'] and i == top and (j != 0 and j != right-1):
                    if r > .65:
                        chosen = self.settings['characters']['start']
                        new_row.append(MazeCell(chosen))
                        start_count += 1
                        continue

                if end_count < 1 and self.settings['has_exit'] and i == bot-1 and (j != 0 and j != right-1):
                    if r > .75:
                        chosen = self.settings['characters']['finish']
                        new_row.append(MazeCell(chosen))
                        end_count +=1
                        continue
                
                if self.settings['outer_wall'] and (i == top or i == bot-1 or j == left or j == right-1):
                    chosen = self.settings['characters']['wall']

                # Random Chance of wall
                if r <= self.settings['probabilities']['wall']:
                    chosen = self.settings['characters']['wall']

                if i == top and j == right - 2 and start_count < 1:
                    chosen = self.settings['characters']['start']

                if i == bot and j == right - 2 and end_count < 1:
                    chosen = self.settings['characters']['finish']

                new_row.append(MazeCell(chosen))
            new_maze.append(new_row)

        return new_maze


def main():
    new_maze = Maze(5, 10)
    print(new_maze)

if __name__ == "__main__":
    main()