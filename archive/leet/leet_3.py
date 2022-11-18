import os
from re import L

"""
[ Length of Longest Substring ]

"""

def Solution(s: str):
    sub_string = {}
    cur_start = 0
    cur_length = 0
    longest = 0

    for i, letter in enumerate(s):

        if letter in sub_string and sub_string[letter] >= cur_start:
            cur_start = sub_string[letter] + 1
            cur_length = i - sub_string[letter]
            sub_string[letter] = i
        else:
            sub_string[letter] = i
            cur_length += 1
            if cur_length > longest:
                longest = cur_length
    
    return longest





def main():
    test_string = "abcabcbba"
    print(Solution(test_string))

if __name__ == '__main__':
    main()
