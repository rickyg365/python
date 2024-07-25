import os

from utils.quick_load import load_json, save_json

from game.battle import Battle
from game.player import Player, Enemy

sample_output = f"""
lvl 03  Enemy 
HP|*****            |


lvl 05  Hero
HP|************     | 24/30
MP|@@@@@@@@@@@      | 15/20

[ attack | spell | items | flee ]
>>> 

"""

# Load Enemies
raw_enemy_data = load_json("enemies.json")
SLIME = raw_enemy_data.get('slime', None)
ZOMBIE = raw_enemy_data.get('zombie', None)

def game_loop():
    # Create Character
    character_data = {
        "name": "Bob Joe",
        "starting_experience": 0,
        "hp": 30,
        "max_hp": 30,
        "mana": 20,
        "max_mana": 20,
        "atk": 6,
        "res": 4,
        "sp_atk": 5,
        "sp_res": 5,
        "spd": 5
    }

    if os.path.isfile("data/hero.json"):
        character_data = load_json("data/hero.json")

    c = Player(**character_data)

    # Create Enemies
    enemy1 = Enemy(**SLIME, starting_experience=200)
    enemy2 = Enemy(**ZOMBIE)

    # Sample Battle Loop - battle_condition

    while True:
        combatants = [enemy1, enemy2]
        all_gone = True
        for _ in combatants:
            if _.is_alive:
                all_gone = False

        if all_gone: 
            c_data = c.export()
            save_json(c_data, "data/hero.json")
            break
        
        enemy_display = '\n'.join(f'{e}' for e in combatants)
        display = f"""
Enemy Encounter!
{enemy_display}

{c}
What will you do?
"""
        print(display)

        # User input
        user_input = input("[ (b)attle | (r)un ] >>> ")

        match user_input:
            case 'b':
                Battle(c, combatants)
            case 'r':
                pass
            case 'q':
                break
            case _:
                pass


if __name__ == "__main__":
    # print(sample_output)
    game_loop()

