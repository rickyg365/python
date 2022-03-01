import os
import sys

from rich import print
from rich.panel import Panel
import pandas.io.clipboard as pyperclip

from youtube_link_converter import get_fullscreen_url


if __name__ == '__main__':
    passed_arg = ""
    user_input = "default"

    if len(sys.argv) > 1:
        passed_arg = sys.argv[1]

        if passed_arg[:3] in ["www", "htt"]:
            user_input = passed_arg
    
    if user_input == "default":
        user_input = input("youtube url: ")
    else:
        user_input = passed_arg

    final_url = get_fullscreen_url(user_input)
    
    # Get terminal Size and estimate padding needed to center text
    cols, rows = os.get_terminal_size()
    estimated_padding = int((cols - 2 - len(final_url))/2)

    # Copy to Clipboard
    pyperclip.copy(final_url)

    # Display to Console
    print(Panel(final_url, title="Fullscreen URL", padding=(1, estimated_padding)))
