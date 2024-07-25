

class Character:
    def __init__(self, name: str, id: str, data_source):
        self.name = name
        self.id = id

        self.is_alive = True

        new_data = {}
        if data_source is not None:
            new_data = data_source.get(self.id, None)

        self.current_hp = new_data.get("hp", 0)

        self._max_hp = new_data.get("hp", None)
        self._atk = new_data.get("atk", None)
        self._res = new_data.get("res", None)
        self._spd = new_data.get("spd", None)
        self._lck = new_data.get("lck", None)

    def __str__(self):
        txt = f"{self.name} - {self.id}"
        return txt

    def defend(self, incoming_atk):
        taken_atk = incoming_atk - self._res
        if taken_atk < 0 or not self.is_alive:
            return False

        self.current_hp -= taken_atk
        if self.current_hp < 0:
            self.current_hp = 0
            self.is_alive = False
        return True
    
