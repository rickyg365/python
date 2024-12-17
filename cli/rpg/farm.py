
from utils.exp_system import ExperienceSystem
from utils.ui_elements import progress_bar



'''
FARM

.-----------------.
| - - - - - - - - | Empty
| . . . . . . . . | Seed
| * * * * * * * * | Growth 1
| o o o o o o o o | Growth 2
|                 |
| + + + + + + + + | Health
| # # # # # # # # | Attack
| @ @ @ @ @ @ @ @ | Defense
| ~ ~ ~ ~ ~ ~ ~ ~ | Speed
| $ $ $ $ $ $ $ $ | Special Attack
| & & & & & & & & | Special Defense
| % % % % % % % % | Luck
'-----------------'


Individual Seed Progress
_______________________________________
Health Seed [+]
| o | G2 |  73/100 (-------------    )
_______________________________________

_______________________________________
Seed Name [?]
| ? |(?) 000/000 (-------------    )
_______________________________________


'''

class Seed:
    '''
    Growth
    Seed > phase 1
    5 battles = 100/5 = 20

    phase 1 > phase 2
    10 battles = 100/10 = 10

    phase 2 > final
    50 battles = 100/50 = 2
    '''
    SYMBOL_MAP = {
        'seed': '.',
        'p1': '*',
        'p2': 'o',
        'final': '?'
    }

    EXP_MAP = {
        'seed': 20,
        'p1': 10,
        'p2': 2
    }

    PHASE_MAP = {
        'seed': 'p1',
        'p1': 'p2',
        'p2': 'final'
    }
    VALID_NAMES = [
        'health',
        'attack',
        'defense',
        'speed',
        'sattack',
        'sdefense',
        'luck'
    ]

    def __init__(self, name: str='health', final_symbol: str='+', phase: str='seed'):
        self.name = name
        self.phase = phase
        self.progress = ExperienceSystem()
        self.symbol = self.SYMBOL_MAP.get(phase, '.')
        self.final_symbol = final_symbol

    def __str__(self):
        return f'{self.symbol}'
    
    def status(self):
        pbar = progress_bar(self.progress.experience, 100, 10)
        txt = f"""{self.name} Seed [{self.final_symbol}]
| {self.symbol} | {self.phase} | {self.progress.experience:>3}/100 {pbar}
"""
        return txt

    def add_experience(self, num_battles: int=1):
        for _ in range(num_battles):
            prev_level = self.progress.level
            if prev_level >= 4:
                return
            
            # Add Experience
            exp_amount = self.EXP_MAP.get(self.phase, 0)
            self.progress.add_experience(exp_amount)
            
            # Level Up
            if prev_level < self.progress.level:
                self.phase_up()
    
    def phase_up(self):
        self.phase = self.PHASE_MAP.get(self.phase, None)
        if self.phase == 'final':
            self.symbol = self.final_symbol
            return
        
        self.symbol = self.SYMBOL_MAP.get(self.phase)
    

class Farm:
    def __init__(self, width: int=6, height: int=2):
        self.width = width
        self.height = height
        self.data = self.build_data(Seed)

    def __str__(self):
        s = self.build_text()
        return s
    
    def build_text(self):
        txt = ''
        for i in range(self.height):
            row = ''
            for j in range(self.width):
                curr = self.data[i][j]
                row += f" {curr} "
            txt += f"{row}\n"
        return txt
                
    def build_data(self, default_factory=None):
        data = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(default_factory())
            data.append(row)
        
        return data



    

if __name__ == "__main__":
    s = Seed()

    print(s)

    for _ in range(40):
        s.add_experience(1)
    
    print(s.status())


    COLS = 12
    ROWS = 16
    f = Farm(COLS, ROWS)
    print(f)

    
    for i in range(ROWS):
        for j in range(COLS):
            chosen = f.data[i][j]
            chosen.add_experience(i*j)

    print(f)


