import os
from utils.file_handle import load_json, save_json
from utils.character import Character, Item, Skill





def generate_sample_data(save_dir: str=""):
    ITEMS = []
    SKILLS = []

    for _ in range(5):
        new_item = Item(name=f'Item #{_}')
        ITEMS.append(new_item)

    for _ in range(5):
        new_skill = Skill(name=f'Skill #{_}', description=f'This is the description of skill #{_}')
        SKILLS.append(new_skill)

    # Create dir if doesnt exist

    save_json([i.export() for i in ITEMS], f'{save_dir + "/"}items.json')
    save_json([s.export() for s in SKILLS], f'{save_dir + "/"}skills.json')


if __name__ == "__main__":
    hero_sample_data = {
        'name': 'Hero',
        'hp': 20,
        'attack': 8,
        'defense': 6,
        'speed': 7
    }
    enemy_sample_data = {
        'name': 'Goblin',
        'hp': 15,
        'attack': 6,
        'defense': 5,
        'speed': 5
    }

    CHARACTER_PATH = 'data/character.json'

    # Battle
    # Characters
    new_character = Character(**hero_sample_data)
    if os.path.exists(CHARACTER_PATH):
        new_character = Character(filename=CHARACTER_PATH)
    enemy = Character(**enemy_sample_data)

    # User Options
    def user_turn():
        actions = "| a)ttack | d)efend | e)vade | s)kill | i)tem |"

        bar = f"""{'-'*(len(actions))}
{actions}
{'-'*(len(actions))}
"""

        user_input = input(f'{bar}>>> ')
        match user_input:
            case 'a':
                # Attack
                dmg_dealt = new_character.hit(enemy)
                enemy.take_damage(dmg_dealt)

                print(f"{new_character.name} hit for {dmg_dealt}dmg...")
                
            case 'd':
                # Defend
                new_character.defend()
                
            case 'e':        
                # Evade
                new_character.evade()
                
            case 's':        
                # Skill
                skill_display = "\n".join([f"{s}" for s in new_character.skills])
                print(skill_display)

                new_character.use_skill()

            case 'i':
                # Item
                pass

    # Enemy Option
    def enemy_turn():
        if enemy.current_hp >= enemy.hp/2:
            dmg = enemy.hit(new_character)
            new_character.take_damage(dmg)
            print(f"{enemy.name} hit for {dmg}dmg...")
        else:
            if enemy.speed > enemy.defense:
                enemy.evade()
                print(f"{enemy.name} is ready to evade.")
            else:
                enemy.defend()
                print(f"{enemy.name} is defending.")

    # Handle Turn order
    turn_order = [user_turn, enemy_turn]
    if enemy.speed > new_character.speed:
        turn_order = [enemy_turn, user_turn]

################################################################
    # Main loop
    while True:
        # Display
        display = f"""{enemy.enemy_display()}

{new_character}"""
        print(display)

        # Check win
        if not enemy.is_alive:
            prev_level = new_character.exp.level
            new_character.exp.add_experience(30)
            print("+30 EXP")
            if new_character.exp.level > prev_level:
                print("Leveled Up!")

            print("Hero Wins!!!")
            print(new_character.show_status())
            break

        if not new_character.is_alive:
            print("Game Over!")
            break

        # Handle Turns
        for play_turn in turn_order:
            play_turn()

    # Save Character
    char_data = new_character.export()
    save_json(char_data, "data/character.json")

    # Overworld (Exploration/Farming/)
    # Use items
    # Check status
    # Choose path


    # Start with rogue like make into full rpg













