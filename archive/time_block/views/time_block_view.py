from utils.custom_time import Time

"""
"""

class TimeBlockView:
    def __init__(self, max_length: int=40):
        self.string_cache = ""
        self.size = max_length - 2

    def print(self, time_block_data) -> str:
        # print(time_block_data)
        if self.string_cache == "":
            # print("[cached]")
            # Create Components
            top = self.top_line_text()
            bot = self.bot_line_text()

            title = self.title_text(time_block_data["title"])
            time = self.time_text(Time(**time_block_data["start_time"]), Time(**time_block_data["end_time"]))

            self.string_cache = f"""{top}
│{title:^{self.size}}│
│{time:^{self.size}}│
{bot}"""

        return self.string_cache

    def top_line_text(self) -> str:
        txt = f"╭{'─'*self.size}╮"
        return txt
    
    def title_text(self, title: str) -> str:
        txt = f"{title}"
        return txt

    def time_text(self, start: Time, end: Time) -> str:
        txt = f"{start} -> {end}"
        return txt

    def bot_line_text(self) -> str:
        txt = f"╰{'─'*self.size}╯"
        return txt

