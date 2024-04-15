from typing import List, Any
from game.character import Character, Enemy

def Battle(hero: Character, combatants: List[Enemy]):
    while True:
        # Check Status of enemies
        updated_combatants = []
        for combatant in combatants:
            # Alive
            if combatant.hp > 0:
                updated_combatants.append(combatant)
            # Dead
            else:
                # Hasn't been marked dead
                if combatant.is_alive:
                    combatant.is_alive = False
                    hero.level_sys.add_experience(combatant.reward_value)
        combatants = updated_combatants
        
        # Create Display
        enemies = '\n'.join(f'{e}' for e in combatants)
        text = f"""
Enemies:
{enemies}

{hero}
"""
        # Display
        print(text)
        
        # Break if all enemies defeated
        if len(combatants) == 0: break
        
        user_input = input("[  (a)ttack | (d)efend | (i)tems | (r)un  ]\n>>> ")

        enemy_dmg = sum([x.atk - hero.res for x in combatants])

        match user_input:
            case 'a':
                e = combatants[-1]
                e.hp -= (hero.atk - e.res)
            case 'd':
                enemy_dmg -= hero.res
            case 'i':
                print("Not implemented yet!")
            case 'q':
                break
            case _:
                # for combatant in combatants:
                #     combatant.hp -= 1
                pass
        
        # Enemy Attack
        hero.hp -= min(enemy_dmg, 0)


