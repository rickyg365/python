import os


class Object:
    def __init__(self, **kwargs):
        self.data = kwargs

    def __str__(self):
        return f"{self.data}"

    def export(self):
        return {
            **self.data
        }


class Entry(Object):
    def __init__(self, key: str=None, name: str=None, description: str=None, **kwargs):
        super().__init__(**kwargs)
        self.key = key
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.key}] {self.name}: {self.description}"
    
    def export(self):
        return {
            'key': self.key,
            'name': self.name,
            'description': self.description,
            **self.data
        }

if __name__ == "__main__":
    SAMPLE_DATA = {
        'key': '1',
        'name': 'sample object',
        'items': [1, 2, 3]
    }

    CUSTOM_DATA = {
        'key': '2',
        'name': 'Sample Object',
        'description': 'This is a sample description of a made up onject...',
        'tags': ['random', '1st', 'example']
    }
    
    
    # new_obj = Object(**SAMPLE_DATA)

    # print(new_obj)
    # print(new_obj.data)


    new_obj = Entry(**CUSTOM_DATA)

    print(new_obj)
    print(new_obj.data)

    

