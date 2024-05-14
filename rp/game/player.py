from utils.progress_bar import prog_bar


HP_BAR_CONFIG = {
    "fill": "*",
    "space": " ",
    "side": '|'
}
MANA_BAR_CONFIG = {
    "fill": "-",
    "space": " ",
    "side": '|'
}
XP_BAR_CONFIG = {
    "fill": "=",
    "space": " ",
    "side": '|'
}

class Player:
    def __init__(self, name: str, starting_experience: int=0, *args, **attrs):
        self.name = name
        self.job = attrs.get('job', None)
        
        # Level
        self.level = 1
        self.max_level = 100
        self.experience = 0
        self.experience_to_next_level = 100

        # Attributes
        self.hp = attrs.get('hp', None)
        self.max_hp = attrs.get('max_hp', None)
        self.mana = attrs.get('mana', 20)
        self.max_mana = attrs.get('max_mana', 20)

        self.atk = attrs.get('atk', None)
        self.res = attrs.get('res', None)
        self.sp_atk = attrs.get('sp_atk', None)
        self.sp_res = attrs.get('sp_res', None)
        self.spd = attrs.get('spd', None)


        # Items
        self.items = [*attrs.get('items', list())]

        # Equipment
        self.equipment = {
            "head": None,
            "body": None,
            "left_arm": None,
            "right_arm": None,
            "boots": None,
            "neck": None,
            "accessory_1": None,
            "accessory_2": None
        }

        # Update initial equipment
        self.equipment = {**self.equipment, **attrs.get('equipment', dict())}

        # Spells
        self.spells = [{
            "element": "water",
            "name": "bubble",
            "description": "fires a group of bubbles",
            "power": 10,
            "level": 1,
            "experience": 0,
            "exp_per_usage": 20,
            "exp_to_level": 100
        }]

        # Skills
        self.skills = [{
            "name": "Hero's Journey",
            "infite_growth": "you can't stop growing"
        }]

        # Status
        self.is_alive = True

        self.add_experience(starting_experience)

    def __str__(self):

        txt = f"""lvl {self.level:02}  {self.name}
HP{prog_bar(self.hp, self.max_hp, config=HP_BAR_CONFIG)} {self.hp}/{self.max_hp}
MP{prog_bar(self.mana, self.max_mana, config=MANA_BAR_CONFIG)} {self.mana}/{self.max_mana}
  {prog_bar((100 - self.experience_to_next_level), 100, config=XP_BAR_CONFIG)} {100 - self.experience_to_next_level}/100 EXP"""
        return txt
    
    def add_experience(self, experience_points: int):
        self.experience += experience_points
        self.experience_to_next_level -= experience_points
        
        # Max Level
        if self.level >= self.max_level:
            return
        
        # Exp not enough to level
        if self.experience_to_next_level > 0:
            return
        
        # Exp enough to level
        self.level_up()

        # Exp enough to level more than once
        if self.experience_to_next_level < 0:
            self.add_experience(-self.experience_to_next_level)


    def level_up(self, leftover_exp: int=0, functions=None):
        self.level += 1
        self.experience_to_next_level = 100  # int(self.starting_exp * (self.growth_curve)**(self.level))
        
        self.experience = leftover_exp
        print(f"""
{self.name} Leveled Up!!!
Level: {self.level}
HP: {self.max_hp}
Mana: {self.max_mana}
Attack: {self.atk}
Defense: {self.res}
Sp. Attack: {self.sp_atk}
Sp. Defense: {self.sp_res}
Speed: {self.spd}
Total Experience: {self.experience}
""")
        input("")


    def export(self):
        return {
        "name": self.name,
        "job": self.job,
        "starting_experience": self.experience,
        "hp": self.hp,
        "max_hp": self.max_hp,
        "mana": self.mana,
        "max_mana": self.max_mana,
        "atk": self.atk,
        "res": self.res,
        "sp_atk": self.sp_atk,
        "sp_res": self.sp_res,
        "spd": self.spd
    }


class Enemy(Player):
    def __init__(self, name: str, starting_experience: int = 0, reward_value: int=10, **attrs):
        super().__init__(name, starting_experience, **attrs)
        self.reward_value = reward_value
        self.action_turn = 0
        self.actions = [self.attack, self.defend]

    def __str__(self):
        txt = f"""lvl {self.level:02}  {self.name}
HP{prog_bar(self.hp, self.max_hp, config=HP_BAR_CONFIG)} {self.hp}/{self.max_hp}
"""
        return txt
    
    def act(self, enemy):
        self.actions[self.action_turn%len(self.actions)](enemy)
        self.action_turn += 1
        return 
    
    def attack(self, enemy):
        return (self.atk - enemy.res, 0)
    
    def defend(self, enemy):
        return (0, self.res)
    

