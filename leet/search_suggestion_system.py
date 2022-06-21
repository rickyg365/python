import os
from typing import List
from numpy import full
import pynput

"""
[ MEDIUM ] Search Suggestion System:


Input
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"], search_word="mouse"


Output
    [
        ["mobile", "moneypot", "monitor"],  # M
        ["mobile", "moneypot", "monitor"],  # MO
        ["mouse", "mousepad"],              # MOU
        ["mouse", "mousepad"],              # MOUS
        ["mouse", "mousepad"],              # MOUSE
    ]



Steps
1. Sort by alpha
2. 
3. 
4. 

"""


def search(products: List[str], search_word: str):
    '''
    sorting: nlogn
    worse_case: n*w(length of word) + m(input word length)
    '''
    # Starting Variables
    l_pointer = 0
    r_pointer = len(products) - 1

    result = []

    # Sort
    products.sort()

    for i in range(len(search_word)):
        c = search_word[i]

        # Update Pointers
        # uncrossed_pointers = l_pointer <= r_pointer

        # Length of word < current index, min length check
        # length_check_l = len(products[l_pointer]) <= i
        # length_check_r = len(products[r_pointer]) <= i
        
        # target_char_not_matching = products[l_pointer] != c

        while l_pointer <= r_pointer and (len(products[l_pointer]) <= i or products[l_pointer][i] != c):
            l_pointer += 1
        
        while l_pointer <= r_pointer and (len(products[r_pointer]) <= i or products[r_pointer][i] != c):
            r_pointer -= 1
        
        # print(c, l_pointer, r_pointer)
        result.append([])
        remain = r_pointer - l_pointer + 1
        for _ in range(min(3, remain)):
            result[-1].append(products[l_pointer+_])
    return result


def idk_search(products):
    '''
    sorting: nlogn
    worse_case: n*w(length of word) + m(input word length)
    '''
    # Starting Variables
    l_pointer = 0
    r_pointer = len(products) - 1

    result = []

    # Sort
    products.sort()

    i = 0
    full_word = ""
    while True:
        if result:
            print(result[-1])
        next_letter = input(f"{full_word}")

        if next_letter == ":q":
            break

        c = next_letter
        full_word += next_letter

        # Update Pointers
        while l_pointer <= r_pointer and (len(products[l_pointer]) <= i or products[l_pointer][i] != c):
            l_pointer += 1
        
        while l_pointer <= r_pointer and (len(products[r_pointer]) <= i or products[r_pointer][i] != c):
            r_pointer -= 1
        
        # print(c, l_pointer, r_pointer)
        result.append([])
        remain = r_pointer - l_pointer + 1
        for _ in range(min(3, remain)):
            result[-1].append(products[l_pointer+_])
        i += 1

    return result


def nice_search(search_list):
    u_in = ""
    suggestions = ""

    while 1:
        print(f"""
suggestions: {suggestions}

search: {u_in}        
        
""")
        
        new_letter = input(">>> ")
        if new_letter == "quit":
            break

        u_in += new_letter
        suggestions = search(search_list, u_in)[-1]


if __name__ == '__main__':
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    # search_word = "mouse"
    # result = search(products, search_word)
    # nice_search(products)

    # for _, ch in enumerate(search_word):
    #     print(f"{search_word[_]}: {result[_]}")
    
    result = idk_search(products)

    print(result)