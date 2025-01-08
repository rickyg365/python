import os

from utils.ui_elements import progress_bar
from game_engine.item import Item, Equipment, EquipmentLoadout


class Character:
    def __init__(self, name, hp: int=0, current_hp: int=0, mp: int=0, current_mp: int=0, attack: int=0, defense: int=0, speed: int=0, special: int=0, luck: int=0, equipments: EquipmentLoadout=None,inventory=None):
        self.name = name
        self.hp = hp
        self.current_hp = current_hp
        self.mp = mp
        self.current_mp = current_mp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.special = special
        self.luck = luck

        # Load Items
        self.inventory = inventory

        # Load Equipment
        self.active_loadout = equipments
        if isinstance(equipments, dict):
            # Equipment loadout handles converting raw_data into Equiment obj
            self.active_loadout = EquipmentLoadout().load_from_raw(**equipments)
        
        self.head = self.active_loadout.head
        self.left_arm = self.active_loadout.left_arm
        self.right_arm = self.active_loadout.right_arm
        self.body = self.active_loadout.body
        self.legs = self.active_loadout.legs


    def __str__(self):

        inventory_str = "\n".join(f"{i}" for i in self.inventory)

        s = f'''{self.name}
HP: {self.current_hp:>3}/{self.hp:<3}
MP: {self.current_mp:>3}/{self.mp:<3}
'''
        return s
    
    def export(self):
        return {
            "name": self.name,
            "hp": self.hp,
            "current_hp": self.current_hp,
            "mp": self.mp,
            "current_mp": self.current_mp,
            "attack": self.attack,
            "defense": self.defense,
            "speed": self.speed,
            "special": self.special,
            "luck": self.luck,
            "inventory": self.inventory,
            "equipments": self.active_loadout.export()
        }
    
    def show_status(self):
        inventory_str = "\n".join(f"{i}" for i in self.inventory)

        return f"""
{self.name}
HP: {self.current_hp:>3}/{self.hp:<3}
MP: {self.current_mp:>3}/{self.mp:<3}

Attack: {self.attack}
Defense: {self.defense}
Special: {self.special}
Speed: {self.speed}
Luck: {self.luck}

Inventory
{inventory_str}
{self.active_loadout}

"""
    def revive(self):
        return
    
    def add_experience(self, amount: int):
        return
    
    def level_up(self):
        return
    
    def apply_buff(self, attribute: str, buff_amount: int):
        return
    
    def equip(self, part: str, equipment):
        return
    
    def take_damage(self, damage_amount: int):
        return
    
    def hit(self, enemy):
        return
    
    def defend(self):
        return
    
    def evade(self):
        return
    
    def use_item(self, item):
        return
    
    def parse_reward(self, rewards):
        return



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
    CHARACTER_DATA={
        "name": "Hero",
        "hp": 20,
        "current_hp": 20,
        "mp": 10,
        "current_mp": 10,
        "attack": 5,
        "defense": 5,
        "speed": 4,
        "special": 1,
        "luck": 1,
        "inventory": [],
        "head": 0,
        "body": 0,
        "legs": 0,
        "right_arm": 0,
        "left_arm": 0,
    }

    c = Character(**CHARACTER_DATA)
    print(c)
