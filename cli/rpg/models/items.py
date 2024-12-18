from dataclasses import dataclass, Field

@dataclass
class Item:
    name: str

    def __str__(self):
        txt = f"{self.name}"
        return txt
    
    def use(self):
        return
    
    def export(self):
        return {
            'name': self.name
        }


if __name__ == "__main__":
    new_item = Item(name='Item #1')

    print(new_item)
    print(new_item.export())

