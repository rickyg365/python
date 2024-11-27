

def text_box(text):
    lines = text.split('\n')
    
    length = len(lines)
    width = 0

    for line in lines:
        width = max(len(line), width)
    
    middle_text = '\n'.join([f"|{l:<{width}}|" for l in lines])

    return f""".{'-'*(width)}.
{middle_text}
'{'-'*(width)}'"""

def progress_bar(current_value: int, max_value: int, bar_width: int=20, style=None):
    if style is None:
        style = {}
    
    FILL = style.get('FILL', '-')
    SPACE = style.get('SPACE', ' ')
    L_END = style.get('L_END', '(')
    R_END = style.get('R_END', ')')

    if max_value == 0:
        max_value = 1

    ratio = current_value/max_value

    fill_length = int(ratio*bar_width)
    
    if current_value > 0 and fill_length <= 0:
        fill_length = 1
    
    space_length = bar_width - fill_length
    
    return f"{L_END}{fill_length*FILL}{space_length*SPACE}{R_END}"

