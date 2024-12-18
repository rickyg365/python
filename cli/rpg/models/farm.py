from models.seed import Seed
from utils.screen import Screen


class Farm(Screen):
    def __init__(self, width: int=6, height: int=4):
        super().__init__(width=width, height=height, default_data=Seed)
            
    def build_text(self):
        '''Used in __str__'''
        txt = ''
        for i in range(self.height):
            row = ''
            for j in range(self.width):
                curr = self.data[i][j]
                row += f" {curr} "
            txt += f"{row}\n"
        return txt


if __name__ == "__main__":
    COLS = 12
    ROWS = 16
    f = Farm(COLS, ROWS)
    print(f)

    
    for i in range(ROWS):
        for j in range(COLS):
            chosen = f.data[i][j]
            chosen.add_experience(i*j)

    print(f)


