import os

"""
Day X: ____________
"""

def load_input(filepath: str="input.txt") -> str:
    try:
        with open(filepath, 'r') as read_file:
            return read_file.read()
    except FileNotFoundError:
        return "N/A"


def solve(input: str):
    return


if __name__ == "__main__":
    raw_input = load_input()
    solution = solve(raw_input)
    
    print(solution)
