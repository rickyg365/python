from dataclasses import dataclass

@dataclass
class Airport:
    name: str
    code: str

    def __str__(self) -> str:
        txt = f"[{self.code}] {self.name}"
        return txt

    def to_dict(self):
        new_dict = {
            "name": self.name,
            "code": self.code
        }
        return new_dict

def main():
    # Airport Data
    sfo_data = {
        "name": "San Francisco",
        "code": "SFO"
    }
    vancouver_data = {
        "name": "Vancouver International Airport",
        "code": "YVR"
    }

    # Airport Objects
    sfo = Airport(**sfo_data)
    yvr = Airport(**vancouver_data)

    # Display
    print(sfo)
    print(yvr)

if __name__ == '__main__':
    main()
