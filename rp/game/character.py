from utils.level import LevelSystem
from utils.progress_bar import prog_bar


class Character:
    def __init__(self, name: str, starting_experience: int=0, max_hp: int=0, hp: int=0, atk: int=0, res: int=0, spd: int=0, items=None, equipment=None):
        self.name = name
        self.level_sys = LevelSystem(starting_experience)  # Level 0 uninitiated level 1 initiated
        
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

        # Status
        self.is_alive = True



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
        xp_bar_config = {
            "fill": "=",
            "space": " ",
            "side": '|'
        }

        txt = f"""lvl {self.level_sys.level:02}  {self.name}
HP{prog_bar(self.hp, self.max_hp, config=hp_bar_config)} {self.hp}/{self.max_hp}
MP{prog_bar(self.mana, self.max_mana, config=mana_bar_config)} {self.mana}/{self.max_mana}
  {prog_bar(self.level_sys.experience, self.level_sys.experience_to_next_level, config=xp_bar_config)} {self.level_sys.experience}/{self.level_sys.experience_to_next_level} EXP"""
        return txt

    def export(self):
        return {
        "name": self.name,
        "starting_experience": self.level_sys.total_experience,
        "max_hp": self.max_hp,
        "hp": self.hp,
        "atk": self.atk,
        "res": self.res,
        "spd": self.spd
    }


class Enemy(Character):
    def __init__(self, name: str, starting_experience: int = 0, max_hp: int = 0, hp: int = 0, atk: int = 0, res: int = 0, spd: int = 0, items=None, equipment=None, reward_value: int=10):
        super().__init__(name, starting_experience, max_hp, hp, atk, res, spd, items, equipment)
        self.reward_value = reward_value

    def __str__(self):
        hp_bar_config = {
            "fill": "*",
            "space": " ",
            "side": '|'
        }

        txt = f"""lvl {self.level_sys.level:02}  {self.name}
HP{prog_bar(self.hp, self.max_hp, config=hp_bar_config)} {self.hp}/{self.max_hp}
"""
        return txt