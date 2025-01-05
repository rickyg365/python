from utils.screen import Screen


class Object:
    def __init__(self, width: int=6, height: int=4, default_data=None):
        self.width = width
        self.height = height
        self.data = default_data

        if default_data is None:
            self.data = self.build_data()

    def __str__(self):
        s = self.build_text()
        return s
    
    def from_str(self, raw_data: str):
        d = []
        
        return self
    
    def build_text(self):
        txt = ''
        for row in self.data:
            line = ''
            for curr in row:
                line += f"{curr}"
            txt += f"{line}\n"
        return txt
                
    def build_data(self, default_data='*'):
        data = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                current_data = default_data
                row.append(current_data)
            data.append(row)
        
        return data
    
    def draw(self, screen: Screen, start_x: int=0, start_y: int=0):
        for y, row in enumerate(self.data):
            for x, curr in enumerate(row):
                screen.update_pixel(start_x + x, start_y + y, curr)
        return 
    
    def export(self):
        return {
            'width': self.width,
            'height': self.height,
            'data': self.data
        }




if __name__ == "__main__":
    SCREEN_WIDTH = 12
    SCREEN_HEIGHT = 8

    s = Screen(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, default_data=' ')
    
    
    custom_object = f"""


"""
    obj = Object()


    print(s)
    input('>>> ')
    obj.draw(s)

    print(s)
    input('>>> ')
    
    print(obj)




