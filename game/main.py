import os

"""
Ideas

Battle
HP [@@@@@@@@@@]
HP [++++++++++]
HP [==========]
HP [**********]
HP [----------]

HP [          ]
HP [__________]

HP @@@@@------
HP $$$$$$$$$--
HP ########---
HP +++++++----

HP [*******   ]
MP @@@@@@@@----


    2 Turns
    Player / Enemy
        Fight
            Attack
            Skills
        Items
        Defend
        Run


Characters
    Level
    Experiece
    Skill Points
    
    Hero/Enemy Stats
        HP
        MP
        ATK
        RES
        MGC
        SPD
        LCK

    Skills

    Equipment
        Helmet
        Chest
        Torso
        Boots

        Accessories
            Bands
            Necklace

                        
Screens

Level Up/Status

Skills

"""


class Character:
    def __init__(
            self,
            name: str = None,
            HP: int = None,
            MP: int = None,
            level: int = None,
            experience: float = None,
            skill_points: int = None,
            atk: int = None,
            res: int = None,
            spd: int = None,
            lck: int = None,
            mgc: int = None):
        self.name = name
        self.level = level
        self.experience = experience
        self.skill_points = skill_points
        self.max_hp = HP
        self.hp = HP
        self.max_mp = MP
        self.mp = MP
        self.atk = atk
        self.res = res
        self.spd = spd
        self.lck = lck
        self.mgc = mgc

    def __str__(self):
        # Health Bar
        BAR_WIDTH = 20
        FILL_CHAR = "*"
        SPACE_CHAR = " "

        scaled_filled_space = int(self.hp * BAR_WIDTH / self.max_hp)
        scaled_empty_space = BAR_WIDTH - scaled_filled_space

        # bugs
        if scaled_filled_space == BAR_WIDTH and self.hp < self.max_hp:
            scaled_filled_space = BAR_WIDTH - 1
            scaled_empty_space = 1

        if scaled_filled_space == 0 and self.hp > 0:
            scaled_empty_space = BAR_WIDTH - 1
            scaled_filled_space = 1

        if scaled_filled_space < 0:
            scaled_filled_space = 0
            scaled_empty_space = BAR_WIDTH

        health_bar = f"HP {self.hp:>2}/{self.max_hp:<2} [{FILL_CHAR * scaled_filled_space}{scaled_empty_space * SPACE_CHAR}]"

        # Mana Bar
        MANA_FILL_CHAR = "-"
        MANA_SPACE_CHAR = " "

        scaled_mana_fill = int(self.mp * BAR_WIDTH / self.max_mp)
        scaled_mana_space = BAR_WIDTH - scaled_mana_fill

        # bugs
        if scaled_mana_fill == BAR_WIDTH and self.mp < self.max_mp:
            scaled_mana_fill = BAR_WIDTH - 1
            scaled_mana_space = 1

        if scaled_mana_fill == 0 and self.mp > 0:
            scaled_mana_space = BAR_WIDTH - 1
            scaled_mana_fill = 1

        if scaled_mana_fill <= 0:
            scaled_mana_fill = 0
            scaled_mana_space = BAR_WIDTH

        mana_bar = f"MP {self.mp:>2}/{self.max_mp:<2} [{scaled_mana_fill * MANA_FILL_CHAR}{scaled_mana_space * MANA_SPACE_CHAR}]"

        final = f"""
{self.name}
{health_bar}
{mana_bar}
"""

        return final


class Game:
    def __init__(self):
        self.running = False

    def run(self):
        self.running = True

        # Event Loop
        while self.running:
            print("ran")
            self.running = False


def main():
    new_game = Game()
    new_game.run()

    # Test Character
    test_data = {
        "name": "Hero",
        "level": 1,
        "experience": 0,
        "skill_points": 0,
        "HP": 20,
        "MP": 10,
        "atk": 8,
        "res": 6,
        "spd": 5,
        "lck": 2,
        "mgc": 4
    }
    test_enemy_data = {
        "name": "Goblin",
        "level": 1,
        "experience": 0,
        "skill_points": 0,
        "HP": 15,
        "MP": 8,
        "atk": 7,
        "res": 5,
        "spd": 4,
        "lck": 1,
        "mgc": 2
    }

    new_char = Character(**test_data)
    print(new_char)

    new_enemy = Character(**test_enemy_data)
    print(new_enemy)

    # Turn
    attacker = new_char
    defender = new_enemy

    while new_char.hp != 0:
        print("_" * 35)

        # Calculate Damage
        dmg = attacker.atk - defender.res
        attacker.mp = new_char.mp - 1

        defender.hp = defender.hp - dmg

        if attacker.mp < 0:
            attacker.mp = 0

        print(new_char)
        print(new_enemy)

        # Check hp
        if defender.hp <= 0:
            print(f"{attacker.name} Wins")
            break

        # Swap Turns
        t = attacker
        attacker = defender
        defender = t

    print(f"\nP > E: {new_char.atk - new_enemy.res}")
    print(f"E > P: {new_enemy.atk - new_char.res}")
    print(f"SPD DIFF: {new_char.spd - new_enemy.spd}")


if __name__ == "__main__":
    main()
