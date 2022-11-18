import os
import json

from utils.save_load import save_json, load_json
from utils.custom_input import input_dict, input_list, input_dict_w_index, input_list_w_index


def generate_cog_test_data():
    data = {
        "title": "Need for Cognition Scale (from Cacioppo, Petty, & Kao, 1984)",
        "instructions": """For each of the statements below, please indicate wether or not the statement is characteristic of you or of what you believe. 
    1 -> Uncharacteristic | Fuck No, I Would NOT do/Like that
    5 -> Characteristic   | Yup, I would do/like that"""
    }
    
    # Input Keys
    data["keys"] = input_dict(
        show_index=False,
        key_text="Key", 
        val_text="Description"
    )

    # Input Questions
    data["questions"] = input_list_w_index(input_text="Question")

    return data


def view_test(filepath: str="data/cog_test.json"):
    test_data = load_json(filepath)
    test_txt = f"{test_data.get('title', 'Title')}\n{test_data.get('description', 'Description')}"
    
    key_list_str = [f"{k} -> {v}" for k, v in test_data.get('keys', {}).items()]
    
    for string in key_list_str:
        test_txt += f"\n{string}"

    print(test_txt)
    
    questions = test_data.get('questions', [])
    answers = {}

    for question in questions:
        print(question)
        u_input = input("[1-5] >>> ")
        answers[question] = int(u_input)
    
    # Get Results,
    total = sum(answers.values())
    length = len(answers)

    result = total/length

    print(f"\nFinal Result: {result:.2f}")

def main():
    # new_data = generate_cog_test_data()
    # save_json(new_data, "mini_test.json")
    view_test()
    

if __name__ == '__main__':
    main()
   
 