import os
import sys

def clear_screen():
    clear_command = "clear" if sys.platform != "win32" else "cls"
    os.system(clear_command)