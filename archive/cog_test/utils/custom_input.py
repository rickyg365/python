"""


"""

# No Index!
def input_list(input_text=">>> ", ref_list=None):
    """ Input a list entry by entry until you input 'q' """
    # Variables
    if ref_list is None:
        ref_list = []
    
    while 1:
        print(' ')
        # Input
        new_input = input(f"{input_text}: ")
        if new_input == 'q':
            break

        ref_list.append(new_input)
    
    return ref_list


def input_dict(key_text="Key", val_text="Value", ref_dict=None):
    """ Input a dict key, val by key, val until you input 'q' """
    # Variabless
    if ref_dict is None:
        ref_dict = {}
    
    while 1:
        print(' ')
        # Input Key
        new_key = input(f"{key_text}: ")
        if new_key == 'q':
            break
        # Input Value
        new_value = input(f"{val_text}: ")
        # Can also add a break check here

        ref_dict[new_key] = new_value

    return ref_dict



# Index
def input_dict_w_index(key_text="Key", val_text="Value", ref_dict=None):
    """ Input a dict key, val by key, val until you input 'q', w/ index """
    # Variables
    index = 1

    if ref_dict is None:
        ref_dict = {}
    
    while 1:
        print(' ')
        # Input Key
        new_key = input(f"{key_text} #{index}: ")
        if new_key == 'q':
            break

        # Input Value
        new_value = input(f"{val_text} #{index}: ")
        # Can also add a break check here

        # Update before next loop
        ref_dict[new_key] = new_value
        index += 1
    return ref_dict


def input_list_w_index(input_text=">>> ", ref_list=None):
    """ Input a list entry by entry until you input 'q', w/ index """
    # Variables
    index = 1

    if ref_list is None:
        ref_list = []
    
    while 1:
        print(' ')
        # Entry
        new_input = input(f"{input_text} #{index}: ")
        if new_input == 'q':
            break
        
        # Update before next loop
        ref_list.append(new_input)
        index += 1

    return ref_list



if __name__ == "__main__":
    # new_list = input_list(input_text=">>> ")
    # new_dict = input_dict()

    # print(new_list)
    # print(new_dict)

    # appended_list = input_list(new_list, ">>> ")
    # appended_dict = input_dict(new_dict)

    # print(appended_list)
    # print(appended_dict)
    pass
