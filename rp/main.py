import os


sample_output = f"""
lvl 03  Enemy 
HP|*****            |


lvl 05  Hero
HP|************     | 24/30
MP|@@@@@@@@@@@      | 15/20

[ attack | spell | items | flee ]
>>> 

"""


def prog_bar(current_value: int, max_value: int, bar_width: int=20, config=None):
    DEFAULT_FILL = "*"
    DEFAULT_SPACE = " "
    DEFAULT_SIDE = "|"
    if config is None:
        config = {
            "fill": DEFAULT_FILL,
            "space": DEFAULT_SPACE,
            "side": DEFAULT_SIDE
        }

    ratio = current_value/max_value
    fill_width = int(ratio * bar_width)
    if current_value > 0:
        fill_width = max(fill_width, 1)

    space_width = bar_width - fill_width

    return f"{config.get('side', DEFAULT_SIDE)}{config.get('fill', DEFAULT_FILL) * fill_width}{config.get('space', DEFAULT_SPACE) * space_width}{config.get('side', DEFAULT_SIDE)}"



class Character:
    def __init__(self, name: str, level: int=0, max_hp: int=0, hp: int=0, atk: int=0, res: int=0, spd: int=0, items=None, equipment=None):
        self.name = name
        self.level = level  # Level 0 uninitiated level 1 initiated
        
        # Attributes
        self.max_hp = max_hp
        self.hp = hp
        self.atk = atk
        self.res = res
        self.spd = spd

        self.max_mana = 20
        self.mana = 20

        # Items
        self.items = items

        # Equipment
        self.equipment = equipment


    def __str__(self):
        hp_bar_config = {
            "fill": "*",
            "space": " ",
            "side": '|'
        }
        mana_bar_config = {
            "fill": "-",
            "space": " ",
            "side": '|'
        }

        txt = f"""lvl {self.level:02}  {self.name}
HP{prog_bar(self.hp, self.max_hp, config=hp_bar_config)} {self.hp}/{self.max_hp}
MP{prog_bar(self.mana, self.max_mana, config=mana_bar_config)} {self.mana}/{self.max_mana}"""
        return txt

    def method(self):
        return


class Enemy(Character):
    def __init__(self, name: str, level: int = 0, max_hp: int = 0, hp: int = 0, atk: int = 0, res: int = 0, spd: int = 0, items=None, equipment=None):
        super().__init__(name, level, max_hp, hp, atk, res, spd, items, equipment)

    def __str__(self):
        hp_bar_config = {
            "fill": "*",
            "space": " ",
            "side": '|'
        }

        txt = f"""lvl {self.level:02}  {self.name}
HP{prog_bar(self.hp, self.max_hp, config=hp_bar_config)} {self.hp}/{self.max_hp}
"""
        return txt


if __name__ == "__main__":

    # print(sample_output)

    # for _ in range(101):
    #     curr_bar = prog_bar(_, 100)
    #     print(f"{_:03}/100 {curr_bar}")

    character_data = {
        "name": "Bob Joe",
        "level": 1,
        "max_hp": 30,
        "hp": 30,
        "atk": 5,
        "res": 4,
        "spd": 5
    }
    slime_data = {
        "name": "Slime",
        "level": 1,
        "max_hp": 20,
        "hp": 20,
        "atk": 3,
        "res": 4,
        "spd": 3
    }
    zombie_data = {
        "name": "Zombie",
        "level": 1,
        "max_hp": 30,
        "hp": 30,
        "atk": 4,
        "res": 2,
        "spd": 2
    }

    c = Character(**character_data)

    enemy1 = Character(**slime_data)
    enemy2 = Character(**zombie_data)


    # Sample loop
    while c.hp >= 0 and enemy1.hp >= 0 and enemy2.hp >= 0:    
        text = f"""
    {c}

    Enemies:
    {enemy1}

    {enemy2}

    """
        print(text)
        user_input = input(">>> ")

        c.hp -= 1
        enemy1.hp -= 1
        enemy2.hp -= 1
