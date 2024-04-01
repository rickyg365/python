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
    def __init__(self, name: str, level: int, attributes=None, items=None, equipment=None):
        self.name = name
        self.level = level
        
        # Attributes
        if attributes is None:
            attributes = {
                "max_hp": 30,
                "hp": 30,
                "atk": 5,
                "res": 4,
                "spd": 5
            }
        
        self.max_hp = attributes.get('max_hp', 0)
        self.hp = attributes.get('hp', 0)
        self.atk = attributes.get('atk', 0)
        self.res = attributes.get('res', 0)
        self.spd = attributes.get('spd', 0)

        # Items
        self.items = items

        # Equipment
        self.equipment = equipment


    def __str__(self):
        txt = f"lvl {self.level:02}  {self.name}\nHP{prog_bar(self.hp, self.max_hp)} {self.hp}/{self.max_hp}"
        return txt

    def method(self):
        return


if __name__ == "__main__":

    # print(sample_output)

    # for _ in range(101):
    #     curr_bar = prog_bar(_, 100)
    #     print(f"{_:03}/100 {curr_bar}")

    character_data = {
        "name": "Bob Joe",
        "level": 1,
        "attributes": {
            "max_hp": 30,
            "hp": 30,
            "atk": 5,
            "res": 4,
            "spd": 5
            },
    }

    c = Character(**character_data)

    print(c)