import os

from typing import List, Union, Self


from ui_elements import status_bar, StatusbarConfig



"""


SP <------    >  6/10
HP [**********] 20/20
MP {@@@@@@@@  } 8/10


"""


HP_BAR_CONFIG = StatusbarConfig(
    fill='+',
    empty=' ',
    left='(',
    right=')'
)

MP_BAR_CONFIG = StatusbarConfig(
    fill='*',
    empty=' ',
    left='{',
    right='}'
)

STAMINA_BAR_CONFIG = StatusbarConfig(
    fill='-',
    empty=' ',
    left='<',
    right='>'
)

# Game Objects

class Character:
    def __init__(self, name):
        self.name = name

        self.level = 1
        self.experience = 0

        # Attributes
        self.hp = 40
        self.mp = 10
        self.stamina = 10

        self.atk = 10
        self.defense = 10
        self.s_atk = 7
        self.s_defense = 8
        self.speed = 8
        self.luck = 9

        # Status Update
        self.current_hp = 40
        self.current_mp = 10
        self.current_stamina = 10

        self.defending = False
        self.evading = False
        self.parrying = False
        self.countering = False        


    def __str__(self):
        # Character Display
        hp_bar = status_bar(self.current_hp, self.hp, 20, config=HP_BAR_CONFIG)
        mp_bar = status_bar(self.current_mp, self.mp, 20, config=MP_BAR_CONFIG)
        stamina_bar = status_bar(self.current_stamina, self.stamina, 23, config=STAMINA_BAR_CONFIG)
        s = f"""
Lvl {self.level} {self.name}
{stamina_bar}
HP {hp_bar}
MP {mp_bar}
"""
        return s
    
    def attack(self, target: Self):
        damage = self.atk * (self.atk/target.defense)
        
        # Defense
        if target.defending:
            damage = 0
            print(f"{target.name} Defended!")
            target.defending = False

        # Evade
        if target.evading:
            damage = 0
            print(f"{target.name} Evaded!")
            target.evading = False

        # Parry
        if target.parrying:
            damage = 0
            print(f"{target.name} Parried!")
            target.parrying = False

        # Counter
        if target.counter:
            self.hp -= 0
            damage = damage * (1/2)
        
        return damage
    
    def defend(self, target: Self):
        """ Defense """
        if self.defense > target.atk * (3/4):
            self.defending = True
        
    def parry(self):
        """ Attack Speed Precision"""
        return
    
    def counter(self):
        """ Attack Defense """
        return
    
    def evade(self, target: Self):
        """ Speed """
        if self.speed > target.speed:
            self.evading = True

        return
    
    # def cast_spell(self):
    #     return
    
    # def use_skill(self):
    #     return
    



# Game

def battle(player: Character, enemy: Character):
    # Turn order
    turn_order = [player, enemy] if player.speed > enemy.speed else [enemy, player]
    
    # Enemy Turn
    enemy_action_rotation = ['a', 'a', 'd']
    current_action_idx = 0

    
    # Loop
    while True:
        print(f"""
{enemy}

{player}
""")
        # Check Conditions
        if player.hp <= 0:
            print(f'Game Over: {enemy.name} Wins!')
            break

        if enemy.hp <= 0:
            print(f'{player.name} Wins!')
            break

        # Player turn
        user_input = input(">>> ")

        match user_input:
            case 'q':
                break
            case 'a':
                dmg = player.attack(enemy)
                enemy.current_hp -= dmg
                print(f"{player.name} hits {enemy.name} for {dmg}dmg")

            case 'd':
                player.defend(enemy)
            case 'e':
                player.evade(enemy)
            case 'p':
                player.parry()
            case 'c':
                player.counter(enemy)
            case _:
                print(f"{user_input} is not recognized...")

        # Enemy Turn
        num_options = len(enemy_action_rotation)
        current_action = enemy_action_rotation[current_action_idx%num_options]
        match current_action:
            case 'a':
                dmg = enemy.attack(player)
                player.current_hp -= dmg
                print(f"{enemy.name} hits {player.name} for {dmg}dmg")
                
            case 'd':
                enemy.defend(player)
            case 'e':
                enemy.evade(player)
            case 'p':
                enemy.parry()
            case 'c':
                enemy.counter(player)
            case _:
                print(f"Error: {current_action} is not recognized...")
    

    return



if __name__ == "__main__":
    hero = Character("Hero")
    enemy1 = Character("Enemy")


    # Start battle
    battle(hero, enemy1)
    
