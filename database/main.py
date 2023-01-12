import os
import sqlite3

import pandas as pd

from typing import List, Dict, Any


"""
ref: https://towardsdatascience.com/automating-sunday-meal-preps-using-sqlite-relational-databases-and-python-c85821099ca8
code_ref: https://github.com/jenniferrkim/recipe_database/blob/master/recipe%20database.ipynb

Sample Schema

Table: Recipe
recipe_id (primary)
recipe_name (str)
recipe_note (str)
cuisine_id (foreign)
instructions (str)

Table: Cuisines
cuisine_id (primary)
cuisine_name (str)

Table: Recipe Ingredients
recipe_id (foreign)
ingredient_id (foreign)
unit_id (foreign)
quantity (int)
prep_method_id (foreign)


Table: Ingredients
ingredient_id (primary)
ingredient_name (str)

Table: Units
unit_id (primary)
unit_name (str)

Table: Prep Method
method_id (primary)
method_name (str)

"""
def create_connection(file_name: str):
    connection = None
    
    try:
        connection = sqlite3.connect(file_name)
    except Exception as e:
        print(e)
    
    return connection

def create_recipe_database(connection: sqlite3.Connection | None):
    if connection is None:
        return

    with connection:
        cur = connection.cursor()

        # Create main Recipe table
        cur.execute("""CREATE TABLE recipe 
        (recipe_id INTEGER PRIMARY KEY NOT NULL,
        recipe_name TEXT,
        recipe_notes TEXT,
        cuisine_id INTEGER,
        instructions TEXT,
        FOREIGN KEY (cuisine_id) REFERENCES cuisine(cuisine_id))""")

        # Create cuisine table
        cur.execute("""CREATE TABLE cuisine
        (cuisine_id INTEGER PRIMARY KEY NOT NULL,
        cuisine_name TEXT""")

        # Create ingredients table
        cur.execute("""CREATE TABLE ingredient
        (ingredient_id INTEGER PRIMARY KEY NOT NULL,
        ingredient_name TEXT""")
        
        # Create units table
        cur.execute("""CREATE TABLE unit
        (unit_id INTEGER PRIMARY KEY NOT NULL,
        unit_name TEXT""")

        # Create preparation methods table
        cur.execute("""CREATE TABLE prep_method 
        (method_id INTEGER PRIMARY KEY NOT NULL,
        method_name TEXT""")
 
        # Create recipe ingredients table
        cur.execute("""CREATE TABLE recipe_ingredient
        (recipe_id INTEGER PRIMARY KEY NOT NULL,
        ingredient_id INTEGER,
        unit_id INTEGER,
        quantity INTEGER,
        method_id INTEGER,
        FOREIGN KEY (recipe_id) REFERENCES recipe(recipe_id),
        FOREIGN KEY (ingredient_id) REFERENCES ingredient(ingredient_id),
        FOREIGN KEY (unit_id) REFERENCES unit(unit_id),
        FOREIGN KEY (method_id) REFERENCES prep_method(method_id))""")

        connection.commit()


# Python Recipe Object
'''
ingredients sample dict

ingredients = [
    {
        name: ???,
        quantity: ???,
        unit: ???,
        prep_method: ???
    },
    ???
]


'''
class Recipe:
    def __init__(self, recipe_name, recipe_note, ingredients, cuisine, instructions) -> None:
        self.name = recipe_name
        self.note = recipe_note
        self.ingredients = ingredients
        self.instructions = instructions
        self.cuisine = cuisine
    
    def add_to_db(self, connection: sqlite3.Connection | None):
        if connection is None:
            print("Failed to connect")
            return

        with connection:
            cur = connection.cursor()

            # Add cuisine
            sql = """INSERT INTO cuisine (cuisine_name) SELECT (?) WHERE NOT EXIST (SELECT 1 FROM cuisine WHERE cuisine = ?)"""
            cur.execute(sql, "cuisine name")
            # Add recipe
            # Add ingredients
            for ingredient in self.ingredients:
                pass


            user_input = input("Save? (y/n):")
            if user_input == 'y':
                connection.commit()



def main():
    database_file = 'data/sample.db'
    try:
        connection = sqlite3.connect(database_file)
        with connection:
            print(f"Loaded {database_file}")

    except Exception as e:
        print(f"failed to connect to {database_file}")



 
if __name__ == "__main__":
    main()