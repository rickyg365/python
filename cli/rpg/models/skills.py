from engine.exp_system import ExperienceSystem


class Skill(ExperienceSystem):
    def __init__(self, name: str, description: str, required_level: int=1, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.description = description

        self.required_level = required_level

    def __str__(self):
        txt = f"{self.name}: {self.description}"
        return txt
    
    def activate(self):
        return
    
    def export(self):
        return {
            'name': self.name,
            'description': self.description,
            'required_level': self.required_level
        }


if __name__ == "__main__":
    new_skill = Skill(name='Skill #1', description='This is the description of skill #1')
    
    print(new_skill)
    print(new_skill.export())





