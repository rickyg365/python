from dataclasses import dataclass, Field

@dataclass
class Skill:
    name: str
    description: str

    required_level: int=1

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





