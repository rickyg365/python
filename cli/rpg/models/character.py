import random

from typing import List, Dict, Self
from dataclasses import dataclass, Field

from models.items import Item
from models.skills import Skill
from engine.exp_system import ExperienceSystem
from utils.file_handle import load_json
from utils.ui_elements import progress_bar


class Character(ExperienceSystem):
    def __init__(self, name: str=None, filename: str=None, hp: int=None, current_hp: int=None, mp: int=None, current_mp: int=None, attack: int=None, defense: int=None, speed: int=None, gold: int=0, inventory: List[Item]=None, skills: List[Skill]=None, is_alive: bool=True, defending: bool=False, evading: bool=False, **kwargs):
        # Exp {level, experience, experience_to_level, total_experience}
        super().__init__(**kwargs)

        # Meta
        self.filename = filename

        # Attributes
        self.name = name
        self.hp = hp
        self.current_hp = current_hp
        self.mp = mp
        self.current_mp = current_mp
        self.attack = attack
        self.defense = defense
        self.speed = speed

        # Data
        self.gold = gold
        self.inventory = inventory
        self.skills = skills
    
        # Status
        self.is_alive = is_alive
        self.defending = defending
        self.evading = evading

 
        # Create Initial Values
        if self.current_hp is None:
            self.current_hp = hp
            
        if self.current_mp is None:
            self.current_mp = mp

        if self.inventory is None:
            self.inventory = []
            
        if self.skills is None:
            self.skills = []


    def __str__(self):
        hp_bar = progress_bar(self.current_hp, self.hp, 20)
        mp_bar = progress_bar(self.current_mp, self.mp, 20)

        display = f"""lvl.{self.level:02} {self.name}
HP {self.current_hp:>3}/{self.hp:<3} {hp_bar}
MP {self.current_mp:>3}/{self.mp:<3} {mp_bar}
"""
        return display
    
    @classmethod
    def load_from_filename(self, filename: str):
        d = load_json(filename)
        return self(**d)
        # return self.__init__(**d)
    
    def enemy_display(self):
        hp_bar = progress_bar(self.current_hp, self.hp, 20)
        
        display = f"""lvl.{self.level:02} {self.name}
HP {self.current_hp:>3}/{self.hp:<3} {hp_bar}
"""
        return display  


    def show_status(self):
        hp_bar = progress_bar(self.current_hp, self.hp, 20)
        mp_bar = progress_bar(self.current_mp, self.mp, 20)
        exp_bar = progress_bar(self.experience, self.experience_to_level, 20)

        display = f"""
lvl.{self.level:02} {self.name}
HP {self.current_hp:>3}/{self.hp:<3} {hp_bar}
MP {self.current_mp:>3}/{self.mp:<3} {mp_bar}
EXP {self.experience}/{self.experience_to_level} {exp_bar}
Items: {len(self.inventory)} | Skills: {len(self.skills)}
"""
        return display
    
    def revive(self):
        self.current_hp = self.hp
        self.current_mp = self.mp
        self.is_alive = True
        
    
    def add_experience(self, amount: int):
        prev_level = self.level
        self._add_experience(amount)
        print(f"+{amount} EXP")
        if self.level > prev_level:
            self.level_up()
            print("Leveled Up!")

    def level_up(self):
        self.hp = self.hp + 10
        self.current_hp = self.hp
        self.mp = self.mp + 5
        self.current_mp = self.mp
        self.attack += 2
        self.defense += 2
        self.speed += 3
        
        return

    def take_damage(self, damage_amount: int):
        # Damage
        self.current_hp -= damage_amount

        if self.current_hp <=0:
            self.current_hp = 0
            self.is_alive = False
    
    def use_item(self):
        return
    
    def use_skill(self):
        return
    
    def hit(self, enemy: Self):
        # Evasion
        if enemy.evading:
            enemy.evading = False
            r = random.randint(0, 100)
            if enemy.speed > r:
                print(f"{enemy.name} evaded the attack!")
                return 0
        
        # Defense
        damage_reduction = 0
        if enemy.defending:
            damage_reduction = max(self.attack - enemy.defense, 0)
            enemy.defending = False
        
        dmg_formula = max(self.attack * self.attack/enemy.defense, 0)
        
        return int(dmg_formula) - damage_reduction
    
    def defend(self):
        self.defending = True
        return
    
    def evade(self):
        self.evading = True
        return
    
    def parse_reward(self, rewards: Dict):
        # Exp
        exp_amount = rewards.get('exp', None)

        if exp_amount is not None:
            self.add_experience(exp_amount)
        
        # Gold
        gold_amount = rewards.get('gold', None)

        if gold_amount is not None:
            self.gold += gold_amount

        # Items
        items = rewards.get('items', None)

        if items is not None:
            self.inventory.extend(items)

    
    def export(self):
        return {
            'filename': self.filename,
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
            **self.level_data(),
        }


class Enemy(Character):
    def __init__(self, exp_reward: int=0, gold_reward: int=0, item_rewards: List[Item]=None, **kwargs):
        super().__init__(**kwargs)

        self.exp_reward = exp_reward
        self.gold_reward = gold_reward
        self.item_rewards = item_rewards

    def drop_reward(self):
        # Rewards
        return {
            'exp': self.exp_reward,
            'gold': self.gold_reward,
            'items': self.item_rewards
        }
    
    def export(self):
        return {
            'exp_reward': self.exp_reward,
            'gold_reward': self.gold_reward,
            'item_rewards': self.item_rewards,
            **super().export(),
            }














