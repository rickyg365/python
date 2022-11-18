import os


class KeySingleRowView:
    def __init__(self, input_data = None, line_width: int=30):
        self.width = line_width
        self.data = input_data
        self.line_data = []
        self.cache = None
    
    def update_data(self, new_data):
        self.data = new_data

    def __str__(self) -> str:
        # Checks
        no_cache = self.cache is None
        no_data = self.data is None

        # Build Initial Cache
        if no_cache:
            if no_data:
                return "No Data"
            
            # Build Cache
            id = f"{self.id_text():^10}"
            name = f"{self.name_text():^10}"
            categories = f"{self.categories_text():^30}"

            self.cache = f"{id} | {name} | {categories}"

            self.line_data.append(id)
            self.line_data.append(name)
            self.line_data.extend(categories)

        return self.cache
    
    def id_text(self):
        return self.data['id']
    
    def name_text(self):
        return self.data['name']
    
    def categories_text(self):
        return self.data['categories']


###

class SingleRowView:
    def __init__(self, input_data = None, line_width: int=30):
        self.width = line_width
        self.data = input_data
        self.line_data = []
        self.cache = None
    
    def update_data(self, new_data):
        self.data = new_data

    def __str__(self) -> str:
        # Checks
        no_cache = self.cache is None
        no_data = self.data is None

        # Build Initial Cache
        if no_cache:
            if no_data:
                return "No Data"
            
            # Build Cache
            id = f"{self.id_text():<10}"
            name = f"{self.name_text():<10}"
            categories = f"{self.categories_text(' '):<30}"

            self.cache = f"{id} | {name} | {categories}"

            self.line_data.append(id)
            self.line_data.append(name)
            self.line_data.extend(categories)

        return self.cache
    
    def id_text(self):
        return self.data['id']
    
    def name_text(self):
        return self.data['name']
    
    def categories_text(self, sep: str=" "):
        lines = []
        for cat in self.data['categories']:
            lines.append(f"[{cat}]")
        
        return sep.join(lines)

def main():
    return

if __name__ == '__main__':
    main()
