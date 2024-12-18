
class ExperienceSystem:
    def __init__(self, level: int=1, experience: int=0, experience_to_level: int=100, total_experience: int=0, **kwargs):
        self.level = level
        self.experience = experience
        self.experience_to_level = experience_to_level
        self.total_experience = total_experience

    def __str__(self):
        FILL = '*'
        SPACE = ' '
        L_END = '['
        R_END = ']'

        bar_display_width = 20
        ratio = self.experience/self.experience_to_level

        fill_val = int(ratio * bar_display_width)
        space_val = bar_display_width - fill_val

        return f"LVL{self.level:>2} {L_END}{fill_val * FILL}{space_val * SPACE}{R_END} {self.experience:>2}/{self.experience_to_level}"
    
    def level_str(self):
        FILL = '*'
        SPACE = ' '
        L_END = '['
        R_END = ']'

        bar_display_width = 20
        ratio = self.experience/self.experience_to_level

        fill_val = int(ratio * bar_display_width)
        space_val = bar_display_width - fill_val

        return f"LVL{self.level:>2} {L_END}{fill_val * FILL}{space_val * SPACE}{R_END} {self.experience:>2}/{self.experience_to_level}"
    
    def _level_up(self):
        self.experience_to_level = 100
        self.experience = 0

        self.level += 1

    def _add_experience(self, amount: int):
        self.experience = self.experience + amount
        conj = self.experience_to_level - self.experience

        if conj == 0:
            self._level_up()

        if conj < 0:
            self._level_up()
            self._add_experience(abs(conj))

    def level_data(self):
        """ Experience System Data

        level : int
        experience : int
        experience_to_level : int
        total_experience : int
        """
        return {
            'level': self.level,
            'experience': self.experience,
            'experience_to_level': self.experience_to_level,
            'total_experience': self.total_experience
        }


    def export(self):
        """ Experience System Export

        Returns::

            level : int
            experience : int
            experience_to_level : int
            total_experience : int
        """
        return {
            'level': self.level,
            'experience': self.experience,
            'experience_to_level': self.experience_to_level,
            'total_experience': self.total_experience
        }


if __name__ == "__main__":
    exp = ExperienceSystem()

    while True:
        # Display
        print(exp)

        # User Input
        u_in = input(">>> ")

        if u_in == 'q':
            break
        
        # Update
        exp.add_experience(20)
