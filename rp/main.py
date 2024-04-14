import os
from game.character import Character, Enemy
from battle import Battle

sample_output = f"""
lvl 03  Enemy 
HP|*****            |


lvl 05  Hero
HP|************     | 24/30
MP|@@@@@@@@@@@      | 15/20

[ attack | spell | items | flee ]
>>> 

"""



if __name__ == "__main__":

    # print(sample_output)

    # for _ in range(101):
    #     curr_bar = prog_bar(_, 100)
    #     print(f"{_:03}/100 {curr_bar}")

    character_data = {
        "name": "Bob Joe",
        "starting_experience": 75,
        "max_hp": 30,
        "hp": 30,
        "atk": 6,
        "res": 4,
        "spd": 5
    }
    slime_data = {
        "name": "Slime",
        "max_hp": 20,
        "hp": 20,
        "atk": 5,
        "res": 4,
        "spd": 3
    }
    zombie_data = {
        "name": "Zombie",
        "max_hp": 28,
        "hp": 28,
        "atk": 5,
        "res": 2,
        "spd": 2
    }

    c = Character(**character_data)

    enemy1 = Enemy(**slime_data)
    enemy2 = Enemy(**zombie_data)


    # Sample Battle Loop - battle_condition
    combatants = [enemy1, enemy2]

    Battle(c, combatants)


#     while True:
#         # Check Status of enemies
#         updated_combatants = []
#         for combatant in combatants:
#             # Alive
#             if combatant.hp > 0:
#                 updated_combatants.append(combatant)
#             # Dead
#             else:
#                 # Hasn't been marked dead
#                 if combatant.is_alive:
#                     combatant.is_alive = False
#                     c.level_sys.add_experience(combatant.reward_value)
#         combatants = updated_combatants
#         enemies = '\n'.join(f'{e}' for e in combatants)
#         text = f"""
# Enemies:
# {enemies}

# {c}
# """
#         # Display
#         print(text)
        
#         # Break if all enemies defeated
#         if len(combatants) == 0: break
        
#         user_input = input("[  (a)ttack | (d)efend | (i)tems | (r)un  ]\n>>> ")

#         enemy_dmg = sum(x.atk - c.res for x in combatants)

#         match user_input:
#             case 'a':
#                 e = combatants[-1]
#                 e.hp -= (c.atk - e.res)
#             case 'd':
#                 enemy_dmg -= c.res
#             case 'i':
#                 print("Not implemented yet!")
#             case _:
#                 # for combatant in combatants:
#                 #     combatant.hp -= 1
#                 pass

#         c.hp -= min(enemy_dmg, 0)

