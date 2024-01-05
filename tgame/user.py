
class User:
    def __init__(self, symbol: str="@"):
        self.coordinates = [0, 0]
        self.symbol = symbol
        self.action = ""
        self.VALID_ACTIONS = {"w", "a", "s", "d"}

    def __str__(self):
        return self.symbol

    def update_action(self, new_action: str):
        # Validate Action
        if new_action not in self.VALID_ACTIONS:
            return
        
        self.action = new_action

    def perform_action(self):
        if self.action == "w":
            self.movement(0, -1)
        if self.action == "s":
            self.movement(0, 1)
        if self.action == "a":
            self.movement(-1, 0)
        if self.action == "d":
            self.movement(1, 0)
            

    def movement(self, x_update: int=0, y_update: int=0):
        if x_update == 0 and y_update == 0:
            return
        
        NEW_X = self.coordinates[0]
        NEW_Y = self.coordinates[1]

        if x_update == 0:
            NEW_Y += y_update

        else:
            NEW_X += x_update
        
        self.coordinates = [NEW_X, NEW_Y]

