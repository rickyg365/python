"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest 
substring without repeating characters.

"""


def lengthOfLongestSubstring(s: str) -> int:
    # Initial Variables, left pointer and max
    total_max = l = 0
    # Inital set to contain characters we have encountered
    seen = set()

    # Iterate through the string
    for r, c in enumerate(s):
        # While the current char is in seen
        while c in seen:
            # remove the leftmost value and increase left pointer
            seen.remove(s[l])
            l += 1
        # Add the new char to seen
        seen.add(c)
        # make the total the greater value between, total_max or the length of the sliding window
        total_max = max(total_max, r - l + 1)
    return total_max


if __name__ == "__main__":
    e1 = "abcabcbb"
    e2 = "bbbbb"
    e3 = "pwwkew"
    
    print(f"""
Solutions
1. {lengthOfLongestSubstring(e1)}

2. {lengthOfLongestSubstring(e2)}

3. {lengthOfLongestSubstring(e3)}    
""")
