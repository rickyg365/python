import os
from ui_elements import status_bar, StatusbarConfig
"""
Goals:
    Handle Stats/Attributes
    Handle Leveling
    Handle Battles
    Handle Inventory
    Handle Equipment
    Export
"""
SAMPLE_CHARACTER_DATA = {
    'name': 'Hero',
    'level': 1,
    'health': 20,
    'attack': 5,
    'defense': 5,
    'speed': 5,
    'experience': 0
}


class Character:
    def __init__(self, name: str, level: int=0, experience: int=0, health: int=0, current_health: int=None, attack: int=0, defense: int=0, speed: int=0):
        self.name = name

        # Battle Attributes
        self.level = level
        self.experience = experience

        self.health = health
        self.current_health = health if current_health is None else current_health

        self.attack = attack
        self.defense = defense
        self.speed = speed

    def __str__(self):
        # Create bars
        custom_config = {
            'fill': '*',
            'left': '(',
            'right': ')'
        }

        exp_config = {
            'fill': '-',
            'left': '|',
            'right': '|'
        }

        hp_bar = status_bar(self.current_health, self.health, config=StatusbarConfig(**custom_config))
        exp_bar = status_bar(self.experience, (100 - self.experience), config=StatusbarConfig(**exp_config))
        # mp_bar = status_bar(20, 30, config=StatusbarConfig(**custom_config))
        

        # Create Final
        s = f'''lvl.{self.level:02} {self.name}
HP: {self.current_health:>3}/{self.health:<3} {hp_bar}
EP: {self.experience:>3}/{100-self.experience:<3} {exp_bar}
'''
        return s











if __name__ == "__main__":
    c = Character(**SAMPLE_CHARACTER_DATA)
    print(c)
