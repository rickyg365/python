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

class Character:
    def __init__(self, name: str, starting_experience: int=0, max_hp: int=0, hp: int=0, atk: int=0, res: int=0, spd: int=0, items=None, equipment=None):
        self.name = name
        
        # Level
        self.level = 0
        self.max_level = 100
        self.experience = 0
        self.total_experience = 0
        self.experience_to_next_level = 0

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

        self.add_experience(starting_experience)

    def __str__(self):

        txt = f"""lvl {self.level:02}  {self.name}
HP{prog_bar(self.hp, self.max_hp, config=HP_BAR_CONFIG)} {self.hp}/{self.max_hp}
MP{prog_bar(self.mana, self.max_mana, config=MANA_BAR_CONFIG)} {self.mana}/{self.max_mana}
  {prog_bar(self.experience, self.experience_to_next_level, config=XP_BAR_CONFIG)} {self.experience}/{self.experience_to_next_level} EXP"""
        return txt
    
    def add_experience(self, experience_points: int):
        self.experience += experience_points
        self.total_experience += experience_points
        
        # Max Level
        if self.level >= self.max_level:
            return
        
        # Exp not enough to level
        if self.experience < self.experience_to_next_level:
            return
        
        # Exp enough to level
        leftover_exp = self.experience - self.experience_to_next_level 
        self.level_up()

        # Exp enough to level more than once
        if leftover_exp > 0:
            self.add_experience(leftover_exp)


    def level_up(self, leftover_exp: int=0, functions=None):
        self.level += 1
        self.experience_to_next_level = 100  # int(self.starting_exp * (self.growth_curve)**(self.level))
        
        self.experience = leftover_exp
        print(f"""
{self.name} Leveled Up!!!
Level: {self.level}
HP: {self.max_hp}
Attack: {self.atk}
Defense: {self.res}
Speed: {self.spd}
Total Experience: {self.total_experience}
""")
        input("")


    def export(self):
        return {
        "name": self.name,
        "starting_experience": self.total_experience,
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
    

