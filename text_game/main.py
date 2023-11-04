import os
import json

from utils.bar import StatusBar
from objects.character import Character

# Character Data
CDATA = None

with open("data/sample_character_data.json", 'r') as character_data:
    CDATA = json.load(character_data)

# Character Objects
c1 = Character("Character 1", "0004", CDATA)
c2 = Character("Character 2", "0005", CDATA)

# Battle
turn_number = 1
# Determine Turn Order
current_character = c1
other_character = c2

if c2._spd > c1._spd:
    current_character = c2
    other_character = c1


while c1.is_alive and c2.is_alive:
    # Current Battle Status
    status = f"""Battle Turn #{turn_number}
{c1.name}  HP: {c1.current_hp}/{c1._max_hp} {StatusBar(c1.current_hp, c1._max_hp)}
{c2.name}  HP: {c2.current_hp}/{c2._max_hp} {StatusBar(c2.current_hp, c2._max_hp)}
"""
    print(status)
    input(">>> Attack")
    
    # Choose Character Action
    #   Attack
    succesful_atk = other_character.defend(current_character._atk)

    if succesful_atk:
        print(f"{current_character.name} attacked {other_character.name}")
    else:
        print(f"{current_character.name} missed!")

    # After Turn Text
    print("")

    # Swap Characters
    temp = current_character
    current_character = other_character
    other_character = temp

    # Update turn number
    turn_number += 1

# Check Battle Results
status = f"""Battle Turn #{turn_number}
{c1.name}  HP: {c1.current_hp}/{c1._max_hp} {StatusBar(c1.current_hp, c1._max_hp)}
{c2.name}  HP: {c2.current_hp}/{c2._max_hp} {StatusBar(c2.current_hp, c2._max_hp)}
"""
print(status)

# Winner
if c1.is_alive:
    print(f"{c1.name} has won the battle!")

else:
    print(f"{c2.name} has won the battle!")






