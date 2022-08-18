import os
from dataclasses import dataclass


@dataclass
class Pokemon:
    id: int
    name: str
    type: str=None

    def __str__(self):
        txt = f"[{self.id:03}] {self.name}"
        return txt


def main():
    fake_poke_data = {
            "id": 42,
            "name": "Fakemon",
            "type": "normal"
            }

    new_pokemon = Pokemon(**fake_poke_data)

    print(new_pokemon)


if __name__ == '__main__':
    main()

