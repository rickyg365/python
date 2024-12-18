
from engine.exp_system import ExperienceSystem
from utils.ui_elements import progress_bar

'''
Seed: Type & Progress

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

class Seed(ExperienceSystem):
    '''
    Growth
    Seed > phase 1
    5 battles = 100/5 = 20

    phase 1 > phase 2
    10 battles = 100/10 = 10

    phase 2 > final
    20 battles = 100/20 = 5
    '''
    SYMBOL_MAP = {
        'seed': '.',
        'p1': '*',
        'p2': 'o'
    }

    EXP_MAP = {
        'seed': 20,
        'p1': 10,
        'p2': 5
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

    def __init__(self, name: str='health', final_symbol: str='+', phase: str='seed', **kwargs):
        super().__init__(**kwargs)
        
        self.name = name
        self.phase = phase
        self.symbol = self.SYMBOL_MAP.get(phase, '.')
        self.final_symbol = final_symbol

        # self.progress = ExperienceSystem()

    def __str__(self):
        return f'{self.symbol}'
    
    def status(self):
        pbar = self.level_str()
        txt = f"""{self.name} Seed [{self.final_symbol}]
| {self.symbol} | {self.phase} | {self.experience:>3}/100 {pbar}
"""
        return txt

    def add_experience(self, num_battles: int=1):
        for _ in range(num_battles):
            prev_level = self.level
            if prev_level >= 4:
                return
            
            # Add Experience
            exp_amount = self.EXP_MAP.get(self.phase, 0)
            self._add_experience(exp_amount)
            
            # Level Up
            if prev_level < self.level:
                self.phase_up()
    
    def phase_up(self):
        self.phase = self.PHASE_MAP.get(self.phase, None)
        if self.phase == 'final':
            self.symbol = self.final_symbol
            return
        
        self.symbol = self.SYMBOL_MAP.get(self.phase)
    


if __name__ == "__main__":
    s = Seed()
    print(s)

    for _ in range(40):
        s.add_experience(1)
    
    print(s.status())


