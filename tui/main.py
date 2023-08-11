import os
from typing import List

from debug import debug

"""
Goals:
1. Take in User Input


2. Display Data


provide list of questions
"""


# @debug
def get_user_input(prompt: str, multi_input: bool = False):
    """  """
    if not multi_input:
        return input(prompt)

    data = []
    print(prompt)
    while True:
        user_input = input("> ")
        if user_input == "":
            break
        data.append(user_input)

    return data


def create_survey(prompts: List[str], min_spacing: int = 12, gap_char: str = ": "):
    RESULTS = []

    for prompt in prompts:
        fixed_prompt = f"{prompt}{gap_char}"
        answer = get_user_input(f"{fixed_prompt:<{min_spacing}}")
        RESULTS.append(answer)
    return RESULTS


def main():
    QUESTIONS = [
        "How many?",
        "How much?",
        "How come?",
        "How?",
        "When?"
    ]

    # RESULTS = []

    # for question in QUESTIONS:
    #     answer = get_user_input(f"{question:<12}: ")
    #     RESULTS.append(answer)

    # print(RESULTS)

    results = create_survey(QUESTIONS)
    print(results)


if __name__ == "__main__":
    main()
