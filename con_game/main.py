import os

from enum import Enum

from sqlalchemy import false

"""
Status Screen
--------------------------------------------------
[1] Bulbasaur [grass] [poison]
--------------------------------------------------
Overgrow [False]
Chlorophyll [True]

Height: 7
Weight: 69

Hp             : 45
Attack         : 49
Defense        : 49
Special Attack :*65
Special Defense: 65
Speed          : 45
--------------------------------------------------

Battle Line

MainPlayer lvl.3 {~burn~}
20/20 [##########] 


"""

# Characters:
#   - Player
#   - Enemy

# Items:
#   - Item
#   - Inventory

# Display:
#   - Bar

def create_bar(value: int, max_value: int):
    """
    Bar Styles
    1. ■■■■■■■■■▢ 90%
    2. ▕, █, ▏
    3. ▮ ▯
    """
    size = 15
    fill_char = "■"
    space_char = "▢"

    ratio = value/max_value

    filled_len = int(ratio*size)
    unfilled_len = size - filled_len

    return f"{filled_len*fill_char}{unfilled_len*space_char}"


class StatusCondition(Enum):
    burn: str = "BURNED"
    freeze: str = "FROZEN"
    paralyze: str = "PARALYZED"
    confuse: str = "CONFUSED"


class Character:
    def __init__(self, name: str, level: int, hp: int, attack: int, resistance: int, speed: int):
        # self.id = 0, maybe for npc subclass
        self.name = name
        self.level = level

        self.current_hp = hp
        self.status = ""

        self.total_hp = hp
        self.atk = attack
        self.res = resistance
        self.spd = speed

        self.fainted = False

    def __str__(self) -> str:
        """ """
        # Components
        hp_bar = create_bar(self.current_hp, self.total_hp) 
        status_txt = "" if self.status == "" else f" - {self.status}"

        # Build Final Display
        line_1 = f"{self.name.title()} lvl.{self.level}{status_txt}"
        line_2 = f"HP: {self.current_hp}/{self.total_hp} {hp_bar}"

        txt = f"\n{line_1}\n{line_2}\n"
        return txt
    
    def take_damage(self, enemy_attack: int):
        dmg_taken = enemy_attack - self.res

        if dmg_taken > 0:
            self.current_hp -= dmg_taken
            # Check if hp is less than 0, if char is donezo
            if self.current_hp <= 0:
                self.fainted = True
                self.current_hp = 0
        return dmg_taken # Returns negative falsy if no dmg is taken
    
    def heal(self, heal_amount: int):
        self.current_hp += heal_amount

        if self.current_hp > self.total_hp:
            self.current_hp = self.total_hp



def menu_attack_action(attacker: Character, defender: Character):
    """ dmg_taken, fainted_status, hit_status """
    fainted = False
    hit = True
    # Player attacks Enemy
    input(f"\n{attacker.name} attacked {defender.name}...")
    dmg_taken = defender.take_damage(attacker.atk)
    if dmg_taken > 0:
        print(defender)
        input(f"{defender.name} took {dmg_taken} dmg!")
        
        # Check if Fainted
        if defender.fainted:
            fainted = True
            input(f"{defender.name} has fainted!")
            return False
    else:
        hit = False
        input(f"{defender.name} took no damage!")
    
    return dmg_taken, fainted, hit

def menu_bag_action():
    return

def menu_party_action():
    return

def menu_run_action():
    return


def battle_menu_loop(player: Character, enemy: Character):
    while True:
        print(enemy)
        print(player)
        # print("[ F: Fight | B: Bag | P: Party | R: Run ]")
        battle_choice = input("F: Fight   B: Bag\nP: Party   R: Run\n>>> ")

        match battle_choice:
            case "f":
                # print("\nFight!")

                # Player attacks Enemy
                input(f"\n{player.name} attacked {enemy.name}...")
                enemy_dmg_taken = enemy.take_damage(player.atk)
                if enemy_dmg_taken > 0:
                    print(enemy)
                    input(f"{enemy.name} took {enemy_dmg_taken} dmg!")
                    
                    # Check if Fainted
                    if enemy.fainted:
                        input(f"{enemy.name} has fainted!")
                        break
                else:
                    input(f"{enemy.name} took no damage!")
                # dmg, faint, hit = menu_attack_action(new_char, enemy)

            case "b":
                print("\nBag!")
            case "p":
                print("\nParty!")
            case "r":
                print("\nRun!")
            case "q":
                print("\n[ ***Force Exit***")
                break
            case _:
                input("\nUnrecognized Input!")
        print("\n--- Player Turn End ---\n")
        
        # Enemy Attacks back, this should be in the enemy ai's turn but will be here for simplicity rn
        input(f"\n{enemy.name} attacked {player.name}...")
        player_dmg_taken = player.take_damage(enemy.atk)
        if player_dmg_taken > 0:
            print(player)
            input(f"{player.name} took {player_dmg_taken} dmg!")

            # Check if Fainted
            if player.fainted:
                input(f"{player.name} has fainted!")
                break
        else:
            input(f"{player.name} took no damage!")
        print("\n--- Enemy Turn End ---\n")
    print("\n[ Battle Over ]\n")


def main():
#     print("""
# MainPlayer lvl.3 - burn
# HP: 15/20 [#########_____]
# """)
    char_data = {
        "name": "ash ketchum",
        "level": 3,
        "hp": 20,
        "attack": 8,
        "resistance": 6,
        "speed": 11
    }
    new_char = Character(**char_data)

    enemy_data = {
        "name": "small goblin",
        "level": 2,
        "hp": 15,
        "attack": 7,
        "resistance": 5,
        "speed": 7
    }
    enemy = Character(**enemy_data)


    # print(new_char)
    # print(enemy)
    battle_menu_loop(new_char, enemy)
    


if __name__ == '__main__':
    main()
