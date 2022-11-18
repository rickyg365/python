
from typing import List, Any

class Drawable:
    def __init__(self, data: str | List[List[str]]):
        self.data = data
        self.str_cache = None
        
        # Refactor
        d_type = type(data)
        if d_type is str:
            self.str_cache = data
            self.data = self.split_raw_data(data)
        if d_type is list:
            self.str_cache = self.render()
        
    def __str__(self):
        if self.str_cache is None:
            self.str_cache = self.render()

        return f"{self.str_cache}"
    
    @staticmethod
    def split_raw_data(raw_data: str):
        return [list(line) for line in raw_data.split('\n')]

    def render(self) -> str:
        return "\n".join(["".join(line) for line in self.data])
    
    def export(self) -> str:
        self.render()  # Make sure its updated
        return self.str_cache
    
    def json(self) -> List[List[str]]:
        return self.data
