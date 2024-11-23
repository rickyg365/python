from utils.file_handle import load_json, save_json
from utils.character import Character, Item, Skill


if __name__ == "__main__":
    new_item = Item(name='Item #1')
    new_skill = Skill(name='Skill #1', description='This is the description of skill #1')

    print(new_item)
    print(new_skill)
    
    # new_item.export()
    # new_skill.export()

    items = [new_item]
    skills = [new_skill]

    save_json([i.export() for i in items], 'data/items.json')
    save_json([s.export() for s in skills], 'data/skills.json')

    # Character
    new_character = Character(name="Hero")
    
    print(new_character)

    # Battle
    enemy = Character('Goblin')

    # Handle Turn order

    # User Options
    # Attack
    new_character.attack()
    # Defend
    new_character.defend()
    # Evade
    new_character.evade()
    # Skill
    skill_display = "\n".join([f"{s}" for s in new_character.skills])
    print(skill_display)
    
    new_character.use_skill()
    # ITem
    # Enemy Option



    # Overworld (Exploration/Farming/)
    # Use items
    # Check status
    # Choose path


    # Start with rogue like make into full rpg













