from data_object import DataObject


class CustomObject(DataObject):

    def __init__(
        self, id_number: int, data=None, filename: str = "custom_object_dump.json"
    ):
        super().__init__(data, filename)
        self.id_number = id_number

    def __str__(self):
        string = "empty"
        if self.data is not None:
            string = f"[{self.id_number}]\n{self.data}"
        return f"{string}"

    def export(self):
        return {"id_number": self.id_number, "data": self.data}
