
from enum import Enum

class SCREEN_CHARACTERS(Enum):
    EMPTY = " "
    FILL = "."
    WALL = "@"

    HORIZONTAL = "─"
    VERTICAL = "│"
    
    TOP_RIGHT = "┐" 
    TOP_LEFT = "┌"
    BOT_RIGHT = "┘" 
    BOT_LEFT = "└"

    C_TOP_RIGHT = "╮" 
    C_TOP_LEFT = "╭" 
    C_BOT_RIGHT = "╯" 
    C_BOT_LEFT = "╰" 
    
