import os, shutil
from typing import List

def batch_clone_dir(template_filepath: str, clone_input: List[str] | int):
    """ 
    Params:
        template_filepath: str
            name of base directory to clone

        input_list: list or int

            input_list:
                iterates list of names and creates a copy of template file named the current list iteration
        
            int:
                creates that many copies of template file 


    BUGS: 
        1. Throws error if name already exists
    
    """
    # Handle Integer Case by creating a list of names
    if type(clone_input) is int:
        clone_input = [f"{template_filepath}_{x+1}" for x in range(clone_input)]

    # Iterate through names
    print(f"\nCloning >>> {template_filepath} -> ___ : ")
    for _, name in enumerate(clone_input):
        result = "Success"
        # Copy template and name it the new name
        new_path = f"{name}"

        # Check if new path already exists
        if os.path.isdir(new_path):
            result = "Failure"
        else:
            shutil.copytree(template_filepath, new_path)
        
        print(f"[{result}] {new_path}")
    
    return True


def input_batch_names() -> List[str]:
    """ 
    Infinite Loop for inputing directory names 
    returns them as a list.
    
    break by inputing q or quit (case-sensitive) 
    """

    user_input = []
    count = 1
    
    while True:
        curr_input = input(f"{count}. ")
        
        # Break Conditions
        break_conditions = ["q", "quit"]

        if curr_input in break_conditions:
            # Return List of names
            print(f"{'_'*40}")
            return user_input

        # Add to list and iterate count
        count += 1
        user_input.append(curr_input)


def run():
    # Variables
    template_filename = "starter"
    
    print(f"Current Template Filename: {template_filename}")
    batch_names = input_batch_names()

    batch_clone_dir(template_filename, batch_names)
    
    return

if __name__ == '__main__':
    run()
