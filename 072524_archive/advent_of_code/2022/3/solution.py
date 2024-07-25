import os

"""
Day 3: Rucksack Reorganization
"""

def load_input(filepath: str="input.txt") -> str:
    try:
        with open(filepath, 'r') as read_file:
            return read_file.read()
    except FileNotFoundError:
        return "N/A"


def parse_char(raw_char: str) -> int:
    """ Convert char into an int     
    base: 96 - u for lower; (64 - u) + 26 for Upper
    print(ord('z'))   # ord(CHAR) -> int
    """
    upper_formula = lambda x: (x - 64) + 26
    lower_formula = lambda x: x - 96
    
    i = ord(raw_char)

    # Early Termination
    if len(raw_char) > 1:
        return 0

    if i > 122 or i < 64:
        return 0
    # Need to add case between 90-97

    # Return converted int
    if 64 < i <= 90:
        return upper_formula(i)

    return lower_formula(i)


def solve(input: str):
    total_sum = 0
    # Split Raw input line by line
    for line in input.split("\n"):
        # For each line get length and split line in 2 equal parts, always same number in both comps gauranteed
        midpoint = len(line)//2
        p1, p2 = line[:midpoint], line[midpoint:]
        
        # For each compartment see if they have any common items
        for item in set(p1):
            # Item Match
            if item in p2:
                # Convert common item for each line into number
                parsed_item = parse_char(item)
                print(item, parsed_item)
                total_sum += parsed_item
                # add up all the numbers from each line    
    return total_sum


def solve2(input: str):
    total_sum = 0

    idx = 0
    groups = []
    l = []
    for line in input.split('\n'):
        # Add current item and update index
        l.append(line)
        idx += 1

        # If index is at 3, reset index, reset list and add list to groups
        if idx == 3:
            idx = 0
            # Add to groups
            groups.append(l)
            # Reset List
            l = []

    # Split input into groups
    for group in groups:
        # Split groups into indv
        s1, s2, s3 = [set(x) for x in group]
        one_two = []
        two_three = []
        
        # Find common item between all 3 groups
        # Find 1 and 2 common
        for item in s1:
            if item in s2:
                one_two.append(item)
        
        # Find 2 and 3 common
        for item in s2:
            if item in s3:
                two_three.append(item)

        # Find common and check against
        for item in one_two:
            if item in two_three:
                ## Chosen ITem
                parsed = parse_char(item)
                # Sum Priorites
                total_sum += parsed

    return total_sum


if __name__ == "__main__":
    # raw_input = load_input("sample_input.txt")
    raw_input = load_input("input.txt")
    
    # solution = solve(raw_input)
    # print(solution)

    solution2 = solve2(raw_input)
    print(solution2)



