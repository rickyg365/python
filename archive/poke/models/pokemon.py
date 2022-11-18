from dataclasses import dataclass


@dataclass
class Pokemon:
    id: int
    name: str
    type: str=None

    def __str__(self):
        txt = f"[{self.id:03}] {self.name.title()} [{self.type}]"
        return txt
    
    def export(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type
            }


if __name__ == '__main__':
    fake_poke_data = {
            "id": 42,
            "name": "Fakemon",
            "type": "normal"
            }

    new_pokemon = Pokemon(**fake_poke_data)

    print(new_pokemon)
