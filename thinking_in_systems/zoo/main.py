import os

from typing import List, Dict

from models.animal import Animal
from models.keeper import Keeper
# from models.guest import Guest
from models.exhibit import Exhibit
from models.zoo import Zoo




def main():
    # Test Keeper 
    new_keeper = Keeper("Fred")

    # W/out Chaining
    # new_keeper.adjust_salary(200_000)
    # new_keeper.set_availability(40)
    
    print(new_keeper)

    # Test Animal 
    new_animal = Animal("Alligator")

    # W. Chaining!!!!
    new_animal.set_feed_amount(5).set_height(7).set_width(3)

    print(new_animal)
    
    return

if __name__ == '__main__':
    main()
