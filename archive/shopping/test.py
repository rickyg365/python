import os
import pytest

from recipe import Recipe


# Sample Recipe Data
test_recipe_data = {
    "name": "Philly CheeseSteak",
    "description": "A delicious blend of steak and cheese grilled with peppers and enjoyed on a nice bread roll.",
    "ingredients": {
        "salt": "1 teaspoon",
        "pepper": "1 teaspoon",
        "Steak": "1 lb",
        "Cheese": "1/2 lb",
        "Onion": "1 whole",
        "Bell Peppers": "2 whole",
        "French Roll": "1 loaf"
},
    "steps": [
        "Chop Onion, Bell Peppers, and Steak",
        "Grill and season Veggies",
        "Grill and season Steak",
        "Top Steak with Cheese",
        "Toast French Roll",
        "Assemble",
        "Enjoy"
    ]
}

new_recipe = Recipe(**test_recipe_data)


def test_create_recipe(): 
    assert(isinstance(new_recipe,Recipe)) 

    
if __name__ == '__main__':
    test_create_recipe()

sample_output = """
Philly CheeseSteak:
_____________________________________________
A delicious blend of steak and cheese
grilled with peppers and enjoyed on a nice
bread roll.
_____________________________________________

Ingredients:
---------------------------------------------
  Salt: 1 TEASPOON
  Pepper: 1 TEASPOON
  Steak: 1 LB
  Cheese: 1/2 LB
  Onion: 1 WHOLE
  Bell Peppers: 2 WHOLE
  French Roll: 1 LOAF
---------------------------------------------

Instructions:
---------------------------------------------
  1. Chop Onion, Bell Peppers, and Steak
  2. Grill and season Veggies
  3. Grill and season Steak
  4. Top Steak with Cheese
  5. Toast French Roll
  6. Assemble
  7. Enjoy
---------------------------------------------"""
