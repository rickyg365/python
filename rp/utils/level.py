import os
from utils.progress_bar import prog_bar


class LevelSystem:
    def __init__(self, starting_experience: int=0, config=None):
        if config is None:
            config = {
                "max_level": 100,
                "experience_between": 100,
                "growth_curve": 1.1
            }
        self.level = 1
        self.max_level = config.get('max_level', 0)
        self.experience = 0
        self.total_experience = 0
        self.experience_to_next_level = config.get("experience_between", 0)
        self.starting_exp = config.get("experience_between", 0)

        self.growth_curve = config.get('growth_curve')
        self.config = config

        if starting_experience > 0:
            self.add_experience(starting_experience)

    def __str__(self):
        txt = f"lvl {self.level:<2} {prog_bar(self.experience, self.experience_to_next_level, 20)} {self.experience:>3}/{self.experience_to_next_level:<3} EXP"
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
        self.experience_to_next_level = int(self.starting_exp * (self.growth_curve)**(self.level))
        
        self.experience = leftover_exp

    def export(self):
        return {
            "experience": self.total_experience
        }
        

def main():
    default_config = {
                "max_level": 100,
                "experience_between": 100,
                "growth_curve": 1.1
            }
    
    l1 = LevelSystem(config=default_config)
    l2 = LevelSystem(100)
    l3 = LevelSystem(200)


    print(f"""
{l1}
{l2}
{l3}
""")
    return

if __name__ == "__main__":
    main()