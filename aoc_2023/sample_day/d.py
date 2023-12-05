import os


def read_file(input_file: str):
    data = None
    with open(input_file, 'r') as input_buffer:
        data = input_buffer.read()

    return data

def solve_p1(data):
    return

def solve_p2(data):
    return


if __name__ == "__main__":
    SAMPLE_INPUT_P1 = "inputs/p1_sample_input.txt"
    SAMPLE_INPUT_P2 = "inputs/p2_sample_input.txt"
    INPUT_P1 = "inputs/p1_input.txt"
    INPUT_P2 = "inputs/p2_input.txt"

    data = read_file(SAMPLE_INPUT_P1)

    s1 = solve_p1(data)
    s2 = solve_p2(data)

    print(s1)
    print(s2)
