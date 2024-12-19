
import os

from typing import List

from models.items import Item
from models.skills import Skill
from models.character import Character, Enemy


from utils.ui_elements import text_box
from utils.file_handle import load_json, save_json




class Game:
    """
    hero can be a path: str to the location of hero data
    
    """
    def __init__(self, filename: str, hero: Character=None, enemies: List[Enemy]=None):
        self.filename = filename
        self.hero = hero
        self.enemies = enemies
        self.load_game()
    
    def __str__(self):
        return
    
    def export(self):
        return {
            'hero': self.hero.export(),
            'enemies': [e.export() for e in self.enemies],
        }
    
    def load_game(self):
        data = {
            'hero': {
                'name': 'Hero',
                'hp': 20,
                'attack': 8,
                'defense': 6,
                'speed': 7
            },
            'enemies': [
                {
                    'name': 'Goblin',
                    'hp': 15,
                    'attack': 6,
                    'defense': 5,
                    'speed': 5,
                    'exp_reward': 25,
                    'gold_reward': 5,
                }
            ]
        }
        if os.path.exists(self.filename):
            data = load_json(self.filename)

        hero_data = data.get('hero', dict())
        self.hero = Character(**hero_data)
        
        enemy_data = data.get('enemies', list())
        self.enemies = [Enemy(**e) for e in enemy_data]

        return

    def save_game(self):
        data = self.export()
        save_json(data, self.filename)
    
    def enemy_turn(self, current_enemy: Character):
        def turn_function():
            if current_enemy.current_hp >= current_enemy.hp/2:
                dmg = current_enemy.hit(self.hero)
                self.hero.take_damage(dmg)
                print(f"{current_enemy.name} hit for {dmg}dmg...")
            else:
                if current_enemy.speed < self.hero.speed:
                    current_enemy.evade()
                    print(f"{current_enemy.name} is ready to evade.")
                else:
                    current_enemy.defend()
                    print(f"{current_enemy.name} is defending.")

        return turn_function
    
    def hero_turn(self, current_enemy: Character):
        def turn():
            # Display
            actions = "(a)ttack | (s)kill | (i)tem | (d)efend | (e)vade "

    #         bar = f"""{'-'*(len(actions))}
    # {actions}
    # {'-'*(len(actions))}
    # """
            user_input = input(f'{actions}\n>>> ')
            match user_input:
                case 'a':
                    # Choose Enemy
                    
                    # Attack
                    dmg_dealt = self.hero.hit(current_enemy)
                    current_enemy.take_damage(dmg_dealt)

                    print(f"{self.hero.name} hit for {dmg_dealt}dmg...")
                    
                case 'd':
                    # Defend
                    self.hero.defend()
                    
                case 'e':        
                    # Evade
                    self.hero.evade()
                    
                case 's':        
                    # Skill
                    skill_display = "\n".join([f"{s}" for s in self.hero.skills])
                    if skill_display == "":
                        skill_display = "No Skills Available"
                    print(skill_display)

                    self.hero.use_skill()

                case 'i':
                    # Item
                    pass
        return turn

    def battle(self, enemy: Enemy):
        enemy_turn_function = self.enemy_turn(enemy)
        hero_turn_function = self.hero_turn(enemy)
        
        turn_order = [hero_turn_function, enemy_turn_function]
        if enemy.speed > self.hero.speed:
            turn_order = [enemy_turn_function, hero_turn_function]

        while True:
            # Display
            display = f"""{enemy.enemy_display()}

{self.hero}"""
            
            # Clear Display
            os.system('cls')

            # Show Display
            print(display)
            # print(text_box(display))

            # Check win
            if not enemy.is_alive:
                # Add Exp
                self.hero.parse_reward(enemy.drop_reward())
                # self.hero.add_experience(50)
                
                print("Hero Wins!!!")
                # print(self.hero.show_status())
                
                enemy.revive()
                input("")
                break

            if not self.hero.is_alive:
                print("Game Over!")
                # Reset Hero
                self.hero.revive()
                enemy.revive()
                break

            # Handle Turns
            for play_turn in turn_order:
                play_turn()
            
            input("")
        
    def run(self):
        # Load Enemies
        goblin = self.enemies[0]
        hobgoblin = self.enemies[1]
        lord_goblin = self.enemies[2]
        king_goblin = self.enemies[3]

        # Overworld (Exploration/Farming/)
        while True:
            options = f"""
i)nventory | b)attle | e)xplore | f)arm | s)ave
"""

            # Check status
            display = f"""{self.hero.show_status()}
{options}"""
            print(display)
            u_in = input(">>> ")

            match u_in:
                case 'i':
                    # Show items
                    items = '\n'.join(self.hero.inventory)
                    print(items)
                    
                    # Use items
                    input(">>> ")

                case 'b':
                    beginner = True
                    intermediate = self.hero.level > 5
                    advanced = self.hero.level >= 20
                    master = self.hero.level > 35

                    if beginner:
                        self.battle(goblin)
                    
                    if intermediate:
                        self.battle(hobgoblin)
                    
                    if advanced:
                        self.battle(lord_goblin)
                    
                    if master:
                        self.battle(king_goblin)


                case 'e':
                    # Choose path
                    pass
                case 'f':
                    pass
                case 's':                            
                    # Save
                    self.save_game()
                case 'q':
                    break
                case _:
                    beginner = True
                    intermediate = self.hero.level > 5
                    advanced = self.hero.level >= 20
                    master = self.hero.level > 35

                    if beginner:
                        self.battle(goblin)
                    
                    if intermediate:
                        self.battle(hobgoblin)
                    
                    if advanced:
                        self.battle(lord_goblin)
                    
                    if master:
                        self.battle(king_goblin)
                    pass
        return




if __name__ == "__main__":
    g = Game('new_save.json')
    g.run()

    # Start with rogue like make into full rpg




