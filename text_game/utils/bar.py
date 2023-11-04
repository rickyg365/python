def StatusBar(current_value, max_value, max_num_characters: int=20):
    FILL_CHAR = '='
    SPACE_CHAR = ' '
    
    scale = current_value/max_value

    fill_chars = int(scale * max_num_characters)

    if current_value > 0 and fill_chars == 0:
        fill_chars = 1
    
    # Might not need
    if current_value == 0:
        fill_chars = 0

    space_chars = max_num_characters - fill_chars

    return f"[{fill_chars*FILL_CHAR}{space_chars*SPACE_CHAR}]"
