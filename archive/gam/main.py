import os

import random

from typing import List, Dict
from dataclasses import dataclass, field



"""
Sample Output

Name lvl.0   
HP: [###############]


[ HP BAR ]

HP: [###############]

HP: [#######        ]

DISPLAY_SIZE = 15
FILL_CHAR = '#'
EMPTY_CHAR = ' '

# HP_RATIO = current_hp/total_hp
fill_length = int( ( current_hp/total_hp ) * DISPLAY_SIZE )  

empty_length = 15 - filled_length


final_hp_txt = f"HP: [{ fill_length*FILL_CHAR }{ empty_length * EMPTY_CHAR }]" 

"""


class Character:
    # def __init__(self, name: str, hp: int, atk: int, res: int, spd: int):
    #     self.name = None

    #     self.hp = None
    #     self.atk = None
    #     self.res = None
    #     self.spd = None

    #     self.current_hp = hp
    #     pass
    def __init__(self, **character_data):
        """ Lazy Way Gives user of method no info but its easy for the creator hehehe """
        self.name = character_data.get('name', "No Name")
        self.level = character_data.get('level', 0)
        self.current_hp = character_data.get('hp', 40)

        self.hp = self.current_hp
        self.atk = character_data.get('atk', 0)
        self.res = character_data.get('res', 0)
        self.spd = character_data.get('spd', 0)

        self.fainted = False


    def __str__(self) -> str:
        BAR_SIZE = 15
        FILL_CHAR = '#'
        EMPTY_CHAR = ' '

        # HP_RATIO = current_hp/total_hp
        fill_length = int( ( self.current_hp/self.hp ) * BAR_SIZE )  

        empty_length = BAR_SIZE - fill_length

        final_hp_txt = f"HP: [{ fill_length*FILL_CHAR }{ empty_length * EMPTY_CHAR }]" 

        txt = f"{self.name.title()} lvl.{self.level:<3}\n{final_hp_txt}"
        return txt
    
    def defend(self, raw_atk: int):
        """ Takes in a Raw Attack value and updates dmg according to resistance and dmg calc """
        dmg = raw_atk - self.res

        if dmg <= 0:
            # No Damage
            return

        self.take_dmg(dmg)
        return dmg        

    def attack(self, enemy):
        """ Takes in Raw Defense Value and returns dmg that should be dealt """
        # dmg = self.atk - raw_res

        # if dmg <= 0:
        #     # You Deal No Damage
        #     return 0
        
        # return dmg
        return enemy.defend(self.atk)

    def heal(self, heal_amount: int):
        """ Restores X amount of Character HP """
        if heal_amount < 0:
            # Damage
            return
        
        if self.fainted:
            self.fainted = False

        new_amount = self.current_hp + heal_amount
        
        if new_amount > self.hp:
            self.current_hp == self.hp
            return

        self.current_hp = new_amount        
        return

    def take_dmg(self, damage_amount: int):
        if damage_amount < 0:
            # Heal
            return

        new_amount = self.current_hp - damage_amount

        if new_amount < 0:
            self.fainted = True
            self.current_hp = 0
            return
        self.current_hp = new_amount
        return


def main():
    # Create Hero
    hero_data = {
        "name": "Hero",
        "level": 3,
        "hp": 50,
        "atk": 12,
        "res": 10,
        "spd": 11,
        "test": "value"
    }

    hero = Character(**hero_data)
    # print(hero)

    # Create Enemy
    enemy_data = {
        "name": "Generic Enemy",
        "level": 4,
        "hp": 50,
        "atk": 10,
        "res": 9,
        "spd": 11
    }

    enemy = Character(**enemy_data)
    # print(enemy)


    battle = True
    while battle:
        # Show Current Status
        display = f"""
{hero}

{enemy}

What will you do?

- [a]: Attack
- [d]: Defend
- [h]: Heal
"""
        print(display)

        # Hero Turn
        u_in = input(">>> ")

        match u_in:
            case 'q':
                battle = False
                break
            case 'a':
                # enemy.defend(hero.atk)
                dmg_dealt = hero.attack(enemy)
                print(f"Hero Attacks Enemy, {dmg_dealt} dealt!")
            case 'd':
                print("Hero Defends")
                pass
            case 'h':
                x = random.randint(5, 10)
                print(f"Healed {x} amount!")
            case _:
                print("Unrecognized Input...")
        
        # Enemy Turn
        # Heal, Attack,  Defend
        choices = 3
        r = random.randint(1, 3)

        match r:
            case 1:
                # Attack
                # hero.defend(enemy.atk)
                dmg_taken = enemy.attack(hero)
                print(f"Enemy Attacks, {dmg_taken} taken!")
            case 2:
                # Defend
                print("Enemy gets ready to defend")
                pass
            case 3:
                # Heal
                y = random.randint(5, 10)
                print(f"Enemy heals {y} amount!")
                pass


    # Battle Sequence
    # attack = lambda atkr, dfnr: dfnr.defend(atkr.atk)
    # # Turn #1
    # # Hero 1
    # attack(hero, enemy)
    # enemy.defend(hero.atk)  # hero attack, feels backwards
    # # Enemy 1
    # hero.defend(enemy.atk)  # enemy attack,

    # # Turn #2
    # # Hero 2
    # hero.take_dmg(10)
    # # Enemy 2
    # enemy.attack(hero)

    # # Turn #3
    # # Hero 3
    # hero.attack(enemy)
    # # Enemy 3
    # enemy.heal(10)

  
    

if __name__ == '__main__':
    main()
 