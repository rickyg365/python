import os

from typing import List


class Screen:
    def __init__(self, width: int, height: int, border: bool=False):
        self.border = border
        self.width = width
        self.height = height
        self.data = self.create_data(" ")

    def __str__(self):
        debug = f'W:{self.width} H:{self.height}'
        self.add_string(0, 0, debug)

        if not self.border:
            return '\n'.join([''.join(row) for row in self.data])
        
        # Border Case
        top = f".{self.width * '-'}."
        body = '\n'.join([''.join(['|', *row, '|']) for row in self.data])
        bot = f"'{self.width * '-'}'"
        
        return f"""{top}
{body}
{bot}"""
    
    def create_data(self, char: str):
        data = []
        for j in range(self.height):
            row = []
            for i in range(self.width):
                row.append(char)
            data.append(row)
        
        return data
    
    def update_pixel(self, x: int, y: int, new_char: str):
        self.data[y][x] = new_char
    
    def add_string(self, x: int, y: int, string: str):
        l = len(string)
        over_bound = self.width - (l + x) 
        
        # Out of Boundss
        if over_bound < 0:
            string = string[:-(over_bound)]  # Remove extra chars

        for _ in range(len(string)):
            self.data[y][x + _] = string[_]

    def add_data(self, x: int, y: int, data: List[List]):
        h = len(data)
        w = len(data[0])

        over_width = self.width - (x + w)
        over_height = self.height - (y + h)

        if over_width < 0 or over_height < 0:
            return  # For now do nothing if over boundaries

        for j in range(h):
            for i in range(w):
                self.data[y+j][x+i] = data[j][i]
        
        


if __name__ == "__main__":
    S_WIDTH = 40
    S_HEIGHT = 20
    
    s = Screen(S_WIDTH, S_HEIGHT, border=True)
    print(s)

    HALF_WIDTH = S_WIDTH//2 
    HALF_HEIGHT = S_HEIGHT//2

    TL = Screen(HALF_WIDTH, HALF_HEIGHT)
    TR = Screen(HALF_WIDTH, HALF_HEIGHT)
    BH = Screen(S_WIDTH, HALF_HEIGHT)

    TL.update_pixel(HALF_WIDTH//2, HALF_HEIGHT//2, new_char='1')
    TR.update_pixel(HALF_WIDTH//2, HALF_HEIGHT//2, new_char='2')
    BH.update_pixel(HALF_WIDTH, HALF_HEIGHT//2, new_char='3')

    s.add_data(0, 0, TL.data)
    s.add_data(HALF_WIDTH, 0, TR.data)
    s.add_data(0, HALF_HEIGHT, BH.data)

    print("_________________")
    print(s)

    """
    VISION

    .--------------------------.
    |                          |
    |    S1            S2      |
    |                          |
    |                          |
    |                          |
    |                          |
    |           S3             |
    |                          |
    '--------------------------'
    
    
    """



