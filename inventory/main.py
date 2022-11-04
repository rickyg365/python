from enum import Enum

from dataclasses import dataclass

from models.container import Pan, Bowl, Container


def main():
    new_container = Container(Bowl.BIG)

    print(f"{new_container = }")
    

if __name__ == "__main__":
    main()