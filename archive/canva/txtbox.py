import os

# Ignores periods
def max_width(raw_paragraph: str, max_length: int=30):
    new_lines = []
    words = raw_paragraph.strip().replace("\n", " ").split(" ")
    
    # Build New Lines
    line_total = 0
    line = ""

    for word in words:
        l = len(word) + 1  # +1 for space
        if line_total + l > max_length:
            # Add Line
            new_lines.append(line)

            # Start New Line
            line = ""
            line_total = 0
            continue
        
        # Add word to line
        if word in ['', ' ', '\n']: 
            continue

        if '.' in word or '!' in word or '?' in word:
            line +=  f"{word}\n"
            
            # Add Line
            new_lines.append(line)

            # Start New Line
            line = ""
            line_total = 0
            continue

        line +=  f"{word} "
        line_total += l

        #! DEBUG        
        # print(l, line_total, line)
        # input()

    return "\n".join(new_lines)




def main():
    sample_paragraph = """
Wake up to reality! Nothing ever goes as planned in this accursed world. The
longer you live, the more you realize that the only things that truly
exist in this reality are merely pain, suffering and futility.

Listen, everywhere you look in this world, wherever there is light, 
there will always be shadows to be found as well. 

As long as there is a concept of victors, the vanquished will also exist. 

The selfish intent of wanting to preserve peace, 
initiates war and hatred is born in order to protect love. 

There are nexuses causal relationships that cannot be separated.
"""
    baby_paragraph = """
Wake up to reality! Nothing ever goes as planned in this accursed world.

The longer you live, the more you realize that the only things that truly 
exist in this reality are merely pain, suffering and futility.
"""
    c, r = os.get_terminal_size()
    new_p = max_width(sample_paragraph, c - 5)
    print(new_p)
    return

if __name__ == '__main__':
    main()
