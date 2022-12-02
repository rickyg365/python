import os


def load_input(filepath: str="input.txt"):
    with open(filepath, 'r') as read_file:
        return read_file.read()


def parse_raw_input(raw_data):
    # Split by "\n\n"
    first_split = raw_data.split("\n\n")

    # Split each element of first_split by "\n"
    final_split = [chunk.split("\n") for chunk in first_split]

    return final_split


def solve_one(given_input):
    # Splits input into multidimensional array, 1st layer - elf, 2nd layer - indv. calorie counts
    parsed_input = parse_raw_input(given_input)
    
    maximum_calories = 0
    for elf in parsed_input:
        # Get calorie total for current elf
        current_total = 0
        for calorie_count in elf:
            current_total += int(calorie_count)

        # Update max using current_total
        if current_total > maximum_calories:
            maximum_calories = current_total

    print(maximum_calories)
    return maximum_calories


def solve_two(given_input):
    # Splits input into multidimensional array, 1st layer - elf, 2nd layer - indv. calorie counts
    parsed_input = parse_raw_input(given_input)
        
    list_totals = []
    for elf in parsed_input:
        # Get calorie total for current elf
        current_total = 0
        for calorie_count in elf:
            current_total += int(calorie_count)
        list_totals.append(current_total)
    list_totals.sort()
    print(list_totals[-3:])    
    return sum(list_totals[-3:])


if __name__ == "__main__":
    # Get User Input
    first_given = load_input("first_input.txt")
    solution_one = solve_one(first_given)

    # second_given = load_input("second_input.txt")
    solution_two = solve_two(first_given)

    print(solution_two)
    

    