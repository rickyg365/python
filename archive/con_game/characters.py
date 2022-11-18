from utils.ascii_bar import create_bar
from data.types.status import StatusCondition
""" 
MainPlayer lvl.3 - burn
HP: 15/20 [#########_____]
"""

class Character:
    def __init__(self, name: str, level: int, hp: int, attack: int, resistance: int, speed: int, status_condition: StatusCondition = ""):
        # self.id = 0, maybe for npc subclass
        self.name = name
        self.level = level

        self.status = status_condition

        self.total_hp, self.current_hp = hp, hp
        self.atk = attack
        self.res = resistance
        self.spd = speed

        self.fainted = False

    def __str__(self) -> str:
        """ """
        # Components
        hp_bar = create_bar(self.current_hp, self.total_hp)  # from utils.ascii_bar
        status_txt = "" if self.status == "" else f" - {self.status.value}"

        # Build Final Display
        line_1 = f"\n{self.name.title()} lvl.{self.level}{status_txt}"
        line_2 = f"\nHP: {self.current_hp}/{self.total_hp} {hp_bar}"

        txt = f"{line_1}{line_2}\n"
        return txt
    
    def update_fainted(self):
        """ Updates and returns fainted status based on current hp """
        if self.current_hp <= 0:
            self.current_hp = 0  # hp cant be negative
            self.fainted = True
    
    def take_damage(self, enemy_attack: int):
        dmg_taken = enemy_attack - self.res

        if dmg_taken > 0:
            self.current_hp -= dmg_taken
            # Check if hp is less than 0, if char is donezo
            self.update_fainted()

            if self.fainted:
                return self.total_hp - (self.current_hp+dmg_taken)

        return dmg_taken
    
    def heal(self, heal_amount: int):
        self.current_hp += heal_amount
        healed_for = heal_amount

        if self.current_hp > self.total_hp:
            healed_for = self.total_hp - (self.current_hp - heal_amount)
            self.current_hp = self.total_hp

        return healed_for


def main():
    # Load Test Data
    with open("data/test/characters.json", 'r') as in_data:
        new_data = json.load(in_data)

    hero_data, enemy_data = new_data

    hero = Character(**hero_data)
    enemy = Character(**enemy_data)

    print(hero)
    print(enemy)
    

if __name__ == '__main__':
    import json

    main()
