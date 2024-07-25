import os
import random

"""
Possibilities
- Enemy Encounter
- Treasure Found
- Trap Activated
- Hidden Door Found
- Choice Room(update possibilities)
- Nothing Happens (Blank)
"""




class Room:
    def __init__(self, description="", interactions=None):
        self.description = description
        self.interactions = interactions
        self.next_room = None
        self.prev_room = None
    
    def enter(self):
        print(self.description)
        return self

    def get_result(self):
        if self.interactions is None:
            return self.next_room

        print("Options:\n")
        print("\n".join(self.interactions.keys()))
        user_input = input(">>> ")

        match user_input:
            case _:
                print("default")

        return self.next_room


class Dungeon:
    def __init__(self, length: int=1):
        self.length = length
        self.rooms = {
                "battle": [],
                "treasure": [],
                "trap": [],
                "secret": [],
                "choice": []
                }
        
        self.stats = {
                "battle": .35,
                "treasure": .05,
                "trap": .05,
                "secret": .05,
                "choice": .10,
                }

    def add_room(self, room_type, description, interactions):
        rooms = self.rooms.get(room_type, list())
        rooms.append(Room(description, interactions))
        

    def run(self):
        MAX_ITERATIONS = 999
        i = 0

        while self.current_room is not None:
            r = random.randint(100)/100
            current_room = None


            self.current_room = self.current_room.enter().get_result()

            # check iterationn
            i += 1
            if i > MAX_ITERATIONS:
                break





if __name__ == "__main__":
    d = Dungeon(5)
    
    # Rooms
    # battle
    # Treasure
    

    d.add_room()



