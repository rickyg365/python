import os
import time
import random

# Models
from models.party import Party
from models.pokemon import Pokemon

# Poke API
from poke_api.client import load_pokemon

# Utilities
from utils.lsjson import load_json, save_json

"""
For Next Time

Let the user select a slot and reroll the pokemon in that slot!

"""
class Trainer:
    def __init__(self, trainer_id: int, party: Party, path: str):
        self.id = trainer_id
        self.party = party
        self.path = path

    def __str__(self) -> str:
        txt = f"[{self.id}]: \n{self.party}"
        return txt



def get_random_poke():
    pid = random.randint(1, 500)
    return Pokemon(**load_pokemon(pid))


def run_prog():
    # Need to load in already created parties
    trainer_ids = [raw.split(".")[0] for raw in os.listdir("data/party")]
    
    trainers = [Trainer(int(f_id), Party().load(f"data/party/{f_id}.json"), f"data/party/{f_id}.json") for f_id in trainer_ids]
    curr_trainer = trainers[0] if len(trainers) > 0 else ""

    while True:
        print(curr_trainer)
        u_in = input("Choice: \nA: Add Trainer \nL: Load Trainer \nQ: Quit Program \n>>> ")

        match u_in:
            case "a":
                '''
                {
                    "id": new_trainer_id,
                    "party": Party(),
                    "save_path": f"data/party/{new_trainer_id}.json"
                }
                '''
                new_trainer_id = int(input("\nNew Trainer ID: "))
                print("Adding New Trainer...")
                new_savepath = f"data/party/{new_trainer_id}.json"
                print("Creating New Party...")
                new_party = Party()
                for _ in range(6):
                    print(f"\r{(_+1)*'*'}", end="\r")
                    random_pokemon = get_random_poke()
                    new_party.add(random_pokemon)
                    
                    time.sleep(1)
                new_party.save(new_savepath)
                print("New Trainer Created, Party Saved!")
                trainers.append(Trainer(new_trainer_id, new_party, new_savepath))
                
            case "l":
                l_id = int(input("\nTrainer ID to load: "))
                chosen = [i for i in trainers if i.id == l_id][0]
                curr_trainer = chosen
            case "q":
                break


def main():
    trainer_id = 1234
    datapath = f"data/party/{trainer_id}.json"

    my_party = Party()
    my_party.load(datapath)

    # for _ in range(6):
    #     random_pokemon = get_random_poke()
    #     my_party.add(random_pokemon)
        
    #     time.sleep(1)

    my_party.save(datapath)
    print(my_party)
    

if __name__ == '__main__':
    # main()
    run_prog()
