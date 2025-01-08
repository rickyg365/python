
import os
import random

from typing import List, Dict, Callable, Self


from  utils.ui_elements import progress_bar
from game_engine.item import Item, Equipment, Consumable, Inventory
'''
Goals:
- save/load data
- basic crud operations

Items
- Key
- Consumable
- Equipment

'''
class Character:
    def __init__(self, name: str, health: int=0, mp: int=0, attack: int=0, defense: int=0, speed: int=0, critical_chance: int=0, block_chance: int=0, level: int=0, experience: int=0, exp_to_level: int=100, inventory: List[Item]=None, is_alive: bool=True, defending: bool=False, evading: bool=False, current_health: int=None, current_mp: int=None, gold: int=0, head: Equipment=None, body: Equipment=None, right_arm: Equipment=None, left_arm: Equipment=None, legs: Equipment=None, accessory_1: Equipment=None, accessory_2: Equipment=None, skills: List=None, spells: List=None):
        # Status
        self.is_alive = is_alive
        self.defending = defending
        self.evading = evading

        # Attributes
        self.level = level
        self.experience = experience
        self.exp_to_level = exp_to_level
        self.name = name
        self.health = health
        self.current_health = current_health
        self.mp = mp
        self.current_mp = current_mp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.critical_chance = critical_chance
        self.block_chance = block_chance

        # Data
        self.gold = gold
        self.inventory = Inventory(data=inventory)

        self.head = head
        self.body = body
        self.right_arm = right_arm
        self.left_arm = left_arm
        self.legs = legs
        self.accessory_1 = accessory_1
        self.accessory_2 = accessory_2

        # Abilities/Spells
        self.skills = skills
        self.spells = spells
        
        # Create Initial Values
        if self.current_health is None:
            self.current_health = health
            
        if self.current_mp is None:
            self.current_mp = mp

    def __str__(self):
        hp_bar = progress_bar(self.current_health, self.health, 20)
        mp_bar = progress_bar(self.current_mp, self.mp, 20)
        exp_bar = progress_bar(self.experience, self.exp_to_level, 20)

        display = f"""
lvl.{self.level:02} {self.name}
HP {self.current_health:>3}/{self.health:<3} {hp_bar}
MP {self.current_mp:>3}/{self.mp:<3} {mp_bar}
EXP {self.experience}/{self.exp_to_level} {exp_bar}
Items: {self.inventory.length} | Skills: 0
"""
        return display
    
    
    def export(self):
        return {
            "is_alive": self.is_alive,
            "defending": self.defending,
            "evading": self.evading,
            "level": self.level,
            "experience": self.experience,
            "exp_to_level": self.exp_to_level,
            "name": self.name,
            "health": self.health,
            "current_health": self.current_health,
            "mp": self.mp,
            "current_mp": self.current_mp,
            "attack": self.attack,
            "defense": self.defense,
            "speed": self.speed,
            "critical_chance": self.critical_chance,
            "block_chance": self.block_chance,
            "gold": self.gold,
            "inventory": self.inventory.export(),
            "head": self.head,
            "body": self.body,
            "right_arm": self.right_arm,
            "left_arm": self.left_arm,
            "legs": self.legs,
            "accessory_1": self.accessory_1,
            "accessory_2": self.accessory_2,
            "skills": self.skills,
            "spells": self.spells,
        }
    
    def show_status(self):
            return f"""
{self.name}
HP: {self.health}
Attack: {self.attack}
Defense: {self.defense}
Speed: {self.speed}
crit {self.critical_chance}% | block {self.block_chance}%

{self.inventory}
Equipment:
    Head: {self.head}
    Body: {self.body}
    Left Arm: {self.right_arm}
    Right Arm: {self.left_arm}
    Legs: {self.legs}
    Accessory 1: {self.accessory_1}
    Accessory 2: {self.accessory_2}

"""
    
    def revive(self):
        self.current_health = self.health
        self.current_mp = self.mp
        self.is_alive = True
        
    def add_experience(self, amount: int):        
        print(f"+{amount} EXP")
        conj = self.exp_to_level - amount

        # Update
        if conj <= 0:
            # Level Up
            self.level_up()
            self.add_experience(-1*conj)
        else:
            # Add Experience
            self.exp_to_level = conj
            self.experience += amount

    def level_up(self):
        input(f"Leveled Up!!!\n{self}")

        # Udpate Level
        self.level += 1
        self.exp_to_level = 100

        # Update Attributes
        self.health = self.health + 10
        self.current_health = self.health
        self.mp = self.mp + 5
        self.current_mp = self.mp
        self.attack += 2
        self.defense += 2
        self.speed += 3

        # Update Skills
        # Update Spells

    def apply_buff(self, attribute: str, buff_amount: int):
        attribute_exists = hasattr(self, attribute)
        if not attribute_exists:
            return

        current = getattr(self, attribute)
        setattr(self, attribute, current + buff_amount)
        
        return

    def equip(self, part: str, equipment: Equipment):
        if not hasattr(self, part):
            return
    
        # Check if something is equipped
        current = getattr(self, part, None)

        if current is not None:
            current.remove(self)
        
        # Equip new
        setattr(self, part, equipment)
        equipment.apply(self)

       
    def take_damage(self, damage_amount: int):
        # Damage
        self.current_health -= damage_amount

        if self.current_health <=0:
            self.current_health = 0
            self.is_alive = False
    
    def hit(self, enemy: Self):
        # Evasion
        if enemy.evading:
            r = random.randint(0, 100)
            if enemy.speed > r:
                print(f"{enemy.name} evaded the attack!")
                return 0
            enemy.evading = False
        
        # Defense
        damage_reduction = 0
        if enemy.defending:
            damage_reduction = max(enemy.defense - self.attack, 0)
            enemy.defending = False
        
        dmg_formula = max(self.attack * self.attack/enemy.defense, 0)
        
        return int(dmg_formula) - damage_reduction
    
    def defend(self):
        self.defending = True
    
    def evade(self):
        self.evading = True
        
    def use_item(self, item: Consumable):
        item.use(self)

        # Remove item from inventory
        return
    
    def use_skill(self):
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
            for item in items:
                self.inventory.add(item)

