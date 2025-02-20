import os


class ScreenConfig:
    def __init__(self, default_char: str=' ', border: bool=False, display_title: bool=False, pixel_size: int=1):
        self.default_char = default_char
        self.border = border
        self.display_title = display_title
        self.pixel_size = pixel_size

class Screen:
    def __init__(self, title: str, width: int, height: int, config: ScreenConfig=None):
        self.title = title
        self.width = width
        self.height = height

        # Config
        self.config = ScreenConfig() if config is None else config
        
        # data
        self.data = self.build_data()

    def __str__(self):
        s = self.build_str()
        return s
    
    def build_data(self):
        d_char = self.config.default_char
        return [[d_char for entry in range(self.width)] for r in range(self.height)] 

    def build_str(self):
        data = '\n'.join([''.join(r) for r in self.data])
        return data
    
    def check_within_bounds(self, row: int, column: int):
        # Check bounds
        lr_bound = False
        ud_bound = False

        # Check left-right bound
        if 0 < column < self.width:  # Assumes first column is same length as all columns
            lr_bound = True
        
        # Check up_down bound
        if 0 < row < self.height:
            ud_bound = True

        return lr_bound and ud_bound

    def update_pixel(self, new_pixel: str, row: int, column: int, bound_check: bool=True):
        # Check bounds
        if bound_check:
            # within_bounds = self.check_within_bounds(row, column) 
            if not self.check_within_bounds(row, column):
                return
            
            if len(new_pixel) > self.config.pixel_size:
                return

        # Update Data
        self.data[row][column] = new_pixel

    def add_string(self, data: str, row: int=0, column: int=0, bound_check=True):
        # Assume no multiline for now

        # Check if string exceeds length, so we dont have to check bounds at each pixel
        if bound_check:    
            if len(data) + column > self.width:
                return

        for _, px in enumerate(data):
            # End of loop break condition
            if _ == self.width - 1:
                break
            # self.update_pixel(px, row, (column + _)%(self.width), bound_check=False)
            self.update_pixel(px, row, column + _, bound_check=False)

        return


if __name__ == "__main__":
    config_data = {
        'default_char': '.',
        'border': False,
        'display_title': False
    }
    
    # screen_config = ScreenConfig(**config_data)
    new_screen = Screen("New Screen Title", 8, 4, config=ScreenConfig(**config_data))
    # print(new_screen)

    new_screen.add_string("This is a sample", 1, 1, bound_check=False)
    print(new_screen)