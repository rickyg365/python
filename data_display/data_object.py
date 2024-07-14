class DataObject:
    def __init__(self, data=None, filename: str = "object_dump.json"):
        self.data = data
        self.filename = filename

    def __str__(self):
        string = f"{self.data}"
        if self.data is None:
            string = "Empty"
        txt = f"{string}"
        return txt

    def export(self):
        return self.data


d = DataObject()
