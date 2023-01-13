""" 20 - Valid Parentheses
Given a string s containing just the characters 
'(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.


"""
def solution(s: str) -> bool:
    stack = []
    matches = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    # Odd number of chars is instant fail
    if len(s)%2 == 1:
        return False

    for ch in list(s):
        # Close Value
        if ch in matches.values():
            stack.append(ch)
            continue
        
        # Open Value
        open_ch = matches[ch]
        if open_ch in stack and open_ch == stack[-1]:
            stack.pop()
        else:
            return False
        
    return len(stack) == 0


# Optimized, time: O(n) space: O(n)
def optimized_solution(s: str) -> bool:
    stack = []
    matches = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    if len(s)%2 == 1:
        return False

    for ch in list(s):
        # Closer
        if ch in matches:
            if stack and matches[ch] == stack[-1]:
                stack.pop()
            else:
                return False
        # Opener
        else:
            stack.append(ch)
        
    return len(stack) == 0


if __name__ == "__main__":
    EXAMPLES = [
        '()', 
        '()[]{}', 
        '(]'
    ]

    for example in EXAMPLES:
        sol = f"""
Example: {example}
Solution:  {solution(example)}
Optimized: {optimized_solution(example)} 
"""
        print(sol)
