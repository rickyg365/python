

def progress_bar(current_value: int, max_value: int, bar_width: int=20):
    FILL = '*'
    SPACE = ' '
    L_END = '['
    R_END = ']'

    if max_value == 0:
        max_value = 1

    ratio = current_value/max_value

    fill_length = int(ratio*bar_width)
    
    if current_value > 0 and fill_length <= 0:
        fill_length = 1
    
    space_length = bar_width - fill_length
    
    return f"{L_END}{fill_length*FILL}{space_length*SPACE}{R_END}"