class Enemy(Character):
    def __init__(self, exp_reward: int=0, gold_reward: int=0, item_rewards: List[Item]=None, **kwargs):
        super().__init__(**kwargs)

        self.exp_reward = exp_reward
        self.gold_reward = gold_reward
        self.item_rewards = list() if item_rewards is None else item_rewards
 
    def __str__(self):
        hp_bar = progress_bar(self.current_health, self.health, 20)
        
        display = f"""lvl.{self.level:02} {self.name}
HP {self.current_health:>3}/{self.health:<3} {hp_bar}
"""
        return display  

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

     
        

if __name__ == "__main__":
    HERO_DATA = {
        'name': 'Hero',
        'health': 20,
        'attack': 20,
        'defense': 20,
        'speed': 20,
    }

    hero = Character(**HERO_DATA)
    print(hero)


    POTION_DATA = {
        'key': 'ttrrppid',
        'name': 'Potion',
        'item_type': 'consumable',
        'description': 'Heals a small amount of health.',
        'attributes': {
            'health': 10
        },
    }

    WOODEN_SWORD = {
        'key': 'ttrrppid',
        'name': 'Wooden Sword',
        'item_type': 'weapon',
        'description': 'A small wooden sword',
        'attributes': {
            'attack': 10,
            'critical_chance': 2
        },   
    }

    WOODEN_SHIELD = {
        'key': 'ttrrppid',
        'name': 'Wooden Shield',
        'item_type': 'equipment',
        'description': 'A small wooden shield',  # be careful not to get a splinter.
        'attributes': {
            'defense': 8,
            'block_chance': 10
        },
    }

    potion = Consumable(**POTION_DATA)
    wood_sword = Equipment(**WOODEN_SWORD)
    wood_shield = Equipment(**WOODEN_SHIELD)
    

    hero.equip('left_arm', wood_shield)
    hero.equip('right_arm', wood_sword)

    hero.consume(potion)

    print()
    print(hero)

