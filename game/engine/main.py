import os

from utils.file_handler import load_json, save_json

"""
Planning


[Flow]
Intro Screen
Main Menu
Overworld
    Pause Menu
    Player Menu
    Inventory Menu
    Save Menu

    Actions
        Explore
            Battle
                Farm Monsters Materials
                Experience
                
            Find Materials
                Farm Plants/Trees/Seeds/Resources
                Mine Ore
            
            Find Treasure
                Keys
                Weapons
                Armor
            * Build maps to have quick access to all the hotspots



[Features]
    [level up]
        Overworld
            mapping
                perception: find hidden spots/items; see hidden enemies/ambushes
                  
    
        [Damage Types]
            Severing - gets boost from
                attack
                speed
            Blunt - gets boost from
                defense
                speed
            Impact - gets boost from
                attack
                defense
                speed
            Slice
                Speed
                Accuracy
                Attack
        
        [Magic]
            Elemental
                element[ fire|water|air|earth|electric ]
            
            Modifiers
                Speed
                Power
                Duration



              s  p  d  
            s ss sp ds
            p ps pp pd
            d ds dp dd

            embers - starting
            ball - default ?:?:?
            charge - Duration>Power>Speed 2:1:1
            stream/thrower - Duration>Speed>Power 4:2:1
            blast - Power>Speed>Duration 4:2:1
            beam - Power>Duration>Speed 4:2:1
            shot - Speed>Power>Duration 4:2:1
            boom - Speed>Duration>Power 4:2:1

            s:p:d            
            start 1:1:1

            by default can only use 
            fireball

            on lvl up +1

            2:1:1 shot
            1:2:1 blast
            1:1:2 charge

            
            power
            flow rate
            hold/duration



            physical
            punch/kick/headbutt/charge/tackle
            slash/slice/cleave/stab/draw/
                
                punch>jab>pistol
                kick> 

            projectile
            shot/ball/blast/
            stream/thrower/beam/

                
            start - elemental(a small spattering of {element}) - embers/bubbles/leafs/dusts

            ball
            blast
            
            shot
            boom
            
            stream
            beam
            
            charge

            
            ball
                blast/charge - power
                stream/beam - duration/stamina
                shot/boom - speed

            fire>flame>magma>solar>nova/star
            
            water>hydro>river>ocean>lunar
            
            air>turbulent>cyclonic>vacumn
            
            earth>boulder>mountain>tectonic>planetary


        [Elements]
            Fire>Exploding>Solar>nova/star
            Water>hydro>oceanic>lunar
            Earth>tectonic>planetary
            Air>wind>cyclonic>vacumn

            Steam (Fire + Water)
            Magma (Fire + Earth)
            Electric (Fire + Air)

            Mud (Water + Earth)
            Ice (Water + Air)

            Sand (Earth + Air)
        
        [Attack Types]
            Physical/enhance
                body
                    punch>jab>pistol
                    kick>Jump Kick|Round Kick
                    Tackle>Charge
                Weapon
                    Slash/Slice/Cleave/
                    poke/pierce
                    hit/smash/

            Projectile
                ball
                    blast/charge - power
                    stream/beam - duration/stamina
                    shot/boom - speed

                



"""


class Screen:
    DEFAULT_CHAR = "*"
    def __init__(self, width: int=8, height: int=4, data=None):
        self.width = width
        self.height = height

        self.data = data if data is not None else self.generate_data(self.DEFAULT_CHAR)

    def __str__(self):
        s = f'w:{self.width}  h:{self.height}'
        return s
    
    def generate_data(self, data: str=None):
        return [[data for i in self.width] for j in self.height]
    
    def update_pixel(self, x: int, y: int, new_data: str):
        self.data[y][x] = new_data

    def refresh(self):
        return
    
    def display(self):
        print(self)


class Scene:
    def __init__(self, name: str, data=None):
        self.name = name

        self.height = 0
        self.width = 0
        self.data = data
        
        self.analyze()

    def __str__(self):
        s = f'{self.name}'
        return s
    
    def analyze(self):
        if self.data is None:
            return
        
        first = self.data[0]
        self.width = 0 if first is None else len(first[0])
        self.height = len(first)
    
    def draw(self, screen, start_x: int=0, start_y: int=0):
        s_x = screen.width - start_x
        s_y = screen.height - start_y

        min_x = min(s_x, self.width)
        min_y = min(s_y, self.height)

        for j in range(min_y):
            for i in range(min_x):
                screen.update_pixel(start_x + i, start_y + j, self.data[j][i])

    def export(self):
        return self.data


def main():
    CHARACTER = {
        'name': 'Hero',
        'level': 1,
        'experience': 0,
        'stats': {    
            'health': 20,
            'mana': 10,
            'attack': 5,
            'defense': 5,
            'speed': 5,
        },
        'inventory': {
            'key_items': [],
            'consumables': [],
            'general': []
        },
        'equipment': {
            'head': None,
            'body': None,
            'l_arm': None,
            'r_arm': None,
            'boots': None,
        },
        'skills': [],
    }
    ENEMY = {
        'name': 'Bunny',
        'level': 1,
        'stats': {    
            'health': 20,
            'mana': 10,
            'attack': 5,
            'defense': 5,
            'speed': 5,
        },
        'equipment': {
            'head': None,
            'body': None,
            'l_arm': None,
            'r_arm': None,
            'boots': None,
        },
        'skills': [],
    }

    GAME_TITLE = "New Game"
    width, height = os.get_terminal_size()
    # print(f"{height=}\n{width=}")


    # Title Screen
    TITLE_SCREEN_STR = f"""{'-'*width}
{GAME_TITLE:^{width}}
{'-'*width}
{'\n'*(height-6)}
"""
    print(TITLE_SCREEN_STR)
    input('')


    # Main Menu
    # Game Loop
    while True:
        os.system('cls')
        user_input = input(">>> ")

        if user_input == 'q':
            break



    #     Pause Menu
    #     Actions
    #         Menus
    #             Inventory
    #             Player
    #             Notes
    #             Save
    #             Settings
    #         Farm - Found zones, saved by player while exploring
    #             Get Resources/Materials
    #             Upgradable!

    #         Explore - Overworld, Dungeons, Castles, Ruins, Ships, Crashes, Abandoned places
    #             Battle
    #                 Farm Monsters Materials
    #                 Experience
                    
    #             Find Materials/locations
    #                 Farm Plants/Trees/Seeds/Resources
    #                 Mine Ore
                
    #             Find Treasure
    #                 Keys
    #                 Weapons
    #                 Armor
    #             * Build maps to have quick access to all the hotspots/farms



if __name__ == "__main__":
    main()
