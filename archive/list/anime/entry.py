import os

class Entry:
    def __init__(self, name: str, *other_data, **key_data):
        self.name = name
        self.data = other_data
        self.key_data = key_data
    
    def __str__(self):
        txt = f"{self.name}\n{self.data}\n{self.key_data}"
        return txt

def input_test(single: str, *other_data, **key_data):
    txt = f"{single}\n{other_data}\n{key_data}"
    print(txt)


def main():
    input_test(
        "Bob",
        1,
        2,
        3,
        "4",
        5,
        hp= 5,
        atk= 3,
        res= 4
    )


    new_entry = Entry("test")
    print(new_entry)


if __name__ == '__main__':
    main()
