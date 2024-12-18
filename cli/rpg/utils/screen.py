from typing import Callable


class Screen:
    def __init__(self, width: int=6, height: int=4, default_data: Callable=None):
        self.width = width
        self.height = height
        self.default = default_data
        self.data = self.build_data(default_data)

    def __str__(self):
        s = self.build_text()
        return s
    
    def build_text(self):
        txt = ''
        for i in range(self.height):
            row = ''
            for j in range(self.width):
                curr = self.data[i][j]
                row += f"{curr}"
            txt += f"{row}\n"
        return txt
                
    def build_data(self, default_factory: Callable=None):
        data = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                if default_factory is None:
                    row.append(' ')
                    continue
                row.append(default_factory())
            data.append(row)
        
        return data
    
    def export(self):
        return {
            'width': self.width,
            'height': self.height,
            'data': self.data
        }

