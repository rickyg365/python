import random

from typing import List, Dict, Self
from dataclasses import dataclass, Field

from utils.items import Item
from utils.skills import Skill
from utils.exp_system import ExperienceSystem
from utils.file_handle import load_json
from utils.progress_bar import progress_bar


@dataclass
class Character:
    name: str = None
    inventory: List[Item] = None
    skills: List[Skill] = None
    exp: ExperienceSystem = None

    hp: int=10
    current_hp: int=None
    mp: int=0
    current_mp: int=None
    attack: int=0
    defense: int=0
    speed: int=0

    is_alive: bool=True
    defending: bool=False
    evading: bool=False

    filename: str=None

    def __post_init__(self):
        if self.filename is not None:
            self.load_from_file()

        if self.current_hp is None:
            self.current_hp = self.hp
            
        if self.current_mp is None:
            self.current_mp = self.mp

        if self.inventory is None:
            self.inventory = []
            
        if self.skills is None:
            self.skills = []

        if self.exp is None:
            self.exp = ExperienceSystem()


    def __str__(self):
        hp_bar = progress_bar(self.current_hp, self.hp, 20)
        mp_bar = progress_bar(self.current_mp, self.mp, 20)

        display = f"""lvl.{self.exp.level:02} {self.name}
HP {self.current_hp:>3}/{self.hp:<3} {hp_bar}
MP {self.current_mp:>3}/{self.mp:<3} {mp_bar}
"""
        return display
    
    def enemy_display(self):
        hp_bar = progress_bar(self.current_hp, self.hp, 20)
        
        display = f"""lvl.{self.exp.level:02} {self.name}
HP {self.current_hp:>3}/{self.hp:<3} {hp_bar}
"""
        return display    


    def show_status(self):
        hp_bar = progress_bar(self.current_hp, self.hp, 20)
        mp_bar = progress_bar(self.current_mp, self.mp, 20)
        exp_bar = progress_bar(self.exp.experience, self.exp.experience_to_level, 20)

        display = f"""
lvl.{self.exp.level:02} {self.name}
HP {self.current_hp:>3}/{self.hp:<3} {hp_bar}
MP {self.current_mp:>3}/{self.mp:<3} {mp_bar}
EXP {self.exp.experience}/{self.exp.experience_to_level} {exp_bar}
Items: {len(self.inventory)} | Skills: {len(self.skills)}
"""
        return display


    def load_from_file(self):
        ''' Raw Data Format
        {
            "name": str,
            "inventory": [],
            "skills": [],
            "exp": {
                "level": int,
                "experience": int,
                "experience_to_level": int,
                "total_experience": int
            }
        }

        *assuming filename was provided
        '''
        data = load_json(self.filename)
        
        self.name = data.get('name', '')
        self.hp = data.get('hp', 0)
        self.current_hp = data.get('current_hp', 0)
        self.mp = data.get('mp', 0)
        self.current_mp = data.get('current_mp', 0)
        self.attack = data.get('attack', 0)
        self.defense = data.get('defense', 0)
        self.speed = data.get('speed', 0)
        
        self.inventory = [Item(**i) for i in data.get('inventory', [])]
        self.skills = [Skill(**s) for s in data.get('skills', [])]
        self.exp = ExperienceSystem(**data.get('exp', {}))
        return

    def take_damage(self, damage_amount: int):
        # Evasion
        if self.evading:
            self.evading = False
            r = random.randint(0, 100)
            if self.speed > r:
                return
        # Defense
        damage_reduction = 0
        if self.defending:
            damage_reduction = max(damage_amount - self.defense, 0)
            self.defending = False
        
        # Damage
        self.current_hp -= (damage_amount - damage_reduction)

        if self.current_hp <=0:
            self.current_hp = 0
            self.is_alive = False
    
    def use_item(self):
        return
    
    def use_skill(self):
        return
    
    def hit(self, enemy: Self):
        dmg_formula = max(self.attack - enemy.defense, 0)
        
        return dmg_formula
    
    def defend(self):
        self.defending = True
        return
    
    def evade(self):
        self.evading = True
        return
    
    def export(self):
        return {
            'name': self.name,
            'hp': self.hp,
            'current_hp': self.current_hp,
            'mp': self.mp,
            'current_mp': self.current_mp,
            'attack': self.attack,
            'defense': self.defense,
            'speed': self.speed,
            'inventory': [i.export() for i in self.inventory],
            'skills': [s.export() for s in self.skills],
            'exp': self.exp.export(),
            'filename': self.filename
        }
