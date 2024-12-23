from typing import List, Dict, Callable

from utils.menu import Menu, MenuOption
from utils.screen import clear_screen

from game_engine.character import Character, Enemy
from game_engine.item import Item, Consumable, Equipment, Inventory

'''


'''


POTION_DATA = {
    'key': 'ttrrppid',
    'name': 'Potion',
    'item_type': 'consumable',
    'description': 'Heals a small amount of health.',
    'attributes': {
        'health': 10
    },
}

WOODEN_SWORD = {
    'key': 'ttrrppid',
    'name': 'Wooden Sword',
    'item_type': 'weapon',
    'description': 'A small wooden sword',
    'attributes': {
        'attack': 10,
        'critical_chance': 2
    },   
}

WOODEN_SHIELD = {
    'key': 'ttrrppid',
    'name': 'Wooden Shield',
    'item_type': 'equipment',
    'description': 'A small wooden shield',  # be careful not to get a splinter.
    'attributes': {
        'defense': 8,
        'block_chance': 10
    },
}




class Game:
    STARTING_HERO_DATA = {
        'name': 'Hero',
        'health': 20,
        'attack': 20,
        'defense': 20,
        'speed': 20,
    }
    def __init__(self, filename: str='default_appdata.json'):
        self.filename = filename
        self.player = Character(**self.STARTING_HERO_DATA)
        self.enemies = []
        self.current_enemies = []

        # Add starting items
        self.player.equip('left_arm', Equipment(**WOODEN_SWORD))
        self.player.equip('right_arm', Equipment(**WOODEN_SHIELD))

        self.player.inventory.add_multiple(Consumable(**POTION_DATA), 5)


    def __str__(self):
        s = f'{self.filename}'
        return s
    
    def attack_menu(self):
        print('\n'.join([f'{e}' for e in self.current_enemies]))
        idx = input(">>> ")
        current_enemy = self.current_enemies[idx]
        dmg_dealt = self.player.hit(current_enemy)
        current_enemy.take_damage(dmg_dealt)

        print(f"{self.player.name} hit for {dmg_dealt}dmg...")


    def skill_menu(self):
        input("use skill")
        # skill_display = "\n".join([f"{s}" for s in self.player.skills])
        # if skill_display == "":
        #     skill_display = "No Skills Available"
        # print(skill_display)

        self.player.use_skill()
        return
    
    def item_menu(self):
        items = []

        for _, i in enumerate(self.player.inventory.data):
            k = _
            txt = i.name
            action = lambda : i.use(self.player)

            new_option = MenuOption(
                key=k,
                display_text=txt,
                action=action
            )
            items.append(new_option)
        
        i_menu = Menu('Item Menu', items)
        i_menu.run()
        
        return
    
    def status(self):
        input(self.player.show_status())
    
    def scout(self):
        input('scouting...')
        return
    
    def explore_skill_menu(self):
        
        explore_skills_menu = Menu('Explore Skills')
        explore_skills_menu.run()
    
    def overworld_skill_menu(self):
        
        overworld_skill_menu = Menu('Overworld Skills')
        overworld_skill_menu.run()
    
        return
    
    def travel_menu(self):
        
        travel_menu = Menu('Travel Menu')
        travel_menu.run()
    
        return
    
    def enemy_turn(self, current_enemy: Character):
        def turn_function():
            if current_enemy.current_health >= current_enemy.health/3:
                dmg = current_enemy.hit(self.player)
                self.player.take_damage(dmg)
                print(f"{current_enemy.name} hit for {dmg}dmg...")
            else:
                if current_enemy.speed > self.player.speed:
                    current_enemy.evade()
                    print(f"{current_enemy.name} is ready to evade.")
                else:
                    current_enemy.defend()
                    print(f"{current_enemy.name} is defending.")

        return turn_function

    def hero_turn(self):
        # Display
        menu_options = [
            MenuOption(
                key='a',
                display_text='Attack',
                action=self.attack_menu
            ),
            MenuOption(
                key='s',
                display_text='Skill',
                action=self.skill_menu
            ),
            MenuOption(
                key='i',
                display_text='Item',
                action=self.item_menu
            ),
            MenuOption(
                key='d',
                display_text='Defend',
                action=self.player.defend
            ),
            MenuOption(
                key='e',
                display_text='Evade',
                action=self.player.evade
            ),
        ]

        battle_menu = Menu('Player Attack Menu', menu_options, clear=False)
        battle_menu.run()
        
    def battle(self, enemy: Enemy):
        enemy_turn_function = self.enemy_turn(enemy)
        hero_turn_function = self.hero_turn
  

        turn_order = [hero_turn_function, enemy_turn_function]
        if enemy.speed > self.player.speed:
            turn_order = [enemy_turn_function, hero_turn_function]

        while True:
            # Display
            display = f"""{enemy}

{self.player}"""

            # Clear Display
            clear_screen()

            # Show Display
            print(display)
            # print(text_box(display))

            # Check win
            if not enemy.is_alive:
                # Add Exp
                self.player.parse_reward(enemy.drop_reward())
                # self.player.add_experience(50)

                print("Hero Wins!!!")
                # print(self.player.show_status())

                enemy.revive()
                input("")
                break

            if not self.player.is_alive:
                print("Game Over!")
                # Reset Hero
                self.player.revive()
                enemy.revive()
                break

            # Handle Turns
            for play_turn in turn_order:
                play_turn()

            input("")

    
    def explore_menu(self):
        '''
        Battle
        Scout
        Item
        Skill
        Status
        '''
        enemies = [Enemy(name="goblin", health=20)]
        run_battle = lambda : self.battle(enemies[0])
        menu_options = [
            MenuOption(
                key='b',
                display_text='Battle',
                action=run_battle
            ),
            MenuOption(
                key='sc',
                display_text='Scout',
                action=self.scout
            ),
            MenuOption(
                key='i',
                display_text='Item',
                action=self.item_menu
            ),
            MenuOption(
                key='s',
                display_text='Skill',
                action=self.explore_skill_menu
            ),
            MenuOption(
                key='stat',
                display_text='Status',
                action=self.status
            ),
        ]

        explore_menu = Menu('Exploration', menu_options)
        explore_menu.run()
        return
    
    def overworld_menu(self):
        '''
        Explore
        Item
        Skill
        Travel
        '''
        menu_options = [
            MenuOption(
                key='e',
                display_text='Explore',
                action=self.explore_menu
            ),
            MenuOption(
                key='i',
                display_text='Item',
                action=self.item_menu
            ),
            MenuOption(
                key='s',
                display_text='Skill',
                action=self.overworld_skill_menu
            ),
            MenuOption(
                key='t',
                display_text='Travel',
                action=self.travel_menu
            ),
        ]

        over_menu = Menu('Overworld', menu_options)
        over_menu.run()

        return
    
    def load_menu(self):
        # Read save files
        # Make each save file into menu option
        # Create menu
        # run
        return
    
    def run(self):
        clear_screen()
        title_screen = f"""Press Enter to start game"""
        input(title_screen)
        
        while True:
            clear_screen()
            options = f"""Title Screen
___________________
s)tart Game
l)oad Game
q)uit

>>> """
            u_in = input(options)

            match u_in:
                case 'q':
                    break
                case 's':
                    self.overworld_menu()
                case 'l':
                    self.load_menu()
                case _:
                    pass
    


if __name__ == "__main__":

    g = Game()
    g.run()


